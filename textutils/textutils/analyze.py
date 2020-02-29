# created by -Ritesh
from django.http import HttpResponse
from django.shortcuts import render
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt

def sentiment(request):
    inputdata = request.GET.get('inputreview','Default')
    print(inputdata)
    sid = SentimentIntensityAnalyzer()
    output = sid.polarity_scores(inputdata)
    print(output)
    data = pd.DataFrame(data=output,columns=['neg', 'neu', 'pos', 'compound'],index=[0])

    def pieplot(inputdata):
        explode = (0.1, 0, 0, 0)
        objects = ('Negative', 'Normal', 'Positive', 'Combination')
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
        plt.pie(inputdata, explode=explode, labels=objects, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')
        plt.savefig('pie.jpg', dpi=200)

    def histplot(inputdata):               # Define function to create histogram plot for data visulization
        inputdata.plot.hist()
        plt.xlabel('Predict Emotions Value')
        plt.ylabel('Total FREQUENCY')
        plt.savefig('hist.png')

    def barplot(inputdata):                 # Define function to create bar plot for data visulization
        inputdata = inputdata.values.tolist()
        objects = ('Negative', 'Normal', 'Positive', 'Combination')
        inputdata = inputdata.pop(0)
        plt.figure(figsize=(8, 8))
        x = plt.bar(inputdata, objects, align='edge', width=0.2, alpha=0.7, color=['red', 'yellow', 'green', 'blue', ])
        x = plt.xticks(inputdata, objects)
        plt.xticks(rotation='45')
        y = plt.ylabel('')
        x = plt.title('')
        plt.savefig('bar.png', dpi=200, bbox_inches='tight')


    pieplot(data)  # call pie graph function
    histplot(data)      # call histogram function
    barplot(data)       # call barplot function
    neg = output['neg'] * 100
    neu = output['neu'] * 100
    pos = output['pos'] * 100
    mix = output['compound'] * 100
    url = 'img1.jpg'
    params = {'pos': pos,'neg' : neg,'neu': neu, 'mix': mix, 'url': url}
    return render(request, 'analysis.html', params)