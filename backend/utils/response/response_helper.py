from flask import jsonify
from dataclasses import asdict, is_dataclass

def api_response(status: bool = True, message: str = None, data=None, status_code: int = 200):
    if is_dataclass(data) and not isinstance(data, type):
        data = asdict(data)

    response = {
        "status": "success" if status else "failed",
        "message": message,
        "data": data,
        "status_code": status_code
    }

    filtered_response = {key: value for key, value in response.items() if value is not None}

    return jsonify(filtered_response), status_code


def pager(results, page: int = 1, limit: int = 10, total: int = 0):
    return {
        "page": page,
        "limit": limit,
        "total": total,
        "total_pages": (total + limit - 1) // limit if limit else 0,
        "results": results
    }