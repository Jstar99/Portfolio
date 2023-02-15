from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "main/home.html")

def ProjectEnnead(request):
    return render(request, "main/ennead.html")

def SocialBook(request):
    return render(request, "main/socialbook.html")

def Bot(request):
    return render(request, "main/bot.html")

def MusicPlayer(request):
    return render(request, "main/musicPlayer.html")

def SudokuSolver(request):
    return render(request, "main/sudoku.html")

def Contact(request):
    return render(request, "main/contact.html")