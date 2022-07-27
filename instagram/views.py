from django.views.generic import ListView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import InstagramPost

post_list = ListView.as_view(model=InstagramPost)

# def post_list(request):
#     # print(request)
#     # print(f"request.method: {request.method}")
#     # print(f"request.META: {request.META}")
#     # print(f"request.GET: {request.GET}")
#     # print(f"request.POST: {request.POST}")
#     # print(f"request.FILES: {request.FILES}")
#     # print(f"request.body: {request.body}")
#
#     qs = InstagramPost.objects.all()
#     q = request.GET.get('q', '')
#
#     if q:
#         qs = qs.filter(message__icontains=q)
#
#     return render(request, 'instagram/post_list.html', {
#         'post_list': qs,
#         'q': q,
#     })


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    response = HttpResponse()
    response.write('Hello World')
    response.write('Hello World')
    response.write('Hello World')
    return response
