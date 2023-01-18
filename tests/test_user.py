from app.user.models import User
from fastapi import HTTPException


def test_check_cpf_success_without_caracter():
    cpf = "12345678910"
    assert User.check_cpf(cpf) == cpf


def test_check_cpf_success_with_caracter():
    cpf = "123.456.789-10"
    assert User.check_cpf(cpf) == cpf


def test_check_cpf_size():
    insufficient_number_cpf = "1234567891"
    extra_number_cpf = "123456789101"
    try:
        User.check_cpf(insufficient_number_cpf)
        User.check_cpf(extra_number_cpf)
        assert False
    except HTTPException:
        assert True


def test_check_cpf_letter():
    include_letter_cpf = "12345678910a"
    error_letter_cpf = "1234567891O"
    try:
        User.check_cpf(include_letter_cpf)
        User.check_cpf(error_letter_cpf)
        assert False
    except HTTPException:
        assert True


def test_check_name():
    name = "Some Name"
    assert User.check_name(name) == name


def test_check_name_with_number():
    name = "Some name 1"
    try:
        assert User.check_name(name) == name
        assert False
    except HTTPException:
        assert True


def test_check_name_is_empty():
    name = ""
    try:
        assert User.check_name(name) == name
        assert False
    except HTTPException:
        assert True


def test_valid_email():
    email = "my.email@email.com"
    assert User.check_name(email) == email


def test_check_invalid_email():
    email = "ankitrai326.com"
    try:
        assert User.check_name(email) == email
        assert False
    except HTTPException:
        assert True


def test_check_email_is_empty():
    email = ""
    try:
        assert User.check_name(email) == email
        assert False
    except HTTPException:
        assert True


def test_check_tell_success_without_caracter():
    tell = "61912345678"
    assert User.check_tell(tell) == tell


def test_check_tell_success_with_caracter():
    tell = "(61)912345678"
    assert User.check_tell(tell) == tell


def test_check_tell_size():
    insufficient_number_tell = "(61)91234567"
    extra_number_tell = "(61)9123456788"
    try:
        User.check_tell(insufficient_number_tell)
        User.check_tell(extra_number_tell)
        assert False
    except HTTPException:
        assert True


def test_check_tell_letter():
    include_letter_tell = "(61)912345678a"
    error_letter_tell = "(61)91234567O"
    try:
        User.check_tell(include_letter_tell)
        User.check_tell(error_letter_tell)
        assert False
    except HTTPException:
        assert True
