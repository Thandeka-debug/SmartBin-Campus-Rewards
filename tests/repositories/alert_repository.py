"""
Alert Repository Interface
"""

from abc import ABC
from typing import List, Optional
from datetime import datetime
from src.alert import Alert

from repositories.repository_interface import Repository


class AlertRepository(Repository[Alert, str], ABC):
    """
    Entity-specific repository for Alert.
    """
    
    def find_by_bin_id(self, bin_id: str) -> List[Alert]:
        """Find all alerts for a specific bin"""
        pass
    
    def find_unacknowledged_alerts(self) -> List[Alert]:
        """Find all alerts that are not yet acknowledged"""
        pass
    
    def find_by_severity(self, severity: str) -> List[Alert]:
        """Find alerts by severity (warning, critical)"""
        pass