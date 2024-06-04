from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import viewsets

from rest_framework.decorators import action

from myapp.models import Movie,Actor,Album,Tracks

from api.serializers import MovieSerializer,ActorSerializer,AlbumSerializer,TrackSerializer,ReviewSerializer


# Create your views here.

class MovieListCreateView(APIView):

    def get(self,request,*args,**kwargs):

        qs=Movie.objects.all()

        serializer_instance=MovieSerializer(qs,many=True)  #serialization

        # logic for returning all movies

        return Response(data=serializer_instance.data)
    

    def post(self,request,*args,**kwargs):

        # logic for adding a new movie

        serializer_instance=MovieSerializer(data=request.data) #deserialization

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)

class MovieRetrieveUpdateDestroyView(APIView):

    def get(self,request,*args,**kwargs):

        # logic for returning movie detail 

        id=kwargs.get("pk")

        movie_obj=Movie.objects.get(id=id)   #model instance

        serializer_instance=MovieSerializer(movie_obj,many=False)

        return Response(data=serializer_instance.data)
    
    def put(self,request,*args,**kwargs):

        # logic for updating movie details

        id=kwargs.get("pk")

        movie_obj=Movie.objects.get(id=id)

        serializer_instance=MovieSerializer(data=request.data,instance=movie_obj) #deserialization

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)

    
    def delete(self,request,*args,**kwargs):

        # logic for deleting movie details

        id=kwargs.get("pk")

        Movie.objects.get(id=id).delete()

        return Response(data={"message":"movie-delete"})
    
class LanguagesView(APIView):

    def get(self,request,*args,**kwrags):

        qs=Movie.objects.all().values_list("language",flat=True).distinct()

        return Response(data=qs)

class GenresView(APIView):

    def get(self,request,*args,**kwargs):

        qs=Movie.objects.all().values_list("genre",flat=True).distinct()

        return Response(data=qs)
    
#  ======================== viewset ==============================================================

class ActorViewset(viewsets.ViewSet):

    def list(self,request,*args,**kwargs):

        qs=Actor.objects.all()

        serializer_instance=ActorSerializer(qs,many=True)

        return Response(data=serializer_instance.data)
    
    
    def create(self,request,*args,**kwargs):

        serializer_instance=ActorSerializer(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)
        
        
    def retrieve(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        actor_obj=Actor.objects.get(id=id)

        serialzer_instance=ActorSerializer(actor_obj,many=False)

        return Response(data=serialzer_instance.data)
    
    def update(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        actor_obj=Actor.objects.get(id=id)

        serializer_instance=ActorSerializer(data=request.data,instance=actor_obj)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)
    

    def destroy(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Actor.objects.get(id=id).delete()

        return Response(data={"message":"actor-delete"})

# =========== modelviewset=========================================

class AlbumViewsetView(viewsets.ModelViewSet):

    serializer_class=AlbumSerializer

    queryset=Album.objects.all()

    @action(methods=["GET"],detail=False)
    def languages(self,request,*args,**kwargs):

        qs=Album.objects.all().values_list("language",flat=True).distinct()

        return Response(data=qs)
    
    
    @action(methods=["GET"],detail=False)
    def directors(self,request,*args,**kwargs):

        qs=Album.objects.all().values_list("director",flat=True).distinct()

        return Response(data=qs)
    
    
    @action(methods=["POST"],detail=True)
    def add_track(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        album_obj=Album.objects.get(id=id)

        serializer_instance=TrackSerializer(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save(album_object=album_obj)

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)
        

    @action(methods=["POST"],detail=True) 
    def add_review(self,request,*args,**kwargs):
      
      id=kwargs.get("pk")

      album_obj=Album.objects.get(id=id)

      serializer_instance=ReviewSerializer(data=request.data)

      if serializer_instance.is_valid():
          
          serializer_instance.save(album_object=album_obj)

          return Response(data=serializer_instance.data)
      
      else:
          
          return Response(data=serializer_instance.errors)
      

class TrackViewsetView(viewsets.ModelViewSet):

    serializer_class=TrackSerializer

    queryset=Tracks.objects.all()