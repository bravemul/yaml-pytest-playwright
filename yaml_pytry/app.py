def login_api(username: str, password: str) -> dict:
    if username == "admin" and password == "123456":
        return {"code": 200, "msg": "success"}
    else:
        return {"code": 401, "msg": "unauthorized"}
