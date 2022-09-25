from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from .models import Term, Synonyms


class TermSynonymSerializer(serializers.ModelSerializer):
    class Meta:
      model = Synonyms
      fields = ('id', 'name', 'scope', 'type')

      def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.DATA, many=True)
        if serializer.is_valid():
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED,
                            headers=headers)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TermSerializer(serializers.ModelSerializer):
    synonyms = TermSynonymSerializer(
        many=True,
    )

    class Meta:
        model = Term
        fields = ["label", "has_children", "is_obsolete", "is_defining_ontology", 'is_defining_ontology',
                  'obo_id',
                  'description',
                  'lang',
                  'ontology_name', 'ontology_prefix', 'short_form', 'synonyms']
