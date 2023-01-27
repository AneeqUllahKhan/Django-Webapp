from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {'name': 'Aneeq', }
    return render(request, 'index.html', params)


def analyze(request):

    # Get Text
    Dtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == "on":

     punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
     analyzed = ""
     for char in Dtext:
        if char not in punctuations:
            analyzed = analyzed + char

     params = {'purpose':  'Removed Punctuations', 'analyzed_text': analyzed}
     Dtext = analyzed

    if (fullcaps == "on"):
        analyzed = ""
        for char in Dtext:
            analyzed = analyzed + char.upper()

        params = {'purpose':  'Changed To Uppercase', 'analyzed_text': analyzed}
        Dtext = analyzed
    if (newlineremover == "on"):
        analyzed = ""
        for char in Dtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose':  'Remove New Lines', 'analyzed_text': analyzed}
        Dtext = analyzed
      
    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(Dtext):
            if not(Dtext[index] == " " and Dtext[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose':  'Remove Extra Spaces', 'analyzed_text': analyzed}
        Dtext = analyzed
     
    if (charcount == "on"):
        analyzed = len(Dtext)
        params = {'purpose':  'Character Counts', 'analyzed_text': analyzed}
             

    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on" and charcount!="on"):
        params = {'purpose':  'Error Please Try Again :(', }
        return render(request, 'error.html', params)
   
    return render(request, 'analyze.html', params)