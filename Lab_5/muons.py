#Patrick Roscio
#Lab_5: muons.py
#Description: Creates an 8x8 grid with random variables up to 500. Returns the Mazimum and Minimum values as well
# as their position in the grid.
import random

list_dimension = 8

particle_detector_grid = [[0 for i in range(list_dimension)]for j in range(list_dimension)]

for i in range(len(particle_detector_grid)):
    for g in range(len(particle_detector_grid[i])):
        value = random.randrange(501)
        particle_detector_grid[i][g] = value

max_value= 0
min_value=501 
for i in range(len(particle_detector_grid)):
    for y in range(len(particle_detector_grid[i])):
        test_value = particle_detector_grid[i][y]
        if max_value <= test_value:
             max_value = test_value
             max_position = [i,y]
        elif min_value >= test_value:
             min_value = test_value
             min_position = [i,y]
     
print(f"The Maximum value is: {max_value} at position ( {max_position[0]+1} , {max_position[1]+1} )")
print(f"The Minimum value is: {min_value} at position ( {min_position[0]+1} , {min_position[1]+1} )")

print("Detector Grid Output: ") 
for l in range(len(particle_detector_grid)):
        print(particle_detector_grid[l])            
    