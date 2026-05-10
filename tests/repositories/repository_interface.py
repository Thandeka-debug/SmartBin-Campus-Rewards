"""
Generic Repository Interface with CRUD operations
"""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Optional

T = TypeVar('T')
ID = TypeVar('ID')


class Repository(ABC, Generic[T, ID]):
    """
    Generic repository interface for CRUD operations.
    
    Type parameters:
    - T: Entity type (e.g., User, Transaction)
    - ID: ID type (e.g., str, int)
    """
    
    @abstractmethod
    def save(self, entity: T) -> None:
        """Save or update an entity (Create/Update)"""
        pass
    
    @abstractmethod
    def find_by_id(self, id: ID) -> Optional[T]:
        """Find an entity by its ID (Read)"""
        pass
    
    @abstractmethod
    def find_all(self) -> List[T]:
        """Get all entities (Read All)"""
        pass
    
    @abstractmethod
    def delete(self, id: ID) -> None:
        """Delete an entity by its ID (Delete)"""
        pass
    
    @abstractmethod
    def exists_by_id(self, id: ID) -> bool:
        """Check if an entity exists (Helper method)"""
        pass