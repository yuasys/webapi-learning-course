from flask import Flask, jsonify, make_response, render_template
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def index():
    """
    HTML ページをサーブするエンドポイント
    """
    return render_template('index.html')

@app.route('/cache/no-stale-while-revalidate', methods=['GET'])
def no_stale_while_revalidate():
    """
    Cache-Control: stale-while-revalidate を含まないレスポンス
    """
    now = datetime.utcnow()
    response = make_response(
        jsonify({
            "message": "no-stale-while-revalidate response",
            "timestamp": now.isoformat() + "Z",
        })
    )
    response.headers['Cache-Control'] = "max-age=30"
    return response

@app.route('/cache/with-stale-while-revalidate', methods=['GET'])
def with_stale_while_revalidate():
    """
    Cache-Control: stale-while-revalidate response を含むレスポンス
    """
    now = datetime.utcnow()
    response = make_response(
        jsonify({
            "message": "with-stale-while-revalidate response エンドポイント",
            "timestamp": now.isoformat() + "Z",
        })
    )
    response.headers['Cache-Control'] = "max-age=30, stale-while-revalidate=30"
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
