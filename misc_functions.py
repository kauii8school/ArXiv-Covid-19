from dateutil.relativedelta import relativedelta

def yearsago(years, from_date=None):
    return from_date - relativedelta(years=years)