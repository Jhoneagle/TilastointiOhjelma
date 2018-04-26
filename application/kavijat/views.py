from application import app, db
from flask import redirect, render_template, request, url_for
from application.kavijat.models import Kavijat
from application.kavijat.forms import KayntiForm, ListKayntiForm
from application.kayttis.models import Kayttis
from application.selain.models import Selain
from flask_login.utils import login_required, current_user
from application.sivu.models import Sivu
from sqlalchemy.sql import text

@app.route("/kavijat/lisaa/", methods=["GET", "POST"])
@login_required
def kavija_lisays():
    if request.method == 'POST':
        form = KayntiForm(request.form)
    
        if not form.validate():
            return render_template("kavijat/uusiTulija.html", title="Uusia kävijöitä", form = form)

        result = Sivu.query.filter_by(osoite=form.tuloSivu.data).first()
    
        sivuId = None

        if result is None:
            s = Sivu(form.tuloSivu.data, form.osoiteRyhma.data)
            s.account_id = current_user.id
            db.session.add(s)
            db.session.commit()
        
            r = Sivu.query.filter_by(osoite=form.tuloSivu.data).first()
            sivuId = r.id
        else:
            sivuId = result.id
        
        k = Kayttis(form.kaynnit.data, form.kayttis.data)
        selain = Selain(form.kaynnit.data, form.selain.data)
        kavija = Kavijat(form.kaynnit.data, form.vuosi.data, form.kuukausi.data)
        kavija.sivu_id = sivuId
        
        db.session().add(kavija)
        db.session().commit()

        result = Kavijat.query.filter_by(sivu_id=sivuId).filter_by(kaynnit=form.kaynnit.data).filter_by(vuosi=form.vuosi.data).filter_by(kuukausi=form.kuukausi.data).first()
        k.kavijat_id = result.id
        selain.kavijat_id = result.id

        db.session().add(k)
        db.session().add(selain)
        db.session().commit()

        return redirect(url_for("kavijat_listaus"))
    else:
        return render_template("kavijat/uusiTulija.html", title="Uusia kävijöitä", form = KayntiForm())

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
        return render_template("kavijat/List.html", title="Kävijöiden listaus", form = ListKayntiForm())

@app.route("/kavijat/poisto/<kavijat_id>", methods=["POST"])
@login_required
def kavija_poisto(kavijat_id):
    stmt = text("DELETE FROM kavijat WHERE id = :id").params(id=kavijat_id)
    db.engine.execute(stmt)
    
    stmt = text("DELETE FROM selain WHERE kavijat_id = :id").params(id=kavijat_id)
    db.engine.execute(stmt)

    stmt = text("DELETE FROM kayttis WHERE kavijat_id = :id").params(id=kavijat_id)
    db.engine.execute(stmt)

    return redirect(url_for("kavijat_listaus"))