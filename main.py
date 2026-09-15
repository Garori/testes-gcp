from requests import Request
def main(request:Request):
    print(request.headers.get("nomenome"))
    print(request.get_json())
    print(request.headers.items())
    # print(request.)
    return {"status": 200, "msg": "opa"}
