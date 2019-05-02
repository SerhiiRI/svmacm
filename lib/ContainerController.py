from pprint import PrettyPrinter

import docker.errors


class ContainerController:
    """ Image controller """
    def __init__(self):
        self._client = docker.from_env()
        self.__list = self._client.containers.list()


    def list(self, filter=""):
        try:
            if(filter in ["restarting", "running", "paused", "exited"]):
                containers = (self._client.containers.list(all=True, filters={"status": filter}))
            else:
                containers = (self._client.containers.list(all=True))
            return containers
        except docker.errors.APIError:
            print("API ERROR")
        return None

    def get(self, image_name):
        try:
            return self._client.containers.get(image_name)
        except docker.errors.NotFound:
            print("not found container")
        return None

    def run(self, image_name, auto_remove=True, detach=False):
        self._client.containers.run(image_name, tty=True, auto_remove=auto_remove, detach=detach)

    def pull(self, repository, tag=None):
        try:
            self._client.images.pull(repository, tag)
        except docker.errors.NotFound:
            print("repository wasn't found")
            return False
        except docker.errors.APIError:
            print("api error")
            return False
        return True

    def delete(self, id_or_name):
        try:
            container = self._client.containers.get(id_or_name)
            container.stop()
            container.remove(force=True)
        except docker.errors.APIError:
            print("container does not isset")
            return False
        return True

    def stop_container(self, id_or_name):
        try:
            container = self._client.containers.get(id_or_name)
            container.stop()
        except docker.errors.APIError:
            print("can not stop container {} ".format(id_or_name))
            return False
        return True

    def start_container(self, id_or_name):
        try:
            container = self._client.containers.get(id_or_name)
            container.start()
        except docker.errors.APIError:
            print("can not start container {} ".format(id_or_name))
            return False
        return True

    def stats_container(self, id_or_name):
        try:
            container = self._client.containers.get(id_or_name)
            stats = container.stats(stream=False)
        except docker.errors.APIError:
            print("can not get container stats: container: {} ".format(id_or_name))
            return False
        return stats


    def proces_container(self, id_or_name):
        try:
            container = self._client.containers.get(id_or_name)
            pslist = container.top()
        except docker.errors.APIError:
            print("can not get process stats from container {} ".format(id_or_name))
            return False
        return pslist

    def prune_container(self):
        try:
            self._client.containers.prune()
        except docker.errors.APIError:
            print("container remove error")
            return False
        return True

    def stop_all_containers(self):
        for container in self.list(filter="running"):
            try:
                container.stop()
            except docker.errors.APIError:
                print("stop container error")
        for container in self.list(filter="restarting"):
            try:
                container.stop()
            except docker.errors.APIError:
                print("stop container error")
        return True

    def start_all_containers(self):
        for container in self.list(filter="exited"):
            try:
                container.start()
            except docker.errors.APIError:
                print("start container error")
        for container in self.list(filter="paused"):
            try:
                container.start()
            except docker.errors.APIError:
                print("start container error")
        return True

    def remove_all_containers(self):
        self.stop_all_containers()
        for containers in self.list():
            try:
                containers.remove(force=True)
            except docker.errors.APIError:
                print("stop container error")
        return True

