# Sprint Plan: SmartBin System

## Sprint Overview

| Field | Detail |
|-------|--------|
| **Sprint Duration** | 2 weeks (10 working days) |
| **Sprint Goal** | Implement core recycling functionality: account creation, authentication, point earning, and reward redemption for students, with basic bin monitoring for admins. |

## Selected User Stories for Sprint

| Story ID | User Story | Priority (MoSCoW) | Story Points |
|----------|------------|-------------------|--------------|
| US-001 | Register for account | Must-have | 3 |
| US-002 | Log in to account | Must-have | 2 |
| US-003 | Deposit item and earn points | Must-have | 5 |
| US-004 | View point balance | Must-have | 1 |
| US-006 | Browse available rewards | Must-have | 3 |
| US-007 | Redeem points for rewards | Must-have | 5 |
| US-009 | Monitor bin fill levels | Must-have | 5 |

**Total Story Points:** 24

## Task Breakdown

### US-001: Register for Account (3 points)

| Task ID | Task Description |
|---------|------------------|
| T-001.1 | Create database schema for users table |
| T-001.2 | Implement registration API endpoint |
| T-001.3 | Add email validation for university domain |
| T-001.4 | Implement email verification service |
| T-001.5 | Create registration UI screen |
| T-001.6 | Add form validation and error handling |

### US-002: Log in to Account (2 points)

| Task ID | Task Description |
|---------|------------------|
| T-002.1 | Implement login API endpoint with JWT |
| T-002.2 | Add password hashing verification |
| T-002.3 | Implement session management |
| T-002.4 | Create login UI screen |
| T-002.5 | Add rate limiting for failed attempts |

### US-003: Deposit Item and Earn Points (5 points)

| Task ID | Task Description |
|---------|------------------|
| T-003.1 | Create bin simulator script |
| T-003.2 | Implement QR code scanning in mobile app |
| T-003.3 | Create deposit API endpoint |
| T-003.4 | Implement points calculation logic |
| T-003.5 | Create transactions table and repository |
| T-003.6 | Add push notification service for points |
| T-003.7 | Create deposit confirmation UI |

### US-004: View Point Balance (1 point)

| Task ID | Task Description |
|---------|------------------|
| T-004.1 | Create points balance API endpoint |
| T-004.2 | Display balance on home screen |
| T-004.3 | Add real-time balance update |

### US-006: Browse Available Rewards (3 points)

| Task ID | Task Description |
|---------|------------------|
| T-006.1 | Create rewards table and schema |
| T-006.2 | Implement rewards catalog API endpoint |
| T-006.3 | Create rewards catalog UI screen |
| T-006.4 | Add search and filter functionality |

### US-007: Redeem Points for Rewards (5 points)

| Task ID | Task Description |
|---------|------------------|
| T-007.1 | Create redemption API endpoint |
| T-007.2 | Implement points deduction logic |
| T-007.3 | Generate unique QR code vouchers |
| T-007.4 | Create redemption confirmation UI |
| T-007.5 | Add email confirmation service |
| T-007.6 | Implement voucher verification endpoint |

### US-009: Monitor Bin Fill Levels (5 points)

| Task ID | Task Description |
|---------|------------------|
| T-009.1 | Create bins table and schema |
| T-009.2 | Implement bin data API endpoint |
| T-009.3 | Create bin simulator fill level updates |
| T-009.4 | Create admin dashboard map view |
| T-009.5 | Add color-coded bin status indicators |

## Definition of Done

A user story is complete when:
- All acceptance criteria are met
- Code is reviewed and merged
- Unit tests pass with >80% coverage
- No critical bugs remain
- Documentation updated
- Deployed to staging environment

## Sprint Timeline

| Week | Day | Focus |
|------|-----|-------|
| **Week 1** | Day 1-2 | Database setup, US-001 (Registration) |
| | Day 3-4 | US-002 (Login) |
| | Day 5-6 | US-004 (Point Balance), US-006 (Reward Catalog) |
| **Week 2** | Day 7-8 | US-003 (Deposit Item) |
| | Day 9-10 | US-007 (Redemption), US-009 (Bin Monitoring) |
| | Day 11-12 | Integration testing, bug fixes, sprint review |
