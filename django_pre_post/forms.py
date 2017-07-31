from django import forms
from django_pre_post.models import Questionaire


class CSRFQuestionaireForm(forms.Form):
    model = Questionaire
    fields = []
