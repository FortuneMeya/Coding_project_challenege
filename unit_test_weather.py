from unittest.mock import Mock
from service import WeatherService

def test_service_initialization():
    mock_api = Mock()
    service = WeatherService(api=mock_api)
    assert service.api == mock_api