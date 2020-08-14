import operator
from pprint import pprint

import requests

r = requests.get("https://www.juntadeandalucia.es/institutodeestadisticaycartografia/badea/stpivot/stpivot/Print?cube=467f3d64-c682-427c-82a1"
                 "-3ba0a5bec7fb&type=3&foto=si&ejecutaDesde=&codConsulta=38676&consTipoVisua=JP")

text = r.text.strip().splitlines()[1:]

cases = {}

for line in text:
    values = line.split(";")
    if values[1] == "Confirmados PCR":
        cases[values[0]] = int(values[2]) if values[2] else 0

pprint(cases)
