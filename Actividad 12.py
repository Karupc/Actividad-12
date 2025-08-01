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
        print(f"Información estudiante #{i+1}")
        try:
            nombre_est = input("Ingrese el nombre del estudiante: ")
            cantidad_notas = int(input("¿Cuántas notas desea ingresar?: "))
            notas = []
        except ValueError:
            print("Error: Debe ingresar un valor numérico")
        except Exception as e:
            print("Se produjo un error inesperado:", e)
        else:
            for i in range(cantidad_notas):
                try:
                    nota = input(f"Ingrese nota {i + 1}: ")
                except ValueError:
                    print("Error: Debe ingresar un valor numérico")
                except Exception as e:
                    print("Se produjo un error inesperado:", e)
                else:
                    notas.append(nombre_est, nota)