from rest_framework import generics
from postings.models import BlogPost


class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'

    def get_queryset(self):
        return BlogPost.objects.all()
