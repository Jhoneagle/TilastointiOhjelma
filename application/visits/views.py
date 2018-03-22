from application import app, db
from flask import redirect, render_template, request, url_for
from application.visits.models import Visit

@app.route("/visits/new/")
def visits_form():
    return render_template("visits/new.html", title="Add visit")

@app.route("/visits/", methods=["POST"])
def visits_create():
    v = Visit(osoite=request.form.get("osoite"), kuukausi=request.form.get("kuukausi"), vuosi=request.form.get("vuosi"))
    db.session().add(v)
    db.session().commit()

    return redirect(url_for("visit_index"))

@app.route("/visits", methods=["GET"])
def visit_index():
    return render_template("visits/list.html", title="All visits", visits = Visit.query.all())