

'''
	@Author : sbhat
	Date: 13 June 2018
	Thanks to Willians for inventing such a nice algorithm. 
	https://www.programiz.com/dsa/heap-sort
	https://www.hackerearth.com/practice/algorithms/sorting/heap-sort/tutorial/

	logic:  heap is complete binary tree , so we can represent it as an arry.
			we consider tree is given in the format of array where left child can be obtained by the index 2*index+1 and 
			right child using 2*i+2. 

			
			So To build a max-heap from any tree, we can thus start heapifying each sub-tree 
			from the bottom up and end up with a max-heap after the function is applied 
			on all the elements including the root element.

			Since its a complete binary tree the first index of non-leaf node is given by n/2 - 1
			So start from n/2-1 and reach the root (i.e index 0)

			first we construct max heap by heapifying the input array from the index n/2-1 to i and apply heapy recursively.

			after that to sort we apply below logic
			1. We swap largest element which is at index 0 (as root will always contain max element in max heap and root is at index 0).
				with last element and now we have places the largest element at last index so we can ingonre that from the rest of the logic
				so we heapify the array leaving last index.
				in this way we continue by leaving last index every time until we exahust the array(max heap constructed above) 
	'''

def heapify(arr,n,i):

	left =  2*i + 1

	right = 2*i + 2

	largest = i 

	if left < n and arr[left] > arr[largest]:
		largest = left
		

	if right < n and arr[right] > arr[largest]:
		largest = right
		
	if largest != i:
		arr[largest],arr[i] = arr[i],arr[largest] 
		#heapify again with largest index
		heapify(arr,n,largest)




def heapSort(arr):
	'''
	constrcut a max heap by heapifying
	'''
	n = len(arr)
	for i in range(int(n/2)-1,-1,-1):
		heapify(arr,n,i)

	print arr

  	'''
  	 arrange elements in a sorted order by applying above mentioned algorithm
  	'''

  	for i in range(n-1,0,-1):
  		'''
  		swap root at index 0 with last inex(i index which start from n-1)
  		'''
  		arr[0],arr[i] = arr[i],arr[0] 
  		'''
  		now that u swapped (altered the heap) u need to apply heapify again on 0 the index only up to i the index (n==i)
  		'''
  		heapify(arr,i,0)



if __name__== '__main__':

	#arr = list(map(int, input().strip().split()))
	#arr = [4,5,6,3,7,8,1,10]
	arr = [1,12,9,5,6,10]
	print(arr)
 	heapSort(arr)
 	print(arr)


	


