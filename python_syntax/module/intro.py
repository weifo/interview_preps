# import my_module as mm
from my_module import find_index,square
import sys
import datetime
import calendar
import os

subjects=['History','Math','Physics','English']

index=find_index(subjects,'Math')
# the path list that python will look into
# print(sys.path)

# print(datetime.date.today())
# print(square)
# print(calendar.isleap(2024))

# print(os.getcwd())
print(os.__file__)