# -*- coding: utf-8 -*-

import haystack
from haystack.indexes import SearchIndex

from text.models import Text

class TextIndex(SearchIndex):
    desc = haystack.fields.CharField(document=True)

haystack.site.register(Text, TextIndex)
