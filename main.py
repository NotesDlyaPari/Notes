from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class Note:
    def __init__(self, author, content):
        self.author = author
        self.content = content

notes = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Здесь можно добавить логику авторизации через ASP
        # Пока просто предполагаем, что введенные данные верны
        return redirect(url_for('notes'))
    return render_template('login.html')

@app.route('/notes', methods=['GET', 'POST'])
def notes_page():
    if request.method == 'POST':
        content = request.form['content']
        author = request.form['author']
        notes.append(Note(author, content))
    return render_template('notes.html', notes=notes)

if __name__ == '__main__':
    app.run(debug=True)