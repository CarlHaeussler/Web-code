curl -X POST -H "Content-type: application/json" \
-d "{  \
     \"nummer\"  : \"4   \",    \
     \"vorname\" : \"Olaf\",    \
     \"nachname\": \"Scholz\",      \
     \"strasse\":  \"kek straße 9\",  \
     \"plz\"   :\"187\",         \
     \"stadt\":\"hier\",         \
     \"telefon\":\"033\"   \
}"                              \
"localhost:5008/BestMitarbeiter"
