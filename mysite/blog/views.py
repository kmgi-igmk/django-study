from django.views.generic import DetailView, ListView
from blog.models import Post

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

class PostDetailsView(DetailView):
    model = Post
    pk_url_kwarg = 'post_id'
    template_name = 'post_details.html'
    context_object_name = 'post'
