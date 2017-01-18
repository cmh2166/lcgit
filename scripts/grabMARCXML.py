"""Using list of identifiers in names.list, grab MARC/XML records + commit."""
import requests
import pushToGH

lccn_url = "https://lccn.loc.gov/{0}/marcxml"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) \
           AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 \
           Safari/537.36'}
URIs = set()

with open("identifiers/names.list") as fi:
    for line in fi:
        URIs.add(line.strip('\n'))
print("Processing %i URIs." % len(URIs))


pushToGH.setBranch("marcxml")
for URI in URIs:
    lccn = URI.replace('http://id.loc.gov/authorities/names/', '').strip('>')
    lccn_req = lccn_url.format(lccn)
    try:
        resp = requests.get(lccn_req, headers=headers).text
        file_out = 'data/' + lccn + ".marcxml.xml"
        with open(file_out, 'w') as out:
            out.write(resp)
        pushToGH.commitToGH("marcxml", lccn)
    except Exception as e:
        print("Error with %s : %s" % (lccn, e))
        continue
