from http.client import HTTPException
from django.http import HttpResponseRedirect
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework import status
from helpers import base62
from shorturl.settings import SERVER_BASE_URL
from .serializers import UrlSerializer
from apps.urls.models import Url


@api_view(['GET'])
def get_all(request):
    urls = Url.objects.all()
    serializer = UrlSerializer(urls, many=True)
    if urls: 
        return Response(serializer.data, status.HTTP_200_OK)
    return Response({'msg': 'no data'}, status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_one(request, short):
    url = Url.objects.filter(short_url = short).first()
    if url: 
        serializer = UrlSerializer(url)
        return Response(serializer.data, status.HTTP_200_OK)
    return Response({'msg': 'not found.'}, status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def create(request):
    long = request.data.get('url', None)
    if long: 
        url = Url.objects.filter(long_url = long).first()
        if url: 
            short = f'{SERVER_BASE_URL}/s/{url.short_url}'
            return Response(short, status.HTTP_200_OK)
        try:  
            new = Url(long_url = long)
            new.save()
            new.short_url = base62.encode(new.id)
            new.save()
            short = f'{SERVER_BASE_URL}/s/{new.short_url}'
            return Response(short, status.HTTP_201_CREATED)
        except HTTPException as e:
            return Response({'error': e}, status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': e}, status.HTTP_500_INTERNAL_SERVER_ERROR)    
    return Response({'error': 'missing data'}, status=status.HTTP_400_BAD_REQUEST) 

    
@api_view(['GET'])
def get(request,short):
    url = Url.objects.filter(short_url = short).first()
    if url: 
        return Response(url.long_url, status.HTTP_200_OK)
    return Response({'error': 'not found'}, status=status.HTTP_400_BAD_REQUEST)  
        