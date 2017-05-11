import csv
from collections import OrderedDict
from product import Product
import datetime

class ProductWriter:
	def __init__(self):
		self.__fieldnames = ['Parent', 'parent_sku', 'post_title', 'post_name', 'ID', 'post_excerpt',
		'post_content', 'post_status', 'menu_order', 'post_date', 'post_parent', 'post_author', 'comment_status', 
		'sku', 'downloadable', 'virtual', 'visibility', 'stock_status', 'backorders', 'manage_stock', 'regular_price',
		'sale_price', 'weight', 'length', 'width', 'height', 'tax_status', 'featured', 'images', 'tax:product_type',
		'tax:product_cat', 'tax:product_tag', 'tax:product_shipping_class',
		'attribute:pa_color', 'attribute_data:pa_color', 'attribute:pa_size', 'attribute_data:pa_size']

		Form = OrderedDict.fromkeys(self.__fieldnames)
		self.rowForm = OrderedDict((key, '') for key, value in Form.items())

		self.nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	
	def run(self, prods, product_csv):
		writer = csv.DictWriter(product_csv, fieldnames=self.__fieldnames)
		writer.writeheader()

		for prod in prods:
			rows = self.product(prod)
			for row in rows:
				writer.writerow(row)

	def product(self, prod):
		res = list()

		parentRow = self.parentProduct(prod)
		childRows = self.childProduct(prod)

		res.append(parentRow)
		res += childRows

		return res

	def parentProduct(self, prod):
		row = self.rowForm.copy()

		row['post_title'] = prod.getData()['name']
		row['post_name'] = prod.getData()['name'].lower().replace(' ', '_')

		row['ID'] = 1

		excerpt = self.makePostExcerpt(prod)
		row['post_excerpt'] = excerpt

		row['post_status'] = 'publish'
		row['menu_order'] = 0
		row['post_date'] = self.nowTime

		row['post_parent'] = 0

		row['post_author'] = 2
		row['comment_status'] = 'open'

		#row['sku'] = 
		
		row['downloadable'] = 'no'
		row['virtual'] = 'no'

		row['visibility'] = 'visible'
		row['stock_status'] = 'instock'

		row['backorders'] = 'no'
		row['manage_stock'] = 'no'

		row['regular_price'] = prod.getData()['price']

		row['tax_status'] = 'taxable'
		row['featured'] = 'no'

		row['tax:product_type'] = 'variable'

		#row['tax:product_cat']
		
		row['tax:product_shipping_class'] = 'Taxable Goods'

		colors = prod.getData()['color'].replace(',', '|')
		row['attribute:pa_color'] = prod.getData()['color'].replace(',', '|')

		row['attribute_data:pa_color'] = '0|1|1'

		sizeCounter = 0
		sizes = list()
		if prod.getData()['isSize1'] != None:
			sizeCounter += 1
			sizes.append(prod.getData()['size1']['name'])
		if prod.getData()['isSize2'] != None:
			sizeCounter += 1
			sizes.append(prod.getData()['size2']['name'])
		if prod.getData()['isSize3'] != None:
			sizeCounter += 1
			sizes.append(prod.getData()['size3']['name'])


		if sizeCounter > 1:
			sizeNames = ''
			sizeData = '0'
			for i in range(len(sizes)):
				if i != 0:
					sizeNames += '|'
					sizeData += '|1'
				sizeNames += sizes[i]
			row['attribute:pa_size'] = sizeNames
			row['attribute_data:pa_size'] = '0|1|1'

		return row

	def childProduct(self, prod):
		childRows = list()

		for i in range(len(prod.getData()['color'].split(','))):
			row = self.rowForm.copy()
			row1 = self.makeChildProduct(prod, row, 'color', prod.getData()['color'].split(',')[i])
			childRows.append(row1)

		sizeCounter = 0
		sizes = list()
		if prod.getData()['isSize1'] != None:
			sizeCounter += 1
			sizes.append(prod.getData()['size1']['name'])
		if prod.getData()['isSize2'] != None:
			sizeCounter += 1
			sizes.append(prod.getData()['size2']['name'])
		if prod.getData()['isSize3'] != None:
			sizeCounter += 1
			sizes.append(prod.getData()['size3']['name'])

		if sizeCounter > 1:
			for i in range(sizeCounter):
				row = self.rowForm.copy()
				row1 = self.makeChildProduct(prod, row, 'size', sizes[i])
				childRows.append(row1)

		return childRows


	def makeChildProduct(self, prod, row, type, variable):
		row['Parent'] = prod.getData()['name']

		row['post_status'] = 'publish'
		row['menu_order'] = 0
		row['post_date'] = self.nowTime

		row['post_parent'] = 1

		row['post_author'] = 2
		row['comment_status'] = 'closed'

		row['downloadable'] = 'no'
		row['virtual'] = 'no'

		row['visibility'] = 'visible'
		row['stock_status'] = 'instock'

		row['backorders'] = 'no'
		row['manage_stock'] = 'no'

		row['regular_price'] = prod.getData()['price']

		row['tax_status'] = 'taxable'
		row['featured'] = 'no'

		row['tax:product_type'] = 'simple'

		if type == 'color':
			row['attribute:pa_color'] = variable

		if type == 'size':
			row['attribute:pa_size'] = variable


		return row

	''' after category
	def topProduct(self, prod, row):

	def outerProduct(self, prod, row):

	def bottomProduct(self, prod, row):

	def accProduct(self, prod, row):
	'''

	def makePostExcerpt(self, prod):
		if prod.getType() == 'top':
			return self.makeTopPostExcerpt(prod)
		elif prod.getType() == 'bottom':
			return self.makeBottomPostExcerpt(prod)
		elif prod.getType() == 'outer':
			return self.makeOuterPostExcerpt(prod)
		elif prod.getType() == 'acc':
			return self.makeAccPostExcerpt(prod)


	def makeTopPostExcerpt(self, prod):
		res = ''

		description = prod.getData()['description']
		
		composition = '*Product Specification <br>'
		composition += prod.getData()['composition']

		size = '*Flat Measurement (cm) : <br>'

		isSize1 = prod.getData()['isSize1']
		isSize2 = prod.getData()['isSize2']
		isSize3 = prod.getData()['isSize3']

		if isSize1 != None:
			rowSize1 = prod.getData()['size1']
			size1 = 'Shoulder: ' + str(rowSize1['shoulder']) + ' / Bust: ' + str(rowSize1['chest']) + ' / Length: ' + str(rowSize1['length']) + ' / Sleeve: ' + str(rowSize1['sleeve'])

		if isSize2 != None:
			rowSize2 = prod.getData()['size2']
			size2 = 'Shoulder: ' + str(rowSize2['shoulder']) + ' / Bust: ' + str(rowSize2['chest']) + ' / Length: ' + str(rowSize2['length']) + ' / Sleeve: ' + str(rowSize2['sleeve'])

		if isSize3 != None:
			rowSize3 = prod.getData()['size3']
			size3 = 'Shoulder: ' + str(rowSize3['shoulder']) + ' / Bust: ' + str(rowSize3['chest']) + ' / Length: ' + str(rowSize3['length']) + ' / Sleeve: ' + str(rowSize3['sleeve'])

		isSizeCounter = 0
		if isSize1 != None:
			isSizeCounter += 1
		if isSize2 != None:
			isSizeCounter += 1
		if isSize3 != None:
			isSizeCounter += 1

		if isSizeCounter == 1:
			if isSize1 != None:
				size += size1
			if isSize2 != None:
				size += size2
			if isSize3 != None:
				size += size3

		if isSizeCounter > 1:
			if isSize1 != None:
				sizename = prod.getData()['size1']['name']
				size += sizename + ' - ' + size1 + '<br>'

			if isSize2 != None:
				sizename = prod.getData()['size2']['name']
				size += sizename + ' - ' + size2 + '<br>'

			if isSize3 != None:
				sizename = prod.getData()['size3']['name']
				size += sizename + ' - '  + size3 + '<br>'

		laundry = '*' + prod.getData()['laundry']

		if isSizeCounter > 1:
			res = description + '<br><br>' + composition + '<br><br>' + size + '<br>' + laundry
		else:
			res = description + '<br><br>' + composition + '<br><br>' + size + '<br>' + laundry

		return res

	def makeBottomPostExcerpt(self, prod):
		res = ''

		description = prod.getData()['description']
		
		composition = '*Product Specification <br>'
		composition += prod.getData()['composition']

		size = '*Flat Measurement (cm) : <br>'

		isSize1 = prod.getData()['isSize1']
		isSize2 = prod.getData()['isSize2']
		isSize3 = prod.getData()['isSize3']

		if isSize1 != None:
			rowSize1 = prod.getData()['size1']
			size1 = 'Waist: ' + str(rowSize1['waist']) + ' / Length: ' + str(rowSize1['length'])

		if isSize2 != None:
			rowSize2 = prod.getData()['size2']
			size2 = 'Waist: ' + str(rowSize2['waist']) + ' / Length: ' + str(rowSize2['length'])

		if isSize3 != None:
			rowSize3 = prod.getData()['size3']
			size3 = 'Waist: ' + str(rowSize3['waist']) + ' / Length: ' + str(rowSize3['length'])

		isSizeCounter = 0
		if isSize1 != None:
			isSizeCounter += 1
		if isSize2 != None:
			isSizeCounter += 1
		if isSize3 != None:
			isSizeCounter += 1

		if isSizeCounter == 1:
			if isSize1 != None:
				size += size1
			if isSize2 != None:
				size += size2
			if isSize3 != None:
				size += size3

		if isSizeCounter > 1:
			if isSize1 != None:
				sizename = prod.getData()['size1']['name']
				size += sizename + ' - ' + size1 + '<br>'

			if isSize2 != None:
				sizename = prod.getData()['size2']['name']
				size += sizename + ' - ' + size2 + '<br>'

			if isSize3 != None:
				sizename = prod.getData()['size3']['name']
				size += sizename + ' - '  + size3 + '<br>'

		laundry = '*' + prod.getData()['laundry']

		if isSizeCounter > 1:
			res = description + '<br><br>' + composition + '<br><br>' + size + '<br>' + laundry
		else:
			res = description + '<br><br>' + composition + '<br><br>' + size + '<br>' + laundry

		return res

	def makeOuterPostExcerpt(self, prod):
		res = ''

		description = prod.getData()['description']
		
		composition = '*Product Specification <br>'
		composition += prod.getData()['composition']

		size = '*Flat Measurement (cm) : <br>'

		isSize1 = prod.getData()['isSize1']
		isSize2 = prod.getData()['isSize2']
		isSize3 = prod.getData()['isSize3']

		if isSize1 != None:
			rowSize1 = prod.getData()['size1']
			size1 = 'Shoulder: ' + str(rowSize1['shoulder']) + ' / Bust: ' + str(rowSize1['chest']) + ' / Length: ' + str(rowSize1['length']) + ' / Sleeve: ' + str(rowSize1['sleeve'])

		if isSize2 != None:
			rowSize2 = prod.getData()['size2']
			size2 = 'Shoulder: ' + str(rowSize2['shoulder']) + ' / Bust: ' + str(rowSize2['chest']) + ' / Length: ' + str(rowSize2['length']) + ' / Sleeve: ' + str(rowSize2['sleeve'])

		if isSize3 != None:
			rowSize3 = prod.getData()['size3']
			size3 = 'Shoulder: ' + str(rowSize3['shoulder']) + ' / Bust: ' + str(rowSize3['chest']) + ' / Length: ' + str(rowSize3['length']) + ' / Sleeve: ' + str(rowSize3['sleeve'])

		isSizeCounter = 0
		if isSize1 != None:
			isSizeCounter += 1
		if isSize2 != None:
			isSizeCounter += 1
		if isSize3 != None:
			isSizeCounter += 1

		if isSizeCounter == 1:
			if isSize1 != None:
				size += size1
			if isSize2 != None:
				size += size2
			if isSize3 != None:
				size += size3

		if isSizeCounter > 1:
			if isSize1 != None:
				sizename = prod.getData()['size1']['name']
				size += sizename + ' - ' + size1 + '<br>'

			if isSize2 != None:
				sizename = prod.getData()['size2']['name']
				size += sizename + ' - ' + size2 + '<br>'

			if isSize3 != None:
				sizename = prod.getData()['size3']['name']
				size += sizename + ' - '  + size3 + '<br>'

		laundry = '*' + prod.getData()['laundry']

		if isSizeCounter > 1:
			res = description + '<br><br>' + composition + '<br><br>' + size + '<br>' + laundry
		else:
			res = description + '<br><br>' + composition + '<br><br>' + size + '<br>' + laundry

		return res

	def makeAccPostExcerpt(self, prod):
		res = ''

		description = prod.getData()['description']
		
		composition = '*Product Specification <br>'
		composition += prod.getData()['composition']

		size = '*Flat Measurement (cm) : <br>'

		rowSize = prod.getData()['size']
		size = 'Width: ' + str(rowSize['width']) + ' / Height: ' + str(rowSize['heigth']) + ' / Depth: ' + str(rowSize['depth']) + ' / Strap: ' + str(rowSize['strap'])

		laundry = '*' + prod.getData()['laundry']

		res = description + '<br><br>' + composition + '<br><br>' + size + '<br><br>' + laundry

		return res











