from proyecto.interfaz.metodos import solicitar_cantidad
import sys
import os
from unittest.mock import patch
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_solicitar_cantidad():
    with patch('builtins.input', side_effect=["abc", 12]):
        with patch('builtins.print') as mock_print:
            assert type(solicitar_cantidad()) == float
            mock_print.assert_called_with(
                "❌ Cantidad inválida. Por favor, introduce una cantidad válida.")
