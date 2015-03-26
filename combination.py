import numpy as np

def getCombination(n):
	c = (n*n -n)/2
	A = np.zeros(c,dtype = np.uint16)
	B = np.zeros(c,dtype = np.uint16)
	addingArray = np.array(range(1,n), dtype=np.uint16)
	start = 0
	end = 0


	for element in range(n-1):
		start = end
		end = start + n-1 - element
		A[start:end] = element
		
	print("Array A finished")
	
	end = 0
	
	for element in range(n-1):
		start = end
		end = start + n-1 - element

		elementListLen = n-1 - element
		
		
		
		
		B[start:end] = addingArray[element:]
		
	print("Array B finished")
	return np.dstack((A,B))

x = getCombination(50000)
