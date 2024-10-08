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
    
    return render(request, 'index.html')

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

def animal_memory(request):
    
    return render(request, 'FlipCardNew/animal_memory/index.html')

def fend_project_memory_game(request):
    
    return render(request, 'FlipCardNew/fend_project_memory_game/index.html')
def Flip_and_Find(request):
    
    return render(request, 'FlipCardNew/Flip_and_Find/index.html')


# views.pyfrom django.shortcuts import render
from django.shortcuts import render
from .models import Card
from filpcardgameapi.models import Image
import random
from django.http import JsonResponse
def hs_memorygame(request):
    cards = list(Card.objects.all())
    backgrounds = list(Image.objects.all())

    if len(cards) < 16:
        raise ValueError("Not enough images in the database")

    if not backgrounds:
        raise ValueError("No background images in the database")

    max_level = len(backgrounds)
    level = int(request.GET.get('level', 1))

    if level > max_level:
        level = max_level

    selected_cards = random.sample(cards, 16) * 2
    random.shuffle(selected_cards)

    card_data = [{'id': i, 'image_url': card.image_url()} for i, card in enumerate(selected_cards)]
    background_image = backgrounds[level - 1].image_url.url

    unlocked_background_images = [bg.image_url.url for bg in backgrounds[:level]]

    # Pass the total number of containers (cards) to the template
    total_containers = 16  # Adjust if necessary based on your game logic

    return render(request, 'FlipCardNew/hs_memorygame/index.html', {
        'card_data': card_data,
        'background_image': background_image,
        'level': level,
        'max_level': max_level,
        'unlocked_background_images': unlocked_background_images,
        'total_containers': total_containers,  # Pass total containers to the template
    })



def memory___game(request):
    
    return render(request, 'FlipCardNew/memory___game/index.html')
def Memory__games(request):
    
    return render(request, 'FlipCardNew/Memory__games/index.html')
def memory_game(request):
    
    return render(request, 'FlipCardNew/memory_game/index.html')
def Memory_Game_2(request):
    
    return render(request, 'FlipCardNew/Memory_Game_2/index.html')
def memory_game_3(request):
    
    return render(request, 'FlipCardNew/memory_game_3/index.html')