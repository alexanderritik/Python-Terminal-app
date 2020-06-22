#TO STUDY THIS api
#https://railwayapi.com/api/#station-autocomplete-suggest
from pprint import pprint
import requests
import json
import time
import calendar
print("PRESS 1 FOR LIVE TRAIN STATUS")
print("PRESS 2 FOR PNR STATUS")
print("PRESS 3 FOR TRAIN ROUTE")
print("PRESS 4 FOR SEAT AVAILBILITY ")
print("PRESS 5 FOR Train Between Stations ")
print("PRESS 6 Train Name/Number ")
print("PRESS 7 Train Fare Enquiry ")
print("PRESS 8 Train Arrivals ")
print("PRESS 9 Cancelled Trains ")
print("PRESS 10 Rescheduled Trains ")
print("PRESS 11 Station Name to Code ")
print("PRESS 12 Station Code to Name ")
choice=int(input('Enter your choice : '))

if choice==1:
  yyyy=int(input('Enter the year : ' ))
  mm=int(input('Enter the month : ' ))
  calendar_year=calendar.month(yyyy,mm)
  print(calendar_year)
  dd=int(input('Enter the date of travel :'))

  stat=input('Enter the station code :  ')
  t=input('Enter the train number : ')
  apikey="guqzuxis9j"
  url=f"https://api.railwayapi.com/v2/live/train/{t}/station/{stat}/date/{dd}-{mm}-{yyyy}/apikey/guqzuxis9j/"

  info7=requests.get(url)
  info_7=info7.text
  info=json.loads(info_7)
  #for more additional information
  #pprint(info)
  if info['status']['has_arrived'] == True:
      a="yes"
  else:
      a="no"
  print("Its position is",info['position'])
  print("the starting date is",info['start_date'],"from station name",info['station']['name'])
  print("the status "
        "actual date is",info['status']['actarr_date'],
        "from actual departed time",info['status']['actdep'],
        "it has arrived",a ,
        "it is late for ",info['status']['latemin'],
        "it is arrived ",info['status']['scharr'],
        "at date",info['status']['scharr_date'])


elif choice==10:
    stat=input('PLEASE ENTER STTATION NAME TO KNOE STATION CODE AND STATION NAME : ')
    url=f"https://api.railwayapi.com/v2/suggest-station/name/{stat}/apikey/guqzuxis9j/"
    data= requests.get(url)
    inf = data.text
    info = json.loads(inf)
    pprint(info)


elif choice==2:
    pnrno=input('please enter your pnr no ')
    #1234567890
    url=f"https://api.railwayapi.com/v2/pnr-status/pnr/{pnrno}/apikey/guqzuxis9j/"
    data = requests.get(url)
    inf = data.text
    info = json.loads(inf)
    pprint(info)


elif choice==3:
    trainno=int(input('please enter train no for which you want to know train route '))
    url=f"https://api.railwayapi.com/v2/route/train/{trainno}/apikey/guqzuxis9j/"
    data = requests.get(url)
    inf = data.text
    info = json.loads(inf)
    pprint(info)


elif choice==4:
    yyyy = int(input('Enter the year in yyyy format : '))
    mm = int(input('Enter the month in mm format : '))
    calendar_year = calendar.month(yyyy, mm)
    print(calendar_year)
    dd = input('Enter the date of travel in dd format :')
    trainno =input('please enter train no for seat availability :')
    statcode= input('please enter the boarding station code  :')
    destcode=  input('please enter the destination station code  :')
    print("1A - FIRST AC \n"
          "EC - EXECUTIVE CLASS \n" 
          "EA - EXECUTIVE ANUBHUTI \n"
          "2A - SECOND AC \n"
          "3A - THIRD AC \n"
          "3E - AC Economy \n"
          "CC - AC CHAIR CAR \n"
          "FC - FIRST CLASS \n"
          "SL - SLEEPER CLASS \n"
          "2S - SECOND SEATING \n")
    classcode=  input('please enter the class code :  ')
    print("TQ - Tatkal Quota \n"
          "LD - Ladies Quota \n"
          "DF - Defence Quota \n "
          "FT - Foreign Tourist Quota \n"
          "SS - Lower Berth Quota \n"
          "PT - Premium Tatkal Quota  \n"
          "YU - Yuva Quota \n"
          "DP - Duty Pass Quota \n"
          "HP - Handicaped Quota \n "
          "PH - Parliament House \n "
          "GN - General Quota \n ")
    quotacode= input('please enter the quota code : ')
    yyyy=str(yyyy)
    mm=str(mm)
    url=f"https://api.railwayapi.com/v2/check-seat/train/{trainno}/source/{statcode}/dest/{destcode}/date/{dd}-{mm}-{yyyy}/pref/{classcode}/quota/{quotacode}/apikey/guqzuxis9j/"
    data = requests.get(url)
    inf = data.text
    info = json.loads(inf)
    #pprint(info)

    print("THe train is available ", info['availability'][0]['date'], "and the status is",
          info['availability'][0]['status'])
    print("form boarding station ", info['from_station']['name'], "to destination station", info['to_station']['name'],
          "form journey class", info['journey_class']['name'], "the quota is ", info['quota']['name'])
    for query in info['train']['classes']:
        print("it is available in ", query['name'], "is present", query['available'])

    print("form train ", info['train']['name'], "and its train number", info['train']['number'])


elif choice==5:
    yyyy = int(input('Enter the year in yyyy format : '))
    y = yyyy
    mm = int(input('Enter the month in mm format : '))
    m = mm
    calendar_year = calendar.month(yyyy, mm)
    print(calendar_year)
    dd = input('Enter the date of travel in dd format :')
    yyyy = str(yyyy)
    mm = str(mm)
    obj = calendar.Calendar()
    d = int(dd)

    statcode = input('Enter the boarding station code : ')
    destcode = input('Enter the destination code : ')

    url = f"https://api.railwayapi.com/v2/between/source/{statcode}/dest/{destcode}/date/{dd}-{mm}-{yyyy}/apikey/guqzuxis9j/"

    data = requests.get(url)
    inf = data.text
    info = json.loads(inf)
    # pprint(info)
    i = 0
    oi = 0
    day = []
    val = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    while i<info['total']  :
        for days in obj.itermonthdays2(y, m):
            day.append(days)
        # print(day)
        for p, j in day:
            if p == d:
                # print(j)
                val1 = val[j]
                # print(val1)
        while oi < 7:
            if val1 == info['trains'][i]['days'][oi]['code']:
                if info['trains'][i]['days'][oi]['runs'] == 'Y':
                    print("The train name is ", info['trains'][i]['name'], "and the train number is",
                          info['trains'][i]['number'], "the departure is", info['trains'][i]['src_departure_time'],
                          "the travel time is", info['trains'][i]['travel_time'],
                          "the destination arrival time is", info['trains'][i]['dest_arrival_time'])
            oi = oi + 1
        i = i + 1
        oi = 0

elif choice==7:
    yyyy = int(input('Enter the year in yyyy format : '))
    mm = int(input('Enter the month in mm format : '))
    calendar_year = calendar.month(yyyy, mm)
    print(calendar_year)
    dd = input('Enter the date of travel in dd format :')
    trainno = input('please enter train no for seat availability :')
    statcode = input('please enter the boarding station code  :')
    destcode = input('please enter the destination station code  :')
    print("1A - FIRST AC \n"
          "EC - EXECUTIVE CLASS \n"
          "EA - EXECUTIVE ANUBHUTI \n"
          "2A - SECOND AC \n"
          "3A - THIRD AC \n"
          "3E - AC Economy \n"
          "CC - AC CHAIR CAR \n"
          "FC - FIRST CLASS \n"
          "SL - SLEEPER CLASS \n"
          "2S - SECOND SEATING \n")
    classcode = input('please enter the class code :  ')
    print("TQ - Tatkal Quota \n"
          "LD - Ladies Quota \n"
          "DF - Defence Quota \n "
          "FT - Foreign Tourist Quota \n"
          "SS - Lower Berth Quota \n"
          "PT - Premium Tatkal Quota  \n"
          "YU - Yuva Quota \n"
          "DP - Duty Pass Quota \n"
          "HP - Handicaped Quota \n "
          "PH - Parliament House \n "
          "GN - General Quota \n ")
    quotacode = input('please enter the quota code : ')
    yyyy = str(yyyy)
    mm = str(mm)
    age=input('Enter your age plaese : ')
    url=f"https://api.railwayapi.com/v2/fare/train/{trainno}/source/{statcode}/dest/{destcode}/age/{age}/pref/{classcode}/quota/{quotacode}/date/{dd}-{mm}-{yyyy}/apikey/guqzuxis9j/"
    data = requests.get(url)
    inf = data.text
    info = json.loads(inf)
    pprint(info)


elif choice==6:
    url="https://api.railwayapi.com/v2/between/source/<stn code>/dest/<stn code>/date/<dd-mm-yyyy>/apikey/<apikey>/"
    #you can do the thing as previous


