# Changelog - SmartBin System

## [1.0.0] - 2024-05-03

### Added - Assignment 10

#### Core Classes (/src directory)
- Added `User` class with registration, login, and points management
- Added `Transaction` class for recycling deposits and point calculation
- Added `Reward` class for catalog items with inventory management
- Added `Voucher` class for QR code generation and redemption
- Added `SmartBin` class with fill level monitoring and status tracking
- Added `Alert` class for threshold-based notifications
- Added `Report` class for sustainability analytics

#### Creational Patterns (/creational_patterns directory)
- Added **Simple Factory** (`UserFactory`) - Centralized user creation by role
- Added **Factory Method** (`NotificationFactory`) - Email, Push, SMS notification services
- Added **Abstract Factory** (`UIFactory`) - Mobile and Web UI component families
- Added **Builder** (`RewardBuilder`) - Step-by-step complex reward construction
- Added **Prototype** (`BinCache`) - SmartBin cloning with configuration preservation
- Added **Singleton** (`DatabaseConnection`) - Thread-safe database connection manager

#### Unit Tests (/tests directory)
- Added tests for Simple Factory pattern
- Added tests for Factory Method pattern
- Added tests for Abstract Factory pattern
- Added tests for Builder pattern
- Added tests for Prototype pattern
- Added tests for Singleton pattern (including thread safety)
- Added `run_all_tests.py` to execute all tests

### Test Results
- All 6 creational patterns tested and verified
- All tests passed successfully
- Singleton thread safety verified with 10 concurrent threads

### Commit History
- `31a96b9` - Complete Assignment 10: All 6 creational patterns implemented and tested
