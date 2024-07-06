import sqlite3
from time import sleep
from typing import List
from flask import Flask, render_template, request
# from jinja2 import TemplateNotFound

app = Flask(__name__) # create a flask instance
app.config.from_object(__name__) # load config from this file
# load default config and override config frojm an os.environment variable
app.config.update(SECRET_KEY=b'__u53r!53Y13rc35')# secret key for sessions

def fetch_data(query: str) -> List:
    con = sqlite3.connect("results.db")
    cur = con.cursor()
    cur.execute(query)
    res = cur.fetchall()
    con.close()
    return res


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result/", methods=["GET", "POST"])
def result():
    error = False
    if request.method == "POST":
        registration_no = request.form.get("registration_no")
        exam_year = request.form.get("exam_year")
        semester = request.form.get("semester")
        department = request.form.get("department")
        sleep(1)
        if exam_year == "2024":
            query = f"SELECT subject_1, subject_2, subject_3, subject_4, subject_5, subject_6, subject_7, subject_8, subject_9, subject_10, gpa FROM result_2024 WHERE (registration_no={registration_no} AND year={exam_year})"
        elif exam_year == "2023":
            query = f"SELECT subject_1, subject_2, subject_3, subject_4, subject_5, subject_6, subject_7, subject_8, subject_9, subject_10, gpa FROM result_2023 WHERE (registration_no={registration_no} AND year={exam_year})"
        elif exam_year == "2022":
            query = f"SELECT subject_1, subject_2, subject_3, subject_4, subject_5, subject_6, subject_7, subject_8, subject_9, subject_10, gpa FROM result_2022 WHERE (registration_no={registration_no} AND year={exam_year})"
        elif exam_year == "2021":
            query = f"SELECT subject_1, subject_2, subject_3, subject_4, subject_5, subject_6, subject_7, subject_8, subject_9, subject_10, gpa FROM result_2021 WHERE (registration_no={registration_no} AND year={exam_year})"
        elif exam_year == "2020":
            query = f"SELECT subject_1, subject_2, subject_3, subject_4, subject_5, subject_6, subject_7, subject_8, subject_9, subject_10, gpa FROM result_2020 WHERE (registration_no={registration_no} AND year={exam_year})"
        elif exam_year == "2019":
            query = f"SELECT subject_1, subject_2, subject_3, subject_4, subject_5, subject_6, subject_7, subject_8, subject_9, subject_10, gpa FROM result_2019 WHERE (registration_no={registration_no} AND year={exam_year})"
        else:
            query = ""
        res_list = fetch_data(query)
        res_marks = res_list[0]
        query = f"SELECT subject_code, subject_name FROM subjects WHERE (semester={semester} AND subject_dept={department})"
        res_list = fetch_data(query)
        sub_dict = dict(res_list)
        tmp = 0
        final_res = []
        for key, value in sub_dict.items():
            final_res.append((key, value, res_marks[tmp]))
            tmp = tmp + 1
        print(final_res)
        return render_template("marksheet.html", final_res=final_res)
    else:
        error = True
        print(f"error: {error}")
        # return redirect(url_for("result"))
    return render_template("result.html")

@app.route("/about/")
def about():
    return render_template("about-us.html")
@app.route("/contact/")
def contact():
    return render_template("contact-us.html")

@app.route("/privacy-policy/")
def privacyPolicy():
    return render_template("privacy-policy.html")

@app.route("/licencing/")
def licencing():
    return render_template("licence.html")


if __name__ == "__main__":
    app.run(debug=True)
