# System Requirements Document: SmartBin

## 1. Functional Requirements

### FR1: User Registration
**Description:** The system shall allow students to register for an account using their university email address.
**Rationale:** Students need a unique identity to track their points and redemptions.
**Acceptance Criteria:**
- Registration form accepts valid university email (@university.edu)
- Password must meet security requirements (min 8 chars, 1 number, 1 special)
- Verification email is sent within 60 seconds
- Duplicate email addresses are rejected with clear error message

### FR2: User Authentication
**Description:** The system shall authenticate users via email/password or campus ID card scan.
**Rationale:** Students need secure access to their accounts; QR scan provides quick bin access.
**Acceptance Criteria:**
- Login with valid credentials succeeds in < 3 seconds
- Failed login attempts are limited to 5 before temporary lockout
- QR code scan auto-authenticates user
- Session expires after 30 minutes of inactivity

### FR3: Point Awarding
**Description:** The system shall award points to students when they deposit recyclable items.
**Rationale:** Core gamification mechanic that incentivizes recycling behavior.
**Acceptance Criteria:**
- Points awarded immediately upon deposit confirmation
- Point values vary by item type (plastic bottle: 10 pts, can: 8 pts, paper: 5 pts)
- User receives push notification when points are awarded
- Transaction appears in history within 5 seconds

### FR4: Point Balance Viewing
**Description:** The system shall display the user's current point balance and transaction history.
**Rationale:** Students need visibility into their earnings to stay motivated.
**Acceptance Criteria:**
- Balance updates in real-time after each transaction
- History shows last 50 transactions with date, type, points
- Filter by date range and transaction type
- Export history as CSV or PDF

### FR5: Reward Catalog
**Description:** The system shall maintain a catalog of rewards that students can redeem with their points.
**Rationale:** Provides incentive and redemption options for earned points.
**Acceptance Criteria:**
- Catalog displays reward name, point cost, description, image
- Search by reward name or point range
- Real-time availability status
- Admin can add/edit/remove rewards without code changes

### FR6: Reward Redemption
**Description:** The system shall allow students to redeem points for rewards.
**Rationale:** Completes the gamification loop; students get tangible benefits.
**Acceptance Criteria:**
- Redemption requires confirmation step
- Points deducted immediately upon redemption
- Generates unique QR code for voucher verification
- Insufficient points prevents redemption with clear message

### FR7: Bin Fill-Level Monitoring
**Description:** The system shall track and display fill levels for all smart bins on campus.
**Rationale:** Facilities admins need to know when bins need emptying.
**Acceptance Criteria:**
- Fill level updates when bin simulator sends data
- Visual indicator (green/yellow/red) for bin status
- History chart shows fill patterns over time
- Map view shows all bin locations with status

### FR8: Fill-Level Alerts
**Description:** The system shall send alerts when bins reach critical fill levels.
**Rationale:** Prevents overflow and enables proactive maintenance.
**Acceptance Criteria:**
- Alert triggers at 80% (warning) and 95% (critical)
- SMS/email/push notification to facilities staff
- Acknowledgment required to clear alert
- Escalation if not acknowledged within 2 hours

### FR9: Recycling Analytics Dashboard
**Description:** The system shall provide dashboards with recycling metrics and trends.
**Rationale:** Sustainability officer needs data for reporting and improvement.
**Acceptance Criteria:**
- Daily/weekly/monthly recycling totals
- Breakdown by bin location and item type
- Participation rate (unique users per day)
- Environmental impact (CO2 saved, trees saved)
- Export charts as PNG or data as CSV

### FR10: Admin Reward Management
**Description:** The system shall allow administrators to manage the reward catalog.
**Rationale:** Dining services and sustainability office need to update available rewards.
**Acceptance Criteria:**
- Add new reward with name, description, point cost, image
- Edit existing reward details
- Disable rewards (hide from catalog)
- Inventory tracking for limited quantity rewards

### FR11: Bin Simulator Control
**Description:** The system shall include a simulator interface for testing bin events.
**Rationale:** Developers need to test without physical bins; demo purposes.
**Acceptance Criteria:**
- Manual trigger for "item deposited" with item type selection
- Manual fill level adjustment (0-100%)
- Simulate multiple bins with different IDs
- Log all simulated events for debugging

### FR12: Leaderboard
**Description:** The system shall display a leaderboard of top recyclers.
**Rationale:** Gamification element that encourages competition and engagement.
**Acceptance Criteria:**
- Shows top 20 users by points this week/month/all-time
- Anonymous mode option for privacy
- User sees their own rank even if not in top 20
- Updates daily (not real-time to prevent gaming)

- ## 2. Non-Functional Requirements

### Usability

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| NFR-U1 | The mobile app shall be usable by students with no training. | New user can complete registration and first scan in < 3 minutes in usability testing. |
| NFR-U2 | The interface shall comply with WCAG 2.1 AA accessibility standards. | Pass automated accessibility testing (WAVE, Lighthouse). Screen reader compatible. |
| NFR-U3 | The system shall support both English and Spanish language interfaces. | Language toggle switches all UI text; 95%+ translation coverage. |
| NFR-U4 | Error messages shall be user-friendly and suggest solutions. | "Invalid login" becomes "Email or password incorrect. Reset password?" |

### Deployability

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| NFR-D1 | The system shall be deployable on Linux and Windows servers. | Backend runs on Ubuntu 20.04+ and Windows Server 2019+ without code changes. |
| NFR-D2 | Deployment shall use containerization (Docker) for consistency. | Dockerfile provided; container starts in < 30 seconds. |
| NFR-D3 | The system shall support cloud deployment (AWS/Azure/Google Cloud). | Deployment scripts work on EC2, Azure VMs, or Compute Engine. |
| NFR-D4 | Database migrations shall be automated and reversible. | Migration script runs on deploy; rollback available within 1 command. |

### Maintainability

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| NFR-M1 | API documentation shall be auto-generated and always up-to-date. | Swagger/OpenAPI spec available at `/api-docs`. All endpoints documented. |
| NFR-M2 | Source code shall have minimum 70% test coverage. | Coverage report shows >70% for backend; critical paths >90%. |
| NFR-M3 | Logging shall include appropriate detail levels (debug, info, error). | Logs include timestamp, severity, component, and correlation ID. |
| NFR-M4 | Code comments shall explain "why" not "what" for complex logic. | Peer review confirms complex sections have explanatory comments. |

### Scalability

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| NFR-S1 | The system shall support 1,000 concurrent users during peak hours. | Load testing with 1,000 concurrent users shows < 5% error rate. |
| NFR-S2 | The database shall handle 10,000 transactions per hour. | Stress test maintains response times with 10K transactions/hour. |
| NFR-S3 | The system shall scale horizontally by adding application server instances. | Adding second server doubles throughput in load tests. |
| NFR-S4 | Static assets (images, CSS) shall be served via CDN for scalability. | Asset loading time < 500ms from any geographic region. |

### Security

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| NFR-SEC1 | All user data shall be encrypted at rest using AES-256. | Database encryption verified; backups also encrypted. |
| NFR-SEC2 | All network traffic shall be encrypted using TLS 1.3. | SSL Labs rating A+; no weak ciphers enabled. |
| NFR-SEC3 | Passwords shall be hashed using bcrypt with salt. | Password verification uses bcrypt; plaintext never stored. |
| NFR-SEC4 | The API shall implement rate limiting to prevent abuse. | 100 requests per minute per IP; returns 429 status when exceeded. |
| NFR-SEC5 | User sessions shall expire after 30 minutes of inactivity. | Session token invalid after 30 mins; user must re-authenticate. |

### Performance

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| NFR-P1 | API response time shall be < 300ms for 95% of requests. | Monitoring shows 95th percentile response time under 300ms. |
| NFR-P2 | Point balance lookup shall complete in < 100ms. | Database indexed; query execution time under 50ms. |
| NFR-P3 | Search results shall load within 2 seconds. | Search across 10K+ rewards returns in < 2 seconds. |
| NFR-P4 | The system shall handle 100 simultaneous bin sensor reports per second. | Message queue processes 100 msgs/sec without backlog. |
| NFR-P5 | Mobile app cold start shall be < 3 seconds. | App launches to home screen in under 3 seconds on mid-range device. |

## Requirements Traceability Matrix

| Requirement ID | Description | Stakeholder(s) Addressed |
|----------------|-------------|--------------------------|
| FR1 | User Registration | Student, IT Admin |
| FR2 | User Authentication | Student, IT Admin |
| FR3 | Point Awarding | Student, Sustainability Officer |
| FR4 | Point Balance Viewing | Student |
| FR5 | Reward Catalog | Student, Dining Services |
| FR6 | Reward Redemption | Student, Finance Office |
| FR7 | Bin Fill-Level Monitoring | Facilities Admin |
| FR8 | Fill-Level Alerts | Facilities Admin |
| FR9 | Analytics Dashboard | Sustainability Officer, Marketing |
| FR10 | Admin Reward Management | Dining Services, Finance |
| FR11 | Bin Simulator Control | Developer |
| FR12 | Leaderboard | Student, Marketing |
