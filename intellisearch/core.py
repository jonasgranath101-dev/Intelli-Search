# Import the CFFI-generated module and the ffi object
from _default_cffi import ffi, lib
import ctypes


# lib contains the C functions we defined via cdef
# ffi can be used for more advanced cffi features (like

### AI ###


### AI ###

### MOD ###


def httpSearch(i, y, k, p):

    return lib.httpSearch(i, y, k, p)


def xordecrypt(a, b, c):

    return lib.xordecrypt(a, b, c)


def data_lambda(h):

    return lib.data_lambda(h)


def decrypt_lambda(x):

    return lib.decrypt_lambda(x)


### MOD ###
