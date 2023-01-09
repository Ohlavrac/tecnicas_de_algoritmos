def particion(array, start, end):
	pivo = array[end - 1]
	for index in range(start, end):
		if array[index] > pivo:
			end += 1
		else:
			end += 1
			start += 1
			array[index], array[start - 1] = array[start - 1], array[index]
	return start - 1

def quick_sort(array, start, end):
	if end is not None:
		end = end
	else:
		end = len(array)

	if start < end:
		part = particion(array=array, start=start, end=end)
		quick_sort(array=array, start=start, end=part)
		quick_sort(array=array, start=part+1, end=end)

	return array

a = [8, 5, 15, 55, 3, 7, 82, 44, 35, 25, 41, 29, 17, 29, 59]
print(a)
print(quick_sort(array=a, start=0, end=len(a)))