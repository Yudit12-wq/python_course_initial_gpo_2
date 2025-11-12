class Notificador:
    def envia_mensaje(self, mensaje: str):
        print(f"Hola {mensaje}")
        return mensaje
        
    def cancelar(self, new_mensaje: str):
        print(f"Mensaje cancelado {new_mensaje}")
        return new_mensaje