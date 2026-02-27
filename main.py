saldo_inicial=1000
op=int(input("Cuanto operaciones desea realizar"))
for i in range(op):
    menu=int(input("digite que desar realizar"))
print("-----------CAJERO AUTOMATICO--------------" \
"1. consultar saldo" \
"2.retirar dinero" \
"3.Depositar Dinero" \
"4.salir")

if(menu==3):
    monto_deposito=input(int("cuanto desea depositar"))

while monto_deposito < 0:
    print("el monto no puede ser negativo")
    monto_deposito=input(int("cuanto desea depositar"))






