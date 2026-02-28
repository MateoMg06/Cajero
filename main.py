
saldo_inicial=1000
op=int(input("Cuanto operaciones desea realizar "))
for i in range(op):
    menu=int(input("digite que desar realizar "))
   
print("-----------CAJERO AUTOMATICO--------------")
print("1. consultar saldo ") 
print("2. retirar dinero ") 
print("3. Depositar Dinero ")
<<<<<<< HEAD
<<<<<<< HEAD
print("4. salir ") 
=======
print("4. salir ")
>>>>>>> depositar
=======
print("4. salir ") 





>>>>>>> depositar

if(menu==1):
    print("su saldo es: ",saldo_inicial) 
    
if menu == 2:
    while True:
<<<<<<< HEAD
        retiro = int(input("Digite el valor a retirar: "))
        if retiro <= saldo_inicial:
            saldo_inicial -= retiro
            print("Retiro exitoso. Saldo actual:", saldo_inicial)
            break
        else:
            print("Saldo insuficiente, intente otra vez")    
=======
        monto_depositar = int(input("Digite qué monto desea depositar: "))

        if monto_depositar <= 0:
            print("Error, digite el monto nuevamente")
        else:
            saldo_inicial += monto_depositar
            print("Depósito exitoso, su saldo actual es:", saldo_inicial)
            break 
    
<<<<<<< HEAD
>>>>>>> depositar
=======
            
            
   
>>>>>>> depositar


    








=======
>>>>>>> retirar



