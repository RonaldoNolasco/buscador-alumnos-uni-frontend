#El caracter salto de linea es solo un espacio, no dos

#print("codigo,especialidad,ap,am,nombre")
f = open("1_codigos_scrapping.txt","r")
f1 = f.readlines()
for i in range (0,len(f1)):
    test = ""
    res = ""
    x=f1[i].split()
    test = x[2]
    for j in range(3, len(x)):
        test = test + " " + x[j]
    fin = test.split('-')
    res = x[0] + "," + x[1]
    for j in range(0, len(fin)):
        res = res + "," + fin[j]
    print(res)

#Tener cuidado con el 20101447E

#Falta ver los que tienen 2 o 4 en y, F

#Pasarlo a json en https://www.csvjson.com/csv2json

#Al hacer el split se van los espacios en blanco y el salto de linea, por lo que
#evitamos complicaciones
"""
print("codigo, especialidad, nombre")
f = open("codigos_sql.txt","r")
f1 = f.readlines()
for i in range (0,len(f1)):
    x=f1[i].split()
    res = x[0] + ", "+ x[1]+","
    for j in range(2, len(x)):
        res = res + " " + x[j]
    print(res)
"""

"""
print("codigo, especialidad, nombre")
f = open("4_codigos_sql.txt","r")
f1 = f.readlines()
for i in range (0,len(f1)):
#No puede ser [:-2], se borra una letra del ultimo nombre
    f1[i]=f1[i][:-1]
    for j in range (0,3):
        if f1[i].endswith(' '):
            f1[i]=f1[i][:-1]
    x=f1[i].split()
    res = x[0] + ", "+ x[1]+","
    for j in range(2, len(x)):
        res = res + " " + x[j]
    print(res)
print(f1)
"""