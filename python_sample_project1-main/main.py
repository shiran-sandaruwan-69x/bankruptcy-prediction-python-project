#ar =["1",3,"4","AA",0.5]
#print(ar)

ar=[1,2,3,4,5,6,7,7,7,8,9,9,9,10]
print(ar)

ar[:8]
print(ar[:8])
#array eka apita ona vidihata limit kara ganna puluwan
ar[8:]
print(ar[8:])

ar[5:8]
print(ar[5:8])

#----------- array 2 kak ethayhu karanna
ar2=ar[2:5]+ar[6:8]
print(ar2)

#----------------- value ekak assign krnn puluwan mehema
ar3=[3,4,5,7,7]
ar3[3]=500
print(ar3)

#---------- length ek blaganne array eke
print(len(ar3))