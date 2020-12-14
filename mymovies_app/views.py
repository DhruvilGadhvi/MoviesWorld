import requests
import json
from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie_Data

def index(request):
   
    response = requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=4d8f107a19366ff018ab05901d44eb84&language=en-US&page=1')
   
    json_str= json.dumps(response.json(),indent=2)
    data=json.loads(json_str)

    if request.method == 'GET':
        for i in range(len(data['results'])):
            # movie_id = data['results'][i]['id']
            title = data['results'][i]['title']
            overview = data['results'][i]['overview']
            popularity = data['results'][i]['popularity']
            poster_path = data['results'][i]['poster_path']

            if not Movie_Data.objects.filter(title=title).exists():
                Movie_Data.objects.create(title=title,poster_path =poster_path ,overview =overview ,popularity=popularity)
                print("Data Created")
            
            # else:
            #     print("Data Exists...")
    
    
    # movie_data={}
    # for i in range(len(data['results'])):
    #     movie_data[data['results'][i]['id']] = {"poster_path":data['results'][i]['poster_path'],
    #                                         "title":data['results'][i]['title'],
    #                                         "overview":data['results'][i]['overview'],
    #                                         "popularity":data['results'][i]['popularity'],
    #                                         }
    
    movie_data = Movie_Data.objects.all()
    context={
       'movie_data':movie_data,
    }
    # return HttpResponse("Hello")
    return render(request, 'mymovies_app/index.html',context)
