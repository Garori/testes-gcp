def main(request):
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "POST,OPTIONS",
        "Access-Control-Allow-Headers": "*",
        "Access-Control-Max-Age": "3600",
    }

    if request.method == "OPTIONS":
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        return ("", 204, headers)

    # Set CORS headers for the main request

    print(request.headers)
    print(request.get_json())
    for item in request.headers.items():
        print(item)
    # print(request.)
    return {"msg":"teste"}, 200
