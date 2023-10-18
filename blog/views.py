from django.shortcuts import render, redirect,get_object_or_404
from .models import PostModel
from .forms import PostModelForm, PostUpdateForm, CommentForm
from django.contrib.auth.decorators import login_required


# Create your views here.
# def blogs_draft(request):
#     posts = PostModel.objects.all()
#     posts = PostModel.objects.filter().order_by('-date_created')
#     return render(request, "blog/draft.html", {'posts_draft':posts})

def ViewDraft(request):
    posts = PostModel.objects.all()
    posts = PostModel.objects.filter(status = 'draft')
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('draft')
    else:
        form = PostModelForm()
    context = {
        'draft_post': posts,
        'form': form
    }
    return render(request, 'blog/draft.html', context)

def push_draft(request,blog_id):
    post = get_object_or_404(PostModel,id =blog_id)
    post.status = 'published'
    post.save()
    return redirect('/')
# @login_required
# def blogs_draft(request):
#     posts = PostModel.objects.all()
#     if request.method == 'POST':
#         form = PostModelForm(request.POST)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.author = request.user
#             instance.save()
#             return redirect('blogs_draft')
#     else:
#         form = PostModelForm()
#     context = {
#         'posts': posts,
#         'form': form
#     }

#     return render(request, 'blog/draft.html', context)

@login_required
def index(request):
    posts = PostModel.objects.all()
    posts = PostModel.objects.filter(status = 'published')
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('blog-index')
    else:
        form = PostModelForm()
    context = {
        'posts': posts,
        'form': form
    }

    return render(request, 'blog/index.html', context)
    
@login_required
def post_detail2(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.user = request.user
            instance.post = post
            instance.save()
            return redirect('blog-post-detail2', pk=post.id)
    else:
        c_form = CommentForm()
    context = {
        'post': post,
        'c_form': c_form,
    }
    return render(request, 'blog/post_detail2.html', context)

@login_required
def post_detail(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.user = request.user
            instance.post = post
            instance.save()
            return redirect('blog-post-detail', pk=post.id)
    else:
        c_form = CommentForm()
    context = {
        'post': post,
        'c_form': c_form,
    }
    return render(request, 'blog/post_detail.html', context)

@login_required
def post_edit(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog-post-detail', pk=post.id)
    else:
        form = PostUpdateForm(instance=post)
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'blog/post_edit.html', context)

@login_required
def post_delete(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('draft')
    context = {
        'post': post
    }
    return render(request, 'blog/post_delete.html', context)
