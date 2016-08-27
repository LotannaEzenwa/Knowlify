# This one decides what to do
from abc import ABCMeta, abstractproperty

import knowlify
import microserver



class Engine(object):
    __metaclass__ = ABCMeta

    @abstractproperty
    def __init__(self):
        raise NotImplementedError

    @abstractproperty
    def __enter__(self):
        raise NotImplementedError

    @abstractproperty
    def __exit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError


class KnowlingEngine(Engine):
    """
    Knowlifies a given html file
    """

    def __init__(self, url_or_filename):
        super(url_or_filename)

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class ChunkingEngine(Engine):
    """
    Auto-Chunks and selects the words to knowl
    """

    def __init__(self, path):
        super(path)

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

class ContextingEngine(Engine):
    """
    Live-Contexting of links
    """

    def __init__(self, base_filepath):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class LocalServerEngine(Engine):
    """
    Because Javascript is holding the world hostage
    """

    def __init__(self, port, data_dir):
        self._port = port
        self._data_dir = data_dir

    def __enter__(self):
        self._server, self._handler =\
            microserver.start_server(self._port, self._handler)

    def __exit__(self, exc_type, exc_val, exc_tb):
        microserver.close_server(self.server_instance)

    @property
    def server_instance(self):
        return self._server

    @property
    def handler(self):
        return self._handler

    @property
    def port(self):
        return self._port

    @property
    def data_directory(self):
        return self._data_dir