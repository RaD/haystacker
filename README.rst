Test application to check search engines performance
====================================================

This simple project used to compare Whoosh ans Xapian backends for
Haystack Search Engine.

Dependencies
************

Xapian
------

With active virtual environment do the following::

    cd ~/tmp

    wget http://oligarchy.co.uk/xapian/1.2.7/xapian-core-1.2.7.tar.gz
    tar xzf xapian-core-1.2.7.tar.gz
    cd xapian-core-1.2.7
    ./configure --prefix=${VIRTUAL_ENV} && make && make install
    cd -

    wget http://oligarchy.co.uk/xapian/1.2.7/xapian-bindings-1.2.7.tar.gz
    tar xzf xapian-bindings-1.2.7.tar.gz
    cd xapian-bindings-1.2.7
    ./configure --prefix=${VIRTUAL_ENV} --with-python \
        --without-php --without-ruby --without-tcl --without-csharp \
        --without-java --without-perl --without-lua && make && make install
    cd -

Sorl
----

Solr is required the java environment::

    cd ~/tmp
    wget http://apache.infocom.ua/lucene/solr/1.4.1/apache-solr-1.4.1.tgz
    cd apache-solr-1.4.1/example
    python manage.py build_solr_schema > ~/tmp/apache-solr-1.4.1/example/solr/conf/schema.xml
    java -jar start.jar

Result
******

Incremental indexing
--------------------

===== ============ ============ ============
Items    Whoosh       Xapian        Solr
===== ============ ============ ============
 10K  02:59, 2.8MB 00:13,   4MB 00:10,   1MB
 20K  21:29, 7.5MB 00:26,   8MB 00:16,   2MB
 30K  41:04,  11MB 00:38,  11MB 00:25,   3MB
 40K      --       00:53,  15MB 00:34,   5MB
 50K      --       01:14,  19MB 00:45,   9MB
100K      --       02:25,  37MB 01:45,  16MB
200K      --       05:42,  75MB 02:53,  17MB
300K      --       08:32, 113MB 03:52,  28MB
400K      --       09:20, 151MB
500K      --       13:30, 189MB
  1M      --       27:13, 378MB
===== ============ ============ ============

Rebuilding index
----------------

===== ============ ============ ============
Items    Whoosh       Xapian        Solr
===== ============ ============ ============
 10K
 20K
 30K
 40K
 50K
100K
200K
300K
400K
500K
  1M               20:36, 378MB 13:31,  72MB
===== ============ ============ ============
