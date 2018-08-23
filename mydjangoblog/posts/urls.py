from django.conf.urls import url, include
from . import views as posts_views
from django.views.generic import ListView, DetailView
from .models import Post

urlpatterns = [
    url(r'^$', ListView.as_view(
       queryset = Post.objects.all().order_by("-fecha"),
       template_name = "lista_post.html",
       paginate_by = 4), name = "lista"
    ),

    url(r'^(?P<id>\d+)/(?P<slug>[\w-]+)/$', DetailView.as_view(
        model = Post,
        template_name = "post_solo.html"), name = "solo"),

    url(r'^contacto/$', posts_views.contacto, name="contacto"),
]
