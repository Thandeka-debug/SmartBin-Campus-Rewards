from enum import Enum
from datetime import datetime


class BinStatus(Enum):
    OPERATIONAL = "operational"
    REPORTING = "reporting"
    WARNING = "warning"
    CRITICAL = "critical"
    OFFLINE = "offline"
    DECOMMISSIONED = "decommissioned"


class SmartBin:
    def __init__(self, bin_id: str, location: str):
        self._bin_id = bin_id
        self._location = location
        self._fill_level = 0
        self._status = BinStatus.OPERATIONAL
        self._last_updated_at = datetime.now()
        self._total_deposits = 0

    def get_bin_id(self) -> str:
        return self._bin_id

    def get_location(self) -> str:
        return self._location

    def get_fill_level(self) -> int:
        return self._fill_level

    def get_status(self) -> BinStatus:
        return self._status

    def get_total_deposits(self) -> int:
        return self._total_deposits

    def update_fill_level(self, level: int) -> None:
        self._fill_level = level
        self._last_updated_at = datetime.now()
        
        if level >= 95:
            self._status = BinStatus.CRITICAL
        elif level >= 80:
            self._status = BinStatus.WARNING
        elif level > 0:
            self._status = BinStatus.REPORTING
        else:
            self._status = BinStatus.OPERATIONAL

    def check_capacity(self) -> bool:
        return self._fill_level < 95

    def empty_bin(self) -> None:
        self._fill_level = 0
        self._status = BinStatus.OPERATIONAL
        self._last_updated_at = datetime.now()

    def get_status_color(self) -> str:
        if self._fill_level >= 80:
            return "red"
        elif self._fill_level >= 60:
            return "yellow"
        return "green"

    def decommission(self) -> None:
        self._status = BinStatus.DECOMMISSIONED

    def add_deposit(self) -> None:
        self._total_deposits += 1
        self.update_fill_level(min(100, self._fill_level + 2))

    def __str__(self) -> str:
        return f"SmartBin(id={self._bin_id}, location={self._location}, fill={self._fill_level}%, status={self._status.value})"