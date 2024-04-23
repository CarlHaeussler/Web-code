mitarbeiter = [
  {"nummer":"1",
   "vorname":"Otto",
   "nachname":"Müller",
   "strasse":"Adlergestell 700",
   "plz"   :"12527",
   "stadt":"Berlin",
   "telefon":"030 67549000" 
  },
  {"nummer":"2",
   "vorname":"Hans",
   "nachname":"Lindner",
   "strasse":"Friedenstraße 4",
   "plz"   :"10464",
   "stadt":"Wildau",
   "telefon":"03375 23925"
  },
  {"nummer":"3",
   "vorname":"Eva",
   "nachname":"Habeck",
   "strasse":"Seestraße 5",
   "plz"   :"10430",
   "stadt":"Wildau",
   "telefon":"03375 45321"
  },
]


def GibMitarbeiter(mitarbeiter):
  if mitarbeiter.get('vorname'):
    string='<span id="vorname">'+'Vorname:'+ mitarbeiter["vorname"]+'</span>'+'<br>'
  if mitarbeiter.get('nachname'):
    string+='Nachname:' + mitarbeiter["nachname"]+'<br>'
  if mitarbeiter.get('strasse'):
    string+='Straße:' + mitarbeiter["strasse"]+'<br>'
  if mitarbeiter.get('stadt'):
    string+='Stadt:' + mitarbeiter["stadt"]+'<br>'
  if mitarbeiter.get('tel'):
    string+='Tel:' + mitarbeiter["telefon"]+'<br>'
  if mitarbeiter.get('plz'):
    string+='Plz:' + mitarbeiter["plz"]+'<br>'
  if mitarbeiter.get('nummer'):
    string+='Nummer:' + mitarbeiter["nummer"]+'<br>'
    return string

def GibBestimmtenMitarbeiter(mitarbeiterliste,mitarbeiternummer):
  for mitarbeiter in mitarbeiterliste:
    if mitarbeiter.get("nummer")==str(mitarbeiternummer):
      return mitarbeiter
  return("Mitarbeiter mit dieser Nummer nicht vorhanden")


def GibAlleMitarbeiter(mitarbeiterliste):
	string=''
	for mitarbeiter in mitarbeiterliste:
		string+=GibMitarbeiter(mitarbeiter)+'<br>'
	return string

if __name__=='__main__':
	print(GibMitarbeiter(mitarbeiter))
	print(GibAlleMitarbeiter(mitarbeiterliste))


