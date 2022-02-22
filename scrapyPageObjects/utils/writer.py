import os
import csv

class WriteData:

    def writedata(self,data):
        Filename = 'C:\\scrapyPageObjects\\scrapyPageObjects\\spiders\\pages\\' + data.get('Site') + '\\dump.csv'
        filepath = Filename
        if((not os.path.exists(filepath)) or os.path.getsize(filepath)==0):
            header = data.keys()
            with open(filepath, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(header)
        else:
            try:
                with open(filepath, 'a', newline='', encoding='UTF-8') as csv_file:
                    writer = csv.DictWriter(csv_file, fieldnames=data.keys())
                    writer.writerow(data)
            except Exception as e:
                print('FAILED TO INSERT DATA INTO FILE .... : ',e)