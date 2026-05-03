"""
Run all unit tests for SmartBin System
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from test_simple_factory import test_simple_factory
from test_factory_method import test_factory_method
from test_abstract_factory import test_abstract_factory
from test_builder import test_builder
from test_prototype import test_prototype
from test_singleton import test_singleton, test_singleton_thread_safety


def run_all_tests():
    print("=" * 60)
    print("RUNNING ALL SMARTBIN SYSTEM TESTS")
    print("=" * 60)
    
    test_simple_factory()
    test_factory_method()
    test_abstract_factory()
    test_builder()
    test_prototype()
    test_singleton()
    test_singleton_thread_safety()
    
    print("=" * 60)
    print("ALL TESTS PASSED! ✅")
    print("=" * 60)


if __name__ == "__main__":
    run_all_tests()