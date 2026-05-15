"""
Database Repository Stub - For future implementation.
This shows how the system can be extended to support database storage.
"""

from typing import List, Optional
from repositories.user_repository import UserRepository
from src.user import User


class DatabaseUserRepository(UserRepository):
    """
    STUB: Database implementation of UserRepository.
    This is a placeholder for future work when moving to a real database.
    
    When implemented, this would:
    - Connect to MySQL/PostgreSQL
    - Use SQL queries for CRUD operations
    - Handle connection pooling and transactions
    """
    
    def __init__(self, connection_string: str):
        """
        Initialize database connection.
        
        Args:
            connection_string: Database connection string
                              e.g., "postgresql://user:pass@localhost:5432/smartbin"
        """
        self._connection_string = connection_string
        # In a real implementation: self._connection = create_connection(connection_string)
    
    def save(self, entity: User) -> None:
        """STUB: Save user to database"""
        # Future SQL: INSERT INTO users (...) VALUES (...)
        raise NotImplementedError("Database storage will be implemented in future iteration")
    
    def find_by_id(self, id: str) -> Optional[User]:
        """STUB: Find user by ID from database"""
        # Future SQL: SELECT * FROM users WHERE user_id = ?
        raise NotImplementedError("Database storage will be implemented in future iteration")
    
    def find_all(self) -> List[User]:
        """STUB: Get all users from database"""
        # Future SQL: SELECT * FROM users
        raise NotImplementedError("Database storage will be implemented in future iteration")
    
    def delete(self, id: str) -> None:
        """STUB: Delete user from database"""
        # Future SQL: DELETE FROM users WHERE user_id = ?
        raise NotImplementedError("Database storage will be implemented in future iteration")
    
    def exists_by_id(self, id: str) -> bool:
        """STUB: Check if user exists in database"""
        # Future SQL: SELECT COUNT(*) FROM users WHERE user_id = ?
        raise NotImplementedError("Database storage will be implemented in future iteration")
    
    def find_by_email(self, email: str) -> Optional[User]:
        """STUB: Find user by email from database"""
        raise NotImplementedError("Database storage will be implemented in future iteration")
    
    def find_by_role(self, role: str) -> List[User]:
        """STUB: Find users by role from database"""
        raise NotImplementedError("Database storage will be implemented in future iteration")
    
    def update_points(self, user_id: str, points: int) -> None:
        """STUB: Update user points in database"""
        raise NotImplementedError("Database storage will be implemented in future iteration")


# Similarly, you would create stubs for:
# - DatabaseTransactionRepository
# - DatabaseRewardRepository
# - DatabaseVoucherRepository
# - DatabaseSmartBinRepository
# - DatabaseAlertRepository
# - DatabaseReportRepository