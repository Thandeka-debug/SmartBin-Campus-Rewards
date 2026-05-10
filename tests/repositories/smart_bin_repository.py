"""
SmartBin Repository Interface
"""

from abc import ABC
from typing import List, Optional
from src.smart_bin import SmartBin

from repositories.repository_interface import Repository


class SmartBinRepository(Repository[SmartBin, str], ABC):
    """
    Entity-specific repository for SmartBin.
    """
    
    def find_by_location(self, location: str) -> Optional[SmartBin]:
        """Find bin by its location"""
        pass
    
    def find_bins_by_status(self, status: str) -> List[SmartBin]:
        """Find bins with a specific status (warning, critical)"""
        pass
    
    def find_bins_needing_emptying(self, threshold: int = 80) -> List[SmartBin]:
        """Find bins with fill level above threshold"""
        pass
    
    def update_fill_level(self, bin_id: str, fill_level: int) -> None:
        """Update a bin's fill level"""
        pass