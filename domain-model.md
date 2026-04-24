# Domain Model - Assignment 9

## Overview

This document describes the domain model for the SmartBin system. It identifies 7 key entities, their attributes, methods, relationships, and business rules.

---

## Entity 1: User

| Attribute | Type | Description |
|-----------|------|-------------|
| userId | String | Unique identifier for the user |
| email | String | University email address (@university.edu) |
| passwordHash | String | Encrypted password (bcrypt) |
| name | String | Full name of the user |
| role | Enum | [STUDENT, ADMIN, OFFICER, FINANCE, DINING] |
| pointsBalance | Integer | Current redeemable points |
| lifetimePoints | Integer | Total points earned over time |
| status | Enum | [REGISTERED, VERIFIED, ACTIVE, SUSPENDED, DEACTIVATED] |
| createdAt | Date | Account creation timestamp |
| lastLoginAt | Date | Last login timestamp |

| Method | Return Type | Description |
|--------|-------------|-------------|
| register(email, name, password) | Boolean | Creates new user account |
| verifyEmail(token) | Boolean | Verifies email with valid token |
| login(email, password) | String | Returns JWT session token |
| updatePoints(points) | Void | Adds or deducts points |
| suspend() | Void | Suspends account after 5 failed attempts |
| getTransactionHistory() | List<Transaction> | Returns all user transactions |

---

## Entity 2: Transaction

| Attribute | Type | Description |
|-----------|------|-------------|
| transactionId | String | Unique identifier |
| userId | String | Reference to User who deposited |
| binId | String | Reference to SmartBin used |
| itemType | Enum | [PLASTIC_BOTTLE, ALUMINUM_CAN, GLASS_BOTTLE, PAPER] |
| pointsEarned | Integer | Points awarded (10/8/12/5) |
| timestamp | Date | When transaction occurred |
| status | Enum | [PENDING, PROCESSING, COMPLETED, FAILED] |

| Method | Return Type | Description |
|--------|-------------|-------------|
| createTransaction(userId, binId, itemType) | Transaction | Creates new transaction record |
| calculatePoints(itemType) | Integer | Returns points based on item type |
| awardPoints() | Boolean | Adds points to user account |
| failTransaction(reason) | Void | Marks transaction as failed |

---

## Entity 3: Reward

| Attribute | Type | Description |
|-----------|------|-------------|
| rewardId | String | Unique identifier |
| name | String | Reward name (e.g., "Coffee Voucher") |
| description | String | Detailed description |
| pointCost | Integer | Points required to redeem |
| imageUrl | String | URL to reward image |
| inventoryCount | Integer | Number available (0 = out of stock) |
| status | Enum | [DRAFT, AVAILABLE, LIMITED, OUT_OF_STOCK, DISCONTINUED] |
| createdAt | Date | When reward was created |

| Method | Return Type | Description |
|--------|-------------|-------------|
| createReward(name, cost, inventory) | Reward | Admin creates new reward |
| publishReward() | Void | Moves from DRAFT to AVAILABLE |
| redeemReward(userId) | Voucher | Creates voucher and deducts points |
| restockInventory(quantity) | Void | Increases inventory count |
| discontinueReward() | Void | Marks reward as discontinued |

---

## Entity 4: Voucher

| Attribute | Type | Description |
|-----------|------|-------------|
| voucherId | String | Unique identifier |
| userId | String | Reference to User who redeemed |
| rewardId | String | Reference to Reward redeemed |
| qrCode | String | Unique QR code string |
| status | Enum | [GENERATED, EMAILED, SCANNED, VERIFIED, INVALID, REDEEMED, EXPIRED] |
| generatedAt | Date | When voucher was created |
| expiresAt | Date | 30 days after generation |
| redeemedAt | Date | When voucher was used |

| Method | Return Type | Description |
|--------|-------------|-------------|
| generateVoucher(userId, rewardId) | Voucher | Creates new voucher with QR code |
| sendEmail() | Boolean | Emails QR code to user |
| scanQRCode(code) | Boolean | Validates QR code when scanned |
| verifyVoucher() | Boolean | Checks if voucher is valid and not used |
| markAsRedeemed() | Void | Updates status to REDEEMED |
| checkExpiry() | Boolean | Returns true if 30 days passed |

---

## Entity 5: SmartBin

| Attribute | Type | Description |
|-----------|------|-------------|
| binId | String | Unique identifier |
| location | String | Campus location (e.g., "Library Ground Floor") |
| fillLevel | Integer | Percentage (0-100) |
| status | Enum | [OPERATIONAL, REPORTING, WARNING, CRITICAL, OFFLINE, DECOMMISSIONED] |
| lastUpdatedAt | Date | Last fill level update timestamp |
| totalDeposits | Integer | Count of deposits since deployment |

| Method | Return Type | Description |
|--------|-------------|-------------|
| updateFillLevel(level) | Void | Updates fill level and determines status |
| checkCapacity() | Boolean | Returns true if fill level < 95% |
| emptyBin() | Void | Resets fill level to 0% |
| getStatusColor() | String | Returns green/yellow/red based on fill level |
| decommissionBin() | Void | Marks bin as decommissioned |

---

## Entity 6: Alert

| Attribute | Type | Description |
|-----------|------|-------------|
| alertId | String | Unique identifier |
| binId | String | Reference to SmartBin |
| fillLevel | Integer | Fill level that triggered alert |
| severity | Enum | [WARNING, CRITICAL] |
| status | Enum | [CREATED, SENT, ACKNOWLEDGED, ESCALATED, RESOLVED] |
| createdAt | Date | When alert was created |
| acknowledgedAt | Date | When admin acknowledged |
| acknowledgedBy | String | Admin who acknowledged |

| Method | Return Type | Description |
|--------|-------------|-------------|
| createAlert(binId, fillLevel) | Alert | Creates new alert when threshold exceeded |
| sendNotification() | Void | Sends push and email notifications |
| acknowledgeAlert(adminId) | Void | Marks alert as acknowledged |
| escalateAlert() | Void | Escalates to secondary admin after 2 hours |
| resolveAlert() | Void | Marks alert as resolved after bin emptied |

---

## Entity 7: Report

| Attribute | Type | Description |
|-----------|------|-------------|
| reportId | String | Unique identifier |
| reportType | Enum | [RECYCLING_SUMMARY, PARTICIPATION_RATES, ENVIRONMENTAL_IMPACT] |
| dateRangeStart | Date | Start of reporting period |
| dateRangeEnd | Date | End of reporting period |
| data | JSON | Generated report data |
| status | Enum | [DRAFT, GENERATING, GENERATED, FAILED, DOWNLOADED, EMAILED] |
| generatedAt | Date | When report was generated |
| generatedBy | String | Officer who generated report |

| Method | Return Type | Description |
|--------|-------------|-------------|
| selectParameters(type, startDate, endDate) | Void | Officer selects report parameters |
| generateReport() | JSON | Queries database and generates data |
| exportToCSV() | File | Exports report as CSV |
| exportToPDF() | File | Exports report as PDF |
| sendEmail(stakeholder) | Boolean | Emails report to stakeholders |

---

## Entity Relationships

| From Entity | To Entity | Relationship | Multiplicity | Description |
|-------------|-----------|--------------|--------------|-------------|
| User | Transaction | Association | 1 → 0..* | A user can have many transactions |
| User | Voucher | Association | 1 → 0..* | A user can have many vouchers |
| User | Alert | Association | 1 → 0..* | An admin acknowledges many alerts |
| Transaction | SmartBin | Association | * ← 1 | Many transactions occur at one bin |
| Voucher | Reward | Association | * ← 1 | Many vouchers for one reward |
| Alert | SmartBin | Association | * ← 1 | Many alerts for one bin |
| Report | User | Association | * ← 1 | Many reports generated by one officer |

---

## Business Rules

| Rule ID | Business Rule | Source (Assignment 4) |
|---------|---------------|----------------------|
| BR-001 | A user must register with a valid university email address (@university.edu) | FR1 |
| BR-002 | Account is suspended after 5 failed login attempts | FR2 |
| BR-003 | Points are awarded based on item type: Plastic=10, Can=8, Glass=12, Paper=5 | FR3 |
| BR-004 | A bin can only accept deposits if fill level < 95% | FR7 |
| BR-005 | An alert is triggered when bin fill level reaches 80% (Warning) and 95% (Critical) | FR8 |
| BR-006 | A voucher expires 30 days after generation | FR6 |
| BR-007 | A voucher cannot be redeemed twice | FR14 |
| BR-008 | A reward can only be redeemed if inventory count > 0 | FR5 |
| BR-009 | Points cannot go negative when redeeming rewards | FR6 |
| BR-010 | An alert escalates if not acknowledged within 2 hours | FR8 |

---

## Traceability to Previous Assignments

| Entity | Assignment 8 State Object | Assignment 5 Use Cases | Assignment 6 User Stories |
|--------|--------------------------|------------------------|--------------------------|
| User | Object 1: User Account | UC-001, UC-002 | US-001, US-002 |
| Transaction | Object 2: Recycling Transaction | UC-003 | US-003 |
| Reward | Object 3: Reward | UC-006 | US-006 |
| Voucher | Object 4: Redemption Voucher | UC-005 | US-007, US-014 |
| SmartBin | Object 5: SmartBin | UC-007, UC-008 | US-009, US-010 |
| Alert | Object 6: Alert | UC-008 | US-010 |
| Report | Object 7: Sustainability Report | N/A | US-011, US-012 |
