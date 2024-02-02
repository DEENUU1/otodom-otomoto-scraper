from enum import Enum
from typing import Optional, Literal

from strategy.params import ParamsBase


class Category(Enum):
    OSOBOWE: str = "osobowe"
    CZESCI: str = "czesci"
    MOTOCYKLE: str = "motocykle"
    DOSTAWCZE: str = "dostawcze"
    CIEZAROWE: str = "ciezarowe"
    BUDOWLANE: str = "budowlane"
    PRZYCZEPY: str = "przyczepy"
    ROLNICZE: str = "rolnicze"


class BodyType(Enum):
    MINI: str = "seg-mini"
    CITY_CAR: str = "seg-city-car"
    COUPE: str = "seg-coupe"
    CABRIO: str = "seg-cabrio"
    COMBI: str = "seg-combi"
    COMPACT: str = "seg-compact"
    MINIVAN: str = "seg-minivan"
    SEDAN: str = "seg-sedan"
    SUV: str = "seg-suv"


PRICES = [2000, 3000, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 50000, 65000, 80000, 100000, 200000,
          500000, 1000000, 7500000]

YEAR = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998,
        1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016,
        2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]

MILEAGE = [20000, 35000, 50000, 75000, 100000, 125000, 150000, 170000, 175000, 180000, 200000, 250000]


class FuelType(Enum):
    BENZYNA: str = "petrol"
    BENZYNA_CNG: str = "petrol-cng"
    BENZYNA_LPG: str = "petrol-lpg"
    DIESEL: str = "diesel"
    ELEKTRYCZNY: str = "electric"
    ETANOL: str = "etanol"
    HYBRYDA: str = "hybrid"
    WODOR: str = "hidrogen"


class CarParams(ParamsBase):
    # marka: str = ...
    # model: str = ...
    # generacja: str = ...
    body_type: Optional[BodyType] = None
    price_from: Optional[int] = None
    price_to: Optional[int] = None
    year_from: Optional[int] = None
    year_to: Optional[int] = None
    fuel_type: Optional[FuelType] = None
    mileage_from: Optional[int] = None
    mileage_to: Optional[int] = None
    damage: Optional[Literal[0, 1]] = None
