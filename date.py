from datetime import datetime
from collections import namedtuple

Range = namedtuple('Range', ['start', 'end'])
r1 = Range(start = datetime(2012, 1, 15), end = datetime(2012, 5, 10))
r2 = Range(start = datetime(2021, 3, 20), end = datetime(2021, 9, 15))
latest_start = max(r1.start, r2.start)
earliest_end = min(r1.end, r2.end)
delta = (earliest_end - latest_start).days + 1
overlap = max(0, delta)
if overlap == 0:
    print("Approved")