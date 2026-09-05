from flask import Flask, request, render_template_string
from app.models import db, User

app = Flask(__name__)

# ⚠️ SQL INJECTION
@app.route('/user/<username>')
def get_user(username):
    # VULN: String formatting in SQL query
    query = f"SELECT * FROM users WHERE username = '{username}'"
    result = db.session.execute(query)
    return str(result.fetchone())

# ⚠️ XSS
@app.route('/search')
def search():
    query = request.args.get('q', '')
    # VULN: Unescaped user input in HTML template
    template = f"<h1>Search results for: {query}</h1>"
    return render_template_string(template)

# ⚠️ 
@app.route('/download/<filename>')
def download_file(filename):
    # VULN: No path validation
    filepath = f"/var/www/uploads/{filename}"
    with open(filepath, 'rb') as f:
        return f.read()
