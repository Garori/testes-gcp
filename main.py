def main(request):
    print(request.headers)
    print(request.get_json())
    for item in request.headers.items():
        print(item)
    # print(request.)
    return {"status": 200, "msg": "opa"}
