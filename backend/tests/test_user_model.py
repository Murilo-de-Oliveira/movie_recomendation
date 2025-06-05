import pytest
from models.user_model import UserCreate

def test_user_create_model():
    user = UserCreate(name="João", email="joao@gmail.com", password="Senhalegal")
    assert user.name == "João"
    assert user.email == "joao@gmail.com"
    assert user.password == "Senhalegal"

def test_user_invalid_user():
    with pytest.raises(ValueError) as exinfo:
        UserCreate(name=123, email="inválido", password="inválido")
    
    errors = exinfo.value.errors()
    assert any(e['loc'] == ('name',) for e in errors)
    assert any(e['loc'] == ('email',) for e in errors)