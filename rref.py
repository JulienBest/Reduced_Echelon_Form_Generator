import random

rowCount = 0
ColumnCount = 0

def ToReducedRowEchelonForm(M):
	M2 = M
	global rowCount
	global columnCount
	if not M2: return
	lead = 0
	rowCount = len(M2)
	columnCount = len(M2[0])
	for r in range(rowCount):
		if lead >= columnCount:
			return
		i = r
		while M2[i][lead] == 0:
			i += 1
			if i == rowCount:
				i = r
				lead += 1
				if columnCount == lead:
					return
		M2[i],M2[r] = M2[r],M2[i]
		lv = M2[r][lead]
		M2[r] = [ mrx / float(lv) for mrx in M2[r]]
		for i in range(rowCount):
			if i != r:
				lv = M2[i][lead]
				M2[i] = [ iv - lv*rv for rv,iv in zip(M2[r],M2[i])]
		lead += 1
	return M2

def printMatrix(M):
	output = ''
	for i in range(rowCount):
		output += '\n'
		for j in range(columnCount):
			if (M[i][j] == 0):
				M[i][j] = abs(M[i][j])
			if(M[i][j].is_integer() == False):
				output += str(M[i][j]) + ', '
			else:
				output += str(int(M[i][j])) + '   '
	print(output)

def isRound(M):
	for i in range(rowCount):
		for j in range(columnCount):
			if (M[i][j].is_integer() == False or M[i][j]>100 or M[i][j]<-100):
				return False
	return True



def genMatrix(row, col):
	mnew = [[2 for x in range(col)] for y in range(row)]
	for i in range(row):
		for j in range(col):
			mnew[i][j] = float(random.randint(0,9))
	return mnew


def getRoundRREF(row, col):
	while True: #emulates do while
		matrix = genMatrix(row,col)
		backup = [[2 for x in range(col)] for y in range(row)]
		for i in range(row):
			for j in range(col):
				backup[i][j] = matrix[i][j]
		rref = ToReducedRowEchelonForm(matrix)
		if (isRound(rref)):
			return backup



mtx = [
   [ 1, 2, -1, -4],
   [ 2, 3, -1, -11],
   [-2, 0, -3, 22],]

#printMatrix(ToReducedRowEchelonForm(mtx))

mtx2 = getRoundRREF(4,5)
printMatrix(mtx2)
printMatrix(ToReducedRowEchelonForm(mtx2))
