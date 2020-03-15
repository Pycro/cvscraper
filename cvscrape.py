import requests
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime

#next two lines raspberry pi only and sensehat
from sense_hat import SenseHat
sense = SenseHat()

#create logfile
f = open("cvlog.txt", "a")
f.write("Date,Time,Cases,Deaths,Recovered\n")
f.close()

while True:
    #check if on the hour for update
    currentdate = datetime.now().strftime('%d-%m-%Y')
    currenttime = datetime.now().strftime('%H:%M')
    hrcheck = currenttime.split(":")
    hrcheck2 = hrcheck[1]
    #print(hrcheck2)
    print(currentdate)
    print(currenttime)
    results = "0,0,0,0"
    if(hrcheck2.startswith("00")):
        #grab fresh data
        URL = 'https://www.worldometers.info/coronavirus/country/uk/'
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        cases = soup.find_all('div', class_='maincounter-number')
        results = ""
        for span in cases:
            elem = span.find('span',)
            results += elem.text.replace(",","") + ","
        results2 = results.split(",")
        cases = results2[0].strip()
        deaths = results2[1].strip()
        recovered = results2[2].strip()

        
        f = open("cvlog.txt", "a")
        f.write(currentdate + "," + currenttime + "," + cases + "," + deaths + "," + recovered+"\n")
        f.close()
        print("Cases = " + cases)
        print("Deaths = " + deaths)
        print("Recovered = " + recovered)
        message = "Cases = " + cases + " Deaths = " + deaths + " Rec = " + recovered
        print(message)

        sense.show_message(message,text_colour=[255,0,0])
        sense.show_message('')


        sleep(60)
            
    
    


