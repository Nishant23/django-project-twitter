# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.utils import ErrorList
from django.shortcuts import render, get_object_or_404
from .models import Tweet
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .forms import *
from django import forms
from .mixins import FormUserNeededMixin, UserOwnerMixin
from django.urls import reverse_lazy
from django.db.models import Q

# Create your views here.

class TweetCreateView(FormUserNeededMixin, CreateView):
     form_class = TweetModelForm
     template_name = 'tweets/create_view.html'
     # success_url = reverse_lazy("tweet:detail")
     # login_url = '/admin/'
     # queryset = Tweet.objects.all()
     # fields = ['user', 'content']

     # def form_valid(self, form):
     #     if self.request.user.is_authenticated():
     #         form.instance.user = self.request.user
     #         return super(TweetCreateView, self).form_valid(form)
     #     else:
     #         form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to continue"])
     #         return self.form_invalid(form)


class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    success_url = reverse_lazy("tweet:detail")
    template_name = 'tweets/update_view.html'

class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    success_url = reverse_lazy("tweet:list")
    template_name = 'tweets/delete_view.html'




class TweetDetailView(DetailView):
    template_name = 'tweets/detail-view.html'
    queryset = Tweet.objects.all()

    def get_object(self):
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(Tweet, id=pk)
        return obj

class TweetListView(ListView):
    template_name = 'tweets/list-view.html'

    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(Q(content__icontains=query) | Q(user__username__icontains = query))
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        context['create_form'] = TweetModelForm()
        context['create_url'] = reverse_lazy("tweet:create")
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

# def tweet_detail_view(request, pk):
#     tweet = get_object_or_404(Tweet, id=pk)
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
