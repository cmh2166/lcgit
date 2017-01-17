"""Generates list of URIs for NAF resources from the id.loc.gov data dump."""
import re

naf_dump = "../identifiers/names.nt"
naf_output = "../identifiers/names.list"
uri_re = "http://id.loc.gov/authorities/names/(.+?)"
naf_resources = set()

with open(naf_output) as fi:
    for line in fi.readlines():
        if line.strip('\n'):
            naf_resources.add(line.strip('\n'))

with open(naf_dump) as fh:
    for line in fh:
        if re.search(uri_re, line):
            naf_resources.add(re.search(uri_re, line).group(0))

print("Found %i resources." % len(naf_resources))

naf_list = sorted(list(naf_resources))
num = len(naf_list)
count = 0

for n in naf_list:
    with open(naf_output, 'a') as fo:
        fo.write("%s\n" % n)
    count += 1
    if count % 10000 == 0:
        print("%i IDs written out of %i records." % (count, num))
