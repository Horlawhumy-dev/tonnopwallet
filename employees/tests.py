
from django.test import TestCase
import pytest
from .validators import validate_email, validate_reg_number


@pytest.mark.django_db
def test_validate_email():
    email_exist_or_not = validate_email("olawumiarafat@gmail.com")
    assert email_exist_or_not == True

@pytest.mark.django_db
def test_validate_reg_number():
    reg_num_exist_or_not = validate_reg_number("20220513")
    assert reg_num_exist_or_not == True