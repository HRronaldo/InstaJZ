from django.views.generic import TemplateView, ListView, DetailView     # 告诉页面从django自带的views里面的generic views去导入TemplateView

from Insta.models import Post

class HelloWorld(TemplateView):
    template_name = 'test.html'

class PostsView(ListView):
    model = Post
    template_name = 'index.html'    

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


 

