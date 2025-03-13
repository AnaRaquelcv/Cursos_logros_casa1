def mostrar_menu():
    print("\nMENU FARMACIA SALUDABLE")
    print("Bienvenido querido cliente a nuestro menú de productos. A continuación se mostrarán las opciones que puede realizar.")
    print("\n1. AGREGAR un nuevo medicamento a la cesta de compra")
    print("2. MOSTRAR el contenido de la cesta de compra.")
    print("3. ELIMINAR un medicamento de la cesta de compra.")
    print("4. CALCULAR el precio de la cesta de compra.")
    print("5. SALIR del menú.")

def main():
    cesta_compra = []
    precios = {}

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (AGREGAR/MOSTRAR/ELIMINAR/CALCULAR/SALIR): ").strip().upper()
        
        if opcion == "AGREGAR":
            elemento = input("Ingrese el nombre del nuevo medicamento: ")
            precio = float(input(f"Ingrese el precio del {elemento}: "))
            cesta_compra.append(elemento)
            precios[elemento] = precio
            print(f"{elemento} ha sido agregado a la cesta.")

        elif opcion == "MOSTRAR":
            if cesta_compra:
                print("\nContenido de la cesta de la compra:")
                for item in cesta_compra:
                    print(f"{item} --> Precio: {precios[item]}")
            else:
                print("La cesta de la compra está vacía.")

        elif opcion == "ELIMINAR":
            if cesta_compra:
                elemento = input("Ingrese el nombre del medicamento a eliminar: ")
                if elemento in cesta_compra:
                    cesta_compra.remove(elemento)
                    del precios[elemento]
                    print(f"{elemento} ha sido eliminado de la cesta.")
                else:
                    print(f"{elemento} no se encuentra en la cesta.")
            else:
                print("La cesta de la compra está vacía.")

        elif opcion == "CALCULAR":
            if cesta_compra:
                total = sum(precios[item] for item in cesta_compra)
                print(f"El total de la cesta de la compra es de: {total:.2f}")
            else:
                print("La cesta de la compra está vacía.")

        elif opcion == "SALIR":
            print("\nGracias por utilizar el menú de FARMACIA SALUDABLE.")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

main()