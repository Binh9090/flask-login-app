# Flask Login App

A simple Flask application demonstrating user authentication with Flask-Login. It includes login, logout, and protected routes with custom error handling and flash messages for incorrect login attempts.

## Features
- User authentication with Flask-Login.
- Flash messages for login success and failure.
- Protected routes accessible only after logging in.
- Organized directory structure for templates and static files.

## Project Structure
```
flask_blog/
├── app.py         # Main application file
├── templates/     # HTML templates
│   ├── login.html # Login page
│   ├── base.html  # Base template (if needed)
├── static/        # Static files (CSS, JS)
```

## Installation

1. **Clone the repository**:
   ```bash
   git https://github.com/Binh9090/flask-login-app.git
   cd flask-login-app
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install flask flask-login
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

5. Open your browser and navigate to `http://127.0.0.1:5000`.

## Usage

- Visit `/login` to log in.
- Use **username**: `admin` and **password**: `1234` for testing.
- After logging in, access `/protected` to see the protected content.
- Incorrect login attempts will show a flash message.

## Technologies Used
- **Python**: Core language for the backend.
- **Flask**: Micro web framework.
- **Flask-Login**: User session management.
- **HTML**: Frontend templates.

## Contributing
Feel free to fork the repository and submit pull requests. All contributions are welcome!

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

