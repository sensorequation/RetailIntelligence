__author__ = 'vivek'

from django.http import HttpResponse
from django.shortcuts import render
import datetime
import json

from django.shortcuts import render_to_response

from PIL import Image, ImageFont, ImageDraw

from . import forms
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


from django.shortcuts import render, redirect

import models


'''
def login(request):
    #Test Base HTML Page
    return render(request,'login_simple.html')
'''

def base(request):
    #Test Base HTML Page
    return render(request,'base.html')


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def main_page(request):
    output = "<html><body>It is now</body></html>"
    return HttpResponse(output)

def hello(request):
    return HttpResponse("Hello world")

def index(request):
    return render(request,'index.html')
def blank(request):
    return render(request, 'blank.html')

def social(request):
    return render(request, 'social.html')

def twitter(request):
    return render(request, 'twitter.html')

def searchTweets(request):
    result = searchTwitter()
    #result = '{"responseData": {"data":[]}}';
    #return JsonResponse(json.dumps(result),safe = False )
    return HttpResponse(result , content_type='application/json')


def twittercc(request):

    #return render(request, 'twitter-cc.html', {'data': "http://localhost/cc/twitter_oauth/search.php?q=%23dentist"})
    #return render(request, 'twitter-cc.html')
    return render(request, 'twitterextendsbase.html')


def loginforms(request):
        form = forms.LoginForm()
        return render(request, 'twitterextendsbase.html')

def login(request):
    #Test Base HTML Page
    form = forms.LoginForm()
    # Validate Login Here

    #If Login is successful Go to Post


    if request.method == "POST":
        print "A POST Request"
        form = forms.LoginForm(request.POST)

        #Once Login, go to main page with the summary for the businness
        #return render(request, basesearch)
        #return render(request, 'basesearch.html')
        #return render(request,'basesearch.html')
        #return render_to_response('basesearch.html')
        #return redirect(basesearch)
        return redirect(adminLandingPage)

    return render(request,'login_simple.html',{'form':form})


def logout(request):
    return render(request,'login_simple.html')


def facebookbusinessoverview(request):
    return render(request,'facebookbusinessoverview.html')


def facebookbusinesscompetition(request):
    return render(request,'facebookbusinesscompetiton.html')

def basesearch(request):
    #Test Base HTML Page
    # Test Base HTML Page
    form = forms.SearchForm()
    if request.method == "POST":
        print "A POST Request From Search"
        form = forms.SearchForm(request.POST)

        #Once Login, go to main page with the summary for the businness

        #Validate the search page for a website only.

        #If a WebSite URL then Server the Search Results
        return render(request, 'businessoverview.html')

        #Else Throw an Error saying you need the business name in the form of a URL

    return render(request, 'basesearch.html')


def businessLandingPage(request):
    businessWebsite = "chutneysmi"

    ##### Make a Call to Mongo to see if the Data is present. If Not then Need to handle that

    # Get Facebook Followers / Likes


    # Get the Reviews



    # Get the Twitter Followers




    # Get Yelp Review



    dataForOrganicGraph = vs.getWebTrafficfromDatabase(businessWebsite,"Semrush")


    return render(request, 'businesslandingpage.html', { 'data': json.dumps(dataForOrganicGraph)})



def getLocalCompetitorsForBusiness(request):
    print "Getting the Competitors for Local Business"

    return render(request, 'businesscompetitorpage.html')

def adminLandingPage(request):

    HeaderList = []
    BusinessList = ['YO','yi','uu','8']
    # Header - Business Name, WebsiteName,Address,Status,Actions

    result = {'name': 'John', 'address': 'yo','time':'tt','date':'yyyy'}

    return render(request, 'adminlandingpage.html',{'result':result})
    #return render_to_response('adminlandingpage.html', {'result':result})
    #return render_to_response("adminlandingpage.html", context)

def businessEditPage(request):

    return render(request, 'businessInfoEditPage.html')

def businessProfilePage(request):

    return render(request, 'businesslandingpage.html')

def businessAddPage(request):


    form = forms.UserProfileAddForm()
    print form
    if request.method == "POST":
        print "A POST Request for Saving the Profile Data"
        #form = Forms.SearchForm(request.POST)
        #print form

        #<QueryDict: {u'Username': [u'yo'], u'Address line 1': [u'rrrrrrr'], u'Address line 2': [u'rrrr'], u'City': [u'fdffgggg'], u'Phone Number': [u'1234567890'], u'State': [u'444444'], u'Zipcode': [u'54567'], u'Business Name': [u'rrr'], u'csrfmiddlewaretoken': [u'KzOH9OZvjObjD5aLSn7WngkqoHVxe3kc'], u'email': [u'11@yahooo.com']}>
        #inputtxt = request.POST['Username']



        #print inputtxt
        print request.POST.keys()


        # Insert into the Database

        # For now do the validation logic here. Later on do the validation logic in the Forms

        keyCheck = dbOperations.checkKeyPresenceInDatabase("chutneysmi", "overview")
        if( keyCheck == "Key Not Present"):

            print "Will add to the dictionary"


            dataBuilder = {}

            receivedWeb = request.POST['Website']

            receivedWebSuffix = receivedWeb.split('.')
            receivedWeb = request.POST['Business Name']
            receivedSuffix = receivedWebSuffix[1]
            receivedAddressLine1 = request.POST['Address line 1']
            receivedAddressLine2 = request.POST['Address line 2']
            receivedBusinessName = request.POST['Business Name']
            receivedCity= request.POST['City']
            receivedCountry = request.POST.get('Country', False)
            receivedCountry = request.POST.getlist('Country')
            receivedPhoneNumbers= request.POST['Phone Number']
            receivedState = request.POST['State']
            #receivedUsername = request.POST['Username']
            receivedZip = request.POST['Zipcode']
            receivedEmail = request.POST['email']
            databuilder = {'AddedBy' : "Portal", 'Website' : receivedWeb, 'Address 1' : receivedAddressLine1,'Address 2' : receivedAddressLine2,'Business Name' : receivedBusinessName, 'City' : receivedCity,  'zip' : receivedZip, 'State' : receivedState,'country' : receivedCountry, 'suffix' : receivedSuffix}

            dbOperations.insertIntoBusiness( databuilder, receivedWeb, 'Overview')

            #record_id = self.db.businessinfo.insert({"businessdata": { website : businessData}}, check_keys=False)
            print dataBuilder


            # Insert into Database, if the key not present
        else:

            print "Key there hence no need"
            #dbOperations.insertIntoBusiness( businessData, website, dictkey)
        #Make a Call to the Mongo


        businessData = {}






        ######################################################################################
        return render(request, 'businesslandingpage.html')

        #Else Throw an Error saying you need the business name in the form of a URL

    return render(request, 'businessAddPage.html')

@csrf_exempt
def getbusinessTrafficPage(request):
    print None
@csrf_exempt
def displayDevices(request):
    img = Image.new('RGB', (60, 30), color='red')
    d = ImageDraw.Draw(img)
    d.text((10, 10), "Hello World", fill=(200, 128, 0))

    #img.save('temp2.png')
    #text = pytesseract.image_to_string(Image.open('temp2.jpg'))
    #print(text)
    #image_data = open("", "rb").read()
    #return HttpResponse('temp2.png', content_type="image/png")
    #return render(request, "RetailIntelligence\\temp2.png")
    #img = qrcode.make("some string")
    "https: // raw.githubusercontent.com / ZinggJM / GxEPD2 / master / extras / bitmaps / third200x200.bmp"
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return response

@csrf_exempt
def getNfcData(request):
    print "Got NFC Request"

    print request.GET['msisdn']
    print request.GET['nfcid']

    # p = Warehouse(insertdate=datetime.datetime.now(), generateddate=datetime.datetime.now(), latitude=degreesLat,
    #               longitude=degreesLong, imienumber=Device.objects.get(imienumber=352887078364431))
    # p.save()

    p =

    return HttpResponse("Hello world")
