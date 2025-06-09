"""
Author: Fortune Meya
Date:06/08/2025
Backend
Tests for the weather service
"""
from unittest.mock import Mock
from service import WeatherService

def test_service_initialization():
    """
    Checks the service initialization function
    """
    mock_api = Mock()
    service = WeatherService(api=mock_api)
    assert service.api == mock_api