from string import ascii_uppercase

alphabets = list(ascii_uppercase)

def Columns1():

	return alphabets

def Columns2():

	xalphabets = [''] + alphabets

	res = list()

	for i in range(len(xalphabets)):
		for j in range(len(alphabets)):
			res.append(xalphabets[i] + alphabets[j])

	return res

def Columns3():

	xalphabets = [''] + alphabets

	res = list()

	for i in range(len(xalphabets)):
		if (i == 0):
			for j in range(len(xalphabets)):
				for k in range(len(alphabets)):
					res.append(xalphabets[i] + xalphabets[j] + alphabets[k])
		else:
			for j in range(len(xalphabets)):
				if (j == 0):
					continue
				else:
					for k in range(len(alphabets)):
						res.append(xalphabets[i] + xalphabets[j] + alphabets[k])

	return res

def columns(index):
	if(index < 27):
		return Columns1()[index - 1]

	else:
		return Columns2()[index - 1]