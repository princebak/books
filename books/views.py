from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

class BookListView(APIView):
    def get(self, request):

        Book.objects.create(author="J.K. Rowling", title="Harry Potter", year=1997)
        Book.objects.create(author="George Orwell", title="1984", year=1949)
        Book.objects.create(author="J.R.R. Tolkien", title="The Hobbit", year=1937)

        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
