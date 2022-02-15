"""
Manual steps to write to a file
1. Open notepad and create file
2. Write in the file
3. Close the file

Mode
Read mode : r
Write mode: w
Append mode: a
Read/Write: r+
"""
# save the file to particular location in system.
# f = open("C:\\Sharmila\\Testing references\\writedemo.txt", "w")
# f.write("This is first line")
# f.close()

f = open("C:\\Sharmila\\Testing references\\writedemo1.txt", "w")
l = [65, 78, 588, 909]
for items in l:
    f.write(str(items)+ "\n")
f.close()