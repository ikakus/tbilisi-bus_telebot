from bs4 import BeautifulSoup

from tbilisibus.tableparser import parse_table

html_doc = """
<table cellspacing='0' cellpadding='0' class='arrivalTimesTable'>
    <tr>
        <td class='arrivalTableRouteNumberHeader' title='Route Number'>Route</td>
        <td class='arrivalTableStopNameHeader' title='Route Diretion'>Direction</td>
        <td class='arrivalTableArrivalTimeHeader' title='Bus arrival time'>min.</td>
    </tr>
    <tr>
        <td colspan='3'>
            <div class='arrivalTimesScrol'>
                <table cellspacing='0' cellpadding='0' class='arrivalTimesInnerTable'>
                    <tr>
                        <td class='arrivalTableRouteNumber'>24</td>
                        <td class='arrivalTableStopName' title='Gldani VII - VIII M/D'>Gldani VII - VIII M/D</td>
                        <td class='arrivalTableArrivalTime'>0</td>
                    </tr>
                    <tr>
                        <td class='arrivalTableRouteNumber'>88</td>
                        <td class='arrivalTableStopName' title='Baratashvili Str.'>Baratashvili Str.</td>
                        <td class='arrivalTableArrivalTime'>1</td>
                    </tr>
                    <tr>
                        <td class='arrivalTableRouteNumber'>21</td>
                        <td class='arrivalTableStopName' title='Didi Dighomi IV M/D'>Didi Dighomi IV M/D</td>
                        <td class='arrivalTableArrivalTime'>7</td>
                    </tr>
                    <tr>
                        <td class='arrivalTableRouteNumber'>13</td>
                        <td class='arrivalTableStopName' title='State University  H.B'>State University  H.B</td>
                        <td class='arrivalTableArrivalTime'>10</td>
                    </tr>
                    <tr>
                        <td class='arrivalTableRouteNumber'>150</td>
                        <td class='arrivalTableStopName' title='Baratashvili Str.'>Baratashvili Str.</td>
                        <td class='arrivalTableArrivalTime'>11</td>
                    </tr>
                    <tr>
                        <td class='arrivalTableRouteNumber'>49</td>
                        <td class='arrivalTableStopName' title='Station Square'>Station Square</td>
                        <td class='arrivalTableArrivalTime'>11</td>
                    </tr>
                    <tr>
                        <td class='arrivalTableRouteNumber'>140</td>
                        <td class='arrivalTableStopName' title='Baratashvili Str.'>Baratashvili Str.</td>
                        <td class='arrivalTableArrivalTime'>12</td>
                    </tr>
                    <tr>
                        <td class='arrivalTableRouteNumber'>92</td>
                        <td class='arrivalTableStopName' title='Station Square'>Station Square</td>
                        <td class='arrivalTableArrivalTime'>18</td>
                    </tr>
                    <tr>
                        <td class='arrivalTableRouteNumber'>47</td>
                        <td class='arrivalTableStopName' title='Station square 2'>Station square 2</td>
                        <td class='arrivalTableArrivalTime'>27</td>
                    </tr>
                    <tr>
                        <td class='arrivalTableRouteNumber'>5</td>
                        <td class='arrivalTableStopName' title='Tskneti'>Tskneti</td>
                        <td class='arrivalTableArrivalTime'>42</td>
                    </tr>
                </table>
            </div>
        </td>
    </tr>
</table>
"""
result = parse_table(html_doc)
print(result)
