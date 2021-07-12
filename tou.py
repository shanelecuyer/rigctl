from bs4 import BeautifulSoup
import requests
import re

url = 'https://www.oeb.ca/rates-and-your-bill/electricity-rates'
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')

def getRates():
    results = []
    test = soup.find('ul', class_ = 'homepage-rates-periods')
    results.append(test.find('li', class_=lambda x: x and x.endswith('active')).text.strip())
    for result in test.find_all('li', class_=lambda x: x and not x.endswith('active')):
        results.append(result.text.strip())

    for i, result in enumerate(results):
        result = re.split(' |-',result)
        result = formatRate(result)
        if i == 0:
            result.append(True)
        else:
            result.append(False)
        if result[0] == 'Mid-peak':
            results[i] = result
        elif result[0] == 'Off-peak':
            results[i] = result
        elif result[0] == 'On-peak':
            results[i] = result

    return results

def formatRate(rate):
    rate[0] = rate[0] + '-' + rate[1][0:4]
    rate[1] = rate[1][4:]
    rate = rate[:2]
    return rate

def nextRate():
    test = []
    test.append(soup.find('div', class_ = 'homepage-rates-next').text.strip().split()[1])
    test.append(soup.find('div', class_ = 'homepage-rates-next').text.strip().split()[4])
    return test

def getTime():
    time = soup.find('p', class_ = 'homepage-rates-top-time')
    test = time.text.strip().split()[3:6] 
    return test

if __name__ == '__main__':
    print('Hydro One Time-of-Use electricity rates:')
    print('')
    print('Time:',getTime()[0] + getTime()[1])
    print('Timezone:',getTime()[2])
    print('Active Rate',getRates()[0][0])
    for rate in getRates():
        print(rate[0],rate[1],'cents per kWh')
    print('Next Rate:',nextRate()[0],'in',nextRate()[1],'hh:mm')

