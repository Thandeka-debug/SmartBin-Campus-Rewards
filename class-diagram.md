# Class Diagram - Assignment 9

## Overview

This document contains the UML class diagram for the SmartBin system using Mermaid.js syntax. The diagram includes 7 classes with their attributes, methods, relationships, and multiplicities.

---

## Class Diagram

```mermaid
classDiagram
    class User {
        - userId: String
        - email: String
        - passwordHash: String
        - name: String
        - role: Enum
        - pointsBalance: Integer
        - lifetimePoints: Integer
        - status: Enum
        - createdAt: Date
        - lastLoginAt: Date
        + register(email, name, password): Boolean
        + verifyEmail(token): Boolean
        + login(email, password): String
        + updatePoints(points): Void
        + suspend(): Void
        + getTransactionHistory(): List~Transaction~
    }

    class Transaction {
        - transactionId: String
        - userId: String
        - binId: String
        - itemType: Enum
        - pointsEarned: Integer
        - timestamp: Date
        - status: Enum
        + createTransaction(userId, binId, itemType): Transaction
        + calculatePoints(itemType): Integer
        + awardPoints(): Boolean
        + failTransaction(reason): Void
    }

    class Reward {
        - rewardId: String
        - name: String
        - description: String
        - pointCost: Integer
        - imageUrl: String
        - inventoryCount: Integer
        - status: Enum
        - createdAt: Date
        + createReward(name, cost, inventory): Reward
        + publishReward(): Void
        + redeemReward(userId): Voucher
        + restockInventory(quantity): Void
        + discontinueReward(): Void
    }

    class Voucher {
        - voucherId: String
        - userId: String
        - rewardId: String
        - qrCode: String
        - status: Enum
        - generatedAt: Date
        - expiresAt: Date
        - redeemedAt: Date
        + generateVoucher(userId, rewardId): Voucher
        + sendEmail(): Boolean
        + scanQRCode(code): Boolean
        + verifyVoucher(): Boolean
        + markAsRedeemed(): Void
        + checkExpiry(): Boolean
    }

    class SmartBin {
        - binId: String
        - location: String
        - fillLevel: Integer
        - status: Enum
        - lastUpdatedAt: Date
        - totalDeposits: Integer
        + updateFillLevel(level): Void
        + checkCapacity(): Boolean
        + emptyBin(): Void
        + getStatusColor(): String
        + decommissionBin(): Void
    }

    class Alert {
        - alertId: String
        - binId: String
        - fillLevel: Integer
        - severity: Enum
        - status: Enum
        - createdAt: Date
        - acknowledgedAt: Date
        - acknowledgedBy: String
        + createAlert(binId, fillLevel): Alert
        + sendNotification(): Void
        + acknowledgeAlert(adminId): Void
        + escalateAlert(): Void
        + resolveAlert(): Void
    }

    class Report {
        - reportId: String
        - reportType: Enum
        - dateRangeStart: Date
        - dateRangeEnd: Date
        - data: JSON
        - status: Enum
        - generatedAt: Date
        - generatedBy: String
        + selectParameters(type, startDate, endDate): Void
        + generateReport(): JSON
        + exportToCSV(): File
        + exportToPDF(): File
        + sendEmail(stakeholder): Boolean
    }

    User "1" --> "0..*" Transaction : makes
    User "1" --> "0..*" Voucher : redeems
    User "1" --> "0..*" Alert : acknowledges
    User "1" --> "0..*" Report : generates
    Transaction "*" --> "1" SmartBin : occurs at
    Voucher "*" --> "1" Reward : for
    Alert "*" --> "1" SmartBin : monitors
```

## Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| **No inheritance hierarchy** | The 7 entities have distinct behaviors and don't share enough common attributes to justify inheritance. |
| **User role as Enum** | Fixed set of roles (STUDENT, ADMIN, OFFICER, FINANCE, DINING) with distinct permissions. |
| **Transaction references userId and binId** | Uses string references instead of direct object references to avoid circular dependencies. |
| **Voucher has expiry logic** | `checkExpiry()` method encapsulates business rule that vouchers expire after 30 days. |
| **Alert has escalation logic** | `escalateAlert()` method implements business rule that unacknowledged alerts escalate after 2 hours. |

## Relationship Summary

| Relationship Type | Between Classes | Multiplicity |
|------------------|-----------------|--------------|
| Association | User → Transaction | 1 → 0..* |
| Association | User → Voucher | 1 → 0..* |
| Association | User → Alert | 1 → 0..* |
| Association | User → Report | 1 → 0..* |
| Association | Transaction → SmartBin | * ← 1 |
| Association | Voucher → Reward | * ← 1 |
| Association | Alert → SmartBin | * ← 1 |

## Multiplicity Key

| Symbol | Meaning |
|--------|---------|
| 1 | Exactly one |
| 0..1 | Zero or one |
| 0..* | Zero or more |
| 1..* | One or more |
| * | Many (zero or more) |

## Alignment with Previous Assignments

| Assignment | Alignment |
|------------|-----------|
| Assignment 4 (Functional Requirements) | Business rules map to FR1-FR14 |
| Assignment 5 (Use Cases) | Methods map to UC-001 through UC-008 |
| Assignment 6 (User Stories) | Classes support US-001 through US-015 |
| Assignment 8 (State Diagrams) | Status enums match state diagrams for each object |

## Notes

1. `List~Transaction~` is used instead of `List<Transaction>` because angle brackets cause parsing errors in Mermaid.
2. Enum types are represented in the diagram as attributes with "Enum" type.
3. ID references (`userId`, `binId`, `rewardId`) are used instead of object references to avoid circular dependencies.
