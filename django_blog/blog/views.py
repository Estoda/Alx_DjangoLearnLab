from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import CustomerUserCreationForm, CommentForm
from django.urls import reverse_lazy
from .models import Post, Comment, Tag
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q

def register(request):
    if request.method == 'POST':
        form = CustomerUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomerUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'blog/profile.html')

def HomeView(request):
    return render(request, '/root/ComplateProject/myenv/Alx_DjangoLearnLab/django_blog/blog/templates/blog/base.html')

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author  = self.request.user
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author  = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


def PostCommentsView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        comment_form = CommentForm

    context = {
        'post': post,
        'comment': comments,
        'comment_form': comment_form
    }
    return render(request, 'blog/post_comments.html', context)

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('post-comments', kwargs={'pk': self.kwargs['pk']})

class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def get_success_url(self):
        return reverse_lazy('post-comments', kwargs={'pk': self.object.post.pk})
    
class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('post-comments', kwargs={'pk': self.object.post.pk})

def search(request):
    query = request.GET.get('q')
    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()
    else:
        results = Post.objects.none()
    return render(request, 'blog/search_results.html', {'result': results})

def post_by_tag(request, tag_name):
    tag = Tag.objects.get(name=tag_name)
    posts = tag.posts.all()
    return render(request, 'blog/post_by_tag.html', {'tag': tag, 'posts': posts})


# blog/views.py
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from .models import Post
from taggit.models import Tag

class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/post_list_by_tag.html'  # Create this template
    context_object_name = 'posts'
    paginate_by = 5  # Optional: for pagination

    def get_queryset(self):
        tag_slug = self.kwargs.get('tag_slug')
        self.tag = get_object_or_404(Tag, slug=tag_slug)
        return Post.objects.filter(tags__in=[self.tag])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context




