import pgzrun
from board import draw_square

def draw():
    screen.fill("dark orange")
    draw_square((98654,4543),"black")
    draw_square((859483,549538),"white")

pgzrun.go()
