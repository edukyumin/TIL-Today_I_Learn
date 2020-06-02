# 0511_workshop

## views.py

```python
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Music, Artist, Comment
from .serializers import (MusicSerializer, ArtistSerializer,
                        ArtistDetailSerializer, CommentSerializer,
                        MusicDetailSerializer, CommentDetailSerializer)

# Create your views here.
@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    serializer = MusicDetailSerializer(music)
    return Response(serializer.data)


@api_view(['GET'])
def artist_list(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = ArtistDetailSerializer(artist)
    return Response(serializer.data)


# CREATE
@api_view(['GET', 'POST'])
def comments_create(request, music_pk):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(music_id=music_pk)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def comments_update_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentDetailSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        #serializer = CommentSerializer(data=request.data, instance=comment)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': 'Comment has been updated!!'})
    else:
        comment.delete()
        return Response({'message': "Comment has been deleted!!"})
```



## serializers.py

```python
from rest_framework import serializers
from .models import Music, Artist, Comment


class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ['id', 'name',]


class MusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = ['id', 'title', 'artist_id', ]


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'content', 'music_id',]


class ArtistDetailSerializer(ArtistSerializer):
    musics = MusicSerializer(source='music_set', many=True)
    musics_count = serializers.IntegerField(source='music_set.count')

    class Meta(ArtistSerializer.Meta):
        fields = ArtistSerializer.Meta.fields + ['musics', 'musics_count',]


class MusicDetailSerializer(MusicSerializer):
    comments = CommentSerializer(source='comment_set', many=True)

    class Meta(MusicSerializer.Meta):
        fields = MusicSerializer.Meta.fields + ['comments',]


class CommentDetailSerializer(CommentSerializer):
    music_title = serializers.CharField(source='music.title')

    class Meta(CommentSerializer.Meta):
        fields = CommentSerializer.Meta.fields + ['music_title']
```



## 구동사진

<img src="0511_workshop.assets/image-20200511234838991.png" alt="image-20200511234838991" style="zoom:80%;" />

![image-20200511235034076](0511_workshop.assets/image-20200511235034076.png)