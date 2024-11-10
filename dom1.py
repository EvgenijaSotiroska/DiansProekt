import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
from datetime import datetime
import time
import pandas as pd


def checkFile():
    try:
        df = pd.read_csv("diansDom1.csv")
        if df.empty:
            return (True)
        else:
            return ("The file has data.")
    except pd.errors.EmptyDataError:
        return (True)


def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)


def filter1():
    url_web = "https://www.mse.mk/mk/stats/symbolhistory/kmb"
    response = requests.get(url_web)
    response = response.text
    soup = BeautifulSoup(response, 'html.parser')

    all_issuers = soup.select('.form-control option')
    issuers = []
    for issuer in all_issuers:
        if not has_numbers(issuer.text.strip()):
            issuers.append(issuer.text.strip())
    return issuers


def scrape_info(row, izdavac):
    prometBEST = row.select_one('td:nth-child(8)').text.strip()
    vkupenPromet = row.select_one('td:nth-child(9)').text.strip()
    row_dict = {}
    if (vkupenPromet != "0" and prometBEST != "0"):
        d = row.select_one('td:nth-child(1)').text.strip()
        parts = d.split(".")
        da = parts[1] + "/" + parts[0] + "/" + parts[2]
        datum = datetime.strptime(da, '%m/%d/%Y').date()
        datum = datum.strftime("%m/%d/%Y")
        cenaPoslednaTran = row.select_one('td:nth-child(2)').text.strip()
        max = row.select_one('td:nth-child(3)').text.strip()
        min = row.select_one('td:nth-child(4)').text.strip()
        avg = row.select_one('td:nth-child(5)').text.strip()
        prom = row.select_one('td:nth-child(6)').text.strip()
        kol = row.select_one('td:nth-child(7)').text.strip()
        row_dict = {
            "Shifra": izdavac,
            "Datum": datum,
            "Cena na posledna transakcija": cenaPoslednaTran,
            "Mak.": max,
            "Min.": min,
            "Prosecna cena": avg,
            "%prom": prom,
            "Kolicina": kol,
            "Promet vo BEST vo denari": prometBEST,
            "Vkupen promet": vkupenPromet
        }
    return row_dict


def get_url(url_t, izdavac):
    response = requests.get(url_t)
    response = response.text
    soup = BeautifulSoup(response, 'html.parser')
    rows = soup.select('tbody tr')
    return rows


def fill_data(izdavaci):
    url_base = "https://www.mse.mk/mk/stats/symbolhistory/"
    today = date.today()
    today_values = str(today).split("-")
    data = []
    start = time.time()
    for izdavac in izdavaci:
        for i in range(2014, int(today_values[0])):
            year = i
            url_t = url_base + izdavac + "?fromDate=1.1." + str(year) + "&toDate=31.12." + str(year)
            rows = get_url(url_t, izdavac)
            for row in rows:
                row_dictt = scrape_info(row, izdavac)
                if len(row_dictt) != 0:
                    data.append(row_dictt)

        url_t = url_base + izdavac + "?fromDate=1.1." + today_values[0] + "&toDate=" + today_values[2] + "." + \
                today_values[1] + "." + today_values[0]
        rows = get_url(url_t, izdavac)
        for row in rows:
            row_dictt = scrape_info(row, izdavac)
            if len(row_dictt) != 0:
                data.append(row_dictt)
    end = time.time()
    length = end - start
    print("It took", length / 60, "minutes!")
    return data


def find_last_date(issuer, df):
    dateList = []
    temp = df[df['Shifra'] == str(issuer)]
    for l in temp['Datum']:
        dateList.append(l)
    dates = [datetime.strptime(ts, "%m/%d/%Y") for ts in dateList]
    dates.sort()
    sorteddates = [datetime.strftime(ts, "%m/%d/%Y") for ts in dates]
    if (len(sorteddates) == 0):
        return None
    else:
        return sorteddates[-1]


def filter3(issuer, starting_date):
    url_base = "https://www.mse.mk/mk/stats/symbolhistory/"
    today = date.today()
    today_values = str(today).split("-")
    starting_values = str(starting_date).split("/")
    data = []
    if int(today_values[0]) == int(starting_values[2]):
        url_t = url_base + issuer + "?fromDate=" + str(int(starting_values[1]) + 1) + "." + starting_values[0] + "." + \
                starting_values[2] + "&toDate=" + today_values[2] + "." + today_values[1] + "." + today_values[0]
        rows = get_url(url_t, issuer)
        for row in rows:
            row_dictt = scrape_info(row, issuer)
            if len(row_dictt) != 0:
                data.append(row_dictt)

    for i in range(int(starting_values[2]), int(today_values[0])):
        year = i
        url_t = url_base + issuer + "?fromDate=1.1." + str(year) + "&toDate=31.12." + str(year)
        rows = get_url(url_t, issuer)
        for row in rows:
            row_dictt = scrape_info(row, issuer)
            if len(row_dictt) != 0:
                data.append(row_dictt)
    return data


def filter2(issuers):
    if checkFile() is True:
        data = fill_data(issuers)
        df = pd.DataFrame(data)
        df.to_csv("diansDom1.csv", index=False)
    else:
        df = pd.read_csv("diansDom1.csv")
        issuersWithoutDate = []
        for issuer in issuers:
            last_date = find_last_date(issuer, df)
            if last_date is None:
                issuersWithoutDate.append(issuer)
            else:
                data = filter3(issuer, last_date)
                new_data = pd.DataFrame(data)
                new_data.to_csv("diansDom1.csv", mode='a', index=False, header=False)

        dataW = fill_data(issuersWithoutDate)
        new_data = pd.DataFrame(dataW)
        new_data.to_csv("diansDom1.csv", mode='a', index=False, header=False)


if __name__ == "__main__":
    issuers = filter1()
    filter2(issuers)
