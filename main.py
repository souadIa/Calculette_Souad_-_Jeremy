#test 00000000
# ludi est passé par là
# définir chacun votre fonction
# Je reteste 
class Error(Exception):
	pass

def divide(a,b):
	if b == 0:
		raise Error("Pas de division par zéro")
	res = a / b
	return res

def soustr (a,b):
	res = a - b
	return res

def sum(a,b):
	res = a+b

def multiply(a,b):
	res=a*b	
	return res

if __name__ == '__main__':
	x = 0
