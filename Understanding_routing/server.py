from flask import Flask
app= Flask(__name__)

# routes-----------------
@app.route('/')
def hello_world():
    print("you are in the hello world route")
    return "hello_world"

@app.route('/dojo')
def dojo():
    print("you are in the hello world route")
    return "Dojo!"

@app.route('/say/<name>')
def say(name):
    print(name)
    return "Hi " + name + "!"

@app.route('/repeat/<int:number>/<name>')
def repeat(number, name):
    output = ""
    for i in range(number):
        output += name + " "
    return output


if __name__=="__main__":
    app.run(debug=True)
