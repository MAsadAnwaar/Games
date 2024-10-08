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
    path("flipcard_memory_game", views.flipcard_memory_game, name='flipcard_memory_game'),
    path("FLIP_CARD_MEMORY_GAME", views.FLIP_CARD_MEMORY_GAME, name='FLIP_CARD_MEMORY_GAME'),
    path("Memory_FlipCard_Game", views.Memory_FlipCard_Game, name='Memory_FlipCard_Game'),
    path("picflip", views.picflip, name='picflip'),
    path("animal_memory", views.animal_memory, name='animal_memory'),
    path("fend_project_memory_game", views.fend_project_memory_game, name='fend_project_memory_game'),
    path("Flip_and_Find", views.Flip_and_Find, name='Flip_and_Find'),
    path("hs_memorygame/", views.hs_memorygame, name='hs_memorygame'),
    path("memory___game", views.memory___game, name='memory___game'),
    path("Memory__games", views.Memory__games, name='Memory__games'),
    path("memory_game", views.memory_game, name='memory_game'),
    path("Memory_Game_2", views.Memory_Game_2, name='Memory_Game_2'),
    path("memory_game_3", views.memory_game_3, name='memory_game_3'),
    
]
