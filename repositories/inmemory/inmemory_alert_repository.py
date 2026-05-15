"""
In-Memory implementation of AlertRepository
"""

from typing import Dict, List, Optional
from src.alert import Alert, AlertStatus

from repositories.alert_repository import AlertRepository


class InMemoryAlertRepository(AlertRepository):
    """
    Stores Alert objects in a Python dictionary (HashMap).
    """
    
    def __init__(self):
        self._storage: Dict[str, Alert] = {}
    
    def save(self, entity: Alert) -> None:
        """Save or update an alert"""
        self._storage[entity.get_alert_id()] = entity
    
    def find_by_id(self, id: str) -> Optional[Alert]:
        """Find an alert by ID"""
        return self._storage.get(id)
    
    def find_all(self) -> List[Alert]:
        """Get all alerts"""
        return list(self._storage.values())
    
    def delete(self, id: str) -> None:
        """Delete an alert by ID"""
        if id in self._storage:
            del self._storage[id]
    
    def exists_by_id(self, id: str) -> bool:
        """Check if an alert exists"""
        return id in self._storage
    
    def find_by_bin_id(self, bin_id: str) -> List[Alert]:
        """Find all alerts for a specific bin"""
        return [a for a in self._storage.values() if a.get_bin_id() == bin_id]
    
    def find_unacknowledged_alerts(self) -> List[Alert]:
        """Find all alerts that are not yet acknowledged"""
        return [a for a in self._storage.values() 
                if a.get_status() in [AlertStatus.CREATED, AlertStatus.SENT, AlertStatus.ESCALATED]]
    
    def find_by_severity(self, severity: str) -> List[Alert]:
        """Find alerts by severity"""
        return [a for a in self._storage.values() if a.get_severity().value == severity]