from django.shortcuts import render, HttpResponse
from django.views.generic import View, TemplateView


# before
# # Create your views here.
# def indexpage(request):
#   return render(request, 'indexpage/index.html')


# option 2
# class IndexPageView(View):
#   template_name = 'indexpage/index.html'
#
#   def get(self, request):
#     args = {
#       'spam': 'eggs',
#       'foo': 'bar'
#     }
#     return render(request,self.template_name, args)


# option 3

class IndexPageView(TemplateView):
  template_name = 'indexpage/index.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context.update({
      'spam': 'eggs',
      'foo': 'bar'
    })
    return context

  #  how you can make post

  def post(self, request):
    return HttpResponse('Post is ok')

