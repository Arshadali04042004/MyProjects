# 2*x*x+x+1
Eq = input("Enter the Equation :")
term = Eq.split("+")
firstTerm = term[0]
secTerm = term[1]
thirdTerm = term[2]
global a,b,c
for i in firstTerm:
    digit = i.isdigit()
    
    if  digit == 1:
        
        a = i

for j in secTerm:
    digit = j.isdigit()
    if  digit == 1:
        
        b = i
for k in thirdTerm:
    digit = j.isdigit()
    
    if  digit == 1:
        
        c = i
print(a,b,c)


