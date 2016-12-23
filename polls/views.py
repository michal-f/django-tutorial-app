# -*- coding: utf-8 -*-
import json
import urllib

from vanilla import CreateView, DeleteView, ListView, UpdateView
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.translation import ugettext as _

from .models import Choice, Question
from .forms import QuestionForm, QuestionCreate


class LoggedInMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)


class IndexView(LoggedInMixin, generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    model = Question
    paginate_by = 5

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')


class DetailView(LoggedInMixin, generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(LoggedInMixin, generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


@login_required
def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': p, 'error_message': "You didn't select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


# ############### [ VANILLA VIEWS ] ###################
class ListQuestion(ListView):
    model = Question


class CreateQuestion(CreateView):
    model = Question
    form_class = QuestionCreate
    success_url = reverse_lazy('polls:index')


class EditQuestion(UpdateView):
    model = Question
    form_class = QuestionForm
    success_url = reverse_lazy('polls:index')


class DeleteQuestion(DeleteView):
    model = Question
    success_url = reverse_lazy('polls:index')


# ############### [ AJAX VIEWS ] ###################
class AjaxView(generic.View):
    """
    Ajax POST Requests Handler - Dynamic Content Edition Functionality.
    """

    def post(self, request, **kwargs):
        # print "\n", 80 * "=", "\n", _('>>> IN >>>'), _('Ajax'), ('Post'), urllib.unquote_plus(
        #     self.request._body).decode(
        #     "utf-8"), "\n", 80 * "="
        # ajax_request = urllib.unquote_plus(self.request._body).decode("utf-8").split("&")
        data = {'data':'response data tekst'}
        print "RETURNING RESPONSE"
        return HttpResponse("RESPONSE")


        #
        # if len(ajax_request) > 0:
        #     question_id = int(ajax_request[0].split("=")[1].strip())
        #     action = ajax_request[1].split("=")[1].strip()
        #     value = ajax_request[2].split("=")[1].strip()
        #     q = Question.objects.get(pk=question_id)
        #
        #     # [action: DELETE CHOICE]
        #     if action == "del" and len(value) > 0:
        #         try:
        #             c = q.choice_set.get(choice_text__exact=value)
        #             c.delete()
        #             data = {"result": "ok"}
        #         except Exception:
        #             data = {"result": _("nothing to delete!")}
        #
        #     # [action: ADD CHOICE]
        #     elif action == "add":
        #         try:
        #             print q.choice_set.get(choice_text__exact=value)
        #             print "\n", _('>>>>> choice is already in database!'), "\n"
        #             data = {"result": "dup"}
        #         except Exception:
        #             q.choice_set.create(choice_text=value, votes=0)
        #             data = {"result": "ok", 'user_id': self.request.user.id, 'name': self.request.user.username}
        #
        #     # [action: VOTE +]
        #     elif action == "voteAdd":
        #         try:
        #             selected_choice = q.choice_set.get(choice_text__exact=value)
        #         except (KeyError, Choice.DoesNotExist):
        #             data = {"result": "not_added"}
        #             print "choice not found-vote not added!"
        #         else:
        #             selected_choice.votes += 1
        #             vote_count = selected_choice.votes
        #             selected_choice.save()
        #             data = {"result": "added", "vote_count": vote_count}
        #
        #     # [action: VOTE -]
        #     elif action == "voteRem":
        #         try:
        #             selected_choice = q.choice_set.get(choice_text__exact=value)
        #         except (KeyError, Choice.DoesNotExist):
        #             data = {"result": "not_added"}
        #             print "choice not found - vote not removed!"
        #         else:
        #             if selected_choice.votes < 1:
        #                 print "no votes, nothing to remove"
        #                 data = {"result": "no_votes"}
        #             else:
        #                 selected_choice.votes -= 1
        #                 vote_count = selected_choice.votes
        #                 selected_choice.save()
        #                 print "1 vote removed"
        #                 data = {"result": "removed", "vote_count": vote_count}
        #
        #     # [action: QUESTION TEXT UPDATE]
        #     elif action == "questionUpdate":
        #         try:
        #             q.question_text = value
        #             q.save()
        #         except (KeyError, Choice.DoesNotExist):
        #             data = {"result": "question_not_updated"}
        #             print "error in question update!"
        #         else:
        #             data = {"result": "updated"}
        #
        #     # [action: ALL CHOICES]
        #     elif action == "getChoices":
        #         print '= Get Choices => Question ID:', value, ' post data ->'
        #         try:
        #             choice_list = Question.objects.get(pk=value.strip())
        #             choices = choice_list.choice_set.all()
        #             print
        #         except (KeyError, Choice.DoesNotExist):
        #             data = {"result": "all_choices_failed"}
        #             print "error in retrieving all choices update!"
        #         else:
        #             response_data = ""
        #             for i in choices:
        #                 response_data += str(i) + ';' + str(i.votes) + '\n'
        #             data = {"result": "all_choices", "question_id": value, "question_txt": choice_list.question_text,
        #                     "choices": response_data}
        #     else:
        #         print "[No action recognized]"
        #
        #     responsx = json.dumps(data)
        #     print responsx
        #     print "\n", 80 * "=", "\n", _('<<< OUT <<< '), _('request'), _('successfully'), _('processed'), _(
        #         'returning'), _('response'), "\n", 80 * "=", "\n"

            # return HttpResponse(responsx)


ajax_view = AjaxView.as_view()
