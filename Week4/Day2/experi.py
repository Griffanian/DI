import numpy as np

class Live:
    instances=[]
    def __init__(self,pos:tuple) -> None:
        self.pos=pos
        Live.instances.append(pos)

    def live_neigbours(pos:tuple[int,int]):
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

    def dies(pos:tuple):
        board[pos[0],pos[1]] = 0
    def born(pos:tuple):
        board[pos[0],pos[1]] = 1
# board=np.array([
#     [0, 0, 1, 0, 0, 0],
#     [1, 0, 0, 1, 0, 0], 
#     [0, 0, 1, 0, 1, 0], 
#     [1, 0, 0, 1, 0, 0], 
#     [0, 1, 1, 0, 1, 0], 
#     [1, 0, 0, 1, 0, 0]
#     ])       
board=np.array([[1,0,1],[1,1,0],[1,0,1]])
rows,col = np.where(board==1)
live_positions=[(item,col[i]) for i,item in enumerate(rows)]

def run():
    finished = 0
    
    for i in range(5):
        last_board=board
        # print(*board,sep='\n')
        for i,item in enumerate(board):
            for x,value in enumerate(item):
                neighbors = Live.live_neigbours((i,x))
                if value == 1:
                    live = True
                else:
                    live = False

                if live == True and neighbors < 2:
                    Live.dies((i,x))

                if live == True and neighbors > 3:
                    Live.dies((i,x))
                if live == False and neighbors == 3:
                    Live.born((i,x))
        if np.array_equiv(board,last_board):
            finished+=1
            print(*board,sep='\n')
            print(*last_board,sep='\n')
        print(finished)
run()

