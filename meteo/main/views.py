from django.views.generic import TemplateView, View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
import requests

from app.settings import FLAG, API_TOKEN


@method_decorator(login_required, name="dispatch")
class IndexPageView(TemplateView):
    template_name = "main/index.html"

    def post(self, request):
        value = request.POST.get("choice")
        if not value:
            value = "0"

        uuid = request.COOKIES.get("uuid")
        r = requests.get(
            f"http://chatgpt.local:8000/api/v1/retirement/set/{uuid}",
            params={"retirement": 64, "choice": value},
            headers={"Authorization": f"Basic {API_TOKEN}"},
        )
        if not r.ok:
            headers = "\n".join([f"{e}: {r.request.headers[e]}" for e in r.request.headers])
            return HttpResponse(f"Error detected in {r.request.url}\nDEBUG Headers:\n\n{headers}", content_type="text/plain")
        return redirect("/me")


@method_decorator(login_required, name="dispatch")
class RetirementPageView(View):
    template_name = "main/me.html"

    def get(self, request, *args, **kwargs):
        uuid = request.COOKIES.get("uuid")
        r = requests.get(
            f"http://chatgpt.local:8000/api/v1/retirement/get/{uuid}",
            headers={"Authorization": f"Basic {API_TOKEN}"},
        )
        retirement = None
        if r.ok:
            retirement = r.json()["retirement"]
        return render(
            request, self.template_name, {"retirement": retirement, "flag": FLAG}
        )