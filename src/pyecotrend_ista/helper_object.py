from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional

from dataclasses_json import DataClassJsonMixin, dataclass_json


@dataclass_json
@dataclass
class AverageConsumption(DataClassJsonMixin):
    averageConsumptionValue: float
    residentConsumptionValue: float
    averageConsumptionPercentage: int
    residentConsumptionPercentage: int
    additionalAverageConsumptionValue: float
    additionalResidentConsumptionValue: float
    additionalAverageConsumptionPercentage: int
    additionalResidentConsumptionPercentage: int

    def replace_point(self):
        for _field in self.__dataclass_fields__.values():
            if _field.name in [
                "averageConsumptionValue",
                "residentConsumptionValue",
                "additionalAverageConsumptionValue",
                "additionalResidentConsumptionValue",
            ]:
                if isinstance(getattr(self, _field.name), str):
                    setattr(self, _field.name, float(getattr(self, _field.name).replace(",", ".")))

    def __post_init__(self):
        self.replace_point()


@dataclass_json
@dataclass
class ComparedConsumption:
    lastYearValue: float
    period: Date
    smiley: str
    comparedPercentage: int
    comparedValue: float

    def replace_point(self):
        for _field in self.__dataclass_fields__.values():
            if _field.name in ["lastYearValue", "comparedValue"]:
                if isinstance(getattr(self, _field.name), str):
                    setattr(self, _field.name, float(getattr(self, _field.name).replace(",", ".")))
                else:
                    setattr(self, _field.name, float(getattr(self, _field.name)))

    def __post_init__(self):
        self.replace_point()


@dataclass_json
@dataclass
class Consumption(DataClassJsonMixin):
    type: str
    value: float
    unit: str
    additionalValue: float
    additionalUnit: str
    estimated: bool
    comparedConsumption: Optional[ComparedConsumption]
    comparedCost: Optional[ComparedConsumption]
    averageConsumption: Optional[AverageConsumption]  # field(default_factory=AverageConsumption)

    def replace_point(self):
        for _field in self.__dataclass_fields__.values():
            if _field.name in ["value", "additionalValue"]:
                if isinstance(getattr(self, _field.name), str):
                    setattr(self, _field.name, float(getattr(self, _field.name).replace(",", ".")))

    def __post_init__(self):
        self.replace_point()


@dataclass_json
@dataclass
class Cost(DataClassJsonMixin):
    type: str
    value: int
    unit: str
    estimated: bool
    comparedCost: Optional[ComparedConsumption]


@dataclass_json
@dataclass
class Date(DataClassJsonMixin):
    month: int
    year: int


@dataclass_json
@dataclass
class LastValue(DataClassJsonMixin):
    heating: Optional[float] = None
    warmwater: Optional[float] = None
    water: Optional[float] = None
    month: Optional[int] = None
    year: Optional[int] = None


@dataclass_json
@dataclass
class LastCosts(DataClassJsonMixin):
    heating: Optional[float] = None
    warmwater: Optional[float] = None
    water: Optional[float] = None
    month: Optional[int] = None
    year: Optional[int] = None
    unit: Optional[str] = None


@dataclass_json
@dataclass
class CombinedData(DataClassJsonMixin):
    date: Date
    consumptions: List[Consumption]
    costs: List[Cost]


@dataclass_json
@dataclass
class TotalAdditionalValues(DataClassJsonMixin):
    heating: Optional[float] = None
    warmwater: Optional[float] = None
    water: Optional[float] = None


@dataclass_json
@dataclass
class SumByYear(DataClassJsonMixin):
    heating: Optional[Dict[int, float]] = None
    warmwater: Optional[Dict[int, float]] = None
    water: Optional[Dict[int, float]] = None


@dataclass_json
@dataclass
class CustomRaw(DataClassJsonMixin):
    consum_types: Optional[List[str]]
    combined_data: List[CombinedData]
    total_additional_values: TotalAdditionalValues
    last_value: LastValue
    all_dates: List[Date]
    sum_by_year: SumByYear
    last_costs: Optional[LastCosts]
