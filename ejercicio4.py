cuota_mes = int(input("Ingrese cuota mensual: "))
mes = int(input("Si desea pagar un mes ingrese 1,si no ingrese 0: "))
tres_meses = int(input("Si desea pagar tres meses ingrese 1,si no ingrese 0: "))
seis_meses = int(input("Si desea pagar seis meses ingrese 1,si no ingrese 0: "))
doce_meses = int(input("Si desea pagar doce meses ingrese 1,si no ingrese 0: "))
if tres_meses == 1:
  total = cuota_mes - (cuota_mes * 0.05) 
elif seis_meses == 1:
  total = cuota_mes - (cuota_mes * 0.15) 
elif doce_meses ==1:
  total = cuota_mes - (cuota_mes * 0.40) 
else:
  total = cuota_mes
 
print ("El total es: ", total)

