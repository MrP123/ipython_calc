import numpy as np
#import matplotlib.pyplot as plt
#import pandas as pd
#import scipy
import pint

import os
import sys, pprint
from types import ModuleType, FunctionType
sys.displayhook = pprint.pprint

ureg = pint.UnitRegistry(autoconvert_to_preferred=True)
ureg.default_format = '~P'
ureg.default_preferred_units = [
    ureg.m,               # distance      L
    ureg.kg,              # mass          M
    ureg.s,               # duration      T
    #ureg.degC,            # temperature   Θ
    ureg.N,               # force         L M T^-2
    ureg.Pa,              # pressure      M L^−1 T^−2
    ureg.kg * ureg.m**-3, # density       M L^-3
    ureg.W,               # power         L^2 M T^-3
]

def workspace():
    """
    List all variables in the current active python shell
    """
    tmp = globals().copy()
    [print(F"{k}:\t{v}\ttype={type(v)}") for k, v in tmp.items() if not k.startswith('_') and k!='tmp' and k!='In' and k!='Out' and not callable(v) and not isinstance(v, ModuleType)]

def modules():
    """
    List all modules in the current active python shell
    """
    tmp = globals().copy()
    [print(F"{k}:\t{v}\ttype={type(v)}") for k, v in tmp.items() if isinstance(v, ModuleType)]

def functions():
    """
    List all functions in the current active python shell
    """
    tmp = globals().copy()
    for k, v in tmp.items():
        if not k.startswith('_') and isinstance(v, FunctionType):
            doc_string = v.__doc__.strip() if v.__doc__ else ''
            print(F"{k}:\t{doc_string}")

def cls():
    """
    Clears the console
    """
    os.system('cls')

def clc():
    """
    Clears the console
    """
    cls()