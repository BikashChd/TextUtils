# I have created this file
from curses.ascii import HT
import re
from django.shortcuts import render 
from django.http import HttpResponse
def navigation(request):
    s='''<h2>Welcome to the navigation bar </h1>
    <a href="https://www.youtube.com/watch?v=lcpqpxVowU0&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=12">code with harry</a>
    <a href="https://youtube.com">Youtube</a>
    <a href="https://www.facebook.com/">FAcebook</a>
    <a href="https://www.daraz.com.np">Daraz</a>
    <a href="https://www.amazon.in">Amazon</a>'''
    return HttpResponse(s)


def home(request):
    return render(request,'index.html')

def analyze(request):
    djText=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    capitalize=request.POST.get('capitalize','off')
    newline=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    # print(removepunc)
    punctuation='''!()-[]{};:\,<>./?@#$%^&*_~'''
    analyzed=""
    if removepunc=='on':
        analyzed=""
        for char in djText:
            if char not in punctuation:
                analyzed=analyzed+char
        dictionary={
            'purpose':'Removed Punctuation',
            'analyzed_text':analyzed
        }
        djText=analyzed
    if capitalize=='on':
        analyzed=""
        for char in djText:
            analyzed=analyzed + char.upper()
        dictionary={
            'purpose':'in capital',
            'analyzed_text':analyzed
        }
        djText=analyzed
    
    if newline=='on':
        analyzed=""
        for char in djText:
            if char !="\n" and char!="\r":
                analyzed =analyzed+char
        
        dictionary={
            'purpose':'after removing new line',
            'analyzed_text':analyzed
        }
        
        djText=analyzed
    if extraspaceremover=='on':
        analyzed=""
        analyzed = re.sub(' +', ' ', djText)
        dictionary={
            'purpose':'after removing extra space',
            'analyzed_text':analyzed
        }
        
        djText=analyzed
    if (removepunc!="on" and capitalize!="on" and extraspaceremover!="on" and newline!="on"):
        return HttpResponse("Error!!!!!!!!!!!!!! , Please tick any operation")
    return render (request,'anaylyze.html',dictionary)
    

