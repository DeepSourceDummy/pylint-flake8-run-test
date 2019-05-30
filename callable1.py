"""MOD DOC"""


# from pkg_resources import add_activation_listner
# from callable import my_listener


# my_listener("ser")
# add_activation_listner("ser")

# import os.path
# import pickle
# import platform
# import sys

from pkg_resources import (
    # normalize_path,
    # working_set,
    add_activation_listener,
    # require,
)
# from setuptools import setup, find_packages
# from setuptools.command.build_py import build_py
# from setuptools.command.develop import develop
# from setuptools.command.test import test as test_command

add_activation_listener("Something")
