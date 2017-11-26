# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.utils import ErrorList
from django.shortcuts import render, get_object_or_404
from .models import Tweet
from django.views.generic import DetailView, ListView, CreateView
from .forms import *
from django import forms
from .mixins import FormUserNeededMixin

# Create your views here.

class TweetCreateView(FormUserNeededMixin, LoginRequiredMixin, CreateView):
     form_class = TweetModelForm
     template_name = 'tweets/forms.html'
     success_url = '/tweets/create'
     login_url = '/admin/'
     # queryset = Tweet.objects.all()
     # fields = ['user', 'content']

     # def form_valid(self, form):
     #     if self.request.user.is_authenticated():
     #         form.instance.user = self.request.user
     #         return super(TweetCreateView, self).form_valid(form)
     #     else:
     #         form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to continue"])
     #         return self.form_invalid(form)

class TweetDetailView(DetailView):
    template_name = 'tweets/detail-view.html'
    queryset = Tweet.objects.all()

    def get_object(self):
        pk = self.kwargs.get('id')
        obj = get_object_or_404(Tweet, id=pk)
        return obj

class TweetListView(ListView):
    template_name = 'tweets/list-view.html'
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        return context


# def tweet_create_view(request):
#     form = TweetModelForm(request.POST or None)
#
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.user = request.user
#         instance.save()
#
#     context = {
#         "form": form
#     }
#
#     return render(request, "tweets/forms.html", context)
#

# def tweet_detail_view(request, id):
#     tweet = get_object_or_404(Tweet, id=id)
#     context = {
#         "objects": tweet
#     }
#     return render(request, 'tweets/detail-view.html', context)
#
# def tweet_list_view(request):
#     tweets = Tweet.objects.all()
#     context = {
#         "objects": tweets
#     }
#     return render(request, 'tweets/list-view.html', context)
