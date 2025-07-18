from functools import wraps
from flask import request, g
from backend.error.business_errors import Forbidden
from backend.utils.jwt_helper.token_utils import decode_token


def authentication(role=None, rank=None):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            g.user_id = None
            g.role = "guest"
            g.rank = 0
            g.token = None

            auth_header = request.headers.get("Authorization", "")
            if auth_header.startswith("Bearer "):
                token = auth_header.replace("Bearer ", "").strip()
                payload = decode_token(token, type="access")
                if payload:
                    g.user_id = payload.get("sub")
                    g.role = payload.get("role", "guest")
                    g.rank = int(payload.get("rank", 0))
                    g.token = token
            if role and g.role.lower() != role.lower():
                raise Forbidden()

            if rank is not None and g.rank < rank:
                raise Forbidden()

            return f(*args, **kwargs)

        wrapper._auth_required = True
        return wrapper
    return decorator
