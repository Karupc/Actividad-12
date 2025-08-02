estudiantes = []
print("---PROGRAMA PARA CALCULAR PROMEDIOS---\n")
try:
    cantidad_estudiantes = int(input("¿Cuántos estudiantes desea ingresar?: "))
except ValueError:
    print("Error: Debe ingresar un valor numérico")
except Exception as e:
    print("Se produjo un error inesperado:", e)
else:
    for i in range(cantidad_estudiantes):
        print(f"\nInformación del estudiante #{i+1}")
        try:
            nombre_est = input("Ingrese el nombre del estudiante: ")
            cantidad_notas = int(input("¿Cuántas notas desea ingresar?: "))
            notas = []
            for j in range(cantidad_notas):
                while True:
                    try:
                        nota = float(input(f"Ingrese nota {j + 1}: "))
                        if 0 <= nota <= 100:
                            notas.append(nota)
                            break
                        else:
                            print("La nota debe estar entre 0 y 100.")
                    except ValueError:
                        print("Error: Debe ingresar un valor numérico.")
            estudiantes.append({"nombre": nombre_est, "notas": notas})
        except ValueError:
            print("Error: Debe ingresar un valor numérico.")
        except Exception as e:
            print("Se produjo un error inesperado:", e)
print("\n---RESULTADOS---")
for estudiante in estudiantes:
    print(f"Estudiante: {estudiante['nombre']}")
    print("Notas:", estudiante['notas'])
