from abc import ABC, abstractmethod

class EndpointFlow(ABC):

    def __init__(self, request):
        self.request = request

    @abstractmethod
    def execute(self):
        raise NotImplementedError