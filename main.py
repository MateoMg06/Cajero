
saldo_inicial=1000
op=int(input("Cuanto operaciones desea realizar "))
for i in range(op):
    menu=int(input("digite que desar realizar "))
   
print("-----------CAJERO AUTOMATICO--------------")
<<<<<<< HEAD
print("1. consultar saldo ") 
print("2. retirar dinero ") 
print("3. Depositar Dinero ")
print("4. salir ") 

if(menu==1):
    print("su saldo es: ",saldo_inicial) 
    
    










=======
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
>>>>>>> retirar

    



<<<<<<< HEAD




=======
>>>>>>> retirar



