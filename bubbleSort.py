# Basic script to perform 

def bubbleSort(array):
    arrayLength = len(array)
    
    # Go through all elements
    for i in range(arrayLength):
        
        # i elements are already in place
        for j in range(0, arrayLength-i-1):
            
            # Go through array from 0 to n-i-1
            # Swap if the next element is greater
            
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j] #swapping itself

                
                
sampleArray = [67, 24, 88, 35, 27, 99, 119, 245, 11]

# Execude the method
bubbleSort(sampleArray)

# Print results
print ("Sorted array:")
for i in range(len(sampleArray)):
    print ("%d" %sampleArray[i])
 
