from faker import Faker
from collections import OrderedDict
import dumper
import random
import csv
from datetime import date

def calculate_age(dtob):
    today = date.today()
    return today.year - dtob.year - ((today.month, today.day) < (dtob.month, dtob.day))

def getList(dict): 
    return dict.keys()

def writeToCSV():
    csv_columns = getList(profiles[1])
    csv_file = "profiles.csv"
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in profiles:
                writer.writerow(profiles[data])
    except IOError:
        print("I/O error")

def addRelationshipstatus():
    faker=Faker()
    words = [' ', 'Single', 'In a Relationship', 'Engaged', 'Married', 'It is Complicated']
    return faker.words(1, words, True)

def addBasicDetails():
    faker = Faker()
    profile=OrderedDict()
    profile1=faker.simple_profile()
    profile['UserID']=faker.random_int(100000,999999)
    profile['Job']=faker.job()
    profile['Birthdate']=profile1['birthdate']
    profile['Sex']=profile1['sex']
    profile['Age']=calculate_age(profile['Birthdate'])
    return profile

def updateAccountDetails(profile1):
    faker = Faker()
    profile1['Relationship']= ''.join(map(str, addRelationshipstatus()))
    if profile1['Age'] <= 20:
        profile1['Tenure']=faker.random_int(1,5)
    else: 
        profile1['Tenure']=faker.random_int(1,10)
       
    if profile1['Tenure'] >=5 :
        profile1['Followers']=faker.random_int(1,2000)
        profile1['Following']=faker.random_int(200,2000)
        profile1['Average likes']=faker.random_int(0,1000)
    elif profile1['Tenure'] >=3 : 
        profile1['Followers']=faker.random_int(1,1500)
        profile1['Following']=faker.random_int(200,2000)
        profile1['Average likes']=faker.random_int(0,750)
    else:
        profile1['Followers']=faker.random_int(0,1000)
        profile1['Following']=faker.random_int(0,2000)
        profile1['Average likes']=faker.random_int(0,500)
    profile1['Media Posted']=faker.random_int(0,1000)
    profile1['Pinned Posts']=faker.random_int(0,5)
    

def populateDataset():
    for i in range(1,500):
        faker = Faker()
        profile =faker.simple_profile()
        profile1={}
        profile1=OrderedDict()
        profile1=addBasicDetails() 
        if profile1['Age'] <= 15  or profile1['Age'] >= 90:
            continue
        else:
            updateAccountDetails(profile1)
        profiles[i]=profile1
        #print(profiles[i])
        
profiles={}
populateDataset()
writeToCSV()
        
