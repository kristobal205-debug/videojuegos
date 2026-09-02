from django.shortcuts import render
from faker import Faker

# Create your views here.
def generar_juegos(request):
    fake = Faker("es")
    juegos = []
    for i in range(25):
        juegos.append({
            "nombre": fake.word(),
            "descripcion": fake.text(),
        })
    return render(request, "juegos.html", {"juegos": juegos})