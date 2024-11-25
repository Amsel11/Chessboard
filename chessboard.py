import numpy as np
import matplotlib.pyplot as plt 
import sys
import random
import os

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

import random

def coloured_grids(grid, n):
    mask = (grid == -1)
    colours = np.random.rand(n, 3)
    result = np.zeros((n, *grid.shape, 3))
    result[:, mask] = colours[:, np.newaxis, :]
    
    return result[0]

size = 4
boards = chessboardmaker(size,get_steps(size))
print (boards[1])

for i in range(len(boards)):
    boards[i] = coloured_grids(boards[i],2)


save_dir = "pattern_images"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

for i in range(len(boards)):
    plt.figure(figsize=(5,5))
    plt.imshow(boards[i], cmap='binary')
    plt.axis('off')
    #plt.title(f'Step {i//2 + 1}{"" if i%2==0 else " inverted"}')
    plt.savefig(f'pattern_step_{i//2 + 1}_{"original" if i%2==0 else "inverted"}.jpg', 
                dpi=300,
                bbox_inches='tight',
                pad_inches=0)  # Removed padding
    plt.close()

plt.figure(figsize=(5*len(get_steps(size)*2), 5))
for i in range(len(boards)):
    plt.subplot(1, len(get_steps(size)*2), i+1)

    plt.imshow(boards[i], cmap='binary')  # using list index
    plt.title(f'Step {i+1}')
plt.show()
