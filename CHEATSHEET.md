# Python and Django basics


##  Open Django shell
 
``` bash
$ python manage.py shell
```

## Retrieve first tree

``` python
from berlin import models
t1 = models.BerlinStreetTrees.objects.first()
```

## Find trees within distance

``` python
qs = models.BerlinStreetTrees.within_distance(t1, 0.01)
```
