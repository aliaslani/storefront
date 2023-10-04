
from django.core.exceptions import ValidationError
from pathlib import Path

def validate_file_size(file):
    max_size_kb = 150
    if file.size > max_size_kb * 1024:
        raise ValidationError(
            f'File size should not exceed {max_size_kb} KB.')


def validate_image_extension(file):
    valid_extensions = ['.jpg', '.png']
    file_extension = Path(file.name).suffix
    if file_extension.lower() not in valid_extensions:
        raise ValidationError(
            f'Unsupported file extension. Supported extensions are {valid_extensions}.')