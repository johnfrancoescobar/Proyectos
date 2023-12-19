# hacer un programa que calcule el promedio de 3 notas.
Nota1 = float(input("digite su primera nota, trabajo de lectura"))
Nota2 = float(input("Digite su segunda nota, trabajo en clase"))
Nota3 = float(input("Digite su tercera nota, trabajo escrito"))
prom = (Nota1+Nota2+Nota3)/3
if(prom>=3):
    print("su promedio es: ",prom,"Aprobado")
else:
    print("su promedio es: ",prom,"reprobaste")
    