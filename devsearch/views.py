from django.shortcuts import render


def handler404(request, exception):
    return render(request, '404.html', status=404)


def main_view(request):
    return render(request, 'main.html')


