from django.urls import path
from . import views

urlpatterns = [
    path("Tic_tac_toe", views.Tic_tac_toe, name='Tic_tac_toe'),
    path("single_Tic_tac_toe", views.single_Tic_tac_toe, name='single_Tic_tac_toe'),
    path("DuckHunt", views.DuckHunt, name='DuckHunt'),
    path("Math_Puzzle", views.Math_Puzzle, name='Math_Puzzle'),
    path("PuzzleGame15", views.PuzzleGame15, name='PuzzleGame15'),
    path("Puzzle_image", views.Puzzle_image, name='Puzzle_image'),
    path("need_for", views.need_for, name='need_for'),
    path("", views.WebApps),
    path("WebApps", views.WebApps, name='WebApps'),
    path("bubble_shooter", views.bubble_shooter, name='bubble_shooter'),
    path("Taptap", views.Taptap, name='Taptap'),
    path("piano_tiles", views.piano_tiles, name='piano_tiles'),
    path("piano_tiles2", views.piano_tiles2, name='piano_tiles2'),
    path("Infinite_Runner_game", views.Infinite_Runner_game, name='Infinite_Runner_game'),
    path("menja", views.menja, name='menja'),
    path("Monster_Wants_Candy", views.Monster_Wants_Candy, name='Monster_Wants_Candy'),
    path("pinball", views.pinball, name='pinball'),
    path("rabit", views.rabit, name='rabit'),
    path("tower_blocks", views.tower_blocks, name='tower_blocks'),
    path("The_Cube", views.The_Cube, name='The_Cube'),
]
