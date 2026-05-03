# Test Cases: SmartBin System

## Functional Test Cases

| Test Case ID | Requirement ID | Description | Steps | Expected Result | Actual Result | Status |
|--------------|----------------|-------------|-------|-----------------|---------------|--------|
| TC-FR-001 | FR1 - User Registration | New user registration with valid university email | 1. Open app<br>2. Click Register<br>3. Enter: Thandeka Cacambile, 221350977@mycput.ac.za, Pass123!<br>4. Confirm password<br>5. Submit | Account created; verification email sent within 60 seconds | | |
| TC-FR-002 | FR1 - User Registration | Registration with invalid email domain | 1. Open app<br>2. Click Register<br>3. Enter: Thandeka Cacambile, thandekacacambile4@gmail.com, Pass123!<br>4. Submit | Error: "Please use your university email address" | | |
| TC-FR-003 | FR2 - User Authentication | Login with valid credentials | 1. Open app<br>2. Enter: 221350977@mycput.ac.za, Pass123!<br>3. Click Login | Login successful in <3 seconds; user sees home screen | | |
| TC-FR-004 | FR2 - User Authentication | Login with invalid password | 1. Open app<br>2. Enter: 221350977@mycput.ac.za, WrongPass<br>3. Click Login | Error: "Email or password incorrect" | | |
| TC-FR-005 | FR2 - User Authentication | 5 failed login attempts | 1. Attempt login with wrong password 5 times | Account locked for 15 minutes; error message displayed | | |
| TC-FR-006 | FR3 - Point Awarding | Deposit plastic bottle | 1. Scan bin QR<br>2. Select "Plastic Bottle"<br>3. Confirm deposit | 10 points awarded; transaction recorded; notification sent | | |
| TC-FR-007 | FR3 - Point Awarding | Deposit aluminum can | 1. Scan bin QR<br>2. Select "Aluminum Can"<br>3. Confirm deposit | 8 points awarded; transaction recorded; notification sent | | |
| TC-FR-008 | FR3 - Point Awarding | Deposit glass bottle | 1. Scan bin QR<br>2. Select "Glass Bottle"<br>3. Confirm deposit | 12 points awarded; transaction recorded; notification sent | | |
| TC-FR-009 | FR3 - Point Awarding | Deposit paper | 1. Scan bin QR<br>2. Select "Paper"<br>3. Confirm deposit | 5 points awarded; transaction recorded; notification sent | | |
| TC-FR-010 | FR4 - Point Balance | View current balance after deposits | 1. Student with 50 points logs in<br>2. Navigate to home screen | Balance displays "50 points" | | |
| TC-FR-011 | FR4 - Point Balance | View transaction history | 1. Student logs in<br>2. Click "History" tab | List of last 10 transactions with dates, types, points | | |
| TC-FR-012 | FR6 - Reward Redemption | Redeem reward with sufficient points | 1. Student with 100 points<br>2. Select reward costing 75 points<br>3. Click Redeem | 75 points deducted; QR code generated; transaction recorded | | |
| TC-FR-013 | FR6 - Reward Redemption | Redeem reward with insufficient points | 1. Student with 50 points<br>2. Select reward costing 75 points<br>3. Click Redeem | Error: "You need 25 more points to redeem this reward" | | |
| TC-FR-014 | FR8 - Fill-Level Alerts | Bin reaches 80% fill level | 1. Bin simulator sets fill level to 80%<br>2. System processes update | Alert sent to Facilities Admin (push + email) | | |
| TC-FR-015 | FR8 - Fill-Level Alerts | Bin reaches 95% fill level | 1. Bin simulator sets fill level to 95%<br>2. System processes update | Urgent alert sent; red indicator on dashboard | | |
| TC-FR-016 | FR12 - Leaderboard | View leaderboard | 1. Student logs in<br>2. Click "Leaderboard" tab | Top 20 users displayed with points; user's rank shown | | |

## Non-Functional Test Cases

| Test Case ID | NFR ID | Description | Test Setup | Expected Result | Actual Result | Status |
|--------------|--------|-------------|------------|-----------------|---------------|--------|
| TC-NFR-001 | NFR-P1 (Performance) | API response time under load | Simulate 100 concurrent users making 10 requests each (1,000 total requests) using load testing tool (e.g., JMeter, k6) | 95% of requests complete in <300ms; 0% error rate | | |
| TC-NFR-002 | NFR-P3 (Performance) | Search results load time | Execute search query across reward catalog with 5,000+ rewards | Results display within 2 seconds | | |
| TC-NFR-003 | NFR-P4 (Performance) | Bin event processing throughput | Simulate 100 bin sensors sending reports simultaneously to API | System processes all 100 events without queue backlog; all acknowledged | | |
| TC-NFR-004 | NFR-S1 (Scalability) | Concurrent user support | Ramp up users from 100 to 1,200 over 5 minutes; measure error rates | System maintains <5% error rate at 1,000 concurrent users | | |
| TC-NFR-005 | NFR-SEC1 (Security) | Data encryption at rest | Query database directly for user password fields | Passwords stored as bcrypt hash (not plaintext); no sensitive data unencrypted | | |
| TC-NFR-006 | NFR-SEC3 (Security) | Rate limiting enforcement | Send 150 API requests from same IP within 1 minute | Requests 101-150 return HTTP 429 (Too Many Requests) | | |
| TC-NFR-007 | NFR-SEC2 (Security) | TLS encryption verification | Use SSL Labs test tool to scan API endpoint | TLS 1.3 enforced; SSL Labs rating A or higher | | |
| TC-NFR-008 | NFR-U1 (Usability) | New user onboarding time | Give new user (no training) tasks: register, scan bin, deposit item | User completes all tasks in <3 minutes | | |
| TC-NFR-009 | NFR-U2 (Usability) | Accessibility compliance | Run WAVE accessibility tool on web admin panel | No critical accessibility errors; WCAG 2.1 AA compliant | | |
| TC-NFR-010 | NFR-M2 (Maintainability) | Test coverage verification | Run test coverage report | Backend code coverage >70%; critical paths >90% | | |

## Test Execution Summary

| Category | Total Tests | Passed | Failed | Pending |
|----------|-------------|--------|--------|---------|
| Functional Tests | 16 | | | |
| Non-Functional Tests | 10 | | | |
| **Total** | **26** | | | |

## Notes
- Actual Result and Status columns to be filled during testing phase
- Performance tests require dedicated test environment with monitoring tools
- Security tests should be conducted after deployment
