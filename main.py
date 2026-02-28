
saldo_inicial=1000
op=int(input("Cuanto operaciones desea realizar "))
for i in range(op):
    menu=int(input("digite que desar realizar "))
   
print("-----------CAJERO AUTOMATICO--------------")
print("1. consultar saldo") 
print("2. retirar dinero") 
print("3. Depositar Dinero") 
print("4. salir ")

if menu == 2:
    while True:
        retiro = int(input("Digite el valor a retirar: "))
        if retiro <= saldo_inicial:
            saldo_inicial -= retiro
            print("Retiro exitoso. Saldo actual:", saldo_inicial)
            break
        else:
            print("Saldo insuficiente, intente otra vez")  


    


    



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







