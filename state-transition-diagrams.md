## Object 1: User Account

### Diagram

```mermaid
stateDiagram-v2
    [*] --> Registered : Submit registration form
    Registered --> Verified : Verify email [valid token]
    Verified --> Active : Login [correct credentials]
    Active --> Suspended : Failed login attempts [>=5]
    Suspended --> Verified : Admin reinstates account
    Active --> Deactivated : User deletes account
    Deactivated --> [*]
```

### Explanation

| Element | Description |
|---------|-------------|
| **States** | Registered, Verified, Active, Suspended, Deactivated |
| **Transitions** | Registration, email verification, login, suspension, account deletion |
| **Events** | Submit form, verify email, login attempt, admin action |
| **Guard Conditions** | Valid token required for verification; login only with correct credentials; suspension after ≥5 failed attempts |

### Traceability

**Functional Requirements (Assignment 4):**
- FR1 (User Registration) → Registered state
- FR2 (User Authentication) → Active state
- FR2 (Security) → Suspended state

**Use Cases (Assignment 5):**
- UC-001 (Register Account) → Registered → Verified
- UC-002 (Login/Authenticate) → Verified → Active

**User Stories (Assignment 6):**
- US-001 (Register account) → Registered → Verified
- US-002 (Login) → Verified → Active

**Sprint Tasks (Assignment 6):**
- T-001.1: Create database schema for users table
- T-001.2: Implement registration API endpoint
- T-001.3: Add email validation for university domain
- T-001.4: Implement email verification service
- T-001.5: Create registration UI screen
- T-001.6: Add form validation and error handling
- T-002.1: Implement login API endpoint with JWT
- T-002.2: Add password hashing verification
- T-002.3: Implement session management
- T-002.4: Create login UI screen
- T-002.5: Add rate limiting for failed attempts

## Object 2: Recycling Transaction

### Diagram

```mermaid
stateDiagram-v2
    [*] --> Pending : Scan bin QR code
    Pending --> Processing : Validate QR code [valid bin]
    Processing --> Completed : Award points [success]
    Processing --> Failed : Award points [item invalid OR bin full]
    Completed --> [*]
    Failed --> [*]
```

### Explanation

| Element | Description |
|---------|-------------|
| **States** | Pending, Processing, Completed, Failed |
| **Transitions** | Scan bin, validate QR, award points, transaction failure |
| **Events** | User scans QR code, system validates, system awards points |
| **Guard Conditions** | Valid bin required for processing; item type valid and bin not full for completion |

### Traceability

**Functional Requirements (Assignment 4):**
- FR3 (Point Awarding) → Completed state
- FR7 (Bin Fill-Level Monitoring) → Failed state when bin full

**Use Cases (Assignment 5):**
- UC-003 (Deposit Recyclable Item) → Pending → Processing → Completed

**User Stories (Assignment 6):**
- US-003 (Deposit item and earn points) → Pending → Processing → Completed

**Sprint Tasks (Assignment 6):**
- T-003.1: Create bin simulator script
- T-003.2: Implement QR code scanning in mobile app
- T-003.3: Create deposit API endpoint
- T-003.4: Implement points calculation logic
- T-003.5: Create transactions table and repository
- T-003.6: Add push notification service for points
- T-003.7: Create deposit confirmation UI

## Object 3: Reward

### Diagram

```mermaid
stateDiagram-v2
    [*] --> Draft : Admin creates reward
    Draft --> Available : Admin publishes reward
    Available --> Limited : Student redeems reward [inventory < 5]
    Limited --> OutOfStock : Student redeems reward [inventory = 0]
    Available --> Discontinued : Admin removes reward
    Limited --> Available : Admin restocks inventory
    OutOfStock --> Available : Admin restocks inventory
    Discontinued --> [*]
```

### Explanation

| Element | Description |
|---------|-------------|
| **States** | Draft, Available, Limited, OutOfStock, Discontinued |
| **Transitions** | Create, publish, redeem, restock, discontinue |
| **Events** | Admin action, student redemption, inventory update |
| **Guard Conditions** | Inventory < 5 triggers Limited; inventory = 0 triggers OutOfStock |

### Traceability

**Functional Requirements (Assignment 4):**
- FR5 (Reward Catalog) → Available state
- FR10 (Admin Reward Management) → Draft, Discontinued states

**Use Cases (Assignment 5):**
- UC-006 (View Reward Catalog) → Available and Limited states visible

**User Stories (Assignment 6):**
- US-006 (Browse available rewards) → Available, Limited states visible
- US-014 (Verify redemption vouchers) → Inventory decreases on redemption

**Sprint Tasks (Assignment 6):**
- T-006.1: Create rewards table and schema
- T-006.2: Implement rewards catalog API endpoint
- T-006.3: Create rewards catalog UI screen
- T-006.4: Add search and filter functionality
- T-007.5: Add email confirmation service
- T-007.6: Implement voucher verification endpoint
## Object 4: Redemption Voucher

### Diagram

```mermaid
stateDiagram-v2
    [*] --> Generated : Student redeems points
    Generated --> Emailed : System sends email
    Emailed --> Scanned : Dining services scans QR
    Scanned --> Verified : Validate QR [code valid]
    Scanned --> Invalid : Validate QR [code fake OR already used]
    Verified --> Redeemed : System marks as used
    Generated --> Expired : [30 days pass]
    Invalid --> [*]
    Redeemed --> [*]
    Expired --> [*]
```

### Explanation

| Element | Description |
|---------|-------------|
| **States** | Generated, Emailed, Scanned, Verified, Invalid, Redeemed, Expired |
| **Transitions** | Redeem points, send email, scan QR, validate, mark used, expire |
| **Events** | Student redeems, system emails, dining services scans, system validates |
| **Guard Conditions** | Valid QR code triggers Verified; fake or used QR triggers Invalid; 30 days triggers Expired |

### Traceability

**Functional Requirements (Assignment 4):**
- FR6 (Reward Redemption) → Generated, Emailed, Redeemed states
- FR14 (Verify Voucher) → Verified, Invalid states

**Use Cases (Assignment 5):**
- UC-005 (Redeem Reward) → Generated → Emailed → Redeemed

**User Stories (Assignment 6):**
- US-007 (Redeem points for rewards) → Generated → Emailed
- US-014 (Verify redemption vouchers) → Scanned → Verified/Invalid

**Sprint Tasks (Assignment 6):**
- T-007.1: Create redemption API endpoint
- T-007.2: Implement points deduction logic
- T-007.3: Generate unique QR code vouchers
- T-007.4: Create redemption confirmation UI
- T-007.5: Add email confirmation service
- T-007.6: Implement voucher verification endpoint

## Object 5: SmartBin

### Diagram

```mermaid
stateDiagram-v2
    [*] --> Operational : Bin deployed
    Operational --> Reporting : Send fill level update
    Reporting --> Operational : Fill level < 80%
    Reporting --> Warning : Fill level [>=80% AND <95%]
    Warning --> Critical : Fill level [>=95%]
    Warning --> Operational : Bin emptied
    Critical --> Operational : Bin emptied
    Operational --> Offline : No data [>1 hour]
    Offline --> Operational : Bin reconnects
    Operational --> Decommissioned : Bin removed
    Decommissioned --> [*]
```

### Explanation

| Element | Description |
|---------|-------------|
| **States** | Operational, Reporting, Warning, Critical, Offline, Decommissioned |
| **Transitions** | Deploy, send update, empty bin, lose connection, decommission |
| **Events** | Bin deployment, fill level sensor, staff empties bin, network timeout |
| **Guard Conditions** | Fill level ≥80% AND <95% triggers Warning; fill level ≥95% triggers Critical; no data for 1 hour triggers Offline |

### Traceability

**Functional Requirements (Assignment 4):**
- FR7 (Bin Fill-Level Monitoring) → Reporting state
- FR8 (Fill-Level Alerts) → Warning and Critical states

**Use Cases (Assignment 5):**
- UC-007 (Monitor Bin Fill Levels) → Reporting → Warning → Critical
- UC-008 (Receive Fill-Level Alerts) → Alerts triggered from Warning/Critical

**User Stories (Assignment 6):**
- US-009 (Monitor bin fill levels) → Reporting → Warning → Critical
- US-010 (Receive fill-level alerts) → Alerts triggered from Warning/Critical

**Sprint Tasks (Assignment 6):**
- T-003.1: Create bin simulator script
- T-009.1: Create bins table and schema
- T-009.2: Implement bin data API endpoint
- T-009.3: Create bin simulator fill level updates
- T-009.4: Create admin dashboard map view
- T-009.5: Add color-coded bin status indicators

## Object 6: Alert

### Diagram

```mermaid
stateDiagram-v2
    [*] --> Created : System detects fill level >=80%
    Created --> Sent : System sends notification
    Sent --> Acknowledged : Admin clicks Acknowledge [<2 hours]
    Sent --> Escalated : No acknowledgment [>=2 hours]
    Acknowledged --> Resolved : Bin emptied
    Escalated --> Acknowledged : Secondary admin acknowledges
    Resolved --> [*]
```

### Explanation

| Element | Description |
|---------|-------------|
| **States** | Created, Sent, Acknowledged, Escalated, Resolved |
| **Transitions** | Detect fill level, send notification, acknowledge, escalate, resolve |
| **Events** | System detects threshold, system sends alert, admin acknowledges, staff empties bin |
| **Guard Conditions** | Acknowledgment within 2 hours prevents escalation; no acknowledgment for 2 hours triggers Escalated |

### Traceability

**Functional Requirements (Assignment 4):**
- FR8 (Fill-Level Alerts) → Created, Sent, Escalated states
- FR7 (Bin Monitoring) → Resolved state

**Use Cases (Assignment 5):**
- UC-008 (Receive Fill-Level Alerts) → Created → Sent → Acknowledged/Escalated

**User Stories (Assignment 6):**
- US-010 (Receive fill-level alerts) → Created → Sent → Acknowledged/Escalated

**Sprint Tasks (Assignment 6):**
- T-009.2: Implement bin data API endpoint
- T-009.3: Create bin simulator fill level updates
- T-009.4: Create admin dashboard map view
- T-009.5: Add color-coded bin status indicators
## Object 7: Sustainability Report

### Diagram

```mermaid
stateDiagram-v2
    [*] --> Draft : Officer selects parameters
    Draft --> Generating : Officer clicks Generate
    Generating --> Generated : System queries database [success]
    Generating --> Failed : System queries database [error OR no data]
    Generated --> Downloaded : Officer downloads file
    Generated --> Emailed : Officer emails stakeholders
    Failed --> Draft : Officer retries
    Downloaded --> [*]
    Emailed --> [*]
```

### Explanation

| Element | Description |
|---------|-------------|
| **States** | Draft, Generating, Generated, Failed, Downloaded, Emailed |
| **Transitions** | Select parameters, generate, query database, download, email, retry |
| **Events** | Officer selects date range, system generates report, officer downloads or emails |
| **Guard Conditions** | Database error or no data triggers Failed; successful query triggers Generated |

### Traceability

**Functional Requirements (Assignment 4):**
- FR9 (Recycling Analytics Dashboard) → Draft, Generating, Generated states
- FR9 (Generate Reports) → Downloaded, Emailed states

**User Stories (Assignment 6):**
- US-011 (View recycling analytics) → Data feeds into report
- US-012 (Generate sustainability reports) → Draft → Generating → Generated → Downloaded/Emailed

**Sprint Tasks (Assignment 6):**
- T-003.5: Create transactions table and repository
- T-009.1: Create bins table and schema
- T-009.2: Implement bin data API endpoint

## Object 8: Reward Budget

### Diagram

```mermaid
stateDiagram-v2
    [*] --> Allocated : Finance sets monthly budget
    Allocated --> Spending : Student redeems reward
    Spending --> Depleted : Redeem reward [budget = 0]
    Spending --> Allocated : New month starts OR Finance adds funds
    Depleted --> Allocated : Finance adds funds
    Spending --> Frozen : Detect fraud [suspicious activity]
    Frozen --> Spending : Finance investigates and clears
    Depleted --> [*]
```

### Explanation

| Element | Description |
|---------|-------------|
| **States** | Allocated, Spending, Depleted, Frozen |
| **Transitions** | Set budget, redeem reward, deplete funds, add funds, freeze, unfreeze |
| **Events** | Finance sets budget, student redeems, system detects fraud, finance investigates |
| **Guard Conditions** | Budget = 0 triggers Depleted; suspicious activity triggers Frozen |

### Traceability

**Functional Requirements (Assignment 4):**
- FR13 (Manage reward budget) → Allocated, Spending, Depleted, Frozen states
- NFR-SEC1 (Security) → Frozen state for fraud detection

**User Stories (Assignment 6):**
- US-013 (Manage reward budget) → Allocated → Spending → Depleted
- US-015 (Data encryption) → Security monitoring triggers Frozen

**Sprint Tasks (Assignment 6):**
- T-007.2: Implement points deduction logic
- T-007.6: Implement voucher verification endpoint
- T-009.2: Implement bin data API endpoint

