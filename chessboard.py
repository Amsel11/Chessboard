import numpy as np
import matplotlib.pyplot as plt 
import sys
import random
import os

def get_steps(size):
    k = int(np.log2(size))  
    return [2**i for i in range(k)]  

def chessboardmaker(size, steps): 
    board = np.zeros(size*size)
    grids = []
    for k in range(len(steps)):
        for j in range(0,len(board),1):
            row = j // size
            board[steps[k]*j:steps[k]*(j+2)] = ((-1)**j)*(-1)**row
        board_flipped = -1*board
        grids.append((board.reshape(size,size)))
        grids.append(board_flipped.reshape(size,size))
        board = np.zeros(size**2)        
    return grids

boards = chessboardmaker(64,get_steps(64))

def coloured_grids1(grid):
    # Make sure to only change the elements which were "white"
    mask = (grid == -1)
    colour = np.random.rand(3)  
    result = np.zeros(grid.shape + (3,))  # More explicit way to add RGB dimension
    
    for i in range(3):  
        layer = result[:,:,i]  
        layer[mask] = colour[i]  
    
    return result

#We could ask for a directory
choice = input("Do you want to make a new folder[Y/n]: ").lower()
if choice.startswith('y'): 
    directory = input('give me the name of the directory: ').lower()
    save_dir = os.path.join(os.getcwd(), directory)
else:
    save_dir = os.path.join(os.getcwd(), "pattern_images")

os.makedirs(save_dir, exist_ok=True)

print ('You have made', len(boards),'until now.')
n = int(input("How many colours do you want to create for each board. Choose between 0 and 10: "))
for i in range(len(boards)):
    for k in range(n): 
        plt.figure(figsize=(5,5))
        # Create colored version of the pattern
        pattern = coloured_grids1(boards[i])
                #print(f"Pattern shape: {pattern.shape}") 
        
        plt.imshow(pattern)
        plt.axis('off')
        
        filename = f'new_pattern_step_{i//2 + 1}_{"original" if i%2==0 else "inverted"}_{k}.jpg'
        full_path = os.path.join(save_dir, filename)
        
        plt.savefig(full_path, 
                    dpi=300,
                    bbox_inches='tight',
                    pad_inches=0)  
        plt.close()

print(f"Files saved in: {save_dir}")