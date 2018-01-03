import os
from PyQt4.QtCore import QIcon


def resolve(name):
    """
    Resolve a resource file path.
    :param name: The name of the resource to resolve.
    :return:
    """
    f = os.path.join(os.path.dirname(__file__), name)
    return f

def icon(name):
    """
    Return a QIcon given the resource name.
    :param name: The name of the resource to return
    :return: QIcon loading from the given resource name.
    """
    f = resolve(name)
    return QIcon(f)
