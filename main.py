def main(request):
    print(request.headers.get("nomenome"))
    print(request.get_json())
    for item in request.header.items():
        print(item)
    # print(request.)
    return {"status": 200, "msg": "opa"}
