# Matthew Carr, Evan Kontopantelis, Tim Doran, Christine Campbell, Lorraine Lipscombe, Emma Crosbie, Anothony Howell, Iain E Buchan, Andrew G Renehan, 2024.

import sys, csv, re

codes = [{"code":"C108100","system":"readv2"},{"code":"C108y00","system":"readv2"},{"code":"C106y00","system":"readv2"},{"code":"C108200","system":"readv2"},{"code":"C109200","system":"readv2"},{"code":"66Aa.00","system":"readv2"},{"code":"C10E212","system":"readv2"},{"code":"C10E112","system":"readv2"},{"code":"C10zy00","system":"readv2"},{"code":"C109100","system":"readv2"},{"code":"C109300","system":"readv2"},{"code":"C10yy00","system":"readv2"},{"code":"66AY.00","system":"readv2"},{"code":"C109000","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('diabetes-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["diabetes-compliance---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["diabetes-compliance---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["diabetes-compliance---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
