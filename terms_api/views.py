from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Term
from .serializers import TermSerializer, TermSynonymSerializer

class TermsListApiView(APIView):
    
    def get(self, request, *args, **kwargs):
        terms = Term.objects.prefetch_related('synonyms').all()

        serializer = TermSerializer(terms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # for feature use
    def post(self, request, *args, **kwargs):

        synonyms = request.data.get('synonyms')          

        synSerializer = TermSynonymSerializer(data=synonyms)
        data = {
            'label': request.data.get('label'), 
            'has_children': request.data.get('has_children'), 
            'is_obsolete': request.data.get('is_obsolete'), 
            'is_defining_ontology': request.data.get('is_defining_ontology'), 
            'obo_id': request.data.get('obo_id'), 
            'description': request.data.get('description'), 
            'lang': request.data.get('lang'), 
            'ontology_name': request.data.get('ontology_name'), 
            'ontology_prefix': request.data.get('ontology_prefix'), 
            'short_form': request.data.get('short_form'), 
        }

        serializer = TermSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)