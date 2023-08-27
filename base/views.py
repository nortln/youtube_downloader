from django.shortcuts import render
from pytube import *

def home(request):
    if request.method == "POST":

        link = request.POST["link"]
        video = YouTube(link)

        stream = video.streams.get_lowest_resolution()

        stream.download
    return render(request, "home.html")