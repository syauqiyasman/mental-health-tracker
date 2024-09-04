from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306275752',
        'name': 'Syauqi Muhammad Yasman',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
