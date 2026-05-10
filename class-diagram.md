# Class Diagram - SmartBin System (Updated with Repository Pattern)

## Overview

This document contains the UML class diagram for the SmartBin system including the domain classes (Assignment 9) and the new repository layer (Assignment 11).

---

## Class Diagram

```mermaid
classDiagram
    %% ==================== DOMAIN CLASSES (Assignment 9) ====================
    
    class User {
        -_user_id: str
        -_email: str
        -_name: str
        -_role: Enum
        -_points_balance: int
        -_lifetime_points: int
        -_status: Enum
        -_created_at: Date
        -_last_login_at: Date
        -_failed_attempts: int
        +get_user_id(): str
        +get_email(): str
        +get_name(): str
        +get_role(): Enum
        +get_points_balance(): int
        +get_lifetime_points(): int
        +get_status(): Enum
        +register(email, name, password): bool
        +verify_email(token): bool
        +login(email, password): str
        +update_points(points): void
        +suspend(): void
    }

    class Transaction {
        -_transaction_id: str
        -_user_id: str
        -_bin_id: str
        -_item_type: Enum
        -_points_earned: int
        -_timestamp: Date
        -_status: Enum
        +get_transaction_id(): str
        +get_user_id(): str
        +get_bin_id(): str
        +get_item_type(): Enum
        +get_points_earned(): int
        +get_status(): Enum
        +create_transaction(user_id, bin_id, item_type): Transaction
        +calculate_points(item_type): int
        +award_points(user): bool
        +fail_transaction(reason): void
    }

    class Reward {
        -_reward_id: str
        -_name: str
        -_description: str
        -_point_cost: int
        -_image_url: str
        -_inventory_count: int
        -_status: Enum
        -_created_at: Date
        +get_reward_id(): str
        +get_name(): str
        +get_description(): str
        +get_point_cost(): int
        +get_inventory_count(): int
        +get_status(): Enum
        +set_description(description): Reward
        +set_image_url(url): Reward
        +publish(): void
        +redeem(user): Voucher
        +restock(quantity): void
        +discontinue(): void
    }

    class Voucher {
        -_voucher_id: str
        -_user_id: str
        -_reward_id: str
        -_qr_code: str
        -_status: Enum
        -_generated_at: Date
        -_expires_at: Date
        -_redeemed_at: Date
        +get_voucher_id(): str
        +get_user_id(): str
        +get_reward_id(): str
        +get_qr_code(): str
        +get_status(): Enum
        +get_expires_at(): Date
        +generate_voucher(user_id, reward_id): Voucher
        +send_email(): bool
        +scan_qr_code(code): bool
        +verify_voucher(): bool
        +mark_as_redeemed(): void
        +check_expiry(): bool
    }

    class SmartBin {
        -_bin_id: str
        -_location: str
        -_fill_level: int
        -_status: Enum
        -_last_updated_at: Date
        -_total_deposits: int
        +get_bin_id(): str
        +get_location(): str
        +get_fill_level(): int
        +get_status(): Enum
        +get_total_deposits(): int
        +update_fill_level(level): void
        +check_capacity(): bool
        +empty_bin(): void
        +get_status_color(): str
        +decommission(): void
        +add_deposit(): void
    }

    class Alert {
        -_alert_id: str
        -_bin_id: str
        -_fill_level: int
        -_severity: Enum
        -_status: Enum
        -_created_at: Date
        -_acknowledged_at: Date
        -_acknowledged_by: str
        +get_alert_id(): str
        +get_bin_id(): str
        +get_severity(): Enum
        +get_status(): Enum
        +create_alert(bin_id, fill_level): Alert
        +send_notification(): void
        +acknowledge(admin_id): void
        +escalate(): void
        +resolve(): void
    }

    class Report {
        -_report_id: str
        -_report_type: Enum
        -_date_range_start: Date
        -_date_range_end: Date
        -_data: JSON
        -_status: Enum
        -_generated_at: Date
        -_generated_by: str
        +get_report_id(): str
        +get_status(): Enum
        +select_parameters(start_date, end_date): void
        +generate_report(): JSON
        +export_to_csv(): str
        +export_to_pdf(): str
        +send_email(stakeholder_email): bool
    }

    %% ==================== DOMAIN RELATIONSHIPS ====================
    
    User "1" --> "0..*" Transaction : makes
    User "1" --> "0..*" Voucher : redeems
    Transaction "*" --> "1" SmartBin : occurs at
    Voucher "*" --> "1" Reward : for
    Alert "*" --> "1" SmartBin : monitors

    %% ==================== REPOSITORY LAYER (Assignment 11) ====================
    
    class Repository {
        <<interface>>
        +save(entity: T): void
        +findById(id: ID): Optional~T~
        +findAll(): List~T~
        +delete(id: ID): void
        +existsById(id: ID): bool
    }

    class UserRepository {
        <<interface>>
        +findByEmail(email: str): Optional~User~
        +findByRole(role: str): List~User~
        +updatePoints(userId: str, points: int): void
    }

    class TransactionRepository {
        <<interface>>
        +findByUserId(userId: str): List~Transaction~
        +findByBinId(binId: str): List~Transaction~
        +findByItemType(itemType: Enum): List~Transaction~
        +findByDateRange(start, end): List~Transaction~
        +getTotalPointsByUser(userId: str): int
    }

    class RewardRepository {
        <<interface>>
        +findByStatus(status: str): List~Reward~
        +findAvailableRewards(): List~Reward~
        +updateInventory(rewardId: str, quantity: int): void
    }

    class VoucherRepository {
        <<interface>>
        +findByUserId(userId: str): List~Voucher~
        +findByStatus(status: str): List~Voucher~
        +findValidVouchers(): List~Voucher~
    }

    class SmartBinRepository {
        <<interface>>
        +findByLocation(location: str): Optional~SmartBin~
        +findBinsByStatus(status: str): List~SmartBin~
        +findBinsNeedingEmptying(threshold: int): List~SmartBin~
        +updateFillLevel(binId: str, fillLevel: int): void
    }

    class AlertRepository {
        <<interface>>
        +findByBinId(binId: str): List~Alert~
        +findUnacknowledgedAlerts(): List~Alert~
        +findBySeverity(severity: str): List~Alert~
    }

    class ReportRepository {
        <<interface>>
        +findByGeneratedBy(userId: str): List~Report~
        +findByDateRange(start, end): List~Report~
    }

    class InMemoryUserRepository {
        -_storage: Dict~str, User~
        +save(entity: User): void
        +findById(id: str): Optional~User~
        +findAll(): List~User~
        +delete(id: str): void
        +existsById(id: str): bool
        +findByEmail(email: str): Optional~User~
        +findByRole(role: str): List~User~
        +updatePoints(userId: str, points: int): void
    }

    class RepositoryFactory {
        +getUserRepository(storageType: str): UserRepository
        +getTransactionRepository(storageType: str): TransactionRepository
        +getRewardRepository(storageType: str): RewardRepository
        +getVoucherRepository(storageType: str): VoucherRepository
        +getSmartBinRepository(storageType: str): SmartBinRepository
        +getAlertRepository(storageType: str): AlertRepository
        +getReportRepository(storageType: str): ReportRepository
    }

    %% ==================== REPOSITORY RELATIONSHIPS ====================
    
    UserRepository --|> Repository : extends
    TransactionRepository --|> Repository : extends
    RewardRepository --|> Repository : extends
    VoucherRepository --|> Repository : extends
    SmartBinRepository --|> Repository : extends
    AlertRepository --|> Repository : extends
    ReportRepository --|> Repository : extends

    InMemoryUserRepository ..|> UserRepository : implements
    RepositoryFactory ..> UserRepository : creates
    InMemoryUserRepository --> User : stores
