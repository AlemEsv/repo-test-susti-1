import sys
import os
from unittest.mock import Mock
from service import UserService
from interfaces import IUserRepository

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_welcome_user():
    mock_repo = Mock(spec=IUserRepository)
    mock_repo.get_user.return_value = {"id": "1", "name": "Luis"}
    service = UserService(mock_repo)
    assert service.welcome_user("1") == "Hola Luis"
