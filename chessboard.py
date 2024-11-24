import numpy as np
import matplotlib.pyplot as plt 

def get_steps(size):
    k = int(np.log2(size))  # gets the power of 2 for the size (e.g., 64 -> 6)
    return [2**i for i in range(k)]  # creates [1,2,4,8,16,32] for size=64

def chessboardmaker(size, steps): 
    board = np.zeros(size*size)
    grids = []
    for k in range(len(steps)):
        for j in range(0,len(board),1):
            row = j // size
            #print (row, j) 
            #print (j)
            board[steps[k]*j:steps[k]*(j+2)] = ((-1)**j)*(-1)**row
        board_flipped = -1*board
        grids.append((board.reshape(size,size)))
        grids.append(board_flipped.reshape(size,size))
        board = np.zeros(size**2)
        #grids.append(-1*board.reshape(size,size))     # inverted

    return grids

size = 64
boards = chessboardmaker(size,[32])
firstone = boards[1]
firstoneflipped = -1*boards[1]
print (firstone,firstoneflipped)
plt.figure(figsize=(5*len(get_steps(size)*2), 5))
for i in range(len(boards)):
    plt.subplot(1, len(get_steps(size)*2), i+1)
    plt.imshow(boards[i], cmap='binary')  # using list index
    plt.title(f'Step {i+1}')
plt.show()
