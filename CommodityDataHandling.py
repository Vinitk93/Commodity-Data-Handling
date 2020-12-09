#!/usr/bin/env python
# coding: utf-8

# In[4]:


'''
Program: finalProject-Vinit-01.py
Author: Vinit Keni
Purpose: Program for analysing commodity data and generate bar graph
Revision : First Release
'''
import csv
from datetime import datetime
from statistics import mean
import plotly.offline as py
import plotly.graph_objs as go

with open("produce_csv.csv","r") as csvFile:    #open the csv file for reading
    reader=csv.reader(csvFile)                  #instantiate csv file reader
    data=[row for row in reader]                #add each row in a data

#modified data to make it suitable for computation
data=[[float(item.replace("$","")) if "$" in item                   #remove $ sign if present and convert price
        else datetime.strptime(item,"%m/%d/%Y") if "/" in item      #convert date if '/' in item
        else item for item in row]                                  #else append item as it is
        for row in data]

locations=data.pop(0)[2:]       #remove header from data and make a list of locations

records=[]                      #initiate new list
for row in data:                #iterate through each row in data
    newRow=row[:2]              #list of only commodity and date
    for location,price in zip(locations,row[2:]):       #iterate through each location and price
        records.append(newRow+[location,price])         #append commodity, date, location and price

print(f'{"=" * 30}\n{"Analysis of Commodity Data":^30}\n{"="*30}\n')        #Program header

listProduct=sorted(list(set(row[0] for row in records)))    #list of all products
print("SELECT PRODUCTS BY NUMBER ...")
_ = [print(f'<{i}> {item}') for i,item in enumerate(listProduct)]       #print all products and its corresponding index number

yourProduct = input("Enter product numbers separated by spaces: ")      #ask user to select products by index numbers
selectProduct = yourProduct.split()     
nameProduct = [listProduct[int(item)] for item in selectProduct]        #name of products selected by user
print(f'Selected Products:  {"  ".join(nameProduct)}')                  #print user selected products

dates=sorted(list(set(row[1] for row in records)))              #list of all dates
listDate=[datetime.strftime(row,"%Y-%m-%d") for row in dates]   #Change dates from datetime to string and stored in a list

print("\nSELECT DATE RANGE BY NUMBER ...")
_ = [print(f'<{i}> {item}') for i,item in enumerate(listDate)]  #print all dates and its corresponding index number

print(f"Earliest available date is: {listDate[0]}")             #print earliest available date
print(f"Latest available date is: {listDate[-1]}")              #print latest available date    

yourDate = input("Enter start/end date numbers separated by a space: ")     #ask user to select start and end date
selectDate = yourDate.split()
date1=int(selectDate[0])            #index of start date
date2=int(selectDate[1])            #index of end date
print(f'Dates from {listDate[date1]} to {listDate[date2]}')     #print start and end date

locations.sort()            #sorted locations
print("\nSELECT LOCATIONS BY NUMBER")
_ = [print(f'<{i}> {item}') for i,item in enumerate(locations)]         #print all locations and its corresponding index number

yourLocation = input("Enter location numbers separated by spaces: ")    #ask user to select locations by index number
selectLocation = yourLocation.split()
nameLocation=[locations[int(item)] for item in selectLocation]          #name of locations selected by user
print(f'Selected Locations:  {"  ".join(nameLocation)}')                #print user selected locations

desiredRecords=list(filter(lambda x: x[0] in nameProduct and (dates[date1]<=x[1]<=dates[date2]) 
                            and x[2] in nameLocation,records))      #filter records according to users selection

#creating dictionary with product name as key
recordDict={}                   #empty dictionary
for row in desiredRecords:      #for each data record in desiredRecords
    if row[0] in recordDict:
        recordDict[row[0]].append(row[2:])      #if produck key exists, append location and price
    else:
        recordDict.update({row[0]:[row[2:]]})       #else, create product key and data list

#creating dictionary with location name as secondary key
finalRecords={}                 #start with empty list
for commodity in recordDict:    #for each product in recordDict
    finalRecords[commodity]={}      #create a dictionary that product refers to
    for row in recordDict[commodity]:       #for each list item
        if row[0] in finalRecords[commodity]:
            finalRecords[commodity][row[0]].append(row[1])          #if location key exists, append price data
        else:
            finalRecords[commodity].update({row[0]:[row[1]]})       #otherwise, create location key and add price data

#creating a dictionary with average price of product in different locations
avgRecords={}               #starts with empty dictionary
for row in finalRecords:    #for each product
    avgRecords[row]={}      #create a empty dictionary that product refers to
    for item in finalRecords[row]:      #for each locations
        avgRecords[row][item]=mean(finalRecords[row][item])   #compute average price and update dictionary 
        

#creating a list of traces
traces=[]           #initialize traces
for loc in nameLocation:    #for each user selected location 
    yValues=[]          #create an empty list of yValues
    for pro in avgRecords:      #for each product
        yValues.append(avgRecords[pro][loc])    #append average price of products in particular location
    trace=go.Bar(x=[item for item in avgRecords],y=yValues,name=loc)        #creating a Bar object of plotly.graph_objs module
    traces.append(trace)        #append trace
    
layout=go.Layout(barmode='group',title=f'Produce Prices from {listDate[date1]} through {listDate[date2]}',
                yaxis=dict(title='Average Price',tickformat='$.2f'),
                xaxis=dict(title='Product'))        #layout formatting

fig=go.Figure(data=traces, layout=layout)       #creating a Figure
py.plot(fig, filename='grouped-bar.html')


# In[ ]:




