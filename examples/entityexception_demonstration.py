'''\
This is a demonstration to using entities manually from the base class Entity rather than its children.
There are (for now) there are 4 entities available on the htlib.basicinfo.Entity() base class.

Those entities are:
PonyEn
OtherEn
NoneEn and
VehicleEn
'''

import htlib.basicinfo
import sys, traceback # Import sys and traceback for a more accurate error message.

# Here, we use Cydie Marmalade, the wizardy geek unicorn on this demonstration.
somepony = htlib.basicinfo.Entity('Cydie Marmalade', 'PonyType')

# Here, we use Natalie with an invalid entity.
try:
    someone = htlib.basicinfo.Entity('Natalie', 'NoneType')
except htlib.basicinfo.EntityError:
    extype, exvalue, extb = sys.exc_info()

    print('Try passing NoneType or something else and you get this:\n')
    traceback.print_tb(extb, limit=1)
