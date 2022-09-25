from django.db import models

class Term(models.Model):
    label = models.CharField(max_length = 180)
    has_children = models.BooleanField(default=False)
    is_obsolete = models.BooleanField(default=False)
    is_defining_ontology = models.BooleanField(default=False)
    obo_id = models.CharField(max_length = 200, default = "", primary_key=True)
    description = models.CharField(max_length=2000, default="")
    lang = models.CharField(max_length = 2, default="en")
    ontology_name = models.CharField(max_length = 200, default = "")
    ontology_prefix = models.CharField(max_length = 200, default = "")
    short_form = models.CharField(max_length = 150, default = "")
    

class Synonyms(models.Model):
    name = models.CharField(max_length = 180, default = "", null=False, blank=False)
    scope = models.CharField(max_length = 150, default = "",null=True, blank=True)
    type = models.CharField(max_length = 150, default = "",null=True, blank=True) 
    term = models.ForeignKey(Term, related_name='synonyms', on_delete=models.CASCADE)