from django.shortcuts import RequestContext,HttpResponse, render_to_response, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from models import Post
from forms import PostForm
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
        return HttpResponse("Please login first.<br><a href='login'>Login</a>")


@login_required(login_url='/login')
def new_post(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect(reverse("home"))

    return render_to_response('form.html',{
        'form': form
    }, RequestContext(request))


@login_required(login_url='/login')
def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)

    return render_to_response('detail.html', {
        'post': post
    }, RequestContext(request))


@login_required(login_url='/login')
def delete_post(request, pk):
    post = Post.objects.filter(id=pk).delete()

    return redirect(reverse('home'))