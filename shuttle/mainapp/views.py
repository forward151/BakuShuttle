from django.shortcuts import render
from django.views import View
# Create your views here.


class HomeClientView(View):
    template_name = "shuttle_client.html"
    # template_name = "base.html"

    def get(self, request):
        context = {}

        return render(request, self.template_name, context)


class HomeDriverView(View):
    template_name = "shuttle_driver.html"

    def get(self, request):
        context = {}

        return render(request, self.template_name, context)
