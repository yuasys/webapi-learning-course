from flask import Flask, request, jsonify

app = Flask(__name__)

# ---------------------------------------------------------
# ボタン1用: CORS設定を一切返さないエンドポイント
# ---------------------------------------------------------
@app.route("/no-cors-block")
def no_cors_block():
    return jsonify(message="This response has no CORS headers")

# ---------------------------------------------------------
# ボタン2用: プリフライトは起きないけれど、本リクエストまで通る
# ---------------------------------------------------------
@app.route("/cors-no-preflight-pass")
def cors_no_preflight_pass():
    response = jsonify(message="This response allows your origin")
    response.headers.add("Access-Control-Allow-Origin", "http://localhost:3000")
    return response


# ---------------------------------------------------------
# ボタン3用: プリフライトは起きるけれど、Originが許可されない
# ---------------------------------------------------------
@app.route("/cors-with-preflight-block", methods=["GET", "OPTIONS"])
def cors_with_preflight_block():
    if request.method == "OPTIONS":
        headers = {
            "Access-Control-Allow-Origin": "http://localhost:9999",
            "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type, X-Custom-Header",
        }
        return '', 204, headers  # 204 No Content を返す

    response = jsonify(message="This request was attempted with preflight but the origin wasn't allowed.")
    response.headers.add("Access-Control-Allow-Origin", "http://localhost:9999")
    return response

# ---------------------------------------------------------
# ボタン4用: プリフライトから本リクエストまで通る
# ---------------------------------------------------------
@app.route("/cors-with-preflight-pass", methods=["GET", "OPTIONS"])
def cors_with_preflight_pass():
    if request.method == "OPTIONS":
        headers = {
            "Access-Control-Allow-Origin": "http://localhost:3000",
            "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type, X-Custom-Header",
        }
        return '', 204, headers  # 204 No Content を返す

    response = jsonify(message="This request should succeed after a successful preflight!")
    response.headers.add("Access-Control-Allow-Origin", "http://localhost:3000")
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
