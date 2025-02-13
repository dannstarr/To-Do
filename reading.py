# Please download the three text files a.txt, b.txt, and c.txt from the resources and place them in your computer IDE.
#
# Then, create a program that:
#
# 1. reads each text file and
#
# 2. prints out the content of each file in the command line.
#

filenames = ["a.txt", "b.txt", "c.txt"]

for i in filenames:
    file = open(f"files/{i}", "r")
    content = file.read()
    file.close()
    print(f"The file '{i}' reads: {content}")

