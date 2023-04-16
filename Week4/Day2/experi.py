import numpy as np

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
board_origin=np.array([
    [0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0], 
    [0, 0, 1, 0, 1, 0], 
    [1, 0, 0, 1, 0, 0], 
    [0, 1, 1, 0, 1, 0], 
    [1, 0, 0, 1, 0, 0]
    ])       

blank_board=np.array([[0,0,0],[0,0,0],[0,0,0]])
rows,col = np.where(board_origin==1)
live_positions=[(item,col[i]) for i,item in enumerate(rows)]

def run(board):
    print(board,0)
    q=1
    while True:
        new_board=Live.calc(board_origin)
        print(new_board,q)
        if (board==new_board).all():
            print(Live.calc(new_board),q+1)
            return 'worked'
        else:
            board=new_board
        q+=1
            
        
print(run(board_origin))