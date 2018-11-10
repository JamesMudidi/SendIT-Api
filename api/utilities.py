import string
import random

def serial_generator(size=6, chars=string.ascii_uppercase + string.digits):
    #Generate random serial number
    return ''.join(random.choice(chars) for _ in range(size))

def checks_blank_fields(*fields):
    """the function that checks for a blank field"""
    for field in fields:
        if field == "":
            return True

def check_field_types(parcel_name, description, pickup, destination):
    """Check if the types are string and int for price """
    if isinstance(parcel_name, str) and isinstance(description, str) and isinstance(pickup, str) \
            and isinstance(destination, str):
        return True

def removes_blank_spaces(*fields):
    """Remove blank spaces from the field"""
    for field in fields:
        if not field.strip():
            return True

def validate_status(status):
    """Validate status"""
    if status != "pending" and status != "cancel" and status != "transit" and status != "Delivered":
        return True
