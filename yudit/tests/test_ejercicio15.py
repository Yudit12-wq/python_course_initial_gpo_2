import sys
from pathlib import Path
 
# Agregar la ruta raíz del proyecto al path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from yudit.src.ejercicio15 import Servicio

def test_servicio(mocker):
    mock_logger = mocker.Mock()
    
    service = Servicio(logger=mock_logger)
    
    service.procesar_data()
    
    mocker_logger.info.assert_called_once_with("Procesando data...")