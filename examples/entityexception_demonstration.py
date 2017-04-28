import htlib.basicinfo
import sys, traceback

try:
    someone = htlib.basicinfo.Entity('Natalie', 'NoneType')
except htlib.basicinfo.EntityError:
    extype, exvalue, extb = sys.exc_info()

    traceback.print_tb(extb, limit=1)
