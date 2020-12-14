from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def home(request): 
    # if not request.is_ajax():
    #     raise Http404

    # json_data = {'xval': 10, 'yval': 10}
    # return HttpResponse(json_data,content_type="application/json")
    if request.method == "GET":
        return render(request,'index1.html') 
        # return HttpResponse('Data received')
    
    response = requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=52364270e03d88b2f26ad29cff466e81&language=en-US&page=1')
    # response = requests.get('https://api.themoviedb.org/3/search/movie?api_key=52364270e03d88b2f26ad29cff466e81&language=en-US&query=avengers endgame&page=1&include_adult=false')
    json_str = json.dumps(response.json(), indent=2)
    # return HttpResponse(json_str)
    data = json.loads(json_str)

    movie_data = {}
    for i in range(len(data['results'])):
        movie_data[data['results'][i]['id']] = {"poster_path": data['results'][i]['poster_path'],
                                                "title": data['results'][i]['title'],
                                                "overview": data['results'][i]['overview'],
                                                "popularity": data['results'][i]['popularity'],
                                                }
    context = {
        'movie_data': movie_data,
    }
    # print(data['results'][0]['title'])
    # print(context['movie_data'])
    # return render(request, 'home.html',context)
    context = json.dumps(context,indent=2)
    return HttpResponse(context,content_type="application/json")
        