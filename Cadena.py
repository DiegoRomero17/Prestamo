class ManejadorPrestamo():
    def __init__(self):
        self.next_Manejador = None

    def Manejador(self, request):
        pass

    def set_Manejador(self, manejador):
        self.next_Manejador = manejador

class PrestamoCarro(ManejadorPrestamo):
    def Manejador(self, request):
        if request is "carro":
            print("el prestamo de Carro ha sido aprobado " )
        else:
            print("el prestamo se pasara a PrestamoCasa " )
            if self.next_Manejador is not None:
                self.next_Manejador.Manejador(request)        

class PrestamoCasa(ManejadorPrestamo):
    def Manejador(self, request):
        if request is "casa":
            print("el prestamo de Casa ha sido aprobado " )
        else:
            print("el prestamo se pasara a PrestamoEstudio " )
            if self.next_Manejador is not None:
                self.next_Manejador.Manejador(request)           

class PrestamoEstudio(ManejadorPrestamo):
    def Manejador(self, request):
        if request is "estudio":
            print("el prestamo de Estudio ha sido aprobado" )
        else:
            print("El prestamo que usted solicito no se puede realizar " )
            if self.next_Manejador is not None:
                self.next_Manejador.Manejador(request) 

def Iniciar_Cadena():
    prestamoCarro = PrestamoCarro()
    prestamoCasa = PrestamoCasa()
    prestamoEstudio = PrestamoEstudio()

    prestamoCarro.set_Manejador(prestamoCasa)
    prestamoCasa.set_Manejador(prestamoEstudio)

    return prestamoCarro

if __name__ == '__main__':
    cadena = Iniciar_Cadena()

    cadena.Manejador("casa")                                       
