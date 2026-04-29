"""
Singleton Pattern - Ensure one instance globally
"""

import threading


class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(DatabaseConnection, cls).__new__(cls)
                    cls._instance._initialize()
        return cls._instance
    
    def _initialize(self):
        self.connection_string = "postgresql://localhost:5432/smartbin"
        self.is_connected = False
        self.query_count = 0
        print("DatabaseConnection initialized (Singleton)")
    
    def connect(self) -> bool:
        if not self.is_connected:
            self.is_connected = True
            print(f"Connected to database at {self.connection_string}")
        return self.is_connected
    
    def disconnect(self) -> None:
        if self.is_connected:
            self.is_connected = False
            print("Disconnected from database")
    
    def execute_query(self, query: str) -> list:
        if not self.is_connected:
            self.connect()
        self.query_count += 1
        print(f"Executing query #{self.query_count}: {query[:50]}...")
        return []
    
    def get_query_count(self) -> int:
        return self.query_count


if __name__ == "__main__":
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    
    print(f"db1 is db2: {db1 is db2}")
    
    db1.connect()
    db1.execute_query("SELECT * FROM users")
    db2.execute_query("SELECT * FROM transactions")
    
    print(f"Total queries executed: {db1.get_query_count()}")
    print("Singleton Pattern test passed!")
