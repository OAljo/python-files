#write function 
file=open("test_write.text","a")
# append will add to the end of the  file 
file.write(" this text will be added at the end of the file ")
file.close()
print("check out the file :")
file=open("test_write.text","r")
print(file.read())

###### overwritting the conent of file overwrite 

