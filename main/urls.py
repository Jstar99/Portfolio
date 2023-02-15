from django.urls import path
from . import views


urlpatterns = [
    path("", views.home),
    path("home/", views.home),
    path("ennead/", views.ProjectEnnead),
    path("socialsite/", views.SocialBook),
    path("discordbot/", views.Bot),
    path("sudokusolver/", views.SudokuSolver),
    path("musicplayer/", views.MusicPlayer),
    path("contact/", views.Contact),
    
]
 