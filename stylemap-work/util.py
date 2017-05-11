from Columns import columns
from cell import Cell

'''
return location of given column and row
param: string column, int row
'''
def location(column, row):
	return column + str(row)

'''
@deprecated
def prodSize():
	columnSize = input("column size? : ")
	rowSize = input("row size? : ")

	return [columnSize, rowSize]
'''

'''
return product cell of given index
param: int index(index of product), int columnSize, int rowSize
'''
def findProd(index, cSize, rSize):
	clist = [2, 0, 1]

	prodColumn = clist[index % 3]
	prodRow = (index - 1) / 3
	rowStart = 3

	return Cell(columns((cSize * prodColumn) + 1), (rSize * prodRow) + (prodRow + rowStart))