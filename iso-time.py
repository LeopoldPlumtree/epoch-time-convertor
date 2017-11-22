from datetime import datetime

date_in_iso = "2017-10-23T17:10:00.000+0100"
date_in_iso = date_in_iso[:-12]
new = datetime.strptime(date_in_iso, '%Y-%m-%dT%H:%M')
print(new)