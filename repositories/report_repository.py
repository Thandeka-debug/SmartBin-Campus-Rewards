from abc import ABC, abstractmethod
from typing import List
from src.report import Report
from repositories.repository_interface import Repository

class ReportRepository(Repository[Report, str], ABC):
    @abstractmethod
    def find_by_generated_by(self, user_id: str) -> List[Report]:
        pass