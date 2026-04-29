"""
Prototype Pattern - Clone existing objects
"""

import copy
from typing import Dict


class SmartBin:
    def __init__(self, bin_id: str, location: str):
        self.bin_id = bin_id
        self.location = location
        self.fill_level = 0
        self.status = "operational"
        self.configuration = {
            "warning_threshold": 80,
            "critical_threshold": 95,
            "reporting_interval": 60
        }
    
    def clone(self) -> 'SmartBin':
        return copy.deepcopy(self)
    
    def __str__(self) -> str:
        return f"SmartBin(id={self.bin_id}, location={self.location}, fill={self.fill_level}%)"


class BinCache:
    _bins: Dict[str, SmartBin] = {}
    
    @classmethod
    def load_cache(cls):
        standard_bin = SmartBin("B001", "Standard Location")
        standard_bin.configuration["reporting_interval"] = 60
        cls._bins["standard"] = standard_bin
        
        high_traffic_bin = SmartBin("B002", "High Traffic Location")
        high_traffic_bin.configuration["reporting_interval"] = 30
        high_traffic_bin.configuration["warning_threshold"] = 70
        cls._bins["high_traffic"] = high_traffic_bin
    
    @classmethod
    def get_bin(cls, bin_type: str) -> SmartBin:
        cached_bin = cls._bins.get(bin_type)
        if cached_bin:
            return cached_bin.clone()
        raise ValueError(f"Bin type '{bin_type}' not found")


if __name__ == "__main__":
    BinCache.load_cache()
    
    bin1 = BinCache.get_bin("standard")
    bin1.bin_id = "B003"
    bin1.location = "Library Ground Floor"
    
    bin2 = BinCache.get_bin("standard")
    bin2.bin_id = "B004"
    bin2.location = "Cafeteria"
    
    print("Cloned bin 1:", bin1)
    print("Cloned bin 2:", bin2)
    print("Prototype Pattern test passed!")
