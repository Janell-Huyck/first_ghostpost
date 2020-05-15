from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from poster.forms import GhostPostForm
from poster.models import GhostPost


def index(request):
    posts = GhostPost.objects.all().order_by('submission_time')
    context = {'posts': posts}
    return render(request, 'index.html', context)


def posts_like_view(request, pk):
    ghost_post = GhostPost.objects.get(pk=pk)
    ghost_post.up_votes += 1
    ghost_post.save()
    return HttpResponseRedirect(reverse('home', ))


def posts_dislike_view(request, pk):
    ghost_post = GhostPost.objects.get(pk=pk)
    ghost_post.down_votes += 1
    ghost_post.save()
    return HttpResponseRedirect(reverse('home', ))


def boasts(request):
    context = {}
    if GhostPost.objects.filter(is_boast=True):
        context['posts'] = GhostPost.objects.filter(is_boast=True)
    else:
        context['posts'] = ""
        context['error_message'] = "Sorry no such items exist."
    return render(request, 'boasts.html', context)


def boasts_like_view(request, pk):
    ghost_post = GhostPost.objects.get(pk=pk)
    ghost_post.up_votes += 1
    ghost_post.save()
    return HttpResponseRedirect(reverse('boasts'))


def boasts_dislike_view(request, pk):
    ghost_post = GhostPost.objects.get(pk=pk)
    ghost_post.down_votes += 1
    ghost_post.save()
    return HttpResponseRedirect(reverse('boasts'))


def roasts(request):
    context = {}
    if GhostPost.objects.filter(is_boast=False):
        context['posts'] = GhostPost.objects.filter(is_boast=False)
    else:
        context['posts'] = ""
        context['error_message'] = "Sorry no such items exist."
    return render(request, 'roasts.html', context)


def roasts_like_view(request, pk):
    ghost_post = GhostPost.objects.get(pk=pk)
    ghost_post.up_votes += 1
    ghost_post.save()
    return HttpResponseRedirect(reverse('roasts'))


def roasts_dislike_view(request, pk):
    ghost_post = GhostPost.objects.get(pk=pk)
    ghost_post.down_votes += 1
    ghost_post.save()
    return HttpResponseRedirect(reverse('roasts'))


def post_detail(request, pk):
    post = get_object_or_404(GhostPost, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


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


def new_post_view(request):
    html = "new_post.html/"
    if request.method == "POST":
        form = GhostPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            GhostPost.objects.create(
                is_boast=data['is_boast'],
                title=data['title'],
                text=data['text'],
                up_votes=0,
                down_votes=0,
                magic_string="aaaaaa"
            )
        return HttpResponseRedirect(reverse('home'))
    form = GhostPostForm()
    return render(request, html, {'form': form})
    form = GhostPostForm()
