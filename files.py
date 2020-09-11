#help(open)
file=open("test.text","r")
#open the file 
print("1- the read() output is : ")
print(file.read())
#read only first 6 chars from the file 
print("2- the read(6) output is : ")
print(file.read(6))
print("3- the readline() output is : *notice the output ")
print(file.readline())
print("4- the for loop output is : ")
file=open("test.text","r")
for x in file :
    print(x)

# close the file 
file.close()
#make sure the file is closed 
print(file.read())
#write function 
