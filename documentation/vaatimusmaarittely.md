# Vaatimusmäärittely

## Olemassa olevat toiminnot (User storyt)

### Kirjautuminen sekä rekistöröityminen

Palvelua voi käyttää useampi yritys samaan aikaan sekä yrityksen sisällä useampi työntekijä. Kummallekaan ei ole asetettu rajoituksia paitsi itse tietokanta. 

Jokaisen käyttäjän käyttäjänimen on yksilöllinen ja salasana on vähintään kuusimerkkiä, jolloin virheelliset kirjautumiset eivät ole todennäköisiä. Käyttäjistä julkista tietoa on ainoastaan Yrityksen nimi, jonka kuka vain pystyy näkemään ilman kirjautumista. Tämäkin kuitenkin tapahtuu anonyymisti, joten käyttäjiä ei pysty suoraan yrityslistasta päättelemään ellei ole muuta tietoa. 

Käyttäjien tietoja myös salasanaa, pois lukien käyttäjänimi, on mahdollista muokata kirjautumisen jälkeen. Jolloin esimerkiksi yrityksen nimen muuttuessa työntekijän ei tarvitse luoda uutta tunnusta.

#### kyselyt

Käyttäjän haku kirjautuessa:

```
SELECT * FROM account WHERE username = form.username.data AND password = form.password.data;
```

Rekistöröityessä varmistetaan ettei käyttäjänimi varattu

```
SELECT * FROM account WHERE username = form.username.data;
```

Käyttäjän rekistöröityminen eli uuden käyttäjän lisäys: 

```
INSERT INTO account (name, password, email, company, address, username, password) VALUES(form.name.data, form.phonenumber.data, form.email.data, form.company.data, form.address.data, form.username.data, form.password.data);
```

Käyttäjän tietojen päivitys eli muokkaus: 

```
UPDATE account SET name=newform.name.data, phonenumber=newform.phonenumber.data, email=newform.email.data, company=newform.company.data, address=newform.address.data, password=newform.password.data WHERE id=current_user.id;
```

Käyttäjän tietojen muokkausta varten haetaan tiedot ennen lomaketta: 

```
SELECT * FROM account WHERE id = current_user.id;
```

Käyttäjän poisto: 

```
DELETE FROM account WHERE id = id;
```

Käyttäjien yrityksien listaus: 

```
SELECT company FROM account;
```

### Nettisivujen käynnit

Mahdollisuus lisätä statistiikkaa siitä kuinka monta kertaa eri sivuilla on käyty ylipäätään eli riippumatta onko sama ihminen tullut monta kertaa. 

Kun dataa tästä on tarpeeksi kerääntynyt voidaan verrata sivujen määrää kuinka paljon ihmiset ovat sivulle olleet eri vuosina saman kuukauden aikana. Esimerkiksi, jos joulukuussa ihmisiä on käynyt hilaisesti. Tämän seurauksena tehdään mainoskampanja ajatellen seuraavaa joulukuuta ja sitten kampanjan jälkeen halutaan tietää toiko se jotain tulosta. Eli kasvoiko käyntienmäärä ja millä sivuilla.

#### kyselyt

Uuden tietueen lisäys: 

Haetaan onko nettisivu jo lisätty

```
SELECT * FROM sivu WHERE osoite = form.website.data;
```

Jos ei niin lisätään

```
INSERT INTO sivu (osoite, account_id, ryhma) VALUES (form.website.data, current_user.id, form.websiteGroup.data);
```

Lopuksi käynnin lisäys

```
INSERT INTO sivu (kuukausi, vuosi, lukumaara, sivu_id) VALUES (form.month.data, form.year.data, form.VisitAmount.data, sivuId);
```

Kahden vuoden käyntien vertailussa sivu käyntien haku: 

Mihin vuoteen verrataan kaikki käynnit kuukaudelta

```
SELECT * FROM visit, sivu WHERE visit.kuukausi = form.month.data AND visit.vuosi = form.year.data AND visit.sivu_id = sivu.id AND sivu.account_id = current_user.id;
```

Vuosi jota verrataan, kaikki käyntimäärät kuukaudessa

```
SELECT * FROM visit, sivu WHERE visit.kuukausi = form.month.data AND visit.vuosi = form.year2.data AND visit.sivu_id = sivu.id AND sivu.account_id = current_user.id;
```

### Kävijät nettisivuilla

Pystyy lisäämään tietoa siitä kuinka monta tietyllä käyttöjärjestelmän ja selaimen yhdistelmällä ihmisiä on tullut sivulle kuukaudessa.

Pystyy listaamaan tietyn kuukauden kävijöiden määrät kaikilta sivuilta, jolloin pystyy näkemään kuinka paljon ihmisiä on käynyt sivuilla ilman evästeitä eli mikä on luultavasti todellinen määrä ihmisiä sivuilla kuukauden aikana. 

Kuukauden kävijämäärää lisättäessä: 

Haetaan onko nettisivu jo lisätty

#### kyselyt

```
SELECT * FROM sivu WHERE osoite = form.website.data;
```

Jos ei niin lisätään

Haetaan onko nettisivu jo lisätty

```
SELECT * FROM sivu WHERE osoite = form.website.data;
```

Jos ei niin lisätään

```
INSERT INTO sivu (osoite, account_id, ryhma) VALUES (form.website.data, current_user.id, form.websiteGroup.data);
```

Lopuksi toteutetaan lisäykset

```
INSERT INTO kayttis (kavijat_id, kaynnit, kayttis) VALUES (result.id, form.visitorsAmount.data, form.systemName.data);
INSERT INTO selain (kavijat_id, kaynnit, selain) VALUES (result.id, form.visitorsAmount.data, form.browser.data);
INSERT INTO kavijat (sivu_id, kaynnit, vuosi, kuukausi) VALUES (sivuId, form.visitorsAmount.data, form.year.data, form.month.data);
```

Kävijämäärien tietynä kuukautena eri sivuilla listaus: 

```
SELECT kavijat.id AS id, kayttis.kayttis AS kayttis, selain.selain AS selain, kavijat.kaynnit AS kaynnit, sivu.osoite AS tulosivu FROM kavijat, selain, kayttis, sivu WHERE kavijat.id = kayttis.kavijat_id AND kavijat.id = selain.kavijat_id AND kavijat.kuukausi = form.month.data AND kavijat.vuosi = form.year.data AND kavijat.sivu_id = sivu.id AND sivu.account_id = current_user.id;
```

Kävijä tietueen poisto: 

```
DELETE FROM kavijat WHERE id = visitor_id;
DELETE FROM selain WHERE kavijat_id = visitor_id;
DELETE FROM kayttis WHERE kavijat_id = visitor_id;
```

### Yhteenvedot

Yhteenvetoja on neljää erilaista, jotka ovat

* Käyttäjä haluaa tietää kuinka paljon hänen sivuillaan on käytä vuoden aikana. Katsoessaan useamman vuoden tiedot, niin hän voi tietää miten sivu on kehittynyt tavallisten netissä kulkevien silmissä. Onko esimerkiksi jokin sivu kiinnostavampi, kuin ennen.
* Käyttäjä voi nähädä käyntien määrän sivustoryhmissä tietynä kuukautena. Jolloin pystyy näkemään onko ihmiset eniten kiinnostuneita esimerkiksi peli vai ruoka vai vaate sivuista. Riippuen täysin millaisiin kategorioihin sivut on jaettu.
* Käyttäjä pääsee näkemään kuinka paljon enemmän esimerkiksi Mozilla Firefoxia, kuin Google Chromea on ihmiset käyttäneet heidän tullessaan sivuille. Tästä on apua, kun hän haluaa tietää mitä selainta hänen sivujen on parhaiten tuettava. 
* Käyttäjä voi nähädä lähes todellisen määrän mitä ihmisiä (eli ei aikaisempaa tallennetta tulosta) on käynyt eri sivuilla.  

#### kyselyt

Ensimmäinen kysely: 

```
SELECT sivu.osoite, SUM(visit.lukumaara) AS maara FROM sivu, visit WHERE visit.vuosi = form.year.data AND visit.sivu_id = sivu.id AND sivu.account_id = current_user.id GROUP BY sivu.osoite;
```

Toinen kysely: 

```
SELECT sivu.ryhma AS ryhma, SUM(visit.lukumaara) AS maara FROM sivu, visit WHERE visit.vuosi = form.year.data AND visit.kuukausi = form.month.data AND visit.sivu_id = sivu.id AND sivu.account_id = current_user.id GROUP BY sivu.ryhma;
```

Kolmas kysely: 

```
SELECT selain.selain AS nimi, SUM(selain.kaynnit) AS maara FROM sivu, selain, kavijat WHERE selain.kavijat_id = kavijat.id AND kavijat.vuosi = form.year.data AND kavijat.sivu_id = sivu.id AND sivu.account_id = current_user.id GROUP BY selain.selain;
```

Neljäs kysely: 

```
SELECT sivu.osoite, SUM(kavijat.kaynnit) AS maara FROM sivu, kavijat WHERE kavijat.vuosi = form.year.data AND kavijat.sivu_id = sivu.id AND sivu.account_id = current_user.id GROUP BY sivu.osoite;
```

## Jatkokehitys suuntia

* Validoinnin jatkokehitys tiukemmaksi eri paikoissa.
* Yrityksen nimen yksilöistäminen yritysten listauksessa eli toistojen poisto.
* Madhollisuus hakea ja järjestää dataa listauksissa.
* Mahdollisuus saada kokonaistulos listauksiin. Myös vuosien välinen erotus käyntien vertailuun kaikille sivuille.
* Yhteenvetojen graaffinen visualisointi.
* Lisää datan syöttö ja käyttö mahdollisuuksia.
* Käyttäjä tasojen luonti. Esimerkiksi admin, moderator ja normaali käyttäjä.
