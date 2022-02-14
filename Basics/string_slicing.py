#s[i:j:k] - slices of strings starts from i to j with steps
#s[start index:endindex:step]

s = "welcome to software automation testing"
print(s[5:13:1])
print(s[0:15:2])
print(s[:])
print(s[::-1])

x = "name, age, city"
print(x.index(','))
print(x[0:x.index(',')])
