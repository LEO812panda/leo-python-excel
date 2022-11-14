import csv
from pathlib import Path
import os
import schedule
from datetime import datetime
import time
from time import sleep


import os
import pytz
from datetime import datetime
tz = pytz.timezone('America/New_York')
tzzz = pytz.timezone('Asia/Dubai')
timeH = datetime.now(tz).strftime('%H:%M:%S')
dateH = datetime.now(tz).strftime('%Y-%m-%d')
TimeHour = datetime.now(tz).strftime('%H')
date100 = datetime.today().strftime('%Y-%m-%d')





import logging
import sys
###________________________________________________________________________###
import colorlog
import colorama
from colorama import Fore
from datetime import datetime

from datetime import date

today = date.today()


# Data = f"SP500.SIGNAL.TRADE.2022-11-08.csv"
Data = r'\\192.168.1.2\\US_INDEX_BOT\\SP500\\SP500.SIGNAL.TRADE.2022-11-14.csv'
# op = open(Data)
# dt = csv.DictReader(op)

filename1 = 'LOG' + Data.split('.')[-2] + '.csv'
filename = 'LOG.' + str(today) + '.csv'


logger = logging.getLogger('')
logger.setLevel(logging.INFO)
# fh = logging.FileHandler(f"LOG.{date100}.csv")
fh = logging.FileHandler(filename1)
sh = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(message)s', datefmt='%d-%m-%Y %H:%M:%S')
fh.setFormatter(formatter)
sh.setFormatter(colorlog.ColoredFormatter('%(log_color)s %(message)s', datefmt='%d-%m-%Y %H:%M:%S'))
logger.addHandler(fh)
logger.addHandler(sh)
def hello_logger():
    logger.info("LOG")


len1 = 0
if os.path.exists(filename1):
    op_pre1 = open(filename1)
    dt_pre1 = csv.DictReader(op_pre1, delimiter=" ")
    dt_pre1 = list(dt_pre1)
    len1 = len(dt_pre1)
    op_pre1.close()

if __name__ == "__main__":
    if len1 == 0:
        hello_logger()
        
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)    



def test():
    global filename1
    if os.path.exists(filename1):
        op_pre = open(filename1)
        dt_pre = csv.DictReader(op_pre, delimiter=" ")
        dt_pre = list(dt_pre)
        len_pre_data = len(dt_pre)
        op_pre.close()
    if len_pre_data!=0:
        sequence_number = int(str(dt_pre[len_pre_data - 1]).split('/')[-1].split('\'')[0])
        isLast_short = 'Short' in str(dt_pre[len_pre_data - 1])

        if isLast_short:
            stock_flag = False
        else:
            stock_flag = True
    else:
        sequence_number = 1
        stock_flag = False
            
    up_dt = []
    op = open(Data)
    dt = csv.DictReader(op)
    for num, r in enumerate(dt):
        if len_pre_data < num + 1:
            row = {'DATE','TIME','PRICE','POSITIVE STOCK','NEGATIVE STOCK','ACTIVE STOCK'}
            up_dt.append(row)
            Date = r['DATE']    
            Time = r['TIME']
            Price = r['PRICE']
            Price = float(Price)
            Positive = int(r['POSITIVE STOCK'])
            Negative = int(r['NEGATIVE STOCK'])
            
            if stock_flag is True:                
                if Positive > Negative :
                        stock_flag = True
                        print('LONG')
                        print(1)
                        print(Positive, Negative)
                        log.info(f"{Date},{Time},{Price},{Positive},{Negative},LONG/{sequence_number}")

                if Negative > Positive :
                        sequence_number += 1
                        stock_flag = False
                        print('SHORT')
                        print(2)
                        print(Positive, Negative)
                        log.info(f"{Date},{Time},{Price},{Positive},{Negative},Short/{sequence_number}")
            else:
                if Positive > Negative :
                        if num == 0:
                            sequence_number = 0
                        sequence_number += 1
                        stock_flag = True
                        print('LONG')
                        print(3)
                        print(Positive, Negative)
                        log.info(f"{Date},{Time},{Price},{Positive},{Negative},LONG/{sequence_number}")

                if Negative > Positive :                    
                        print('SHORT')
                        print(4)
                        print(Positive, Negative)
                        stock_flag = False
                        log.info(f"{Date},{Time},{Price},{Positive},{Negative},Short/{sequence_number}")
    op.close()



schedule.every(1).seconds.do(test)


while True:
    schedule.run_pending()
    sleep(0.1)

