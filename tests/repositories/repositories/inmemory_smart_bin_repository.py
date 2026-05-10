"""
In-Memory implementation of SmartBinRepository
"""

from typing import Dict, List, Optional
from src.smart_bin import SmartBin, BinStatus

from repositories.smart_bin_repository import SmartBinRepository


class InMemorySmartBinRepository(SmartBinRepository):
    """
    Stores SmartBin objects in a Python dictionary (HashMap).
    """
    
    def __init__(self):
        self._storage: Dict[str, SmartBin] = {}
    
    def save(self, entity: SmartBin) -> None:
        """Save or update a smart bin"""
        self._storage[entity.get_bin_id()] = entity
    
    def find_by_id(self, id: str) -> Optional[SmartBin]:
        """Find a smart bin by ID"""
        return self._storage.get(id)
    
    def find_all(self) -> List[SmartBin]:
        """Get all smart bins"""
        return list(self._storage.values())
    
    def delete(self, id: str) -> None:
        """Delete a smart bin by ID"""
        if id in self._storage:
            del self._storage[id]
    
    def exists_by_id(self, id: str) -> bool:
        """Check if a smart bin exists"""
        return id in self._storage
    
    def find_by_location(self, location: str) -> Optional[SmartBin]:
        """Find bin by its location"""
        for bin in self._storage.values():
            if bin.get_location().lower() == location.lower():
                return bin
        return None
    
    def find_bins_by_status(self, status: str) -> List[SmartBin]:
        """Find bins with a specific status"""
        return [b for b in self._storage.values() if b.get_status().value == status]
    
    def find_bins_needing_emptying(self, threshold: int = 80) -> List[SmartBin]:
        """Find bins with fill level above threshold"""
        return [b for b in self._storage.values() if b.get_fill_level() >= threshold]
    
    def update_fill_level(self, bin_id: str, fill_level: int) -> None:
        """Update a bin's fill level"""
        bin = self.find_by_id(bin_id)
        if bin:
            bin.update_fill_level(fill_level)