import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from creational_patterns.singleton import DatabaseConnection
import threading


def test_singleton():
    print("\n=== Testing Singleton Pattern ===")
    
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    
    assert db1 is db2
    print("✓ Both instances refer to the same object")
    
    db1.connect()
    assert db1.is_connected == True
    assert db2.is_connected == True
    print("✓ Connection state is shared")
    
    db1.execute_query("SELECT * FROM users")
    db2.execute_query("SELECT * FROM transactions")
    
    assert db1.get_query_count() == 2
    assert db2.get_query_count() == 2
    print("✓ Query count is shared")
    
    print("✅ Singleton Pattern test passed!\n")


def test_singleton_thread_safety():
    print("=== Testing Singleton Thread Safety ===")
    
    db1 = DatabaseConnection()
    
    def get_instance():
        instance = DatabaseConnection()
        assert instance is db1
    
    threads = []
    for i in range(10):
        t = threading.Thread(target=get_instance)
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    print("✓ Thread safety verified (10 threads all got same instance)")
    print("✅ Singleton Thread Safety test passed!\n")


if __name__ == "__main__":
    test_singleton()
    test_singleton_thread_safety()