from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.models import User
from .models import Post, Comment
from .forms import CommentForm


# Create your views here.
@login_required
def index(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'feed/index.html', context)

@login_required
def new(request):
	return render(request, 'feed/new.html')

def get_user_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'feed/user_profile.html', {"user":user})

class PostListView(ListView):
	model = Post 
	template_name = 'feed/index.html'
	context_object_name = 'posts'
	ordering = ['-dateposted']
	paginate_by = 3

class PostDetailView(DetailView):
	model = Post 

class PostCreateView(CreateView):
	model = Post 
	fields = ['caption', 'imageurl']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
"""
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.TextField()
	dateposted = models.DateTimeField(default=timezone.now)
"""
def post_detailview(request): 
	if request.method == 'POST': 
		form = CommentForm(request.POST or None) 
		if form.is_valid(): 
			content = request.cleaned_data.get('body') 
			comment = Comment.objects.create(body = content) 
			comment.save() 
			return redirect(post.get_absolute_url())
		else: 
			form = CommentForm() 

		context ={ 
		'comment_form':form, 
		} 
		return render(request, 'feed/post_detail.html', context)






















