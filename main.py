# Variables para almacenar los datos del curso y los alumnos
curso = input("Nombre del curso: ")
es_teoria = input("¿El curso es teórico o práctico? (teorico/practico): ").lower()
porcentaje_aprobacion = 0.6 if es_teoria == "teorico" else 0.8

num_alumnos = int(input("Cantidad de alumnos: "))
alumnos = {}

# Obtener nombres de los alumnos
for i in range(num_alumnos):
    nombre_alumno = input(f"Nombre del alumno {i + 1}: ")
    alumnos[nombre_alumno] = {
        "notas": {},
        "asistencia": 0,
        "razon_reprobado": "",
        "examen_recuperativo": False,
        "nota_recuperativa": 0.0,
        "ponderacion_recuperativa": 0.0,
    }

# Preguntar por la cantidad de evaluaciones
num_evaluaciones = int(input("Cantidad de evaluaciones: "))
ponderaciones = {}
for i in range(num_evaluaciones):
    nombre_evaluacion = input(f"Nombre de la evaluación {i + 1}: ")
    ponderacion = float(input(f"Ponderación de {nombre_evaluacion} (1-100%): "))
    if 1 <= ponderacion <= 100:
        ponderaciones[nombre_evaluacion] = ponderacion / 100.0
    else:
        print("La ponderación debe estar entre 1% y 100%.")

while True:
    print("\nAcciones disponibles:")
    print("1. Agregar nota")
    print("2. Agregar porcentaje de asistencia")
    print("3. Resumen general del alumno")
    print("4. Marcar examen recuperativo")
    print("5. Resumen general del curso")
    print("6. Salir")

    opcion = input("Seleccione una acción (1/2/3/4/5/6): ")

    if opcion == "1":
        alumno = input("Nombre del alumno: ")
        if alumno in alumnos:
            for evaluacion in ponderaciones:
                nota = float(input(f"Nota para {evaluacion} (1.0-7.0): "))
                if 1.0 <= nota <= 7.0:
                    alumnos[alumno]["notas"][evaluacion] = nota
                    print(f"Nota para {evaluacion} agregada con éxito.")
                else:
                    print("La nota debe estar entre 1.0 y 7.0.")
        else:
            print("Alumno no encontrado.")

    elif opcion == "2":
        for alumno in alumnos:
            asistencia = float(input(f"Porcentaje de asistencia para {alumno} (0-100): "))
            if 0 <= asistencia <= 100:
                alumnos[alumno]["asistencia"] = asistencia
                print(f"Porcentaje de asistencia para {alumno} actualizado con éxito.")
            else:
                print("El porcentaje de asistencia debe estar entre 0 y 100.")

    elif opcion == "3":
        alumno = input("Nombre del alumno: ")
        if alumno in alumnos:
            datos = alumnos[alumno]
            notas = datos["notas"]
            asistencia = datos["asistencia"]
            total_ponderacion = sum(ponderaciones.values())
            nota_final = sum(notas[evaluacion] * ponderaciones[evaluacion] for evaluacion in notas) / total_ponderacion
            if datos["examen_recuperativo"]:
                nota_recuperativa = datos["nota_recuperativa"]
                ponderacion_recuperativa = datos["ponderacion_recuperativa"]
                nota_final = (nota_final * total_ponderacion + nota_recuperativa * ponderacion_recuperativa) / (
                            total_ponderacion + ponderacion_recuperativa)
            if nota_final >= (4.0 if es_teoria == "teorico" else 4.0) and asistencia >= 75:
                estado = "Aprobado"
                razon_reprobado = "Aprobado por notas y asistencia."
            elif nota_final < (4.0 if es_teoria == "teorico" else 4.0):
                estado = "Reprobado"
                razon_reprobado = "Reprobado por notas insuficientes."
            else:
                estado = "Reprobado"
                razon_reprobado = "Reprobado por insuficiencia de asistencia."
            print(f"Resumen para {alumno}:")
            print(f"Notas: {', '.join(f'{k}: {v:.2f}' for k, v in notas.items())}")
            print(f"Asistencia: {asistencia:.2f}%")
            print(f"Nota Final: {nota_final:.2f}")
            print(f"Estado: {estado}")
            print(f"Razón: {razon_reprobado}")
        else:
            print("Alumno no encontrado.")

    elif opcion == "4":
        alumno = input("Nombre del alumno: ")
        if alumno in alumnos:
            datos = alumnos[alumno]
            datos["examen_recuperativo"] = True
            nota_recuperativa = float(input("Nota del examen recuperativo (1.0-7.0): "))
            ponderacion_recuperativa = float(input("Ponderación del examen recuperativo (1-100%): "))
            if 1.0 <= nota_recuperativa <= 7.0 and 1 <= ponderacion_recuperativa <= 100:
                datos["nota_recuperativa"] = nota_recuperativa
                datos["ponderacion_recuperativa"] = ponderacion_recuperativa / 100.0
                print("Examen recuperativo marcado con éxito.")
            else:
                print("La nota del examen recuperativo debe estar entre 1.0 y 7.0, y la ponderación entre 1% y 100%.")
        else:
            print("Alumno no encontrado.")

    elif opcion == "5":
        print("\nResumen general del curso:")
        print(f"{'Nombre del Alumno':<20}{'Notas':<30}{'Asistencia (%)':<20}{'Nota Final':<15}{'Estado':<15}{'Razón'}")
        for alumno, datos in alumnos.items():
            notas = datos["notas"]
            asistencia = datos["asistencia"]
            total_ponderacion = sum(ponderaciones.values())
            nota_final = sum(notas[evaluacion] * ponderaciones[evaluacion] for evaluacion in notas) / total_ponderacion
            if datos["examen_recuperativo"]:
                nota_recuperativa = datos["nota_recuperativa"]
                ponderacion_recuperativa = datos["ponderacion_recuperativa"]
                nota_final = (nota_final * total_ponderacion + nota_recuperativa * ponderacion_recuperativa) / (
                            total_ponderacion + ponderacion_recuperativa)
            if nota_final >= (4.0 if es_teoria == "teorico" else 4.0) and asistencia >= 75:
                estado = "Aprobado"
                razon_reprobado = "Aprobado por notas y asistencia."
            elif nota_final < (4.0 if es_teoria == "teorico" else 4.0):
                estado = "Reprobado"
                razon_reprobado = "Reprobado por notas insuficientes."
            else:
                estado = "Reprobado"
                razon_reprobado = "Reprobado por insuficiencia de asistencia."
            print(f"{alumno:<20}{str(notas):<30}{asistencia:<20.2f}{nota_final:<15.2f}{estado:<15}{razon_reprobado}")

        # Cálculo del promedio general del curso
        notas_totales = [datos["notas"] for datos in alumnos.values()]
        asistencias = [datos["asistencia"] for datos in alumnos.values()]
        notas_finales = [sum(notas[evaluacion] * ponderaciones[evaluacion] for evaluacion in notas) / total_ponderacion
                         for notas in notas_totales]
        asistencia_promedio = sum(asistencias) / num_alumnos
        promedio_notas_finales = sum(notas_finales) / num_alumnos

        print("\nPromedio general del curso:")
        print(f"Promedio de Notas Finales: {promedio_notas_finales:.2f}")
        print(f"Asistencia: {asistencia_promedio:.2f}%")

    elif opcion == "6":
        break

    else:
        print("Opción no válida. Por favor, seleccione una acción válida (1/2/3/4/5/6).")
