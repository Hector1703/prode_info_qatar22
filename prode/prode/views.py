from django.shortcuts import render


def inicio(request):
    templete_name="inicio.html"
    usuario={
        "nombre": "Hector",
        "apellido": "Larre"
    }
    
    ctx={
        "user_dict": usuario
    }
    return render (request, templete_name, ctx)