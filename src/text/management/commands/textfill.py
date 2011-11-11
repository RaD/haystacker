# -*- coding: utf-8 -*-
# (c) 2011 Ruslan Popov <ruslan.popov@gmail.com>

from django.conf import settings
from django.core.management.base import NoArgsCommand

import time
import lxml.html
import urllib2
import re
import random
import cStringIO as IO
import gzip

from text import models

# Mozilla Firefox headers
HEADERS = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0) Gecko/20100101 Firefox/4.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language':'ru,en-us;q=0.7,en;q=0.3',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Charset':'utf-8;q=0.7,*;q=0.7',
    'Keep-Alive':'115',
    'Connection':'keep-alive',
    'Cache-Control':'max-age=0'
}

def retrieve(url, filename):
    print 'Retrieve %s and save into %s' % (url, filename)

    try:
        with open(filename, 'r') as f:
            body = f.read()
        print 'Use cached data'
        return body
    except IOError:
        pass

    while True:
        try:
            time.sleep(random.randint(5,20))
            request = urllib2.Request(url, headers=HEADERS)
            conn = urllib2.urlopen(request, timeout=10)
            body = conn.read()
            if 'gzip' == conn.headers.get('content-encoding'):
                print 'Decompression'
                io = IO.StringIO(body)
                f = gzip.GzipFile(mode='rb', fileobj=io)
                try:
                    body = f.read()
                finally:
                    f.close()
            conn.close()
        except urllib2.HTTPError, e:
            print _(u'Cannot retrieve URL.\nHTTP Error Code: %s') % e.code
        except urllib2.URLError, e:
            print _(u'Cannot retrieve URL: %s') % e.reason[1]
        else:
            with open(filename, 'w') as f:
                f.write(body)
            print 'Cache data'
            return body
        print 'Try again after pause'

class Command(NoArgsCommand):
    help = u'Download a fiction book and fill model with its text.'

    URL = 'http://lib.rus.ec/b/320910/read'
    SPACES_RE = re.compile(r' +')

    def handle_noargs(self, *args, **options):

        words = []
        raw = retrieve(self.URL, './book.html')
        page = unicode(raw, 'utf-8', errors='ignore')
        tree = lxml.html.fromstring(page)
        tokens = tree.xpath("//text()")

        for line in tokens:
            words.extend(filter(lambda x: x not in ['.', ',', ':', '!', '?'], self.SPACES_RE.sub(' ', line).split()))

        max_index = len(words) - 50 - 1

        for i in xrange(100000):
            index = random.randint(0, max_index)
            line = u' '.join(words[index:index+20])
            models.Text(desc=line).save()
