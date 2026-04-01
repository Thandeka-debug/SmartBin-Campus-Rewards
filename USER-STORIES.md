# User Stories: SmartBin System

## Overview
This document contains user stories derived from functional requirements (Assignment 4) and use cases (Assignment 5). Each user story is tracked as a GitHub Issue. Links to issues are provided below.

## User Stories

| Story ID | User Story | Acceptance Criteria | Priority | GitHub Issue |
|----------|------------|---------------------|----------|--------------|
| US-001 | As a **student**, I want to **register for an account using my university email** so that **I can start earning points for recycling**. | - Registration form accepts @university.edu email<br>- Verification email sent within 60 seconds<br>- Duplicate emails rejected with error message | High | [Issue #1](https://github.com/Thandeka-debug/SmartBin-Campus-Rewards/issues/1) |
| US-002 | As a **student**, I want to **log in to my account** so that **I can access my points and redeem rewards**. | - Login with valid credentials succeeds in <3 seconds<br>- Failed attempts limited to 5 before lockout<br>- Session expires after 30 minutes | High | [Issue #2](https://github.com/Thandeka-debug/SmartBin-Campus-Rewards/issues/2) |
| US-003 | As a **student**, I want to **scan a bin QR code and deposit an item** so that **I earn points for recycling**. | - QR code scan authenticates user<br>- Points awarded immediately (10/8/12/5 points)<br>- Push notification sent on success | High | [Issue #3](https://github.com/Thandeka-debug/SmartBin-Campus-Rewards/issues/3) |
| US-004 | As a **student**, I want to **view my current point balance** so that **I know how many points I have**. | - Balance displays on home screen<br>- Updates in real-time<br>- Shows lifetime points earned | High | [Issue #4](https://github.com/Thandeka-debug/SmartBin-Campus-Rewards/issues/4) |
| US-005 | As a **student**, I want to **view my transaction history** so that **I can track my points**. | - Shows last 50 transactions<br>- Filter by date range<br>- Export as CSV | Medium | [Issue #5](https://github.com/Thandeka-debug/SmartBin-Campus-Rewards/issues/5) |
| US-006 | As a **student**, I want to **browse available rewards** so that **I can see what I can redeem**. | - Catalog shows name, point cost, image<br>- Search by name<br>- Shows availability status | High | [Issue #6](https://github.com/Thandeka-debug/SmartBin-Campus-Rewards/issues/6) |
| US-007 | As a **student**, I want to **redeem my points for rewards** so that **I get benefits from recycling**. | - Points deducted immediately<br>- QR code voucher generated<br>- Insufficient points shows error | High | [Issue #7](https://github.com/Thandeka-debug/SmartBin-Campus-Rewards/issues/7) |
| US-008 | As a **student**, I want to **view the leaderboard** so that **I can see my rank**. | - Shows top 20 users<br>- User sees own rank<br>- Updates daily | Medium | [Issue #8](https://github.com/Thandeka-debug/SmartBin-Campus-Rewards/issues/8) |
| US-009 | As a **facilities admin**, I want to **monitor bin fill levels** so that **I can schedule collections**. | - Map view with all bins<br>- Color indicator (green/yellow/red)<br>- Shows last updated timestamp | High | [Issue #9](https://github.com/Thandeka-debug/SmartBin-Campus-Rewards/issues/9) |
| US-010 | As a **facilities admin**, I want to **receive alerts when bins are full** so that **I can prevent overflow**. | - Alert at 80% (warning) and 95% (critical)<br>- Push and email notifications<br>- Escalation if not acknowledged in 2 hours | High | [Issue #10](https://github.com/Thandeka-debug/SmartBin-Campus-Rewards/issues/10) |
| US-011 | As a **sustainability officer**, I want to **view recycling analytics** so that **I can track performance**. | - Dashboard shows daily/weekly/monthly totals<br>- Breakdown by location and item type<br>- Environmental impact metrics | Medium | [Issue #11](https://github.com/Thandeka-debug/SmartBin-Campus-Rewards/issues/11) |
| US-012 | As a **sustainability officer**, I want to **generate sustainability reports** so that **I can share data with leadership**. | - Select date range and report type<br>- Export as PDF or CSV<br>- Includes participation rates | Medium | [Issue #12](https://github.com/Thandeka-debug/SmartBin-Campus-Rewards/issues/12) |
| US-013 | As a **finance officer**, I want to **manage the reward budget** so that **I can control program costs**. | - Monthly cost reports<br>- Fraud detection alerts<br>- Track redemptions by department | Medium | [Issue #13](https://github.com/Thandeka-debug/SmartBin-Campus-Rewards/issues/13) |
| US-014 | As a **dining services manager**, I want to **verify redemption vouchers** so that **I can prevent fraud**. | - Scan QR code validates voucher<br>- Shows redemption status<br>- Prevents duplicate redemptions | High | [Issue #14](https://github.com/Thandeka-debug/SmartBin-Campus-Rewards/issues/14) |
| US-015 | As a **system admin**, I want to **ensure user data is encrypted** so that **security compliance is met**. | - Passwords hashed with bcrypt<br>- Data encrypted at rest with AES-256<br>- TLS 1.3 for all traffic | High | [Issue #15](https://github.com/Thandeka-debug/SmartBin-Campus-Rewards/issues/15) |
| US-016 | As a **system admin**, I want the **system to handle 1,000 concurrent users** so that **performance remains stable**. | - Load testing shows <5% error rate<br>- 95% of requests complete in <300ms<br>- 10,000 transactions/hour | Medium | [Issue #16](https://github.com/Thandeka-debug/SmartBin-Campus-Rewards/issues/16) |

## Story Source Traceability

| Source | Required | Provided |
|--------|----------|----------|
| Functional Requirements (Assignment 4) | 8+ | 12 (US-001 to US-012) |
| Use Cases (Assignment 5) | 4+ | 4 (US-003, US-005, US-007, US-009) |
| **Total** | **12+** | **16** |

## INVEST Criteria Validation

| Criteria | How Addressed |
|----------|---------------|
| **Independent** | Stories can be developed in any order; minimal dependencies |
| **Negotiable** | Acceptance criteria clear but implementation details flexible |
| **Valuable** | Each story delivers value to a specific stakeholder |
| **Estimable** | Story points assigned based on complexity |
| **Small** | Each story can be completed within a single sprint |
| **Testable** | Acceptance criteria provide clear pass/fail conditions |
