#WAP TO FIND THE  IUPAC NAMING :-


formula = input("Enter the formula of compound :")

# prefix = {}
wordRoot = {1:"meth",2:"eth",3:"prop",4:"but",5:"pent",6:"hex",7:"sept",8:"oct",9:"non",10:"dec"}
priSuffix = {"-":"ane","=":"ene","~":"yne"}
secSuffix = {"-OH":"ol"}
bondList = []
carbon = []
hydrogen = []
functG = []
for i in formula:
    if i == "C":
        carbon.append(i)
    if i.isdigit()==1:
        a=int(i)
        for j in range(a):
            hydrogen.append("H")
    bond = ("-","=","~")
    if i in bond:
        bondList.append(i)
if "-OH" in formula:
    functG.append("-OH")    
Nc = len(carbon)
Nh = len(hydrogen)
Nb = max(bondList)

iupacNaming =  wordRoot[Nc] + priSuffix[Nb]

print(iupacNaming.capitalize())
