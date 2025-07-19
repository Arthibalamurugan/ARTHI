from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    return '''
        <h2>Application Submitted Successfully!</h2>
        <a href="/">Go back to form</a>
    '''

if __name__ == '__main__':
    app.run(debug=True)
