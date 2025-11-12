'''
Inyeccion de dependencias
'''

# Inyeccion por constructor
class ServiceEmail:
    def enviar_email(self, mensaje):
        print(f"Email enviado - {mensaje}")

class Notificador:
    def __init__(self, service: ServiceEmail):
        self.service = service
        
    def notificar(self, mensaje):
        self.service.enviar_email(mensaje)

service_email = ServiceEmail()
notifica = Notificador(service=service_email)

notifica.notificar("Contenido constructor")

# Inyeccion por setter
class ServiceEmailS:
    def enviar_email(self, mensaje):
        print(f"Email enviado - {mensaje}")

class NotificadorS:
    def set_email_service(self, service_email: ServiceEmailS):
        self.service = service_email
        
    def notificar(self, mensaje):
        self.service.enviar_email(mensaje)

service_email = ServiceEmailS()
notifica = NotificadorS()
notifica.set_email_service(service_email)
notifica.notificar("Contenido setter")