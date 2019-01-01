#!/usr/bin/env bash

if [ ! -f /usr/local/lib/python3.6/site-packages/django_elasticsearch_dsl/management/commands/search_index.py ]; then
    echo "Creating search index"
    python manage.py search_index --create
    
else
   echo "Search index allready exist."
fi