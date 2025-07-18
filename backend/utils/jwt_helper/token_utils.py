import jwt

def decode_token(token, type=None):
    try:
        payload = jwt.decode(token, options={"verify_signature": False}, algorithms=["HS256"])
        if type and payload.get("type") != type:
            return None
        return payload
    except Exception:
        return None
