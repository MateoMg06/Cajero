saldo_inicial=1000
op=int(input("Cuanto operaciones desea realizar "))
for i in range(op):
    menu=int(input("digite que desar realizar "))
   
print("-----------CAJERO AUTOMATICO--------------")
print("1. consultar saldo ") 
print("2. retirar dinero ") 
print("3. Depositar Dinero ")
print("4. salir ")

            
if menu == 3:
    while True:
        monto_depositar = int(input("Digite qué monto desea depositar: "))

        if monto_depositar <= 0:
            print("Error, digite el monto nuevamente")
        else:
            saldo_inicial += monto_depositar
            print("Depósito exitoso, su saldo actual es:", saldo_inicial)
            break  





     
     
     
     
     
     
     
     
     
     
  
            
 

    











