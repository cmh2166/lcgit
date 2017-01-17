"""Using list of identifiers in names.list, grab MARC/XML records + commit."""
import requests

lccn_url = "https://lccn.loc.gov/{0}/marcxml"
URIs = set()

with open("../identifiers/names.list") as fi:
    for line in fi:
        URIs.add(line.strip('\n'))

print("Processing %i URIs.")

for URI in URIs:
    lccn = URI.replace('http://id.loc.gov/authorities/names/', '')
    lccn_req = lccn_url.format(lccn)
    try:
        resp = requests.get(lccn_req).content
        file_out = lccn + ".marcxml.xml"
        with open('data/' + file_out, 'w') as out:
            out.write(resp)
        