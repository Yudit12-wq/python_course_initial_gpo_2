import sys
from pathlib import Path
 
# Agregar la ruta raíz del proyecto al path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from yudit.src.ejercicio12 import Notificador

def test_enviar():
    notifica = Notificador()
    
    msj = notifica.envia_mensaje("Yudit")
    
    assert "Yudit" in msj
    
def test_cancelar():
    notifica = Notificador()
    
    msj = notifica.cancelar("Yudit cancelada")
    
    assert "Yudit" in msj

