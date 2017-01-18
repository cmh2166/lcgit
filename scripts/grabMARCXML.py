"""Using list of identifiers in names.list, grab MARC/XML records + commit."""
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import pushToGH

lccn_url = "https://lccn.loc.gov/{0}/marcxml"
URIs = set()
s = requests.Session()
retries = Retry(total=5, backoff_factor=1, status_forcelist=[])
s.mount('https://', HTTPAdapter(max_retries=retries))

with open("../identifiers/names.list") as fi:
    for line in fi:
        URIs.add(line.strip('\n'))

print("Processing %i URIs.")

for URI in URIs:
    lccn = URI.replace('http://id.loc.gov/authorities/names/', '')
    lccn_req = lccn_url.format(lccn)
    try:
        resp = s.get(lccn_req).content
        file_out = lccn + ".marcxml.xml"
        with open('data/' + file_out, 'w') as out:
            out.write(resp)
        pushToGH.commitToGH("marcxml", lccn)
