from terms_api.models import Synonyms, Term
import json

from terms_api.serializers import TermSynonymSerializer


def run():
    with open('data_dump/terms.json', 'r', encoding='utf-8') as file:
        reader = json.load(file)

        for row in reader["terms"]:
            

            list_a = row["description"]

            try:
                term = Term.objects.get(obo_id = row['obo_id'])
            except:
                term = None
            

            if not term:
                term = Term(label=row['label'],
                            has_children=row['has_children'],
                            is_obsolete=row['is_obsolete'],
                            is_defining_ontology=row['is_defining_ontology'],
                            obo_id=row['obo_id'],
                            description='' if not list_a else list_a[0],
                            lang=row['lang'],
                            ontology_name=row['ontology_name'],
                            ontology_prefix=row['ontology_prefix'],
                            short_form=row['short_form'])

                term.save()
            if row['obo_synonym']:
                for rowSyn in row['obo_synonym']:
                    synonym = Synonyms(name=rowSyn["name"],
                                    scope=rowSyn["scope"],
                                    type=rowSyn["type"],
                                    term=term)

                    synonym.save()

            
