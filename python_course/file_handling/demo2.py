# lyrics = open('text.txt','r')
# print(lyrics.read())

# lyrics = open("text.txt", "r")
# print(lyrics.read(5))

# lyrics = open("text.txt", "r")
# print(lyrics.readline())

# lyrics = open("text.txt", "r")
# print(lyrics.readline())
# print(lyrics.readline())  

lyrics = open("text.txt", "r")
# for x in lyrics:
#   print(x) 

# lyrics_list = lyrics.readlines()
# print(lyrics_list[2])
#problem print a specfic line in text.txt
# solution
# cgeck the data type 
import os

# print(type(lyrics))

# lyrics_list = lyrics.readlines()

# print(lyrics_list)

# print(lyrics_list[2])

# os.remove('index.html')

if os.path.exists("text.txt"):
  os.remove("text.txt")
else:
  print("The file does not exist")