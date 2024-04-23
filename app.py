import flask, mitarbeiter
from flask import render_template
from flask import request,jsonify
import mitarbeiter
app=flask.Flask(__name__)
app=flask.Flask(__name__, template_folder='templates')


@app.route('/eingabe',methods=['get'])
def mitarbeitereingabe():
     return render_template('formular.html')

@app.route('/mitarbeiter/upload',methods=['POST'])
def formular():
  if request.method=='POST':
    name=request.form['mitarbeitername']
    print('Vorname ist:'+name)
    mitarbeiter.mitarbeiterliste.append({'vorname':name})
    return  "Name eingegeben"



@app.route('/BestMitarbeiter',methods=['get', 'POST'])
def home4():
  if request.method == 'GET':

    if 'nummer' in request.args:
        mitarbeiternr=request.args['nummer']
        print(mitarbeiternr)
        return jsonify(
        mitarbeiter.GibBestimmtenMitarbeiter(
                   mitarbeiter.mitarbeiterliste,
                   int( mitarbeiternr))
    )
    else: return "unbekannte Abfrage"

  elif request.method == 'POST':
    content_type = request.headers.get('content-type')
    if (content_type == 'application/json'):
      json = request.get_json()
      mitarbeiter.mitarbeiterliste.append(json)
      return json
    else:return "unbekanntes Datenformat beim Posten"


@app.route('/mitarbeiter', methods=['GET'])
def home():
    string = mitarbeiter.GibAlleMitarbeiter(mitarbeiter.mitarbeiterliste)
    return render_template('home.html', mycontent=string)

@app.route('/mitarbeiter1', methods=['GET'])
def mitarbeiter1():
    string = mitarbeiter.GibMitarbeiter(mitarbeiter.mitarbeiter1)
    return render_template('home.html', mycontent=string)

@app.route('/mitarbeiter2', methods=['GET'])
def mitarbeiter2():
    string = mitarbeiter.GibMitarbeiter(mitarbeiter.mitarbeiter2)
    return render_template('home.html', mycontent=string)

@app.route('/mitarbeiter3', methods=['GET'])
def mitarbeiter3():
    string = mitarbeiter.GibMitarbeiter(mitarbeiter.mitarbeiter3)
    return render_template('home.html', mycontent=string)

app.run(host='0.0.0.0', port=5008)
