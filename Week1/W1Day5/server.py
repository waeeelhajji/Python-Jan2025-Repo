from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "supersecretkey"

# Display route
@app.route("/")
def form_page():
    return render_template("form.html")

# Action route
@app.route("/submit_form", methods=['POST'])
def submit():
    # print(request.form)
    # session['user_name'] = request.form['user_name']
    # session['message'] = request.form['message']
    # return redirect("/result")
    user_name = request.form['user_name']
    message = request.form['message']
    if 'message_list' not in session:
        session['message_list']= []
    messages = session['message_list']
    messages.append({"username": user_name, "message": message})
    session["message_list"]=messages
    return redirect("/")

# display route for result page
@app.route("/result")
def result():
    return render_template("result.html")

@app.route("/clear")
def clear_session():
    session.clear()
    return redirect("/")
    
if __name__ == "__main__":
    app.run(debug=True)