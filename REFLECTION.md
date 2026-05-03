# Reflection: Balancing Stakeholder Needs in the SmartBin System

## Introduction
This document reflects on the challenges encountered while eliciting and balancing requirements from diverse stakeholders for the SmartBin Campus Sustainability Rewards System.

## Key Challenges Identified

### 1. Student Engagement vs. IT Security
**The Conflict:** Students want frictionless, instant access - ideally just tap their phone and recycle. IT administrators need strong authentication, audit trails, and fraud prevention.

**How I Balanced It:** 
- Implemented QR code scanning for quick bin access (students happy)
- But required initial registration with university email (IT happy)
- Added session timeouts and rate limiting (security maintained)
- Compromise: Authentication takes 3 seconds instead of instant, but re-authentication only needed every 30 minutes

### 2. Real-Time Updates vs. System Performance
**The Conflict:** Students and admins want immediate point awards and fill-level updates. This creates high database load and potential performance issues.

**How I Balanced It:**
- Points awarded immediately (satisfies students)
- But leaderboard updates daily instead of real-time (reduces database load)
- Bin fill levels update on each event, but alerts only at thresholds
- Used message queue to handle spikes without crashing

### 3. Reward Availability vs. Budget Control
**The Conflict:** Students want unlimited, exciting rewards. Finance office needs strict budget control and fraud prevention.

**How I Balanced It:**
- Digital vouchers with QR codes (prevents screenshot fraud)
- Inventory tracking for limited rewards (prevents over-redemption)
- Monthly spending reports for finance (budget visibility)
- Compromise: Some rewards have quantity limits, but popular ones are restocked regularly

### 4. Feature Richness vs. Maintainability
**The Conflict:** Sustainability officer wants every possible data point and report. Developer (me) needs manageable code that can be built in one semester.

**How I Balanced It:**
- Focused on core reporting first (daily/weekly totals)
- Added export functionality for custom reporting (officer can manipulate data)
- Designed modular code so reports can be added later
- Compromise: Some advanced analytics deferred to future versions

### 5. Mobile-First vs. Admin Desktop Needs
**The Conflict:** Students primarily use mobile phones; admins need detailed dashboards best viewed on desktop.

**How I Balanced It:**
- Mobile app optimized for scanning and quick actions
- Web admin panel with larger screens for data analysis
- Shared backend so both benefit from same data
- Responsive design so admin panel works on mobile in emergencies

## Lessons Learned

1. **Early stakeholder identification saves rework** - Talking to all stakeholder types upfront prevents major changes later
2. **Trade-offs are inevitable** - No system can satisfy everyone completely
3. **Traceability matters** - Linking requirements back to stakeholder concerns justifies decisions
4. **Agile helps** - The ability to adjust as requirements change is essential
5. **Specificity prevents misunderstanding** - "Fast" vs. "300ms" makes all the difference

## Conclusion
Balancing stakeholder needs in the SmartBin system required constant negotiation and prioritization. The final requirements document represents a realistic compromise that delivers value to all stakeholders while remaining feasible for a one-person development effort over one semester.
