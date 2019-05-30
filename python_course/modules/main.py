# consider a module to be the same as a code library
# a file ontaining a set of functions you want to include in your appliation
import demo1
import pythonawesomeness as demo2
import platform
print(demo1.sentence)
print(demo1.fruits)
for x in demo1.fruits:
	print(x)

print(demo1.person)
print(demo1.person['name'])
print(demo1.person['age'])

country = demo1.person['country']
print(country)

demo2.get_name('sey')

syse = platform.system()
print(syse)

get_details = dir(demo2)
print(get_details)

for detail in get_details:
	print(detail)

for x in dir(platform):
	print(x)