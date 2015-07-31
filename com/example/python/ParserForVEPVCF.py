#!/usr/bin
import vcf_parser;
vcfReader = vcf_parser.VCFParser(infile='/home/ashish/Downloads/RM15.bwaln.sorted.baq.rdp.fb.targets.filter.annot.vcf');
#vcfReader = vcf_parser.VCFParser(infile='/home/ashish/Downloads/RM15.bwaln.sorted.baq.rdp.fb.targets.filter.vcf');
tsvFile = open('/home/ashish/Downloads/RM15.bwaln.sorted.baq.rdp.fb.targets.filter.annot.vcf.txt','w');
#tsvFile = open('/home/ashish/Downloads/RM15.bwaln.sorted.baq.rdp.fb.targets.filter.vcf.txt','w');
tsvFile.write("CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\t");

for record in vcfReader:
    print record['INFO'];
    splitArray = str(record['INFO']).split(";");
    #print splitArray;
    for i in range(0,len(splitArray)):
        header = splitArray[i].split("=")[0];
        tsvFile.write(header+"\t");
    splitArray = str(record['FORMAT']).split(":");
    for i in range(0,len(splitArray)):
        tsvFile.write(splitArray[i]+"\t");
    break;
tsvFile.write("\n");
position = 0;
try:
    for record in vcfReader:
    #print record['INFO'];
    #tsvFile.write(record.CHROM+"\t"+str(record.P        OS)+"\t"+str(record.ID)+"\t"+record.REF+"\t"+str(record.ALT)+"\t"+str(record.QUAL)+"\t"+str(record.FILTER)+"\n");
        position = str(record['POS']);
        tsvFile.write(record['CHROM']+"\t"+str(record['POS'])+"\t"+str(record['ID'])+"\t"+record['REF']+"\t"+str(record['ALT'])+"\t"+str(record['QUAL'])+"\t"+str(record['FILTER']+"\t"));
        splitArray = str(record['INFO']).split(";");
        for i in range(0,len(splitArray)):
            data1 = splitArray[i].split("=")[1];
            tsvFile.write(data1+"\t");
            #tsvFile.write("\n");
        splitArray = str(record['unknown']).split(":");
        for i in range(0,len(splitArray)):
            tsvFile.write(splitArray[i]+"\t");
        tsvFile.write("\n");
except SyntaxError:
    print "Error in vcf file in record after the record with start position "+str(record['POS'])+" and chromosome "+record['CHROM']+".\nRemove the record and re-run the script";   
tsvFile.close();