def my_sum(lista):
    sum = 0
    for item in lista:
        sum += item
    return sum
	
if __name__ == '__main__':
	print('Usage example')
	lista = list(range(100))
	print(my_sum(lista))