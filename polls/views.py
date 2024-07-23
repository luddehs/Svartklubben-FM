from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:10]


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
            context['vote'] = ChoiceVote.objects.get(users__in=[self.request.user], choice__question=self.get_object())
            print(f'Choice {context["vote"].choice.id}')
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
        user_vote = ChoiceVote(choice=selected_choice)
        user_vote.save()
        if request.user not in user_vote.users.all():
            user_vote.users.add(request.user)
            user_vote.save()
            selected_choice.votes = F("votes") + 1
            selected_choice.save()
            previous_votes = ChoiceVote.objects.filter(choice__question=question)
            for vote in previous_votes:
                if vote.choice != selected_choice:
                    if request.user in vote.users.all():
                        vote.users.remove(request.user)
                        vote.choice.votes -= 1
                        vote.save()
                        vote.choice.save()
            
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
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
    vote = ChoiceVote.objects.get(users__in=[request.user], choice__question=question)
    if request.POST:
        print('should delete')
        vote.users.remove(request.user)
        vote.choice.votes -= 1
        vote.save()
        vote.choice.save()
        return HttpResponseRedirect(reverse("polls:detail", args=(question.id,)))
    return render(request, "polls/delete.html",
                {
                    "question": question,
                    "vote": vote,
                    "error_message": "You didn't select a choice.",
                },
    )
