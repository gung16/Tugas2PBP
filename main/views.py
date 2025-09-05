from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'aplikasi' : 'TokoGungPedia',
        'name': 'I Gusti Ngurah Agung Airlangga Putra',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)