#øvelse datetime
from datetime import datetime

date_string4 = datetime.strftime(datetime.now(), "%x")
date_string5 = datetime.strftime(datetime.now(), "%X")
date_string6 = datetime.strftime(datetime.now(), "%U")

print(
    f"The date is {date_string4}, and it's {date_string5} o'clock. It's the {date_string6} week of the year.")