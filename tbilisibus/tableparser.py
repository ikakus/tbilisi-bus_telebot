from bs4 import BeautifulSoup

from tbilisibus.busInfo import BusInfo


def parse_table(html_table):
    soup = BeautifulSoup(html_table, 'html.parser')
    table = soup.find(class_='arrivalTimesInnerTable')
    rows = table.find_all("tr")

    bus_list = []

    for row in rows:
        data = row.find_all("td")
        bus_list.append(BusInfo(data[0].string, data[1].string, data[2].string))

    return bus_list
