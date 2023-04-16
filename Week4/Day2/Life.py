import pygame as py
import numpy as np
import time

# Define the size of the grid
grid_size_num=100
grid_size_tuple = (grid_size_num, grid_size_num)
cell_size = 800/grid_size_num

grid=np.zeros(grid_size_tuple)
board_origin= np.random.randint(2, size=(8, 8))
print(board_origin)
cols_num=len(board_origin)
board_origin
py.init()

# create a screen:
screen = py.display.set_mode((600,600))
done = False



# (red,green,blue)
red = (255,0,0)
black=(0,0,0)
color = (255,255,255)
# never ending loop now:
screen.fill(color)
class Screen:
    def display_grid(num):
        global size,new_board
        size=int(600/num)
        new_board=np.array([[] for i in range(size)] for i in range(size)) 
    def display_live(x,y):
        py.draw.rect(screen,color,(((x-1)*size),(cols_num-y)*size,size,size))
        py.display.update()
    def display_dead(x,y):
        py.draw.rect(screen,black,(((x-1)*size),(cols_num-y)*size,size,size))
        py.display.update()

class Live:
    instances=[]
    def __init__(self,pos:tuple) -> None:
        self.pos=pos
        Live.instances.append(pos)

    def live_neigbours(board,pos:tuple[int,int]):
        neigbours=0
        for i in range(-1,2):
            row=pos[0]+i
            for x in range(-1,2):
                col=pos[1]+x 
                if row!=pos[0] or col!=pos[1]: 
                    if row >= 0 and col >= 0:
                        if row < len(board) and col < len(board[1]):
                            if board[row][col] == 1:
                                neigbours+=1
        return neigbours

    def dies(board,pos:tuple):
        board[pos[0],pos[1]] = 0
    def born(board,pos:tuple):
        board[pos[0],pos[1]] = 1

    def calc(board):
        new_board=board
        for i,item in enumerate(board):
            for x,value in enumerate(item):
                neighbors = Live.live_neigbours(board,(i,x))
                if value == 1:
                    live = True
                else:
                    live = False

                if live == True and (neighbors < 2):
                    Live.dies(new_board,(i,x))
                if live == True and (neighbors > 3):
                    Live.dies(new_board,(i,x))
                if live == False and (neighbors == 3):
                    Live.born(new_board,(i,x))
        return new_board

board=board_origin
paused = False

while done == False:
    for event in py.event.get():
        if event.type == py.QUIT:
            done = True
        if event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                paused = not paused  # toggle pause state

    Screen.display_grid(cols_num)
    if not paused:
        for i,rows in enumerate(board):
            for q,cols in enumerate(board):
                if board[i][q] == 1:
                    Screen.display_live(cols_num-i,q+1)
                else:
                    Screen.display_dead(cols_num-i,q+1)
        new_board=Live.calc(board)

