def sortAlgorithm(S):
    
    if len(S) > 1:

        #separate list into two halves
        mid = len(S) / 2
        lArray = S[:mid]
        rArray = S[mid:]

        #recursive calls to sorting algorithm on each half of array
        sortAlgorithm(left)
        sortAlgorithm(right)

        #assigning variables for traversal of the arrays
        i = 0
        j = 0
        k = 0
        
        while i < len(lArray) and j < len(rArray):
            
            if lArray[i] < rArray[j]:
                
              #use value from left array (i.e. left half)
              S[k] = lArray[i]
              i += 1
              
            else:
                
                S[k] = rArray[j]
                j += 1
                
            k += 1

        #for the remaining values in the array
        while i < len(lArray):
            
            S[k] = lArray[i]
            i += 1
            k += 1

        while j < len(rArray):
            
            S[k] = rArray[j]
            j += 1
            k += 1


def binarySearch(S, m, n, x):

    if r >= 1: #base case

        mid = m + (n-1)/2

        if S[mid] == x: #element (x) found at the middle of the array

            return True

        elif S[mid] > x: #x is smaller than value at S[mid]

            return binarySearch(S, m, mid-1, x) #recursive call, check left subarray

        else: #x is bigger than value at S[mid]

            return binarySearch(S, m, mid+1, x) #recursive call, check right subarray

    else:

        return False #element does not exist in the array S


#Write main function to implement the sort algorithm on an array 'S',
#followed by the binarySearch to find a specific element in the array,
#array composed of randolmly generated numbers.
