import os
from cffi import FFI

ffibuilder = FFI()

# 1. C-like declarations (from default.h)
ffibuilder.cdef(
    """
    int httpSearch(int var_url, int var_host, int var_path, int var_request);
    int xordecrypt(const char *input, char *output, const char *key);
    int data_lambda(int var_a);
    int decrypt_lambda(char var_encrypt);
"""
)


ffibuilder.set_source(
    "_default_cffi",  # Name of the output C extension module (_my_math_cffi.so or .pyd)
    """
    #include "intellisearch/src/mod/default.h" // Include your C header
    """,
    sources=["intellisearch/src/mod/default.c"],  # List of C source files to compile
    # library_dirs=['path/to/libs'],  # Optional: if linking against precompiled libs
    # libraries=['mylib'],            # Optional: e.g., if you had libmylib.so
    include_dirs=["."],  # Directory where my_c_math.h can be found
)

### MOD ###

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
