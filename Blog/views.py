from django.shortcuts import RequestContext,HttpResponse, render_to_response, redirect, get_object_or_404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from models import Post, Comment
from forms import PostForm, CommentForm
# Create your views here.


def hello(request):
    return HttpResponse("Hello World")


def home(request):
    if request.user.is_authenticated():
        posts = Post.objects.filter(user=request.user).order_by("-created")
        return render_to_response('index.html', {
            'posts': posts
            }, RequestContext(request))
    else:
        return HttpResponse("Please login first.<br><a href='login'>Login</a> or <a href='register'>Register</a>")


@login_required(login_url='/login')
def new_post(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect(reverse("home"))

    return render_to_response('form.html', {
        'form': form
    }, RequestContext(request))


@login_required(login_url='/login')
def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    comments = Comment.objects.filter(post=pk)

    return render_to_response('detail.html', {
        'post': post,
        'comments': comments
    }, RequestContext(request))


@login_required(login_url='/login')
def delete_post(request, pk):
    Post.objects.filter(id=pk).delete()

    return redirect(reverse('home'))

@login_required(login_url='/login')
def edit_post(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))

    return render_to_response('edit.html', {
        'form': form,
        'post': post
    }, RequestContext(request))


@login_required(login_url='/login')
def add_comment(request, pk):
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = Post.objects.get(id=pk)
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return render_to_response('detail.html', {}, RequestContext(request))


@login_required(login_url='/login')
def delete_comment(request, pk):
    Comment.objects.get(id=pk).delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))