from django.core.exceptions import PermissionDenied
from django_pre_post.forms import CSRFQuestionaireForm
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect
from django_pre_post.models import Questionaire, Question, Answer, Attempt
from django_pre_post.util import TemplateBoolean


class FillOutQuestionaire(UpdateView):
    model = Questionaire
    fields = ['name', 'questions']

    def get_object(self):
        obj = super(FillOutQuestionaire, self).get_object()
        if (not obj.public and obj.owner != self.request.user) and not self.request.user.is_superuser:
            raise PermissionDenied()
        self.object = obj
        return obj

    def post(self, request, *args, **kwargs):
        form = CSRFQuestionaireForm(request.POST)
        if form.is_valid():
            attempt = Attempt(questionaire=self.get_object(), owner=request.user)
            attempt.save()
            for item in request.POST:
                try:
                    question = Question.objects.get(id=item)
                    if question.get_type_display() == 'Multiple Choice':
                        answer = Answer(question=question, owner=request.user,
                                        attempt=attempt, multipleChoiceAnswer=request.POST[item])
                    elif question.get_type_display() == 'Numeric':
                        answer = Answer(question=question, owner=request.user,
                                        attempt=attempt, numericAnswer=request.POST[item])
                    else:
                        answer = Answer(question=question, owner=request.user,
                                        attempt=attempt, textAnswer=request.POST[item])
                    answer.save()
                except:
                    pass
        return HttpResponseRedirect('')

    def render_to_response(self, context, **response_kwargs):
        context['doingRankings'] = TemplateBoolean()
        return super(FillOutQuestionaire, self).render_to_response(context, **response_kwargs)


class FramelessQuestionaire(FillOutQuestionaire):
    template_name = "django_pre_post/frameless_questionaire.html"
