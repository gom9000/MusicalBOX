#
# setup.py
#  ___                  _         ___          __  _____ 
# / __| __ _ _ __  _ __| |___ _ _| _ ) _____ __\ \/ / _ \
# \__ \/ _` | '  \| '_ \ / -_) '_| _ \/ _ \ \ / >  <|  _/
# |___/\__,_|_|_|_| .__/_\___|_| |___/\___/_\_\/_/\_\_|  
#                 |_|                                    
#
# Author : Alessandro Fraschetti (mail: gos95@gommagomma.net)
# URL    : http://www.gommagomma.net/SamplerBoxXP/
# License: Creative Commons ShareAlike 3.0 (http://creativecommons.org/licenses/by-sa/3.0/)
# Credits: Joseph Ernest and his SamplerBox (https://github.com/josephernest/SamplerBox/)
#
# SamplerBoxXP - setup module for Cython extensions
#


from distutils.core import setup
from Cython.Build import cythonize
import numpy


setup(ext_modules = cythonize("samplerbox_audio.pyx"), include_dirs=[numpy.get_include()])