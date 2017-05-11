from openpyxl import Workbook
from openpyxl import load_workbook

from util import findProd

from product import Product

class Bottom:

	def __init__(self, sheet, cSize, rSize):
		self.__bottom = sheet
		self.__parsingList = list()

		index = 1
		while(True):
			currentProdCell = findProd(index, cSize, rSize)

			if (self.__bottom[currentProdCell.viewMoveCell(2, 0)].value != None):
				currentProdCell.setSheet(self.__bottom)
				self.__parsingList.append(currentProdCell)
				index += 1
			else:
				break


	def getCellList(self):
		return self.__parsingList

	def run(self, prods):
		self.productify(prods)

	def productify(self, prods):
		parsingList = self.getCellList()

		for cell in parsingList:
			product = Product(cell, 'bottom')

			prods.append(product)
			
