import pandas as pd
from datetime import date
import holidays


for holiday in holidays.India(years=[2020]).items():
    print(holiday)