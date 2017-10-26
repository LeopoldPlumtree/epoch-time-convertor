from datetime import datetime

sdate = "2017-09-01"
stime = "19"
edate = "2017-10-01"
etime = "19"

def convert_to_epoch(thedate, thetime):
    raw = thedate + '-' + thetime
    start = datetime.strptime(raw, '%Y-%m-%d-%H')
    epoch_time = (start - datetime(1970, 1, 1)).total_seconds()
    epoch_time = str(epoch_time)
    epoch_time = epoch_time[:-2]
    epoch_time = epoch_time + '000'
    epoch_time = int(epoch_time)
    return epoch_time

print("Start Date Is {sdate}  Start Time Is: {stime}".format(sdate=sdate, stime=stime))
print("Epoch Start is: {sepoch}".format(sepoch=convert_to_epoch(sdate, stime)))
print("End Date Is: {edate} End Time Is: {etime}".format(edate=edate,etime=etime))
print("Epoch End is: {eepoch}".format(eepoch=convert_to_epoch(edate, etime)))