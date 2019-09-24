# Librerias Future
from __future__ import unicode_literals

# Librerias en carpetas locales
from ..models import PyWParameter
from ..models.post import PyPost
from .web_father import FatherDetailView, FatherListView

def _web_parameter():
    web_parameter = {}
    for parametro in PyWParameter.objects.all():
        web_parameter[parametro.name] = parametro.value
    return web_parameter

POST_FIELDS = [
    {'string': 'Título', 'field': 'title'},
    {'string': 'Creado en', 'field': 'created_on'},
    {'string': 'Contenido', 'field': 'content'},
]

POST_FIELDS_SHORT = ['title','content','created_on']

class BlogView(FatherListView):
    model = PyPost
    template_name = 'blog/blog.html'
    fields = POST_FIELDS
    paginate_by = 8
    extend_from = None
    url_web_post = None
    header_title = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['extend_from'] = self.extend_from
        context['url_web_post'] = self.url_web_post
        context['header_title'] = self.header_title

        return context

class PostDetailView(FatherDetailView):
    model = PyPost
    template_name = 'blog/post.html'
    extend_from = None
    url_web_post = None
    header_title = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['extend_from'] = self.extend_from
        context['url_web_post'] = self.url_web_post
        context['header_title'] = self.header_title
        return context
