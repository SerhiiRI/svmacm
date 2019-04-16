from docker.errors import NotFound
from lib.Interfaces.Controller import Controller

class ImageController(Controller):
    """ Image controller """
    def __init__(self, printing_function):
        super(ImageController, self).__init__()
        # _client = docker.from_env()
        self.__list = self._client.images.list()
        self.__callbackOutFunction = printing_function

    def argument_parser(self, ARG):
        if (ARG.name == ""): return
        if (ARG.run):self.run(ARG.name, False, True); return
        if (ARG.delete):self.delete(ARG.name); return
        if (ARG.list): self.list(); return
        if (ARG.pull): self.pull(ARG.name)
        self.__callbackBackAlert("no option selected")
        return

    def list(self):
        self.__list = self._client.images.list()
        self.__callbackOutFunction(*self._client.images.list())
        return self.__list

    def run(self, image_name, auto_remove=False, detach=True):
        print("run")
        return self._client.containers.run(image_name, tty=True, auto_remove=False, detach=True)

    def pull(self, repository, tag=None):
        self._client.images.pull(repository, tag)

    def delete(self, image):
        try:
            self._client.images.remove(image)
        except NotFound ("not found container by name"):
            print("image by name <" + image + "> not found")

    def __callbackBackAlert(self, message):
        print("[!] ALERT\n")
        print(message)

