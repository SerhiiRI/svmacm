from lib.Interfaces.Controller import Controller
from pprint import PrettyPrinter

class ContainerController(Controller):
    """ Image controller """
    def __init__(self, printing_function):
        super(ContainerController, self).__init__()
        self.pprinter = PrettyPrinter()
        self.__list = self._client.containers.list()
        self.__callbackOutFunction = printing_function

    def list(self):
        containers = (self._client.containers.list(all=True))
        for x in containers:
            print(x.name +" -> " + str(*x.image.tags))
        return containers

    def run(self, image_name, auto_remove=True, detach=False):
        print("run")
        self._client.containers.run(image_name, tty=True, auto_remove=auto_remove, detach=detach)

    def pull(self, repository, tag=None):
        self._client.images.pull(repository, tag)

    def delete(self, id_or_name):
        container = self._client.containers.get(id_or_name)
        container.remove(force=True)

    def __callbackBackAlert(self, message):
        print("[!] ALERT\n")
        print(message)

    def stop_container(self, id_or_name):
        container = self._client.containers.get(id_or_name)
        container.stop()

    def start_container(self, id_or_name):
        container = self._client.containers.get(id_or_name)
        container.start()

    def stats_container(self, id_or_name):
        container = self._client.containers.get(id_or_name)
        stats = container.stats(stream=False)
        # self.pprinter.pprint(stats)
        return stats

    def proces_container(self, id_or_name):
        container = self._client.containers.get(id_or_name)
        pslist = container.top()
        # self.pprinter.pprint(pslist)
        return pslist

    def logs_container(self, id_or_name):
        container = self._client.containers.get(id_or_name)
        self.pprinter.pprint(container.logs(tail=20))

    def prune_container(self):
        self._client.containers.prune()

    def stop_all_containers(self):
        for container in self.list():
            container.stop()

    def start_all_containers(self):
        for container in self.list():
            container.start()

    def remove_all_containers(self):
        self.stop_all_containers()
        for containers in self.list():
            containers.remove(force=True)

    def status_all_containers(self):
        for container in self.list():
            self.pprinter.pprint([container.image, container.name, container.status])
