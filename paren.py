def match(str):
 opo1=[]
 opo2=[]
 opo3=[]
 clo1=[]
 clo2=[]
 clo3=[]
 for i in range(0,len(str)):
   l=str[i]
   if l == "(" :
        opo1=opo1 + ["("]
   elif l == "{" :
        opo2=opo2 + ["{"]
   elif l == "<" :
        opo3=opo3 + ["<"]
   elif l == ")" :
        clo1=clo1 + [")"]
   elif l == "}" :
        clo2=clo2 + ["}"]
   else:
        clo3=clo3 + [">"]
   i=i+1
 if len(opo1)==len(clo1) and len(opo2)==len(clo2) and len(opo3)==len(clo3) :
    return True
 else:
    return False

s=input("enter a string")
d=match(s)
print(d)
