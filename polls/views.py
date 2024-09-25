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
    model = Question
    template_name = "polls/results.html"


@login_required
def vote(request, question_id):
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
    question = get_object_or_404(Question, pk=question_id)
    try:
        vote = ChoiceVote.objects.get(users__in=[request.user], choice__question=question)
        if request.POST:
            vote.users.remove(request.user)
            vote.choice.votes -= 1
            vote.save()
            vote.choice.save()
            messages.success(request, "Your vote has been successfully deleted.")
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
