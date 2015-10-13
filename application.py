from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")

@app.route("/application-form")
def form_application():
    """ return application-form template """

    return render_template('application-form.html')

@app.route("/application", methods=['POST'])
def submit_application():
    """ submits the application and returns all the data input in the applicaiton"""

    fname = request.form.get('firstname')
    lname = request.form.get('lastname')
    salary = request.form.get('salary')
    job = request.form.get('jobtype')


    return render_template('application-response.html', fname1=fname, lname1=lname, salary1=salary, job1=job)


if __name__ == "__main__":
    app.run(debug=True)
