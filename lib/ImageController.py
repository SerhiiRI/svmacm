from docker.errors import NotFound
import docker

class ImageController:
    """ Image controller """
    def __init__(self):
        self._client = docker.from_env()
        self.__list = self._client.images.list()

    def getByName(self, name):
        try:
            return self._client.images.get(name)
        except NotFound:
            return None

    def list(self):
        self.__list = self._client.images.list()
        return self.__list

    def run(self, image_name, auto_remove=False, detach=True):
        container = False
        try:
            container =  self._client.containers.run(image_name, tty=True, auto_remove=auto_remove, detach=detach)
        except docker.errors.APIError:
            print("cannot create container by name {}".format(image_name))
        return container


    def pull(self, repository, tag="latest"):
        if(repository == ""):
            return False
        try:
            self._client.images.pull(repository, tag)
            return True
        except docker.errors.NotFound:
            print("Cannot pull")
        return False

    def delete(self, image):
        try:
            self._client.images.remove(image)
            return True
        except docker.errors.APIError ("not found container by name"):
            print("image by name <" + image + "> not found")
        return False

    def delete_all(self):
        imagelist = self._client.images.list()
        for image in imagelist:
            try:
                for version in image.tags:
                    try:
                        self._client.images.remove(version, force=True)
                    except docker.errors.APIError ("images list crush"):
                        print("cannot delete images")
            except NotFound:
                print("version not found")
        return True

    def prune(self):
        try:
            return self._client.images.prune()
        except docker.errors.APIError:
            print("can not prune")
        return False

    def __callbackBackAlert(self, message):
        print("[!] ALERT\n")
        print(message)

