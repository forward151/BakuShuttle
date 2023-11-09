from django.shortcuts import render
from django.views import View
# Create your views here.


class Home(View):
    template_name = "shuttle_driver.html"
    # template_name = "base.html"

    def get(self, request):
        context = {}

        return render(request, self.template_name, context)

