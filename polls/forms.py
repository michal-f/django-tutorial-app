# -*- coding: utf-8 -*-

from django import forms

from .models import Question, Choice


class QuestionCreate(forms.ModelForm):
    question_text = forms.CharField(widget=forms.TextInput(
        attrs={'id': 'question_single', 'class': 'yes_display bluetxt form-control-lg btn-responsive'}))

    class Meta:
        model = Question
        fields = ['question_text']


class QuestionForm(forms.ModelForm):
    question_text = forms.CharField(widget=forms.TextInput(
        attrs={'id': 'question_single', 'class': 'yes_display bluetxt form-control-lg btn-responsive'}))
    questions = forms.ModelChoiceField(queryset=Question.objects.all(), widget=forms.Select(
        attrs={'id': 'question_dropdown', 'class': 'no_display dropdown bluetxt form-control-lg btn-responsive'}))

    class Meta:
        model = Question
        fields = ['question_text']


class ChoiceForm(forms.ModelForm):
    choice_text = forms.CharField(widget=forms.TextInput(attrs={'id': 'wrapper', 'class': 'bluetxt form-control-lg'}))

    class Meta:
        model = Choice
        fields = ['choice_text']