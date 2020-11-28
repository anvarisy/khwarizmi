from django.shortcuts import render
from django.views import View
# Create your views here.

class ViewHomePage(View):
    template = 'index.html'
    def get(self, request):
        return render(request, self.template,{'title':'Alkhwarizmi'})

