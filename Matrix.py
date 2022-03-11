class Matrix:
  #Call in the constructor
  #Assign lin => each line of the matrix
  #Assign col => each coll of matrix
	def __init__(self, matrix):
		self.col = []
		self.lin = []

		self.newMatrix = []
		
		for index, line in enumerate(matrix):
			self.lin.append(line)

			temp = []

			for i in range(len(line)):

				temp.append(matrix[i][index])
			self.col.append(temp)
  
  #Swap create a new matrix
  #First collumn becomes last line and so on
	@staticmethod
	def RotateMatrix(self):
		for i in range(len(self.lin)):
			self.newMatrix.append(self.col[(len(self.lin)-1)-i])
		return self.newMatrix
  
  #Print the result matrix
	def PrintMatrix(self):
		self.RotateMatrix(self)
		for i in self.newMatrix:
			print(i)

matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

m = Matrix(matrix)
print(m.PrintMatrix())
