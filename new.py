s=input('enter the input :        ' )
myfile=open('myfile.txt' ,'w')
myfile.write(s)
myfile.close()
ufile=open('myfile.txt')
print(ufile.readlines())
ufile.close()