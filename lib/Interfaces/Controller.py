import docker


class Controller(object):

    def __init__(self):
        self._client = docker.from_env()

    def list(self):
        raise NotImplementedError("[!] Controller function not implemented")

    def delete(self):
        raise NotImplementedError("[!] Controller function not implemented")

    def add(self):
        raise NotImplementedError("[!] Controller function not implemented")

    def argument_parser(self):
        raise NotImplementedError("[!] Controller function not implemented")