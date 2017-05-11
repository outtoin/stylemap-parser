import os

from openpyxl import Workbook
from openpyxl import load_workbook

import csv

from Columns import columns

from productWriter import ProductWriter

def run(filePath, path, columnSize, rowSize):

	columnSize = int(columnSize)
	rowSize = int(rowSize)

	stylemap = load_workbook(filePath)
	prods = list()

	returnFileName = 'Variable_Product.csv'
	product_csv = open(os.path.join(path, returnFileName), 'w')

	sheets = stylemap.get_sheet_names()

	if 'TOP' in sheets:
		top = stylemap['TOP']
		if top['B2'].value == 'O':
			from top import Top
			tops = Top(top, columnSize, rowSize)
			tops.run(prods)

	if 'OUTER' in sheets:
		outer = stylemap['OUTER']
		if outer['B2'].value == 'O':
			from outer import Outer
			outers = Outer(outer, columnSize, rowSize)
			outers.run(prods)

	if 'BOTTOM' in sheets:
		bottom = stylemap['BOTTOM']
		if bottom['B2'].value == 'O':
			from bottom import Bottom
			bottoms = Bottom(bottom, columnSize, rowSize)
			bottoms.run(prods)

	if 'ACC' in sheets:
		acc = stylemap['ACC']
		if acc['B2'].value == 'O':
			from acc import Acc
			accs = Acc(acc, columnSize, rowSize - 2)
			accs.run(prods)


	pw = ProductWriter()

	pw.run(prods, product_csv)

	product_csv.close()



































