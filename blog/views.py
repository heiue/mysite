from django.shortcuts import render

from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse, request


# Create your views here.
# 使用Django的通用模板
class IndexView(ListView):
    template_name = 'blog/index.html'

    def get_queryset(self):
        return 'blog'

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super(IndexView, self).get_context_data()
        print(content)
        content['content'] = '内容'
        return content


class CBV(View):

    def get(self, request):
        print(request.GET)
        return render(request, 'blog/index.html', {'content': "cbv"})

    def post(self, request):
        print(request.COOKIES)
        return HttpResponse('b')
