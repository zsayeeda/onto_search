# from django.db import models
# from django import forms

# # class Ontology(models.Model):
#     # Parse owl file here!

# SUBONT_CHOICES = [
#     ('orange', 'Oranges'),
#     ('cantaloupe', 'Cantaloupes'),
#     ('mango', 'Mangoes'),
#     ('honeydew', 'Honeydews'),
#     ]

# TERM_CHOICES = [
#     ('orange', 'Oranges'),
#     ('cantaloupe', 'Cantaloupes'),
#     ('mango', 'Mangoes'),
#     ('honeydew', 'Honeydews'),
#     ]

# class OntologySearch(models.Model):
# 	first_name = forms.CharField(max_length=100)
# 	last_name = forms.CharField(max_length=100)
# 	email = forms.EmailField()
# 	age = forms.IntegerField()
# 	subont1 = models.CharField(max_length=6, choices=SUBONT_CHOICES, default='')
# 	subont2 = models.CharField(max_length=6, choices=SUBONT_CHOICES, default='')
# 	terms1 = models.CharField(max_length=6, choices=TERM_CHOICES, default='')
# 	terms2 = models.CharField(max_length=6, choices=TERM_CHOICES, default='')