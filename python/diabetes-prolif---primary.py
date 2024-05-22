# Matthew Carr, Evan Kontopantelis, Tim Doran, Christine Campbell, Lorraine Lipscombe, Emma Crosbie, Anothony Howell, Iain E Buchan, Andrew G Renehan, 2024.

import sys, csv, re

codes = [{"code":"F420800","system":"readv2"},{"code":"F420200","system":"readv2"},{"code":"2BBR.00","system":"readv2"},{"code":"2BBk.00","system":"readv2"},{"code":"F420100","system":"readv2"},{"code":"2BBV.00","system":"readv2"},{"code":"F420700","system":"readv2"},{"code":"2BBl.00","system":"readv2"},{"code":"2BBS.00","system":"readv2"},{"code":"2BBT.00","system":"readv2"},{"code":"F420600","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('diabetes-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["diabetes-prolif---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["diabetes-prolif---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["diabetes-prolif---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
