from django.core.exceptions import ValidationError
from .models import EmployeeModel



def validate_email(email):
    """Check if email is taken."""
    if EmployeeModel.objects.filter(email=email).exists():
        raise ValidationError(
            "An employee with that email already exists."
        ) from None
    return True


def validate_reg_number(reg_number):
    """Check if email is taken."""
    if EmployeeModel.objects.filter(reg_number=reg_number).exists():
        raise ValidationError(
            "An employee with that registration already exists."
        ) from None
    return True