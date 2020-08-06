try:
    import pymysql
    import requests
    import time
    import os
    from flask import Flask, render_template, url_for, redirect, request

    print("All modules loaded")
except:
    print("Some modules are missing..")

application = Flask(__name__)

PEOPLE_FOLDER = os.path.join("static", "img")

application.config["UPLOAD_FOLDER"] = PEOPLE_FOLDER


dateTime = time.time()


ip = requests.get("https://checkip.amazonaws.com").text.strip()


@application.route("/")
def index():
    data = ip
    s = dateTime
    full_filename = os.path.join(application.config["UPLOAD_FOLDER"], "aws.jpg")
    full_filename2 = os.path.join(application.config["UPLOAD_FOLDER"], "mul.jpg")
    return render_template(
        "index.html",
        data=data,
        s=s,
        user_image=full_filename,
        user_image2=full_filename2,
    )


@application.route("/SmallestEarthquake", methods=["POST", "GET"])
def smallestEarthquake():
    num = request.form.get("numbers")
    if num != " ":
        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
            + server
            + ";DATABASE="
            + database
            + ";UID="
            + username
            + ";PWD="
            + password
        )
        c = conn.cursor()
        query = (
            """SELECT latitude,longitude,magError,mag FROM all_month ORDER BY mag LIMIT """
            + num
        )
        c.execute(query)
        data = c.fetchall()
        c.close()
        conn.close()
        return render_template("output.html", data=data)


@application.route("/LargestEarthquake", methods=["POST", "GET"])
def largestEarthquake():
    num = request.form.get("numbers")
    if num != " ":
        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
            + server
            + ";DATABASE="
            + database
            + ";UID="
            + username
            + ";PWD="
            + password
        )
        c = conn.cursor()
        query = (
            """SELECT latitude,longitude,magError,mag FROM all_month ORDER BY mag DESC LIMIT """
            + num
        )
        c.execute(query)
        data = c.fetchall()
        c.close()
        conn.close()
        return render_template("output.html", data=data)


if __name__ == "__main__":
    application.run(host="127.0.0.1", debug=True)
