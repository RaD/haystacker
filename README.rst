Test application to check search engines performance
====================================================

This simple project used to compare Whoosh ans Xapian backends for
Haystack Search Engine.

Result
------

===== ============ ============
Items    Whoosh      Xapian
===== ============ ============
 10K  02:59, 2.8MB 00:13, 3.8MB
 20K  21:29, 7.5MB 00:25, 7.4MB
 30K  41:04,  11MB 00:38,  11MB
 40K  ---          00:53,  15MB
 50K  ---          01:14,  19MB
100K  ---          02:25,  37MB
200K  ---          05:42,  75MB
300K  ---          08:32, 113MB
400K  ---          09:20, 151MB
500K  ---          13:30, 189MB
  1M  ---          27:13, 378MB
===== ============ ============
