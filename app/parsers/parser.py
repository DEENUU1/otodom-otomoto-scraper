from abc import ABC, abstractmethod
from typing import Optional, List
from dataclasses import dataclass


@dataclass
class ResultBase:
    pass


class ParserStrategy(ABC):

    @abstractmethod
    def parse(self, data: List[Optional[str]]) -> List[Optional[str]]:
        pass


class Parser:
    def __init__(self, parser_strategy: ParserStrategy):
        self.parser_strategy = parser_strategy

    def parse(self, data: List[Optional[str]]) -> List[Optional[ResultBase]]:
        return self.parser_strategy.parse(data)
