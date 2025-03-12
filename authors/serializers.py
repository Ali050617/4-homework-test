from rest_framework import serializers
from .models import Authors


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ('id', 'first_name', 'last_name', 'bio', 'birth_date', 'nationality')


class AuthorBookListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    isbn = serializers.CharField()
    published_date = serializers.DateField()
    copies_available = serializers.SerializerMethodField()

    def get_copies_available(self, obj):
        return obj.book_copies.filter(is_available=True).count()
