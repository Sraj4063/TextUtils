
from django.http import HttpResponse
from django.shortcuts import render


def ex1(request):
    s = '''<h3>Navigation Bar<br></h3>
            <a href = "http://www.youtube.com">youtube.com</a><br>
            <a href = "http://www.google.com">google.com</a><br>
            <a href = "http://www.facebook.com">facebook.com</a><br>
            <a href = "http://www.hp.com">hp.com</a><br>
            <a href = "http://www.apple.com">apple.com</a><br>'''
    return HttpResponse(s)

def index(request):  # request is important else it will show error
    return render(request, 'index.html')



def about(request):  # request is important else it will show error
    return HttpResponse("Hello  about  again")


def analyze(request):  # request is important else it will show error
    # print(request.GET.get('text','default')) # this text will take the input from user and stor it here, if user wont give then default
    # for analyxe the text
    # or you can store it in a variable
    global analyzed
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps= request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    print(removepunc)
    print(djtext)
    #analyzed = djtext
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = " "
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'change to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
       # return render(request, 'analyze.html', params)

    if(newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != '\r':
                analyzed = analyzed + char
            params = {'purpose': 'new line remover', 'analyzed_text': analyzed}
           # return render(request, 'analyze.html', params)
        djtext = analyzed

    if(extraspaceremover == 'on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'extra space remover', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed

    if(charcount == "on"):
        analyzed = " "
        lenn = 0
        for char in djtext:
            if char != " ":
                lenn += 1
        analyzed = lenn
        params = {'purpose': 'extra space remover', 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)
        
    if (charcount != "on" and extraspaceremover != "on" and newlineremover != "on" and fullcaps != "on" and removepunc != "on" ):
        return HttpResponse("you haven't turn on any switch and clicked on analyzed directly ")

    return render(request, 'analyze.html', params)

