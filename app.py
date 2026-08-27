from flask import Flask, render_template, request, redirect, flash
import sqlite3
import random
import string

app = Flask(__name__)
app.secret_key = "super_secret_key"

def init_db():
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS url_map (short_code TEXT PRIMARY KEY, original_url TEXT)''')
    conn.commit()
    conn.close()

def generate_short_code(length=6):
    """Generates a random 6-character string of letters and digits."""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

@app.route('/', methods=['GET', 'POST'])
def index():
    short_url = None
    if request.method == 'POST':
        long_url = request.form.get('long_url')
        
        if not long_url or not long_url.startswith(('http://', 'https://')):
            flash("Please enter a valid URL starting with http:// or https://")
            return render_template('index.html')

        conn = sqlite3.connect('urls.db')
        c = conn.cursor()
        
        short_code = generate_short_code()
        
        c.execute("INSERT INTO url_map (short_code, original_url) VALUES (?, ?)", 
                  (short_code, long_url))
        conn.commit()
        conn.close()
        
        short_url = request.host_url + short_code

    return render_template('index.html', short_url=short_url)

@app.route('/<short_code>')
def redirect_to_url(short_code):
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute("SELECT original_url FROM url_map WHERE short_code = ?", (short_code,))
    result = c.fetchone()
    conn.close()
    
    if result:
        return redirect(result[0])
    else:
        return "URL not found", 404

if __name__ == '__main__':
    init_db()
    app.run(debug=True)