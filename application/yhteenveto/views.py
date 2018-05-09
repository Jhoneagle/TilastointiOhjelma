from application import app, db
from flask import redirect, render_template, request, url_for
from application.visits.models import Visit
from application.yhteenveto.forms import InYearForm, InMonthForm
from flask_login.utils import login_required, current_user
from application.sivu.models import Sivu
from sqlalchemy.sql import text

@app.route("/yhteenveto/alku/", methods=["GET"])
@login_required
def yhteenveto_alku():
    return render_template("yhteenveto/valinta.html", title="Yhteenvedot")

@app.route("/yhteenveto/vuodessa/", methods=["GET", "POST"])
@login_required
def yhteenveto_vuodessa():
    if request.method == 'POST':
        form = InYearForm(request.form)
        stmt = text("SELECT sivu.osoite, SUM(visit.lukumaara) AS maara FROM sivu, visit WHERE visit.vuosi = :vuosi AND visit.sivu_id = sivu.id AND sivu.account_id = :id GROUP BY sivu.osoite").params(vuosi=form.year.data, id=current_user.id)
        
        result = db.engine.execute(stmt)
        return render_template("yhteenveto/vuodessa.html", title="Käyntejä sivuilla vuodessa", vuosi=result)
    else:
        return render_template("yhteenveto/kyselyvuodessa.html", title="Käyntejä sivuilla vuodessa", form = InYearForm())

@app.route("/yhteenveto/ryhma/", methods=["GET", "POST"])
@login_required
def yhteenveto_ryhmatulos():
    if request.method == 'POST':
        form = InMonthForm(request.form)
        stmt = text("SELECT sivu.ryhma AS ryhma, SUM(visit.lukumaara) AS maara FROM sivu, visit WHERE visit.vuosi = :vuosi AND visit.kuukausi = :kuukausi AND visit.sivu_id = sivu.id AND sivu.account_id = :id GROUP BY sivu.ryhma").params(vuosi=form.year.data, kuukausi=form.month.data, id=current_user.id)
        
        result = db.engine.execute(stmt)
        return render_template("yhteenveto/ryhmassa.html", title="Käyntejä sivuryhmissä vuodessa", vuosi=result)
    else:
        return render_template("yhteenveto/kyselyryhmassa.html", title="Vuoden tilasto", form = InMonthForm())

@app.route("/yhteenveto/selaimia/", methods=["GET", "POST"])
@login_required
def yhteenveto_selaimia():
    if request.method == 'POST':
        form = InYearForm(request.form)
        stmt = text("SELECT selain.selain AS nimi, SUM(selain.kaynnit) AS maara FROM sivu, selain, kavijat WHERE selain.kavijat_id = kavijat.id AND kavijat.vuosi = :vuosi AND kavijat.sivu_id = sivu.id AND sivu.account_id = :id GROUP BY selain.selain").params(vuosi=form.year.data, id=current_user.id)
        
        result = db.engine.execute(stmt)
        return render_template("yhteenveto/selaimia.html", title="Selaimien yhteenveto", selaimet=result)
    else:
        return render_template("yhteenveto/selainvuosi.html", title="Vuoden tilasto", form = InYearForm())

@app.route("/yhteenveto/kavijoita/", methods=["GET", "POST"])
@login_required
def yhteenveto_kavijoita():
    if request.method == 'POST':
        form = InYearForm(request.form)
        stmt = text("SELECT sivu.osoite, SUM(kavijat.kaynnit) AS maara FROM sivu, kavijat WHERE kavijat.vuosi = :vuosi AND kavijat.sivu_id = sivu.id AND sivu.account_id = :id GROUP BY sivu.osoite").params(vuosi=form.year.data, id=current_user.id)
        
        result = db.engine.execute(stmt)
        return render_template("yhteenveto/kavijoita.html", title="Kavijoita sivuilla vuodessa", kavijat=result)
    else:
        return render_template("yhteenveto/kavijavuosi.html", title="Vuoden tilasto", form = InYearForm())