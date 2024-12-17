def printArr(arr):
    for row in arr:
        print(row)
    print()

def clean(arr, x, y):
    if arr[x][y] == 1:
        arr[x][y] = 0 

def check(arr):
    for row in arr:
        if 1 in row:  
            return True
    return False

# Directions: right (0,1), down (1,0), left (0,-1), up (-1,0)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direction_index = 0  # Start moving right

# Get room status
print("Enter the status of the rooms (0 for clean; 1 for dirty):")
arr1 = []
for i in range(2):
    row = []
    for j in range(2):
        a = int(input(f"Status of room ({i}, {j}): "))
        row.append(a)
    arr1.append(row)

x, y = 0, 0  #Start cleaning from the first room

while True:
    printArr(arr1)
    if not check(arr1):
        break
    clean(arr1, x, y)
    
    #Move to the next room in the current direction
    dx, dy = directions[direction_index]
    new_x, new_y = x + dx, y + dy
    
    #Check bounds
    if 0 <= new_x < 2 and 0 <= new_y < 2:
        x, y = new_x, new_y
    else:
        #Change direction(turn right)
        direction_index = (direction_index + 1) % 4
        dx, dy = directions[direction_index]
        x, y = x + dx, y + dy  #Move in the new direction

print("All rooms are cleaned!")
