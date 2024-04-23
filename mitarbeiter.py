mitarbeiterliste = [
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

  result = ""
  for attr, value in mitarbeiter.__dict__.items():
        result += f'<span id="{attr}">{attr}: {value}</span><br>'
  return result


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


