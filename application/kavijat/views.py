from application import app, db
from flask import redirect, render_template, request, url_for
from application.kavijat.models import Kavijat
from application.kavijat.forms import VisitorForm
from application.yhteenveto.forms import InMonthForm
from application.kayttis.models import Kayttis
from application.selain.models import Selain
from flask_login.utils import login_required, current_user
from application.sivu.models import Sivu
from sqlalchemy.sql import text

@app.route("/kavijat/lisaa/", methods=["GET", "POST"])
@login_required
def kavija_lisays():
    if request.method == 'POST':
        form = VisitorForm(request.form)
    
        if not form.validate():
            return render_template("kavijat/newVisitor.html", title="Lisää uusi tietue kävijöitä", form = form)

        result = Sivu.query.filter_by(osoite=form.website.data).first()
    
        sivuId = None

        if result is None:
            s = Sivu(form.website.data, form.websiteGroup.data)
            s.account_id = current_user.id
            db.session.add(s)
            db.session.commit()
        
            r = Sivu.query.filter_by(osoite=form.website.data).first()
            sivuId = r.id
        else:
            sivuId = result.id
        
        k = Kayttis(form.visitorsAmount.data, form.systemName.data)
        browser = Selain(form.visitorsAmount.data, form.browser.data)
        visitor = Kavijat(form.visitorsAmount.data, form.year.data, form.month.data)
        visitor.sivu_id = sivuId
        
        db.session().add(visitor)
        db.session().commit()

        result = Kavijat.query.filter_by(sivu_id=sivuId).filter_by(kaynnit=form.visitorsAmount.data).filter_by(vuosi=form.year.data).filter_by(kuukausi=form.month.data).first()
        k.kavijat_id = result.id
        browser.kavijat_id = result.id

        db.session().add(k)
        db.session().add(browser)
        db.session().commit()

        return redirect(url_for("kavijat_listaus"))
    else:
        return render_template("kavijat/newVisitor.html", title="Lisää uusi tietue kävijöitä", form = VisitorForm())

@app.route("/kavijat/listaus/", methods=["GET", "POST"])
@login_required
def kavijat_listaus():
    if request.method == 'POST':
        form = ListKayntiForm(request.form)
        stmt = text("SELECT kavijat.id AS id, kayttis.kayttis AS kayttis, selain.selain AS selain, kavijat.kaynnit AS kaynnit, sivu.osoite AS tulosivu "+
"FROM kavijat, selain, kayttis, sivu WHERE kavijat.id = kayttis.kavijat_id AND kavijat.id = selain.kavijat_id AND kavijat.kuukausi = :month AND kavijat.vuosi = :year "+
"AND kavijat.sivu_id = sivu.id AND sivu.account_id = :id").params(month=form.kuukausi.data, year=form.vuosi.data, id=current_user.id)
        
        result = db.engine.execute(stmt)
        return render_template("kavijat/Result.html", title="Result", tulokset=result)
    else:
        return render_template("kavijat/List.html", title="Kuukautisten Kävijöiden listaus", form = InMonthForm())

@app.route("/kavijat/poisto/<visitor_id>", methods=["POST"])
@login_required
def kavija_poisto(visitor_id):
    stmt = text("DELETE FROM kavijat WHERE id = :id").params(id=visitor_id)
    db.engine.execute(stmt)
    
    stmt = text("DELETE FROM selain WHERE kavijat_id = :id").params(id=visitor_id)
    db.engine.execute(stmt)

    stmt = text("DELETE FROM kayttis WHERE kavijat_id = :id").params(id=visitor_id)
    db.engine.execute(stmt)

    return redirect(url_for("kavijat_listaus"))