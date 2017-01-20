from datetime import date
import re
import requests
import rumps
from bs4 import BeautifulSoup

rumps.debug_mode(True)


class AirtelBundleStatusApp(rumps.App):

    def __init__(self):
        super(AirtelBundleStatusApp, self).__init__(
            'Airtel Bundle Checker', icon='./resources/airtel_logo.png')
        self.menu = ['Remaining Balance']

    @rumps.clicked('Remaining Balance')
    def balance(self, _):
        r = requests.get('http://bundles.airtellive.com/airtelaoc/balance.php')
        # except requests.exceptions.RequestException as e: ...
        soup = BeautifulSoup(r.content, 'html.parser')
        text = soup.find('h5', text=re.compile('You have'))
        rumps.notification(
            'Remaining balance @ {:%d-%m-%Y}'.format(date.today()),
            '',
            '{}'.format(text.text)
        )


if __name__ == '__main__':
    AirtelBundleStatusApp().run()
