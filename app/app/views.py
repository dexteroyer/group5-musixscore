class UpdateGenre(View):
    def post(self, request):
        return HttpResponse()

class AddArtist(View):
    def post(self, request):
        # Get data
        artist_name = request.POST['artist_name']
        genre_id = request.POST['genre_id']
        # Get instance
        genre_instance = Genre.objects.get(id=genre_id)
        # Check redundancy
        redundant = Artist.objects.filter(artist_name__iexact=artist_name, genre=genre_instance)
      
        if len(redundant) == 0:
            query = Artist(artist_name=artist_name, genre=genre_instance)
            query.save()

class DeleteArtist(View):
    def post(self, request):
        artist_id = request.POST['artist_id']
        query = Artist.objects.get(id=artist_id)
        query.delete()
        return HttpREsponse()

class UpdateArtist(View)
    def post(self, request):
        genre_id = request.POST['genre_id']
        artist_id = request.POST['artist_id']
        artist_name = request.POST['artist_name']

        # Check redundancy
        redundant = Artist.objects.filter(artist_name__iexact=artist_name, genre=genre_instance)
      
        if len(redundant) == 0:
            query = Artist(artist_name=artist_name, genre=genre_instance)
            query.save()
            data = dict()
            data['error'] = False 
            return HttpResponse(json.dumps(data), content_type="application/json")
        else:
            data = dict()
            data['error'] = True
            return HttpResponse(json.dumps(data), content_type="application/json")


