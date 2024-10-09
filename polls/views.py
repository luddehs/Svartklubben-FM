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
    Displays the details of a poll question and the available choices.
    Retrieves the current user's vote for the question if it exists,
    and adds it to the context.
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
        context['vote'] = (
            ChoiceVote.objects
            .filter(
                users__in=[self.request.user],
                choice__question=self.get_object()
            )
            .first()
        )
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
    and :model:`polls.ChoiceVote`. This view handles the logic for voting,
    including adding, changing, or preventing a duplicate vote for a specific
    choice. It updates the vote count for both the old and new choices when
    applicable, and provides feedback to the user regarding the vote's status.

    If the user selects the same choice they already voted for, an information
    message is displayed without updating the vote.

    **Context**
    ``question``
         The specific instance of :model:`polls.Question` identified by the
         `question_id`.
    ``selected_choice``
         The specific instance of :model:`polls.Choice` the user selected to
         vote for.
    ``user_previous_vote``
         The user's previous vote, if it exists, for the given question.

    **Template:**
    :template:`polls/detail.html`
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
        user_previous_vote = ChoiceVote.objects.filter(
            choice__question=question, users=request.user
        ).first()

        if user_previous_vote and user_previous_vote.choice == selected_choice:
            messages.info(
                request, "You have already voted for this choice."
            )
            return HttpResponseRedirect(
                reverse("polls:results", args=(question.id,))
            )

        if user_previous_vote:
            user_previous_vote.users.remove(request.user)
            user_previous_vote.choice.votes = F('votes') - 1
            user_previous_vote.choice.save()
            user_previous_vote.save()

        user_vote, created = ChoiceVote.objects.get_or_create(
            choice=selected_choice
        )
        user_vote.users.add(request.user)
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        messages.success(request, "Your vote was successfully submitted.")
        return HttpResponseRedirect(
            reverse("polls:results", args=(question.id,))
        )

    except (KeyError, Choice.DoesNotExist):
        error_message = "You didn't select a valid choice. Please try again."
        messages.error(request, error_message)

        return render(
            request, "polls/detail.html", {
                "question": question,
                "error_message": error_message,
            }
        )


@login_required
def delete_vote(request, question_id):
    """
    Handles the deletion of a user's vote for a question related to
    :model:`polls.Question` and :model:`polls.ChoiceVote`. This view allows
    users to confirm and remove their vote for a particular choice, and updates
    the vote count for the associated choice. If the user has not voted on the
    question, an error message is displayed, and they are redirected back to
    the question's detail view. If a vote is found and the user confirms the
    deletion (via a POST request), the vote is deleted.

    **Context**
    ``question``
         The instance of :model:`polls.Question` identified by `question_id`.
    ``vote``
         The instance of :model:`polls.ChoiceVote` representing the user's vote
         on the question. If the user has voted, this is passed to
         the confirmation template for display.
         If the user hasn't voted, this is `None`.

    **Template:**
    :template:`polls/delete.html` (GET request for confirmation)
    """
    question = get_object_or_404(Question, pk=question_id)
    votes = ChoiceVote.objects.filter(
        users=request.user, choice__question=question
    )

    if not votes.exists():
        messages.error(request, "You have not voted on this question.")
        return HttpResponseRedirect(reverse("polls:detail", args=(question.id,)))

    if request.method == "POST":
        for vote in votes:
            vote.users.remove(request.user)
            vote.choice.votes = F('votes') - 1
            vote.choice.save()
            vote.save()

        messages.success(request, "Your vote has been successfully deleted.")
        return HttpResponseRedirect(reverse("polls:detail", args=(question.id,)))

    return render(
        request, "polls/delete.html", {
            "question": question,
            "vote": votes.first(),
        }
    )
