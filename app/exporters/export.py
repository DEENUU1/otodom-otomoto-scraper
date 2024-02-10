from abc import ABC, abstractmethod
from parsers.parser import ResultBase
from typing import List


class ExportStrategy(ABC):

    @abstractmethod
    def export(self, parsed_data: List[ResultBase]) -> None:
        pass


class Export:
    def __init__(self, strategy: ExportStrategy) -> None:
        self.strategy = strategy

    def export(self, parsed_data: List[ResultBase]) -> None:
        self.strategy.export(parsed_data)
