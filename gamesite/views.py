from django.shortcuts import render

# Create your views here.

def Tic_tac_toe(request):
    
    return render(request, 'Tic-tac-toe/index.html')

def single_Tic_tac_toe(request):
    
    return render(request, 'Tic-tac-toe/TicTacToe-AI/index.html')


def DuckHunt(request):
    
    return render(request, 'DuckHunt/index.html')

def Math_Puzzle(request):
    
    return render(request, 'Math-Puzzle/puzzle.html')


def PuzzleGame15(request):
    
    return render(request, 'PuzzleGame15/index.html')


def Puzzle_image(request):
    
    return render(request, 'Puzzle-image/index.html')

def need_for(request):
    
    return render(request, 'need-for/index.html')

def WebApps(request):
    
    return render(request, 'WebApps/index.html')

def Taptap(request):
    
    return render(request, 'Taptap/index.html')
    
def piano_tiles2(request):
    
    return render(request, 'piano_tiles2/index.html')

def piano_tiles(request):
    
    return render(request, 'piano_tiles/index.html')


def Allgames(request):
    
    return render(request, 'anime/index.html')


def Infinite_Runner_game(request):
    
    return render(request, 'Infinite_Runner_game/index.html')

def menja(request):
    
    return render(request, 'menja/index.html')


def Monster_Wants_Candy(request):
    
    return render(request, 'Monster_Wants_Candy/index.html')


def pinball(request):
    
    return render(request, 'pinball/index.html')


def rabit(request):
    
    return render(request, 'rabit/index.html')


def tower_blocks(request):
    
    return render(request, 'tower_blocks/index.html')

def The_Cube(request):
    
    return render(request, 'The_Cube/index.html')


def bubble_shooter(request):
    
    return render(request, 'bubble_shooter/index.html')


def flipcard_memory_game(request):
    
    return render(request, 'FlipCard/flipcard_memory_game/index.html')

def FLIP_CARD_MEMORY_GAME(request):
    
    return render(request, 'FlipCard/FLIP_CARD_MEMORY_GAME/index.html')

def Memory_FlipCard_Game(request):
    
    return render(request, 'FlipCard/Memory_FlipCard_Game/index.html')


def picflip(request):
    
    return render(request, 'FlipCard/picflip/index.html')