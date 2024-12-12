from flask import Flask, render_template

app = Flask(__name__)

# Route untuk halaman home
@app.route('/')
def home():
    return render_template('home.html')

# Route untuk halaman tentang saya
@app.route('/about')
def about():
    return render_template('about.html')

# Route untuk halaman hobi
@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html')


if __name__ == '__main__':
    app.run(debug=True)