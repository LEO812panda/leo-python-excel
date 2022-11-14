

import csv
from pathlib import Path
import os

import random
import time
from datetime import datetime
import pytz
from datetime import datetime
tz = pytz.timezone('America/New_York')
tzzz = pytz.timezone('Asia/Dubai')
timeH = datetime.now(tz).strftime('%H:%M:%S')
dateH = datetime.now(tz).strftime('%Y-%m-%d')
TimeHour = datetime.now(tz).strftime('%H')
date100 = datetime.today().strftime('%Y-%m-%d')




total_1 = 100
total_2 = 100
total_3 = 3000





while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        date100 = datetime.today().strftime('%Y-%m-%d')
        time100 = f"{current_time}"


        if total_1 > total_2 : 
            total_100 = "LONG"
        else:
            total_100 = "SHORT"  

        print(date100,time100,total_3, total_1, total_2,total_100)
        date100 = datetime.today().strftime('%Y-%m-%d')
        time100 = f"{current_time}"
        total_1 = total_1 + random.randint(-6, 8)
        total_2 = total_2 + random.randint(-6, 8)
        total_3 = total_3 + random.randint(-20, 20)



        def append_to_csv600(path600, fieldnames600, rows600):
            is_write_header600 = not os.path.exists(path600) or _is_empty_file600(path600)
            if not is_write_header600:
                _assert_field_names_match600(path600, fieldnames600)
            _append_to_csv600(path600, fieldnames600, rows600, is_write_header600)


        def _is_empty_file600(path600):
            return os.stat(path600).st_size == 0


        def _assert_field_names_match600(path600, fieldnames600):
            with open(path600, 'r') as f:
                reader600 = csv.reader(f)
                header600 = next(reader600)
                if header600 != fieldnames600:
                    raise ValueError(f'Incompatible header: expected {fieldnames600}, '
                                     f'but existing file has {header600}')


        def _append_to_csv600(path600, fieldnames600, rows600, is_write_header600: bool):
            with open(path600, 'a') as f:
                writer600 = csv.DictWriter(f, fieldnames=fieldnames600)
                if is_write_header600:
                    writer600.writeheader()
                writer600.writerows(rows600)


        file_600 = f"SP500.SIGNAL.TRADE.{date100}.SIM.csv"
        fieldnames_600 = ['DATE', 'TIME', 'PRICE', 'POSITIVE STOCK', 'NEGATIVE STOCK','TRADE SIDE']
        rows_600 = [{'DATE': f"{date100}",'TIME': f"{current_time}",'PRICE': f"{total_3}",'POSITIVE STOCK': f"{total_1}",'NEGATIVE STOCK': f"{total_2}",'TRADE SIDE': f"{total_100}"},]


        append_to_csv600(file_600, fieldnames_600, rows_600)






        time.sleep(1)
