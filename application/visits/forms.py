from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, SelectField, SubmitField
from wtforms import validators, ValidationError

class VisitForm(FlaskForm):
    website = TextField("Nettisivun osoite",[validators.length(1, 1000, "Lisää osoite")])
    websiteGroup = TextField("Nettisivun ryhmän nimi",[validators.length(1, 1000, "Lisää ryhmä")])

    VisitAmount = IntegerField("Käyntejä kuukaudessa",[validators.NumberRange(1, 1000000, "Pitää olla suurempi, kuin 0")])

    year = SelectField("Vuosi", choices = [('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'),
('2006', '2006'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'),
('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020')])

    month = SelectField("Kuukausi", choices = [('1', 'Tammikuu'), ('2', 'Helmikuu'),('3', 'Maaliskuu'), ('4', 'Huhtikuu'),('5', 'Toukokuu'), ('6', 'Kesäkuu'),
('7', 'Heinäkuu'), ('8', 'Elokuu'),('9', 'Syyskuu'), ('10', 'Lokakuu'),('11', 'Marraskuu'), ('12', 'Joulukuu')])

class ListForm(FlaskForm):
    year = SelectField("Valitse vuosi", choices = [('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'),
('2006', '2006'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'),
('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020')])

    year2 = SelectField("Valitse verrattava vuosi", choices = [('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'),
('2006', '2006'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'),
('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020')])

    month = SelectField("Valitse kuukausi", choices = [('1', 'Tammikuu'), ('2', 'Helmikuu'),('3', 'Maaliskuu'), ('4', 'Huhtikuu'),('5', 'Toukokuu'), ('6', 'Kesäkuu'),
('7', 'Heinäkuu'), ('8', 'Elokuu'),('9', 'Syyskuu'), ('10', 'Lokakuu'),('11', 'Marraskuu'), ('12', 'Joulukuu')])