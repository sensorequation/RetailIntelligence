__author__ = 'vivek'

# -*- coding: utf-8 -*-
import urllib
import urllib2
import json

businessData = {}


list = ['www.yelp.com/biz/namaste-flavours-farmington',
          'https://local.yahoo.com/info-48243611-namaste-flavors-farmington',
          'https://locu.com/places/namaste-flavours-farmington-us',
          'https://www.mapquest.com/.../namaste-flavours-303519419',
          'https://www.groupon.com/biz/farmington-mi/namaste-flavours',
          'www.yellowpages.com/farmington-mi/mip/namaste-flavors-451321008',
          'https://www.tripadvisor.com',
          'https://www.zomato.com/detroit/namaste-flavours-indian-kitchen.',
          'https://start.cortera.com/company/research/k9r5kvn8l/',
          'www.yelp.com/biz_photos/namaste-flavours-farmington-4',
          'www.menupix.com/.../Namaste-Flavours-Indian-kitchen-Farmington-MI',
          'friendseat.com/coupons/Farmington/Namaste-Flavors',
          'www.facebook.com',
          'https://www.linkedin.com',
          'https://foursquare.com/',
          'https://foursquare.com/user/',
          'https://local.yahoo.com/MI/Farmington+Hills/',
          'tripwhat.com/USA/Farmington-restaurants',
          'https://www.yelp.ca'
          ]


def main():
    query = "www.namasteflavours.com"
    bing_search(query, 'Web')
    #print bing_search(query, 'Web')
    #print bing_search(query, 'Image')

def bing_search(query, search_type):
    #search_type: Web, Image, News, Video
    key= 'x+Q+z2OTfi85No24ynj7T+IKlmZU7++VuMlVwxp5Ykc'
    query = urllib.quote(query)
    # create credential for authentication
    user_agent = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)'
    credentials = (':%s' % key).encode('base64')[:-1]
    auth = 'Basic %s' % credentials
    #Original
    #url = 'https://api.datamarket.azure.com/Data.ashx/Bing/Search/'+search_type+'?Query=%27'+query+'%27&$top=100&$format=json'
    #Composite Search. This search gives more results
    #url = 'https://api.datamarket.azure.com/Bing/Search/v1/Composite?Sources=%27web%2BRelatedSearch%27&Query=%27www.namasteflavours.com%27&$top=100&$format=json'

    url = 'https://api.datamarket.azure.com/Bing/Search/v1/Composite?Sources=%27web%2BRelatedSearch%27&Query=%27www.namasteflavours.com%27&$top=100&$format=json'

    request = urllib2.Request(url)
    request.add_header('Authorization', auth)
    request.add_header('User-Agent', user_agent)
    request_opener = urllib2.build_opener()
    response = request_opener.open(request)
    response_data = response.read()
    json_result = json.loads(response_data)
    #result_list = json_result['d']['results']
    result_list = json_result['d']['results'][0]['Web']
    #print result_list
    resultsProcessed(result_list,query)
    #return result_list


def resultsProcessed(json_result,query):
    businessData[query] = {}
    if(len(json_result)) == 0 :
        print "No Results generated"

    else:
        for result in json_result:


            #You Can Also call the Database and have these entries in there to, instead of having them in the Code
            #Check for Yelp
            if "http://www.yelp.com/biz/" in result['Url']:
                print result['Url']
                businessData[query]['Yelp'] = result['Url']
            #Check TripAdvisor
            if "https://www.tripadvisor.com/" in result['Url']:
                print result['Url']
                businessData[query]['TripAdvisor'] = result['Url']
            #Check Yahoo
            if "https://local.yahoo.com/" in result['Url']:
                print result['Url']
                businessData[query]['Yahoo'] = result['Url']
            #Check Locu
            if "https://locu.com/places/" in result['Url']:
                print result['Url']
                businessData[query]['Locu'] = result['Url']

            #Check Mapquest
            if "https://www.mapquest.com/" in result['Url']:
                print result['Url']
                businessData[query]['Mapquest'] = result['Url']

            # Check Groupon
            if "https://www.groupon.com/biz/" in result['Url']:
                print result['Url']
                businessData[query]['Groupon'] = result['Url']

            # Check YelloPages
            if "http://www.yellowpages.com/" in result['Url']:
                print result['Url']
                businessData[query]['YellowPages'] = result['Url']

            # Check Trip Advisor Reviews
            if "https://www.tripadvisor.com/ShowUserReviews-" in result['Url']:
                print result['Url']


           # Check Zomato
            if "https://www.zomato.com/" in result['Url']:
                print result['Url']
                businessData[query]['Zomato'] = result['Url']

            # Check Cortera
            if "https://start.cortera.com/company/research/" in result['Url']:
                print result['Url']
                businessData[query]['Cortera'] = result['Url']

            # Check Yelp Photos
            if "http://www.yelp.com/biz_photos/" in result['Url']:
                print result['Url']

            # Check Yelp MenuPix
            if "http://www.menupix.com/" in result['Url']:
                print result['Url']
                businessData[query]['MenuPix'] = result['Url']

        print businessData
if __name__ == "__main__":
    main()
