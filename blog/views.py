from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .models import *
from django.contrib.auth import login, logout

from .forms import *


# user login

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    context = {
        'title': 'Войти',
        'form': form
    }
    return render(request, 'blog/login.html', context)


# user logout
def user_logout(request):
    logout(request)
    return redirect('home')


# user register
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {"form": form})


# Search

class Search(ListView):
    template_name = 'blog/search.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        return Blog.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post__list'] = Blog.objects.all()[:3]
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context

# Add blog

def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'blog/addpost.html', {'form': form, 'title': 'Добавление статьи'})



# Home page
class Home(ListView):
    model = Blog
    queryset = Blog.objects.all()[:2]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post__list'] = Blog.objects.all()[:3]
        context['post__slider'] = Blog.objects.all()[:7]
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        return context


# about page
def about(request):
    context = {
        "title": "ABOUT US",
        "subtitle": "MORE ABOUT US!"
    }
    return render(request, 'blog/about.html', context)


# view all posts
class ViewAllPosts(ListView):
    model = Blog
    queryset = Blog.objects.all()
    paginate_by = 4

    template_name = 'blog/blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post__list'] = Blog.objects.all()[:3]
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        return context


# Detail view
class BlogDetail(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post__list'] = Blog.objects.all()[:3]
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        return context


# Filter by Category
class BlogByCategory(ListView):
    template_name = 'blog/category_list.html'
    context_object_name = 'blog'
    paginate_by = 4
    allow_empty = False
    model = Blog
    queryset = Blog.objects.all()

    def get_queryset(self):
        return Blog.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        context['post__list'] = Blog.objects.all()[:3]
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        return context


# Filter by Tags
class BlogByTag(ListView):
    template_name = 'blog/tags_list.html'
    context_object_name = 'blog'
    paginate_by = 4
    allow_empty = False
    model = Blog
    queryset = Blog.objects.all()

    def get_queryset(self):
        return Blog.objects.filter(tag__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Tag.objects.get(slug=self.kwargs['slug'])
        context['post__list'] = Blog.objects.all()[:3]
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        return context

# def contact(request):
#     if request.method == "POST":
#         message_name = request.POST['message-name']
#         message_email = request.POST['message-email']
#         message = request.POST['message']
#
#         send_mail(
#             message_name,
#             message,
#             message_email,
#             ['muhammadrizotursunboev8@gmail.com']
#         )
#
#         return render(request, 'blog/contact.html', {"message_name": message_name})
#
#     else:
#         return render(request, 'blog/contact.html', {})


# def Register(requests):
#     return render(requests, 'blog/register.html')


# class RegisterUser(DataMixin, CreateView):
#     form_class = UserCreationForm
#     template_name = 'blog/register.html'
#     success_url = reverse_lazy('login')
#
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title="Register")
#         return dict(list(context.items()) + list(c_def.items()))
#
#
