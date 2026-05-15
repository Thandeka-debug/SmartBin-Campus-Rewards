from abc import ABC, abstractmethod
from typing import List
from src.smart_bin import SmartBin
from repositories.repository_interface import Repository

class SmartBinRepository(Repository[SmartBin, str], ABC):
    @abstractmethod
    def find_bins_needing_emptying(self, threshold: int = 80) -> List[SmartBin]:
        pass