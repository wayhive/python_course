def print_name():
    print("My name is Sey")


print_name()#calling a function

def print_country(country_name):
    print("My country is " + country_name)

print_country("Kenya")

developer = "William and Sey"
def get_dev(The_string):
    for x in The_string:
        print(x)

get_dev(developer)


stuff = ["hospitals","schools","offices","houses","cars"]
def get_dev(a_list):
    for x in a_list:
        print(x)

get_dev(stuff)

def say_name(name = "Developer"):
    return "My name is " + name

say_name("Sey")

get_tosh = say_name("Sey")
print(get_tosh)
