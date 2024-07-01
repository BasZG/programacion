import os
menu = print("""
Seleccione una de las opciones:
1.- Registrar vehículo.
2.- Listar todos los vehículos registrados.
3.- Imprimir orden de reparación.
4.- Salir del programa.
""")
vehiculos = []
marcas =[toyota, ford, chevrolet]
auto = f"""\tMarca\taño\tKilometraje\tcosto\reparacion\timpuesto 8%\tcosto total
"""

def registrarVehiculo():
    while True:
        try:  
            marca = input("Ingrese la marca del vehiculo:").capitalize().strip()
            año = input("Ingrese el año del vehiculo:").capitalize().strip()
            Kilometraje = input("Ingrese la cantidad de kilometros del vehiculo:").capitalize().strip()
            CostoReparacion = int(input("Ingrese costo de reparacion"))
            impuestoservicio = CostoReparacion * 0.08
            costototal = CostoReparacion + impuestoservicio
            vehiculo= [marca,año,Kilometraje,CostoReparacion,impuestoservicio,costototal].append() 
            print("Se registro correctamente.")
        except:
            print("Invalido")

def ListarVehiculosRegistrado():
    autito = auto
    for vehiculo in vehiculos:
        autito += f"{vehiculo[0]}".ljust(16)
        autito += f"{vehiculo[1]}".ljust(16)
        autito += f"{vehiculo[2]}".ljust(16)
        autito += f"{vehiculo[3]}".ljust(16)
        autito += f"{vehiculo[4]}".ljust(16)
        autito += f"{vehiculo[5]}".ljust(16)
        autito += "\n"
    return autito
