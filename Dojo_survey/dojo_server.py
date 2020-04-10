from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def form():
    return render_template('mainForm.html')

@app.route('/result', methods=['POST'])
def create_user():
    print("Post info submitted")
    print(request.form)
    form_name = request.form['name']
    form_email = request.form['email']
    form_username = request.form['username']
    form_cohort = request.form['cohort']
    return render_template("results.html", form_name = form_name, form_email = form_email, form_username = form_username, form_cohort = form_cohort)


if __name__=="__main__":
    app.run(debug=True)