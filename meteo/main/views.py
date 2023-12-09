from django.views.generic import TemplateView, View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse, JsonResponse

import requests

from app.settings import FLAG


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
        )
        if not r.ok:
            headers = {e.lower(): r.request.headers[e] for e in r.request.headers}
            return JsonResponse(
                {
                    "error": True,
                    "response": r.text,
                    "url": r.request.url,
                    "headers": headers,
                },
                status=400,
            )
        return redirect("/me")


@method_decorator(login_required, name="dispatch")
class RetirementPageView(View):
    template_name = "main/me.html"

    def get(self, request, *args, **kwargs):
        uuid = request.COOKIES.get("uuid")
        r = requests.get(
            f"http://chatgpt.local:8000/api/v1/retirement/get/{uuid}",
        )
        retirement = None

        if not r.ok:
            headers = {e.lower(): r.request.headers[e] for e in r.request.headers}
            return JsonResponse(
                {
                    "error": True,
                    "response": r.text,
                    "url": r.request.url,
                    "headers": headers,
                },
                status=400,
            )
        retirement = r.json()["retirement"]
        return render(
            request, self.template_name, {"retirement": retirement, "flag": FLAG}
        )
