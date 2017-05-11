from openpyxl import Workbook
from openpyxl import load_workbook

from Columns import Columns1, Columns2, columns

class Cell:

	__sheet = None

	def __init__(self, column, row):
		self.__column = column
		self.__row = row

	def location(self):
		return self.__column + str(self.__row)

	def viewLocation(self, column, row):
		return column + str(row)

	def getSheet(self):
		return self.__sheet

	def setSheet(self, sheet):
		self.__sheet = sheet

	def getColumn(self):
		return self.__column

	def getRow(self):
		return self.__row

	def moveCell(self, cDelta, rDelta):
		currentColumn = self.__column
		currentRow = self.__row

		if (len(self.__column) > 1):
			currentColumnList = Columns2()
		else:
			currentColumnList = Columns1()

		currentColumnIndex = currentColumnList.index(currentColumn)

		resColumnIndex = currentColumnIndex + cDelta + 1
		resColumn = columns(resColumnIndex)

		resRow = currentRow + rDelta

		self.__column = resColumn
		self.__row = resRow

		return self

	def viewMoveCell(self, cDelta, rDelta):
		currentColumn = self.__column
		currentRow = self.__row

		if (len(self.__column) > 1):
			currentColumnList = Columns2()
		else:
			currentColumnList = Columns1()

		currentColumnIndex = currentColumnList.index(currentColumn)

		resColumnIndex = currentColumnIndex + cDelta + 1
		resColumn = columns(resColumnIndex)

		resRow = currentRow + rDelta

		return self.viewLocation(resColumn, resRow)

	def getValue(self):
		return self.__sheet[self.location()].value

	def getValue(self, location):
		return self.__sheet[location].value

	def viewMoveValue(self, cDelta, rDelta):
		currentColumn = self.__column
		currentRow = self.__row

		if (len(self.__column) > 1):
			currentColumnList = Columns2()
		else:
			currentColumnList = Columns1()

		currentColumnIndex = currentColumnList.index(currentColumn)

		resColumnIndex = currentColumnIndex + cDelta + 1
		resColumn = columns(resColumnIndex)

		resRow = currentRow + rDelta

		return self.getValue(self.viewLocation(resColumn, resRow))
