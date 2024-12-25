from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def my_Func():
    return render_template('index.html')

@app.route('/home')
def my_Function():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('aboutus.html')

@app.route('/contact')
def contact():
    return render_template('contactus.html')

@app.route('/countries')
def countires():
    return render_template('countries.html')

@app.route('/usa')
def USA():
    return render_template('usa.html')

@app.route('/australia')
def aus():
    return render_template('aus.html')

@app.route('/germany')
def ger():
    return render_template('germany.html')

if __name__ == '__main__':
    app.run(debug=True)

print("hello wo")

