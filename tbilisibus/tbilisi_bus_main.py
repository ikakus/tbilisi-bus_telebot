import requests

from tbilisibus.tableparser import parse_table

URL = "http://transiten.ttc.com.ge/pts-portal-services/servlet/stopArrivalTimesServlet?stopId={}"


def get_table_for_id(id):
    url = URL.format(id)
    response = requests.get(url)
    result = parse_table(response.content)
    return result


res = get_table_for_id(11)
print(res)
