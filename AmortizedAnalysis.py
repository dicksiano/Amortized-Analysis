F = open("log.txt","w")  

def log(i, cost):
        # Logging cost associated with "i" insertions
        F.write("{0} {1}\n".format(i+1, cost))

def doubleSize(cost, size):
        # 2N operations required to allocate the memory - Malloc
        cost = cost + 2 * size

        # N operations to copy the previous elements
        cost = cost + size

        # Update size
        size = 2 * size

        return cost, size        

def main():
    n = int(input())
    
    dynamicArray = []
    size = 1
    cost = 0
    
    for i in range(0,n):
        # Insert new element in the array
        dynamicArray.append(i)

        # Adding a new element takes constant time - O(1)
        cost  = cost + 1 

        # Check if the Data Structure has no extra space
        if(size == len(dynamicArray)):
            cost, size = doubleSize(cost, size)

        # Logging
        log(i, cost)
    
    F.close()

if __name__ == '__main__':
    main()