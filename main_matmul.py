# Matrix Multiplication 
#This code is for matrix multiplication by scratch without using any libraries

# define a main function
def mat_mul():
	x1 = int(input("Enter No. of rows of 1st Matrix: "))
	x2 = int(input("Enter No. of columns of 1st Matrix: "))

	y1 = int(input("Enter No. of rows of 2nd Matrix: "))

	y2 = int(input("Enter No. of columns of 2nd Matrix: "))


	#Checking if Matrix Multiplication is possible for the given dimensions: (Columns of first should be equal to Rows of the Second)
	if x2!= y1:
		print("Matrix multiplication not possible")
		return 0

	mat_1 = []

	mat_2 = []

	mat1_2 = []

	print("Enter the values of the 1st Matrix: ")

	for i in range(x1): # iterating i over all the rows of the matrix
		x=[]
		for j in range(x2): # iterating j over all the columns of the matrix
			x.append(int(input()))
		mat_1.append(x)

	for a in range(x1):
		for b in range(x2):
			print(mat_1[a][b], end =" ")
		print() 


	print("Enter the values of the 2nd Matrix: ")

	for i in range(y1): # iterating i over all the rows of the matrix
		y=[]
		for j in range(y2): # iterating j over all the columns of the matrix
			y.append(int(input()))
		mat_2.append(y)

	for a in range(y1):
		for b in range(y2):
			print(mat_2[a][b], end =" ")
		print()


	for x in range(x1):
		a = []
		for y in range(y2):
			a.append(0)
		mat1_2.append(a)
    
	for x in range(x1):
		for y in range(y2):
			mat1_2[x][y]
	print("Result is : ")

	# Iterating through the rows of 1st matrix
	for x in range(len(mat_1)):
		for y in range(len(mat_2[0])):
			for z in range(len(mat_2)):
				mat1_2[x][y] += (mat_1[x][z] * mat_2[z][y])

	for r in mat1_2:
		print(r)
        


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
	# call the main function
	mat_mul()
