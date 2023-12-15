my_list = [1, 2, 4, 9, 4, 9, 1, 4, 2, 14, 6, 2, 14, 9, 1, 1, 2]
list = []
for i in my_list:  
	if i not in list:  
		list.append(i)  
my_list = list[:]  
print("La lista con elementos únicos:")
print(my_list)
