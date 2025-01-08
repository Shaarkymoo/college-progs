import sympy

def equation():
    compound = {}
    reactants = []
    while True:
        receive = int(input("press 1 to enter element, 2 to start new compound,3 to balance:"))
        if receive == 1:
            ele = str(input("Enter Element Symbol: "))
            quant = int(input("Enter Element quantity: "))
            compound[ele] = quant
        elif receive == 2:
            reactants.append(compound)
            compound={}
        elif receive == 3:
            reactants.append(compound)
            temper = []  # if temper = reactants, gives an infinite loop because shallow copy
            for a in reactants:
                keylist = list(a.keys())
                keylist.sort()
                tempcomp={}
                for i in keylist:
                    tempcomp[i] = a[i]
                temper.append(tempcomp)
        
            reactants = temper
            break

    return reactants

def simplify(somelist):
    for a in somelist:
        somelist[somelist.index(a)] *= -1
    #print(somelist)
    condition = True

    while condition:
        for a in somelist:
            if a%1!=0:
                condition = True
                break
        else:
            condition = False
        
        if condition == True:
            for b in range(len(somelist)):
                somelist[b] *= ((a%1)**-1)
            #print(somelist)

    return somelist

print("Enter reactants")
reactants = equation()
print("Enter products")
products = equation()

#reactants = [{'C': 2, 'H': 6}, {'O': 2}]
#products = [{'C': 1, 'O': 2}, {'H': 2, 'O': 1}]
print(reactants,products)

columns = len(reactants)+len(products)
rows = []

for a in reactants:
    for b in a:
        if b not in rows:
            rows.append(b)

for a in products:
    for b in a:
        if b not in rows:
            rows.append(b)

#print(rows,columns)

matrix = [rows]
for a in range(len(rows)):
    row = []
    for b in range(columns):
        row.append(0)
    matrix.append(row)

#print(matrix)

chemreac = []
chemreac.append(reactants)
chemreac.append(products)
negative = 1
#print(chemreac)

count = 0
for a in chemreac:
    for b in a:
        for c in b:
            row_index = matrix[0].index(c)
            #print(row_index)
            matrix[row_index+1][count] = negative * b[c] if b[c] else 0
        count+=1
    negative = -1

matrix.remove(rows)
#print(matrix)
M_rref,throwaway = (sympy.Matrix(matrix)).rref()
newmat = []
for a in range(len(matrix)):
    temp = []
    for b in M_rref.row(a):
        temp.append(b)
    newmat.append(temp)
matrix = newmat
#print(matrix)


newmat = []
for a in matrix:
    newmat.append(a[-1])
newmat.append(-1)
newmat = simplify(newmat)
print(newmat)









    