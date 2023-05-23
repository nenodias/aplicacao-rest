# *-* coding:utf-8 *-*
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Artigo, Post
User = get_user_model()

class PostSerializer(serializers.ModelSerializer):

    class Meta:
            model = Post
            fields = ('id', 'titulo', 'conteudo', 'data_publicacao')

class ArtigoSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()

    posts = PostSerializer(many=True)

    class Meta:
        model = Artigo
        fields = ('id', 'titulo', 'conteudo', 'data_publicacao', 'links', 'posts')
    
    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('artigo-detail', kwargs={'pk': obj.pk}, request=request)
        }
    def validate_data_publicacao(self, value):
        novo = not self.instance
        alterado = self.instance and self.instance.data_publicacao != data_publicacao
        if (novo or alterado) and (value < timezone.now() ):
            msg = _('Data de Publicação não pode ser no passado')
            raise serializers.ValidationError(msg)
        return value

    def create(self, validated_data):
        '''
            O Create deve ser reimplementado para tratar a criação dos itens
        '''
        try:
            posts_data = validated_data.pop('posts')
            artigo = Artigo.objects.create(**validated_data)
            for post_data in posts_data:
                post = Post.objects.create(**post_data)
                artigo.posts.add(post)
            return artigo
        except Exception as e:
            print(e)
        return None

class UserSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    
    class Meta:
        model = User
        fields = ('id', User.USERNAME_FIELD, 'full_name', 'is_active', 'links',)
    
    def get_links(self, obj):
        request = self.context['request']
        username = obj.get_username()
        return {
            'self': reverse('user-detail', kwargs={User.USERNAME_FIELD: username}, request=request)	
        }