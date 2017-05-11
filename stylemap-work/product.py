from cell import Cell

class Product:

	def __init__(self, cell, prodType):
		self.__cell = cell
		self.__prodType = prodType
		
		if self.__prodType == 'top':
			self.topProduct()
		if self.__prodType == 'bottom':
			self.bottomProduct()
		if self.__prodType == 'outer':
			self.outerProduct()
		if self.__prodType == 'acc':
			self.accProduct()

	def getType(self):
		return self.__prodType

	def topProduct(self):
		self.data = dict()

		self.data['name']= self.__cell.viewMoveValue(2, 0)
		self.data['description']= self.__cell.viewMoveValue(2, 2)
		self.data['color'] = self.__cell.viewMoveValue(2, 3)
		
		size1 = dict()
		size1['name'] = self.__cell.viewMoveValue(1, 4)
		size1['shoulder'] = self.__cell.viewMoveValue(3, 4)
		size1['chest'] = self.__cell.viewMoveValue(5, 4)
		size1['length'] = self.__cell.viewMoveValue(7, 4)
		size1['sleeve'] = self.__cell.viewMoveValue(9, 4)

		self.data['size1'] = size1
		self.data['isSize1'] = size1['shoulder'] or size1['chest'] or size1['length'] or size1['sleeve']


		size2 = dict()
		size2['name'] = self.__cell.viewMoveValue(1, 5)
		size2['shoulder'] = self.__cell.viewMoveValue(3, 5)
		size2['chest'] = self.__cell.viewMoveValue(5, 5)
		size2['length'] = self.__cell.viewMoveValue(7, 5)
		size2['sleeve'] = self.__cell.viewMoveValue(9, 5)

		self.data['size2'] = size2
		self.data['isSize2'] = size2['shoulder'] or size2['chest'] or size2['length'] or size2['sleeve']

		size3 = dict()
		size3['name'] = self.__cell.viewMoveValue(1, 6)
		size3['shoulder'] = self.__cell.viewMoveValue(3, 6)
		size3['chest'] = self.__cell.viewMoveValue(5, 6)
		size3['length'] = self.__cell.viewMoveValue(7, 6)
		size3['sleeve'] = self.__cell.viewMoveValue(9, 6)

		self.data['size3'] = size3
		self.data['isSize3'] = size3['shoulder'] or size3['chest'] or size3['length'] or size3['sleeve']

		self.data['price'] = self.__cell.viewMoveValue(2, 7)
		self.data['composition'] = self.__cell.viewMoveValue(2, 8)
		self.data['laundry'] = self.__cell.viewMoveValue(2, 9)

	def bottomProduct(self):
		self.data = dict()

		self.data['name']= self.__cell.viewMoveValue(2, 0)
		self.data['description']= self.__cell.viewMoveValue(2, 2)
		self.data['color'] = self.__cell.viewMoveValue(2, 3)
		
		size1 = dict()
		size1['name'] = self.__cell.viewMoveValue(1, 4)
		size1['waist'] = self.__cell.viewMoveValue(3, 4)
		size1['length'] = self.__cell.viewMoveValue(5, 4)

		self.data['size1'] = size1
		self.data['isSize1'] = size1['waist'] or size1['length']

		size2 = dict()
		size2['name'] = self.__cell.viewMoveValue(1, 5)
		size2['waist'] = self.__cell.viewMoveValue(3, 5)
		size2['length'] = self.__cell.viewMoveValue(5, 5)

		self.data['size2'] = size2
		self.data['isSize2'] = size2['waist'] or size2['length']

		size3 = dict()
		size3['name'] = self.__cell.viewMoveValue(1, 6)
		size3['waist'] = self.__cell.viewMoveValue(3, 6)
		size3['length'] = self.__cell.viewMoveValue(5, 6)

		self.data['size3'] = size3
		self.data['isSize3'] = size3['waist'] or size3['length']

		self.data['price'] = self.__cell.viewMoveValue(2, 7)
		self.data['composition'] = self.__cell.viewMoveValue(2, 8)
		self.data['laundry'] = self.__cell.viewMoveValue(2, 9)

	def outerProduct(self):
		self.data = dict()

		self.data['name']= self.__cell.viewMoveValue(2, 0)
		self.data['description']= self.__cell.viewMoveValue(2, 2)
		self.data['color'] = self.__cell.viewMoveValue(2, 3)
		
		size1 = dict()
		size1['name'] = self.__cell.viewMoveValue(1, 4)
		size1['shoulder'] = self.__cell.viewMoveValue(3, 4)
		size1['chest'] = self.__cell.viewMoveValue(5, 4)
		size1['length'] = self.__cell.viewMoveValue(7, 4)
		size1['sleeve'] = self.__cell.viewMoveValue(9, 4)

		self.data['size1'] = size1
		self.data['isSize1'] = size1['shoulder'] or size1['chest'] or size1['length'] or size1['sleeve']


		size2 = dict()
		size2['name'] = self.__cell.viewMoveValue(1, 5)
		size2['shoulder'] = self.__cell.viewMoveValue(3, 5)
		size2['chest'] = self.__cell.viewMoveValue(5, 5)
		size2['length'] = self.__cell.viewMoveValue(7, 5)
		size2['sleeve'] = self.__cell.viewMoveValue(9, 5)

		self.data['size2'] = size2
		self.data['isSize2'] = size2['shoulder'] or size2['chest'] or size2['length'] or size2['sleeve']

		size3 = dict()
		size3['name'] = self.__cell.viewMoveValue(1, 6)
		size3['shoulder'] = self.__cell.viewMoveValue(3, 6)
		size3['chest'] = self.__cell.viewMoveValue(5, 6)
		size3['length'] = self.__cell.viewMoveValue(7, 6)
		size3['sleeve'] = self.__cell.viewMoveValue(9, 6)

		self.data['size3'] = size3
		self.data['isSize3'] = size3['shoulder'] or size3['chest'] or size3['length'] or size3['sleeve']

		self.data['price'] = self.__cell.viewMoveValue(2, 7)
		self.data['composition'] = self.__cell.viewMoveValue(2, 8)
		self.data['laundry'] = self.__cell.viewMoveValue(2, 9)

	def accProduct(self):
		self.data = dict()

		self.data['name']= self.__cell.viewMoveValue(2, 0)
		self.data['description']= self.__cell.viewMoveValue(2, 2)
		self.data['color'] = self.__cell.viewMoveValue(2, 3)
		
		size = dict()
		size['width'] = self.__cell.viewMoveValue(3, 4)
		size['height'] = self.__cell.viewMoveValue(5, 4)
		size['depth'] = self.__cell.viewMoveValue(7, 4)
		size['strap'] = self.__cell.viewMoveValue(9, 4)

		self.data['size'] = size

		self.data['price'] = self.__cell.viewMoveValue(2, 7)
		self.data['composition'] = self.__cell.viewMoveValue(2, 8)
		self.data['laundry'] = self.__cell.viewMoveValue(2, 9)

	def getData(self):
		return self.data