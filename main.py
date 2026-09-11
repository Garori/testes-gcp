def main(request):
    print(request.headers.get("nomenome"))
    print(request.get_json())
    # print(request.)
    return {"status": 200, "msg": "opa"}
