from flask import Flask, render_template
app= Flask(__name__)

@app.route('/play')
def first():
    return render_template('playground_index.html', times=3)

@app.route('/play/<int:boxes>')
def second(boxes):
    return render_template('playground_index.html', times=boxes)

@app.route('/play/<int:boxes>/<color>')
def third(boxes, color):
    return render_template('playground_index.html', times=boxes, pickedColor=color)



if __name__=="__main__":
    app.run(debug=True)    # Run the app in debug mode.
