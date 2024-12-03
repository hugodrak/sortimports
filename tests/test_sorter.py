from sortimports.sorter import sort_imports


def test_sort_imports():
    code = """
from app.module import feature
from App.Module import Feature
import os
from sys import path
import requests
"""
    expected = """
import os
from sys import path

import requests

from app.module import feature
from App.Module import Feature
"""
    assert sort_imports(code) == expected.strip()