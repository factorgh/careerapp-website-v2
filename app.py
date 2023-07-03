from flask import Flask, render_template

app = Flask(__name__)


JOBS = [
    {
        "id": 1,
        "title": "Data Analyst",
        "location": "Bangladesh",
        "salary": "$120,000"
    },
    {
        "id": 2,
        "title": "Data Scientist",
        "location": "Accra",
        "salary": "$110,000"
    },
    {
        "id": 3,
        "title": "Frontend developer",
        "location": "Benin",
        "salary": "$10,000"
    },
    {
        "id": 4,
        "title": "Backend Developer",
        "location": "Egypt",
        "salary": "$1,000"
    },
    {
        "id": 5,
        "title": "Devops engineer",
        "location": "Silicon Valley",
        "salary": "$750"
    },
]


@app.route("/")
def helloworld():
    return render_template("home.html", jobs=JOBS, company_name="Burchells")
