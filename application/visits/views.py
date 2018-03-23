from application import app, db
from flask import redirect, render_template, request, url_for
from application.visits.models import Visit

@app.route("/visits/new/")
def visits_form():
    return render_template("visits/new.html", title="Add visit")

@app.route("/visits/", methods=["POST"])
def visits_create():
    v = Visit(osoite=request.form.get("osoite"), kuukausi=request.form.get("kuukausi"), vuosi=request.form.get("vuosi"), lukumaara=request.form.get("lukumaara"))
    db.session().add(v)
    db.session().commit()

    return redirect(url_for("visit_index"))

@app.route("/visits", methods=["GET"])
def visit_index():
    return render_template("visits/list.html", title="Visit listing")

@app.route("/result/", methods=["GET", "POST"])
def visits_result():
    if request.method == 'POST':
        result = db.engine.execute("SELECT * FROM Visit WHERE kuukausi = :month AND vuosi = :year", {'month':request.form.get("kuukausi"), 'year':request.form.get("vuosi")})
        result2 = db.engine.execute("SELECT * FROM Visit WHERE kuukausi = :month AND vuosi = :year", {'month':request.form.get("kuukausi"), 'year':request.form.get("vuosi2")})
        return render_template("visits/result.html", title="Result", visits=result, visits2=result2)
    else:
        return render_template("visits/result.html", title="Result")