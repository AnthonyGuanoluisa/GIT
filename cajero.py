#cajero donde 1 es consulytar saldo, 2 es depositar, 3 es retirar, 4 es salir
saldo = 0.00
while True:
    print("-----------------------------------")
    print("""Cajero automático UTC
          1. Consultar saldo
          2. Depositar
          3. Retirar
          4. Salir
          """)
    
    opcion = int(input("Ingrese una opción: "))
    print("-----------------------------------")
    match opcion:
        case 1:
            print(f"Su saldo es: ${saldo:.2f}")
        case 2:
            monto = float(input("Ingrese el monto a depositar: "))
            if monto > 0:
                saldo += monto
                print(f"Su nuevo saldo es: ${saldo:.2f}")
            else:
                print("El monto a depositar debe ser mayor que cero.")
        case 3:
            monto = float(input("Ingrese el monto a retirar: "))
            if monto <= saldo:
                saldo -= monto
                print(f"Retiro exitoso. Su nuevo saldo es: ${saldo:.2f}")
            else:
                print("Saldo insuficiente para realizar el retiro.")
        case 4:
            print("Gracias por usar nuestro cajero")
            break
        case _:
            print("Opción inválida")
        # cambios para prueba de commit