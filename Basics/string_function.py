#len - Returns the length of an object
x = "sharmila"
print(len(x))
#upper() - converts string into uppercase
print(x.upper())
#count()- it counts number of values identified in strings.

a = "nr sharmila nr sharmila nr sharmila nr sharmila"
print(a.count("nr"))
#isupper() - validate the strings are upper or lower
print(x.isupper())
print(a.split())
print(a.rsplit("nr"))
#lstrip(char) - removes from left to right
#rstrip(char) - removes from right to left
#replace(old,new(count)) - replaces a specified phrase with another specified phrase.
print(a.replace("nr","nd", 2))