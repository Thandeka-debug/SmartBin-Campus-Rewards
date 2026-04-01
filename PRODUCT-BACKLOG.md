# Product Backlog: SmartBin System

## Overview
This document contains the prioritized product backlog using MoSCoW prioritization. Story points use Fibonacci sequence (1, 2, 3, 5, 8).

## Prioritization Key

| Priority | Meaning | Justification |
|----------|---------|---------------|
| **Must-have** | Critical for MVP; system cannot function without | Core user journeys (registration, login, deposit, redeem) |
| **Should-have** | Important but can be delivered after MVP | Enhances experience but not blocking functionality |
| **Could-have** | Nice to have; delivered if time permits | Adds polish and additional value |
| **Won't-have** | Out of scope for current release | Deferred to future versions |

## Product Backlog

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
| US-010 | Receive fill-level alerts | Should-have | 3 | US-009 |
| US-014 | Verify redemption vouchers | Should-have | 3 | US-007 |
| US-005 | View transaction history | Should-have | 3 | US-004 |
| US-013 | Manage reward budget | Should-have | 3 | US-007 |
| US-016 | Handle 1,000 concurrent users | Should-have | 8 | US-002, US-003 |
| US-008 | View leaderboard | Could-have | 3 | US-004 |
| US-011 | View recycling analytics | Could-have | 5 | US-003, US-009 |
| US-012 | Generate sustainability reports | Could-have | 5 | US-011 |

## MoSCoW Summary

| Category | Count | Percentage |
|----------|-------|------------|
| Must-have | 8 | 50% |
| Should-have | 5 | 31% |
| Could-have | 3 | 19% |
| **Total** | **16** | **100%** |

## Story Point Guide

| Points | Meaning | Examples |
|--------|---------|----------|
| 1 | Simple, few lines of code | US-004 (display balance from database) |
| 2 | Straightforward with minor complexity | US-002 (authentication with JWT) |
| 3 | Moderate complexity, multiple components | US-001 (registration with email validation) |
| 5 | Complex, multiple integrations | US-003 (bin simulator + points + transaction) |
| 8 | Highly complex, significant effort | US-016 (scalability testing and optimization) |

## Prioritization Justification

| Story ID | Stakeholder | Success Metric from Assignment 4 | Why Must-have |
|----------|-------------|----------------------------------|---------------|
| US-001, US-002 | Student | "50% increase in recycling participation" | Requires easy account access |
| US-003 | Student | Core recycling action | Enables point earning |
| US-004, US-006, US-007 | Student | "Average user checks points 2x per week" | Requires visibility and redemption |
| US-009 | Facilities Admin | "80% reduction in overflow incidents" | Requires real-time monitoring |
| US-015 | IT Admin, Finance | "Zero security breaches" | Encryption foundation required |
