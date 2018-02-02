from rest_framework import serializers
from app.models import Profile, Post, Drink
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Profile
        fields = ('id', 'fio', 'age', 'user_id')


class PostSerializer(serializers.ModelSerializer):
    drink_name = serializers.ReadOnlyField(source='drink.name')
    user_id = serializers.ReadOnlyField(source='user.id')

    # user=serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Post
        fields = ('id','user_id', 'pair', 'drink_name')


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ('id', 'name')


class UserSerializer(serializers.ModelSerializer):
    #post = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
    post_id = serializers.ReadOnlyField(source='post.id')
    class Meta:
        model = User
        fields = ('id', 'username', 'post_id')
