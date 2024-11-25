from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

# Khởi tạo ứng dụng Flask
app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Khởi tạo LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"  # Đặt trang login khi chưa đăng nhập

# Cấu trúc dữ liệu giả lập cho database
users = {}

# Khai báo class User
class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

# Load người dùng
@login_manager.user_loader
def load_user(user_id):
    for user in users.values():
        if user.id == user_id:
            return user
    return None

# Trang chủ
@app.route("/")
def index():
    return render_template("index.html")

# Đăng ký
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users:
            flash("Username đã tồn tại!", "warning")
        else:
            user = User(id=str(len(users) + 1), username=username, password=password)
            users[username] = user
            flash("Đăng ký thành công! Đăng nhập ngay nào.", "success")
            return redirect(url_for("login"))
    return render_template("register.html")

# Đăng nhập
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = users.get(username)
        if user and user.password == password:
            login_user(user)
            flash("Đăng nhập thành công!", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Sai username hoặc password! Hãy thử lại.", "danger")  # Thông báo khi nhập sai
            return redirect(url_for("login"))  # Chuyển hướng lại trang đăng nhập
    return render_template("login.html")

# Dashboard (Chỉ cho người dùng đã đăng nhập)
@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", username=current_user.username)

# Đăng xuất
@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Đã đăng xuất!", "info")
    return redirect(url_for("index"))

# Chạy ứng dụng
if __name__ == "__main__":
    app.run(debug=True)
