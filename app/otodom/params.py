from strategy.params import ParamsBase
from dataclasses import dataclass
from enum import Enum
from typing import Optional, Literal


class PropertyType(Enum):
    MIESZKANIA: str = "mieszkanie"
    KAWALERKA: str = "kawalerka"
    DOMY: str = "dom"
    INWESTYCJE: str = "inwestycja"
    POKOJE: str = "pokoj"
    DZIALKI: str = "dzialka"
    LOKALE_UZYTKOWE: str = "lokal"
    HALE_I_MAGAZYNY: str = "haleimagazyny"
    GARAZE: str = "garaz"


class Availability(Enum):
    NOW: str = "NOW"
    THIRTY_DAYS: str = "THIRTY_DAYS"
    NINETY_DAYS: str = "NINETY_DAYS"


class DaysSinceCreated(Enum):
    ONE: int = 1
    THREE: int = 3
    SEVEN: int = 7


@dataclass
class OtoDomParams(ParamsBase):
    price_from: Optional[int] = None
    price_to: Optional[int] = None
    surface_from: Optional[int] = None
    surface_to: Optional[int] = None
    rent_type: Optional[Literal["sprzedaz", "wynajem"]] = None
    property_type: Optional[PropertyType] = None
    availability: Optional[Availability] = None
    created: Optional[DaysSinceCreated] = None
    is_private: Optional[bool] = None
    open_day: Optional[bool] = None
