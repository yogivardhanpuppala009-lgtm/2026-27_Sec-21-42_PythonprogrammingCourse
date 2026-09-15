#logical operators
a=1
result= a>0 and a<10 #logical and operator
print("result of",a,">0 and",a,"<10 is",result)
result= a>2 and a<10 #logical and operator
print("result of",a,">2 and",a,"<10 is",result)

a=5
result= a>0 or a<10 #logical or operator
print("result of",a,">0 or",a,"<10 is",result)
result= a<0 or a<10 #logical or operator
print("result of",a,">0 or",a,"<10 is",result)

a=90
result= not(a>0 and a<11) #logical not operator
print("result of not(",a,">0 and",a,"<11) is",result)
result= not(a>10 and a<15) #logical not operator
print("result of not(",a,">10 and",a,"<15) is",result)