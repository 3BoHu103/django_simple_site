from django.shortcuts import render


def index(request):
    return render(request, 'posts/index.html')


def page_not_found_view(request, exception):
    return render(request, 'posts/404.html', {"path": request.path}, status=404)


def server_error(request):
    return render(request, 'posts/500.html', status=500)
