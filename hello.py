from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
# def index():
#     return "<h1>Hello World!</h1>"

def index():
    first_name = 'Shrujan'
    stuff='This is bold text'
    fevorite_pizza=['Peeperoni', 'Cheese', 'Mushrooms', 41]
    return render_template('index.html', 
            first_name=first_name,
            stuff=stuff,
            fevorite_pizza=fevorite_pizza)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)
    # return "<h1>Hello {}</h1>".format(name)

# Create Custom Error Pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)