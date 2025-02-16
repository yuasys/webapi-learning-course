from flask import Flask, request, jsonify, session, render_template
from flask_session import Session
from functools import wraps

app = Flask(__name__)

# セッション設定
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SESSION_TYPE'] = 'filesystem'               # セッションデータをファイルシステムに保存
app.config['SESSION_COOKIE_NAME'] = 'session-id'        # クッキーのキー名を 'session-id' に変更
Session(app)

# ダミーユーザー情報（通常はDBなどから取得する）
dummy_user = {
    'id': 1,
    'username': 'alice',
    'email': 'alice@example.com'
}

@app.route('/')
def index():
    return render_template('index.html')

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return jsonify({'error': 'Unauthorized: ログインが必要です'}), 401
        return f(*args, **kwargs)
    return decorated_function

@app.route('/auth/login', methods=['POST'])
def login():
    """
    ログインエンドポイント:
    リクエストボディにJSON形式で 'username' と 'password' を含めることを想定。
    認証成功の場合、サーバー側のセッションにユーザ情報を保存する。
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if username == 'alice' and password == 'password':
        # サーバー側のセッションにユーザー情報を保存
        session['user'] = dummy_user
        return jsonify({'message': 'ログイン成功'})
    else:
        return jsonify({'error': '認証失敗'}), 401

@app.route('/users/me', methods=['GET'])
@login_required
def get_current_user():
    """
    認証済みユーザーの情報を返すエンドポイント:
    セッションに保存されたユーザー情報を返す。
    """
    return jsonify(session['user'])

@app.route('/auth/logout', methods=['POST'])
@login_required
def logout():
    """
    ログアウトエンドポイント:
    セッションからユーザー情報を削除してログアウト処理を実施する。
    """
    session.pop('user', None)
    return jsonify({'message': 'ログアウトしました'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
