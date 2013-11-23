from distutils.core import setup
import py2exe

setup(
    windows = ['selenium_cb_python.py'],
    options = {
        "py2exe" : {
            "includes" : [],
            "bundle_files" : 1,
            "compressed" : True
        }
    },
    zipfile = None
)

#python basic_setup.py py2exe