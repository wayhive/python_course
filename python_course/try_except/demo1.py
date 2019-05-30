
fruits = 'apples,berries,grapes'
try:
	print(fruits)
except:
	print('fruits is not defined')
y = 'lesson learnt'
try:
	print (y) 
except NameError:
	print('variable y is not defined')
except SyntaxError as error:
	print(error)
except:
	print('something else went wrong')
else:
	print('nothing went wrong')
finally:
	print('finished')
