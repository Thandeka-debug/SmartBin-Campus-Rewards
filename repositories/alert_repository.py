from abc import ABC, abstractmethod
from typing import List
from src.alert import Alert
from repositories.repository_interface import Repository

class AlertRepository(Repository[Alert, str], ABC):
    @abstractmethod
    def find_unacknowledged_alerts(self) -> List[Alert]:
        pass