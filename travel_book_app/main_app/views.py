from django.shortcuts import render, get_object_or_404


def index(request):
    return render(request, "main_app/index.html")


# def carousel():
#     list_photos_carousel = Image_caroussel.objects.all()
#     context = {"list_pictures": list_photos_carousel}
#     return context


def villes(request):
    return render(request, "main_app/villes.html")


def nantes(request):
    return render(request, "main_app/nantes.html")


def nice(request):
    return render(request, "main_app/nice.html")


def lehavre(request):
    return render(request, "main_app/lehavre.html")


def propos(request):
    return render(request, "main_app/propos.html")


# def partenaires(request):
#     partenaires = Producteurs.objects.all()
#     context = {"partenaires": partenaires}
#     return render(request, "main_app/partenaires.html", context)
