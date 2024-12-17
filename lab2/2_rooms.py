def printArr(arr):
    n=len(arr)
    print(arr[0],arr[1])

def clean(arr,vac):
    if(arr[vac] == 1):
        arr[vac]=0
    if(arr[vac] == 0):
        return
    
def check(arr):
    if(arr[0]==0 and arr[1]==0):
        return False
    else:
        return True
        
print("Enter the status of the room(0 for clean; 1 for dirty):")
arr1 = []
for i in range(0,2):
    a=int(input("Status of the room %d:" %i))
    arr1.append(a)

vac=0
while(True):
    printArr(arr1)
    if(check(arr1) == False):
        break
    clean(arr1,vac)
    if(vac==0):
        vac=1
    else:
        vac=0
print("Rooms are cleaned!")
