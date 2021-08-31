import json

# This code extracts the sleep data from the list of files and writes out as a CSV file
# To get the data from Garmin's website go to: 
# https://www.garmin.com/en-GB/account/datamanagement/exportdata/
# They will send you an email containing a link to a zip file containing all the information

files = ['./DI_CONNECT/DI-Connect-Wellness/2018-02-01_2018-05-12_113293_sleepData.json',
         './DI_CONNECT/DI-Connect-Wellness/2018-05-12_2018-08-20_113293_sleepData.json',
         './DI_CONNECT/DI-Connect-Wellness/2018-08-20_2018-11-28_113293_sleepData.json',
         './DI_CONNECT/DI-Connect-Wellness/2018-11-28_2019-03-08_113293_sleepData.json',
         './DI_CONNECT/DI-Connect-Wellness/2019-03-08_2019-06-16_113293_sleepData.json',
         './DI_CONNECT/DI-Connect-Wellness/2019-06-16_2019-09-24_113293_sleepData.json',
         './DI_CONNECT/DI-Connect-Wellness/2019-09-24_2020-01-02_113293_sleepData.json',
         './DI_CONNECT/DI-Connect-Wellness/2020-01-02_2020-04-11_113293_sleepData.json',
         './DI_CONNECT/DI-Connect-Wellness/2020-04-11_2020-07-20_113293_sleepData.json',
         './DI_CONNECT/DI-Connect-Wellness/2020-07-20_2020-10-28_113293_sleepData.json',
         './DI_CONNECT/DI-Connect-Wellness/2020-10-28_2021-02-05_113293_sleepData.json',
         './DI_CONNECT/DI-Connect-Wellness/2021-02-05_2021-05-16_113293_sleepData.json']

csv = open('out.csv','wt')
csv.write("Date, Deep, Light, REM, Awake\n")

for i in files:
   with open(i) as json_file:
      data = json.load(json_file)
      for en in data:
         try:
            date = en['sleepStartTimestampGMT']
            deep = en['deepSleepSeconds']
            light = en['lightSleepSeconds']
            rem = en['remSleepSeconds']
            awake = en['awakeSleepSeconds']
         
            csv.write('{0}, {1}, {2}, {3}, {4}\n'.format(date,deep,light,rem,awake))
         except(KeyError):
            pass
        
