import sys
import re
from subprocess import PIPE, Popen
# Info
r_info = re.compile(r'''\#\#INFO=<ID=(?P<id>[^,]+),Number=(?P<number>-?\d+|\.|[AG]),Type=(?P<type>Integer|Float|Flag|Character|String),Description="(?P<desc>[^"]*)".*>''', re.VERBOSE);
# Format
r_format = re.compile(r'''\#\#FORMAT=<ID=(?P<id>.+),Number=(?P<number>-?\d+|\.|[AG]),Type=(?P<type>.+),Description="(?P<desc>.*)".*>''', re.VERBOSE);
field_set = []
if len(sys.argv) == 1:
    print("Specify a VCF File")
    sys.exit()
else:
    header, err = Popen(["bcftools", "view", "-h", sys.argv[1]], stdout = PIPE, stderr = PIPE).communicate()
    if err:
        print err
    info = [m.groupdict()["id"] for m in r_info.finditer(header)]
    format = [m.groupdict()["id"] for m in r_format.finditer(header)]
# Construct Query String
query_start = repr("%CHROM\t%POS\t%ID\t%REF\t%ALT\t%QUAL\t%FILTER\t" + \
                   '\t'.join(['%INFO/' + x for x in info]) + \
                   "[" + '\t'.join(['%' + x for x in format]) + "]\n")
print ' '.join(["bcftools", "query","-f", query_start, sys.argv[1]])