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