# fw = open("demofile.txt", "w")
# fw.write("This is sharmila")
# #fw.close()
#
# fr = open("demofile.txt", "r")
# print(fr.read())

with open("demofile1.txt", "w")as fw:
    fw.write("This is from with keyword operation")

with open("demofile1.txt", "r")as fr:
    print(fr.read())
    