from flask import request, g
from backend.utils.jwt_helper.token_utils import decode_token

def authenticate_request():
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
