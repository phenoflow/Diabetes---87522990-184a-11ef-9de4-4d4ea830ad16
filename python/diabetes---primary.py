# Matthew Carr, Evan Kontopantelis, Tim Doran, Christine Campbell, Lorraine Lipscombe, Emma Crosbie, Anothony Howell, Iain E Buchan, Andrew G Renehan, 2024.

import sys, csv, re

codes = [{"code":"9OLA.11","system":"readv2"},{"code":"8A13.00","system":"readv2"},{"code":"2G5K.00","system":"readv2"},{"code":"66A8.00","system":"readv2"},{"code":"8H2J.00","system":"readv2"},{"code":"66AG.00","system":"readv2"},{"code":"2G5B.00","system":"readv2"},{"code":"F440700","system":"readv2"},{"code":"66AJ100","system":"readv2"},{"code":"N030011","system":"readv2"},{"code":"M037200","system":"readv2"},{"code":"250 PR","system":"readv2"},{"code":"250 AN","system":"readv2"},{"code":"250 HP","system":"readv2"},{"code":"250 DR","system":"readv2"},{"code":"250 H","system":"readv2"},{"code":"250 LG","system":"readv2"},{"code":"250 JL","system":"readv2"},{"code":"250 AB","system":"readv2"},{"code":"250 JE","system":"readv2"},{"code":"250 A","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('diabetes-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["diabetes---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["diabetes---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["diabetes---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
