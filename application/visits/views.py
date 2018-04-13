from application import app, db
from flask import redirect, render_template, request, url_for
from application.visits.models import Visit
from application.visits.forms import VisitForm, ListForm
from flask_login.utils import login_required, current_user
from application.sivu.models import Sivu
from sqlalchemy.sql import text

@app.route("/visits/new/")
@login_required
def visits_form():
    return render_template("visits/new.html", title="Add visit", form = VisitForm())

@app.route("/visits/", methods=["POST"])
@login_required
def visits_create():
    form = VisitForm(request.form)
    
    if not form.validate():
        return render_template("visits/new.html", form = form)

    result = Sivu.query.filter_by(osoite=form.osoite.data).first()
    
    sivuId = None

    if result is None:
        s = Sivu(form.osoite.data, form.osoiteRyhma.data)
        s.account_id = current_user.id
        db.session.add(s)
        db.session.commit()
        
        r = Sivu.query.filter_by(osoite=form.osoite.data).first()
        sivuId = r.id
    else:
        sivuId = result.id

    v = Visit(kuukausi=form.kuukausi.data, vuosi=form.vuosi.data, lukumaara=form.lukumaara.data)
    v.sivu_id = sivuId

    db.session().add(v)
    db.session().commit()
    
    return redirect(url_for("visit_index"))

@app.route("/visits", methods=["GET"])
@login_required
def visit_index():
    return render_template("visits/list.html", title="Visit listing", form = ListForm())

@app.route("/result/", methods=["GET", "POST"])
@login_required
def visits_result():
    if request.method == 'POST':
        form = ListForm(request.form)
        stmt = text("SELECT * FROM visit, sivu WHERE visit.kuukausi = :month AND visit.vuosi = :year AND visit.sivu_id = sivu.id AND sivu.account_id = :id").params(month=form.kuukausi.data, year=form.vuosi.data, id=current_user.id)
        stmt2 = text("SELECT * FROM visit, sivu WHERE visit.kuukausi = :month AND visit.vuosi = :year AND visit.sivu_id = sivu.id AND sivu.account_id = :id").params(month=form.kuukausi.data, year=form.vuosi2.data, id=current_user.id)

        result = db.engine.execute(stmt)
        result2 = db.engine.execute(stmt2)
        return render_template("visits/result.html", title="Result", visits=result, visits2=result2)
    else:
        return render_template("visits/result.html", title="Result")