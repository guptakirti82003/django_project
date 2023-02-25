from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("<h1>hello world</h1>")
def about(request):
    return HttpResponse("My name is kirti Goel")
def nice(request):
    return HttpResponse('''
    <button><a href="home">Home</a></button>
    <button><a href="trial">Trial</a></button>''')
def trial(request):
    return HttpResponse('''
                <button><a href="home">Back</a></button>
                <button><a href="nice">Nice</a></button>
                ''')
def templates(request):
    return render(request,'index.html')
def analyzer(request):
    capture=request.GET.get('text')
    case=request.GET.get('case')
    pun=request.GET.get('pun')
    count=request.GET.get('count')
    length=request.GET.get('length')
    scount=request.GET.get('scount')
    text=""
    r1=""
    r2=""
    r3=""
    r4=""

    if case=='on':
        text=capture.upper()
    if pun=='on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for x in capture:
            if x not in punctuations:
                r1= r1 + x
    if count=='on':
        r2 = capture.count(" ")
        r2 = r2+1
    if length=='on':
        r3=len(capture)
    if scount=='on':
        r4=capture.count(" ")
    params={"name":text,"pn":r1,"cn":r2,"ln":r3,"sc":r4}
    return render(request,'analyzer.html',params)