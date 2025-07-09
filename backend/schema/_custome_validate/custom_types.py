from marshmallow import ValidationError


def validate_name(value):
    if not isinstance(value, str):
        raise ValidationError("Tên phải là chuỗi")
    v = value.strip()
    if len(v) < 3:
        raise ValidationError("Tên phải có ít nhất 3 ký tự")
    if len(v) > 100:
        raise ValidationError("Tên không được quá 100 ký tự")

def validate_description(value):
    if not isinstance(value, str):
        raise ValidationError("Mô tả phải là chuỗi")
    v = value.strip()
    if len(v) < 1:
        raise ValidationError("Mô tả không được để trống")
    if len(v) > 500:
        raise ValidationError("Mô tả không được quá 500 ký tự")

def validate_barcode(value):
    if value is None:
        return
    if not isinstance(value, str):
        raise ValidationError("Barcode phải là chuỗi")
    v = value.strip()
    if not v.isdigit():
        raise ValidationError("Barcode chỉ được chứa số")
    if not (8 <= len(v) <= 20):
        raise ValidationError("Barcode phải có từ 8 đến 20 ký tự")

def validate_image_url(value):
    if not isinstance(value, str):
        raise ValidationError("Image URL phải là chuỗi")
    v = value.strip()
    if not (v.startswith('http://') or v.startswith('https://')):
        raise ValidationError("Image URL phải bắt đầu bằng http:// hoặc https://")
    if not v.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):
        raise ValidationError("Image URL phải kết thúc bằng .jpg, .jpeg, .png hoặc .gif")

def validate_category_id(value):
    if not isinstance(value, str):
        raise ValidationError("Category ID phải là chuỗi")
    v = value.strip()
    if not v:
        raise ValidationError("Category ID không được để trống")
    if len(v) > 50:
        raise ValidationError("Category ID không được quá 50 ký tự")

