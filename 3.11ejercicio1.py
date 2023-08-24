horas = float(input("Introduzca las Horas: "))
tarifa = float(input("Introduzca la Tarifa por hora: "))

if horas > 40:
    horas_extras = horas - 40
    salario = (40 * tarifa) + (horas_extras * tarifa * 1.5)
else:
    salario = horas * tarifa

print("Salario:", salario)