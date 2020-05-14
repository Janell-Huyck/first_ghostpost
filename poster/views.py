from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from poster.models import GhostPost


def index(request):

    posts = GhostPost.objects.all().order_by('submission_time')
    context = {'posts': posts}
    return render(request, 'index.html', context)


def boasts(request):
    context = {}
    if GhostPost.objects.filter(is_boast=True):
        context['posts'] = GhostPost.objects.filter(is_boast=True)
    else:
        context['posts'] = ""
        context['error_message'] = "Sorry no such items exist."
    return render(request, 'index.html', context)


def roasts(request):
    context = {}
    if GhostPost.objects.filter(is_boast=False):
        context['posts'] = GhostPost.objects.filter(is_boast=False)
    else:
        context['posts'] = ""
        context['error_message'] = "Sorry no such items exist."
    return render(request, 'index.html', context)


def detail_like_view(request, pk):
    ghost_post = GhostPost.objects.get(pk=pk)
    ghost_post.up_votes += 1
    ghost_post.save()
    return HttpResponseRedirect(reverse('post_detail', kwargs={'pk': pk}))


def detail_dislike_view(request, pk):
    ghost_post = GhostPost.objects.get(pk=pk)
    ghost_post.down_votes += 1
    ghost_post.save()
    return HttpResponseRedirect(reverse('post_detail', kwargs={'pk': pk}))


def post_detail(request, pk):
    post = get_object_or_404(GhostPost, pk=pk)
    return render(request, 'post_detail.html', {'post': post})
