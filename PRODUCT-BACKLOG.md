# Product Backlog: SmartBin System

## Overview
This document contains the prioritized product backlog using MoSCoW prioritization. Story points use Fibonacci sequence (1, 2, 3, 5, 8).

## Prioritization Key

| Priority | Meaning | Justification |
|----------|---------|---------------|
| **Must-have** | Critical for MVP; system cannot function without | Core user journeys (registration, login, deposit, redeem) |
| **Should-have** | Important but can be delivered after MVP | Enhances experience but not blocking functionality |
| **Could-have** | Nice to have; delivered if time permits | Adds polish and additional value |
| **Won't-have** | Explicitly out of scope for current release | Deferred to future versions; documented to prevent scope creep |

## Product Backlog

### Must-have (MVP Critical)

| Story ID | User Story | Priority (MoSCoW) | Story Points | Dependencies |
|----------|------------|-------------------|--------------|--------------|
| US-001 | Register for account | Must-have | 3 | None |
| US-002 | Log in to account | Must-have | 2 | US-001 |
| US-003 | Deposit item and earn points | Must-have | 5 | US-002 |
| US-004 | View point balance | Must-have | 1 | US-002 |
| US-006 | Browse available rewards | Must-have | 3 | None |
| US-007 | Redeem points for rewards | Must-have | 5 | US-004, US-006 |
| US-009 | Monitor bin fill levels | Must-have | 5 | US-003 |
| US-015 | User data encryption | Must-have | 2 | None |

### Should-have (Important but not blocking MVP)

| Story ID | User Story | Priority (MoSCoW) | Story Points | Dependencies |
|----------|------------|-------------------|--------------|--------------|
| US-010 | Receive fill-level alerts | Should-have | 3 | US-009 |
| US-014 | Verify redemption vouchers | Should-have | 3 | US-007 |
| US-005 | View transaction history | Should-have | 3 | US-004 |
| US-013 | Manage reward budget | Should-have | 3 | US-007 |
| US-016 | Handle 1,000 concurrent users | Should-have | 8 | US-002, US-003 |

### Could-have (Nice to have, time permitting)

| Story ID | User Story | Priority (MoSCoW) | Story Points | Dependencies |
|----------|------------|-------------------|--------------|--------------|
| US-008 | View leaderboard | Could-have | 3 | US-004 |
| US-011 | View recycling analytics | Could-have | 5 | US-003, US-009 |
| US-012 | Generate sustainability reports | Could-have | 5 | US-011 |

### Won't-have (Explicitly out of scope for current release)

| Story ID | User Story | Priority (MoSCoW) | Reason for Won't-have |
|----------|------------|-------------------|----------------------|
| US-017 | As a student, I want to compete with friends in recycling challenges so that I can have friendly competition. | Won't-have | Requires social features, friend lists, and real-time notifications. Too complex for MVP. Deferred to future release. |
| US-018 | As a facilities admin, I want to generate predictive maintenance schedules so that I can fix bins before they break. | Won't-have | Requires machine learning model and historical data analysis. Out of scope for current semester. |
| US-019 | As a sustainability officer, I want to integrate with external carbon credit systems so that the university can earn carbon credits. | Won't-have | Requires third-party API integration, legal agreements, and carbon credit certification. Deferred to future release. |
| US-020 | As a student, I want to receive push notifications for double-points events so that I can earn more during promotions. | Won't-have | Requires event scheduling and promotional campaign management. Not critical for MVP. |

## MoSCoW Summary

| Category | Count | Percentage |
|----------|-------|------------|
| Must-have | 8 | 42% |
| Should-have | 5 | 26% |
| Could-have | 3 | 16% |
| Won't-have | 4 | 16% |
| **Total** | **20** | **100%** |

## Story Point Guide

| Points | Meaning | Examples |
|--------|---------|----------|
| 1 | Simple, few lines of code | US-004 (display balance from database) |
| 2 | Straightforward with minor complexity | US-002 (authentication with JWT) |
| 3 | Moderate complexity, multiple components | US-001 (registration with email validation) |
| 5 | Complex, multiple integrations | US-003 (bin simulator + points + transaction) |
| 8 | Highly complex, significant effort | US-016 (scalability testing and optimization) |

## Prioritization Justification

### Why Must-have Stories Are Prioritized

| Story ID | Stakeholder | Success Metric from Assignment 4 | Why Must-have |
|----------|-------------|----------------------------------|---------------|
| US-001, US-002 | Student | "50% increase in recycling participation" | Requires easy account access |
| US-003 | Student | Core recycling action | Enables point earning |
| US-004, US-006, US-007 | Student | "Average user checks points 2x per week" | Requires visibility and redemption |
| US-009 | Facilities Admin | "80% reduction in overflow incidents" | Requires real-time monitoring |
| US-015 | IT Admin, Finance | "Zero security breaches" | Encryption foundation required |

### Why Won't-have Stories Are Deferred

| Story ID | Reason for Deferral | When to Reconsider |
|----------|---------------------|---------------------|
| US-017 | Social features add significant complexity | After MVP is stable and user base grows |
| US-018 | Machine learning requires data collection first | After 6+ months of bin data is available |
| US-019 | Legal and third-party integration is time-consuming | After university approves partnership |
| US-020 | Promotional features are nice-to-have, not core | After core recycling loop is proven |

## Traceability to Prior Assignments

| Story ID | Assignment 4 Requirement | Assignment 5 Use Case |
|----------|-------------------------|----------------------|
| US-001 | FR1 - User Registration | UC-001 - Register Account |
| US-002 | FR2 - User Authentication | UC-002 - Login/Authenticate |
| US-003 | FR3 - Point Awarding | UC-003 - Deposit Item |
| US-004 | FR4 - Point Balance | UC-004 - View Points |
| US-005 | FR4 - Point Balance | UC-004 - View Points |
| US-006 | FR5 - Reward Catalog | UC-006 - View Catalog |
| US-007 | FR6 - Reward Redemption | UC-005 - Redeem Reward |
| US-008 | FR12 - Leaderboard | N/A |
| US-009 | FR7 - Bin Monitoring | UC-007 - Monitor Bins |
| US-010 | FR8 - Fill-Level Alerts | UC-008 - Receive Alerts |
| US-011 | FR9 - Analytics Dashboard | N/A |
| US-012 | FR9 - Analytics Dashboard | N/A |
| US-013 | FR10 - Admin Reward Management | N/A |
| US-014 | FR6 - Reward Redemption | N/A |
| US-015 | NFR-SEC1 - Encryption | N/A |
| US-016 | NFR-S1 - Scalability | N/A |
