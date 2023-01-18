def subconjuntosUtil(A, subconjuto, index):
	print(*subconjuto)
	for i in range(index, len(A)):
		subconjuto.append(A[i])
		subconjuntosUtil(A, subconjuto, i + 1)
		subconjuto.pop(-1)
	return

def subconjuntos(A):
	global res
	subconjunto = []
	index = 0
	subconjuntosUtil(A, subconjunto, index)
	
valores = [1, 2, 3]

subconjuntos(valores)