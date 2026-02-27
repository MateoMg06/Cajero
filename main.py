saldo_inicial=1000
op=int(input("Cuanto operaciones desea realizar"))
for i in range(op):
    menu=int(input("digite que desar realizar"))
print("-----------CAJERO AUTOMATICO--------------" \
"1. consultar saldo" \
"2.retirar dinero" \
"3.Depositar Dinero" \
"4.salir")

if(menu==1):
    print("su saldo es ",saldo_inicial)

elif(menu==2):
    monto_retirar=int(input("Cuanto desea retirar"))
if (monto_retirar>saldo_inicial):
    print("fondos insuficientes")
elif(monto_retirar<=saldo_inicial):
    saldo_nuevo=monto_retirar-saldo_inicial
    print("su saldo ahora es: ",saldo_nuevo)
else:
    print("digite un monto valido")







