from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Choice, Question, ChoiceVote


class IndexView(LoginRequiredMixin, generic.ListView):
    """
    Displays a list of the latest poll questions related to :model:`Question`.
    This view retrieves the last ten published questions for logged-in users.
    """
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last ten published questions (not including those set to be
        published in the future).
        """
        return (
                    Question.objects
                    .filter(pub_date__lte=timezone.now())
                    .order_by("-pub_date")[:10]
                )


class DetailView(LoginRequiredMixin, generic.DetailView):
    """
    Displays the details of a poll question related to :model:`Question`.
    This view shows the question and its available choices for logged-in users,
    excluding unpublished questions.
    """
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        try:
            context['vote'] = (
                ChoiceVote.objects
                .get(users__in=[self.request.user],
                     choice__question=self.get_object())
            )

        except ChoiceVote.DoesNotExist:
            pass
        return context


class ResultsView(LoginRequiredMixin, generic.DetailView):
    """
    Displays the results of a poll question related to :model:`Question`.
    This view shows the results of a specific question for logged-in users.
    """
    model = Question
    template_name = "polls/results.html"


@login_required
def vote(request, question_id):
    """
    Processes a user's vote for a question related to :model:`polls.Question`
    and :model:`polls.ChoiceVote`.
    This view handles the logic for voting, including adding or changing a vote
    for a specific choice and providing appropriate feedback to the user.
    It updates the vote count and either informs the user of a successful vote
    or an already existing vote.

    **Context**
    ``question``
         The specific instance of :model:`polls.Question`
         identified by the `question_id`.
    ``selected_choice``
         The specific instance of :model:`polls.Choice`
         the user selected to vote for.
    ``user_vote``
         The :model:`polls.ChoiceVote` instance representing
         the user's vote for the selected choice.
    **Template:**
    :template:`polls/detail.html`
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
        user_vote, created = (
            ChoiceVote.objects
            .get_or_create(choice=selected_choice)
        )

        vote_changed = False

        if request.user not in user_vote.users.all():
            user_vote.users.add(request.user)
            user_vote.save()
            selected_choice.votes = F("votes") + 1
            selected_choice.save()
        else:
            messages.info(request, "You have already voted for this choice.")
        return HttpResponseRedirect(
            reverse("polls:results", args=(question.id,))
        )

        previous_votes = ChoiceVote.objects.filter(choice__question=question)
        for vote in previous_votes:
            if (vote.choice != selected_choice and
                    request.user in vote.users.all()):

                vote.users.remove(request.user)
                vote.choice.votes -= 1
                vote.save()
                vote.choice.save()
                vote_changed = True

        if vote_changed:
            messages.success(
                request,
                "Your vote has been updated to the new choice."
            )

        else:
            messages.success(request, "Your vote was successfully submitted.")

        url = reverse("polls:results", args=(question.id,))
        return HttpResponseRedirect(url)

    except (KeyError, Choice.DoesNotExist):
        error_message = "You didn't select a valid choice. Please try again."
        messages.error(request, error_message)

        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )


@login_required
def delete_vote(request, question_id):
    """
    Deletes a user's vote for a question related to :model:`polls.Question`
    and :model:`polls.ChoiceVote`.
    This view allows users to remove their vote for a particular
    and updates the vote count for the associated choice.
    If the user has not voted on the question, an error message is displayed.

    **Context**
    ``question``
         The instance of :model:`polls.Question` identified by `question_id`.
    ``vote``
         The instance of :model:`polls.ChoiceVote`
         representing the user's vote on the question.
         If the user hasn't voted, this variable will not exist.
    **Template:**
    :template:`polls/delete.html`
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        vote = ChoiceVote.objects.get(
            users__in=[request.user],
            choice__question=question
        )

        if request.POST:
            vote.users.remove(request.user)
            vote.choice.votes -= 1
            vote.save()
            vote.choice.save()
            messages.success(
                request,
                "Your vote has been successfully deleted."
            )

            return HttpResponseRedirect(
                reverse("polls:detail", args=(question.id,))
            )
    except ChoiceVote.DoesNotExist:
        messages.error(request, "You have not voted on this question.")

    return render(
        request,
        "polls/delete.html",
        {
            "question": question,
            "vote": vote,
            "error_message": "You didn't select a choice.",
        },
    )
