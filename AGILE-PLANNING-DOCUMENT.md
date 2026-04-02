# Agile Planning Document: SmartBin System

## 1. Overview
This document compiles all Agile planning artifacts for the SmartBin system, including user stories, product backlog, sprint plan, and reflection. All artifacts maintain traceability to Assignments 3, 4, and 5.

---

## 2. User Stories

| Story ID | User Story | Acceptance Criteria | Priority | Source |
|----------|------------|---------------------|----------|--------|
| US-001 | As a **student**, I want to **register for an account using my university email** so that **I can start earning points for recycling**. | - Registration form accepts @university.edu email<br>- Verification email sent within 60 seconds<br>- Duplicate emails rejected with error message | High | FR1, UC-001 |
| US-002 | As a **student**, I want to **log in to my account** so that **I can access my points and redeem rewards**. | - Login with valid credentials succeeds in <3 seconds<br>- Failed attempts limited to 5 before lockout<br>- Session expires after 30 minutes | High | FR2, UC-002 |
| US-003 | As a **student**, I want to **scan a bin QR code and deposit an item** so that **I earn points for recycling**. | - QR code scan authenticates user<br>- Points awarded immediately (10/8/12/5 points)<br>- Push notification sent on success | High | FR3, UC-003 |
| US-004 | As a **student**, I want to **view my current point balance** so that **I know how many points I have**. | - Balance displays on home screen<br>- Updates in real-time<br>- Shows lifetime points earned | High | FR4, UC-004 |
| US-005 | As a **student**, I want to **view my transaction history** so that **I can track my points**. | - Shows last 50 transactions<br>- Filter by date range<br>- Export as CSV | Medium | FR4, UC-004 |
| US-006 | As a **student**, I want to **browse available rewards** so that **I can see what I can redeem**. | - Catalog shows name, point cost, image<br>- Search by name<br>- Shows availability status | High | FR5, UC-006 |
| US-007 | As a **student**, I want to **redeem my points for rewards** so that **I get benefits from recycling**. | - Points deducted immediately<br>- QR code voucher generated<br>- Insufficient points shows error | High | FR6, UC-005 |
| US-008 | As a **student**, I want to **view the leaderboard** so that **I can see my rank**. | - Shows top 20 users<br>- User sees own rank<br>- Updates daily | Medium | FR12 |
| US-009 | As a **facilities admin**, I want to **monitor bin fill levels** so that **I can schedule collections**. | - Map view with all bins<br>- Color indicator (green/yellow/red)<br>- Shows last updated timestamp | High | FR7, UC-007 |
| US-010 | As a **facilities admin**, I want to **receive alerts when bins are full** so that **I can prevent overflow**. | - Alert at 80% (warning) and 95% (critical)<br>- Push and email notifications<br>- Escalation if not acknowledged in 2 hours | High | FR8, UC-008 |
| US-011 | As a **sustainability officer**, I want to **view recycling analytics** so that **I can track performance**. | - Dashboard shows daily/weekly/monthly totals<br>- Breakdown by location and item type<br>- Environmental impact metrics | Medium | FR9 |
| US-012 | As a **sustainability officer**, I want to **generate sustainability reports** so that **I can share data with leadership**. | - Select date range and report type<br>- Export as PDF or CSV<br>- Includes participation rates | Medium | FR9 |
| US-013 | As a **finance officer**, I want to **manage the reward budget** so that **I can control program costs**. | - Monthly cost reports<br>- Fraud detection alerts<br>- Track redemptions by department | Medium | FR10 |
| US-014 | As a **dining services manager**, I want to **verify redemption vouchers** so that **I can prevent fraud**. | - Scan QR code validates voucher<br>- Shows redemption status<br>- Prevents duplicate redemptions | High | FR6 |
| US-015 | As a **system admin**, I want to **ensure user data is encrypted** so that **security compliance is met**. | - Passwords hashed with bcrypt<br>- Data encrypted at rest with AES-256<br>- TLS 1.3 for all traffic | High | NFR-SEC1 |
| US-016 | As a **system admin**, I want the **system to handle 1,000 concurrent users** so that **performance remains stable**. | - Load testing shows <5% error rate<br>- 95% of requests complete in <300ms<br>- 10,000 transactions/hour | Medium | NFR-S1 |

---

## 3. Product Backlog (Prioritized with MoSCoW)

### Prioritization Key
| Priority | Meaning | Justification |
|----------|---------|---------------|
| **Must-have** | Critical for MVP; system cannot function without | Core user journeys |
| **Should-have** | Important but can be delivered after MVP | Enhances experience |
| **Could-have** | Nice to have; delivered if time permits | Adds polish |

### Backlog Table

| Story ID | User Story | MoSCoW Priority | Story Points | Dependencies |
|----------|------------|-----------------|--------------|--------------|
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

### MoSCoW Summary
| Category | Count | Percentage |
|----------|-------|------------|
| Must-have | 8 | 50% |
| Should-have | 5 | 31% |
| Could-have | 3 | 19% |
| **Total** | **16** | **100%** |

### Story Point Guide
| Points | Meaning | Examples |
|--------|---------|----------|
| 1 | Simple, few lines of code | US-004 (display balance) |
| 2 | Straightforward with minor complexity | US-002 (authentication) |
| 3 | Moderate complexity, multiple components | US-001 (registration) |
| 5 | Complex, multiple integrations | US-003 (deposit + points) |
| 8 | Highly complex, significant effort | US-016 (scalability) |

---

## 4. Sprint Plan (2-Week Sprint)

### Sprint Overview
| Field | Detail |
|-------|--------|
| **Sprint Duration** | 2 weeks (10 working days) |
| **Sprint Goal** | Implement core recycling functionality: account creation, authentication, point earning, and reward redemption for students, with basic bin monitoring for admins. |

### Selected User Stories
| Story ID | User Story | MoSCoW Priority | Story Points |
|----------|------------|-----------------|--------------|
| US-001 | Register for account | Must-have | 3 |
| US-002 | Log in to account | Must-have | 2 |
| US-003 | Deposit item and earn points | Must-have | 5 |
| US-004 | View point balance | Must-have | 1 |
| US-006 | Browse available rewards | Must-have | 3 |
| US-007 | Redeem points for rewards | Must-have | 5 |
| US-009 | Monitor bin fill levels | Must-have | 5 |

**Total Story Points:** 24

### Task Breakdown

**US-001: Register for Account (3 points)**
- T-001.1: Create database schema for users table
- T-001.2: Implement registration API endpoint
- T-001.3: Add email validation for university domain
- T-001.4: Implement email verification service
- T-001.5: Create registration UI screen
- T-001.6: Add form validation and error handling

**US-002: Log in to Account (2 points)**
- T-002.1: Implement login API endpoint with JWT
- T-002.2: Add password hashing verification
- T-002.3: Implement session management
- T-002.4: Create login UI screen
- T-002.5: Add rate limiting for failed attempts

**US-003: Deposit Item and Earn Points (5 points)**
- T-003.1: Create bin simulator script
- T-003.2: Implement QR code scanning in mobile app
- T-003.3: Create deposit API endpoint
- T-003.4: Implement points calculation logic
- T-003.5: Create transactions table and repository
- T-003.6: Add push notification service for points
- T-003.7: Create deposit confirmation UI

**US-004: View Point Balance (1 point)**
- T-004.1: Create points balance API endpoint
- T-004.2: Display balance on home screen
- T-004.3: Add real-time balance update

**US-006: Browse Available Rewards (3 points)**
- T-006.1: Create rewards table and schema
- T-006.2: Implement rewards catalog API endpoint
- T-006.3: Create rewards catalog UI screen
- T-006.4: Add search and filter functionality

**US-007: Redeem Points for Rewards (5 points)**
- T-007.1: Create redemption API endpoint
- T-007.2: Implement points deduction logic
- T-007.3: Generate unique QR code vouchers
- T-007.4: Create redemption confirmation UI
- T-007.5: Add email confirmation service
- T-007.6: Implement voucher verification endpoint

**US-009: Monitor Bin Fill Levels (5 points)**
- T-009.1: Create bins table and schema
- T-009.2: Implement bin data API endpoint
- T-009.3: Create bin simulator fill level updates
- T-009.4: Create admin dashboard map view
- T-009.5: Add color-coded bin status indicators

### Sprint Timeline
| Week | Day | Focus |
|------|-----|-------|
| **Week 1** | Day 1-2 | Database setup, US-001 (Registration) |
| | Day 3-4 | US-002 (Login) |
| | Day 5-6 | US-004 (Point Balance), US-006 (Reward Catalog) |
| **Week 2** | Day 7-8 | US-003 (Deposit Item) |
| | Day 9-10 | US-007 (Redemption), US-009 (Bin Monitoring) |
| | Day 11-12 | Integration testing, bug fixes, sprint review |

### Definition of Done
- [ ] All acceptance criteria are met
- [ ] Code is reviewed and merged
- [ ] Unit tests pass with >80% coverage
- [ ] No critical bugs remain
- [ ] Documentation updated
- [ ] Deployed to staging environment

---

## 5. Reflection: Challenges in Agile Planning

### Challenge 1: Balancing Must-have Stories with Time Constraints

**The Issue:** When prioritizing the product backlog using MoSCoW, I initially marked 12 stories as "Must-have." However, with a 2-week sprint capacity of approximately 24 story points, I had to reduce the Must-have list to 8 stories totaling 24 points.

**How I Addressed It:** I reviewed each story against the stakeholder success metrics from Assignment 4. Stories that directly enabled core user journeys (registration, login, deposit, redeem) remained Must-have. Stories like "View transaction history" and "Leaderboard" were moved to Should-have because they enhance experience but don't block the core functionality.

**Lesson Learned:** The Product Owner must constantly balance stakeholder desires with development capacity. Just because something is important doesn't mean it must be in the first sprint.

---

### Challenge 2: Estimating Story Points Accurately

**The Issue:** Assigning story points using the Fibonacci sequence (1, 2, 3, 5, 8) was difficult because I had to consider complexity, not just time. For example, US-003 (Deposit item and earn points) required QR code scanning, points calculation, transaction recording, push notifications, and bin simulator integration.

**How I Addressed It:** I set US-004 (View point balance) as a 1-point baseline because it's a simple database read. I then estimated other stories relative to this baseline. Stories with external integrations (like push notifications) received higher estimates.

**Lesson Learned:** Story points should measure relative complexity, not absolute time. Having a baseline story helps calibrate estimates across the backlog.

---

### Challenge 3: Breaking Stories into Small, Testable Tasks

**The Issue:** When breaking US-003 (Deposit item) into tasks, I initially created 3 large tasks. This made tracking progress difficult because a task could take 3-4 days with no visibility into completion.

**How I Addressed It:** I broke each story into smaller tasks that could be completed in 2-4 hours. For US-003, I created 7 tasks: database schema, QR scanning, API endpoint, points logic, transaction table, push notifications, and UI.

**Lesson Learned:** Tasks should be small enough that "in progress" doesn't last more than a day. This improves visibility and reduces risk.

---

### Challenge 4: Aligning Agile with Previous Assignments

**The Issue:** Assignments 3-5 were structured for traditional requirements engineering (specifications, C4 diagrams, use cases). Translating this into Agile user stories required mental shifts. The C4 architecture defined components, but user stories needed to focus on user value, not technical components.

**How I Addressed It:** I mapped each user story back to a functional requirement from Assignment 4 and a use case from Assignment 5. This traceability matrix helped me ensure no critical functionality was missed while maintaining an Agile focus on user value.

**Lesson Learned:** Agile doesn't mean abandoning documentation. Traceability between traditional requirements and user stories helps maintain consistency.

---

### Challenge 5: Defining the Sprint Goal

**The Issue:** I had to define a sprint goal that was ambitious but achievable. Initially, I wanted to include analytics stories (US-011, US-012) in the first sprint, but this would have added 10 story points beyond capacity.

**How I Addressed It:** I focused on the "core recycling loop" - register → login → deposit → view points → redeem. This delivers end-to-end value to students. Admin features were limited to bin monitoring (US-009) because it directly impacts facilities staff's ability to prevent overflow.

**Lesson Learned:** Sprint goals should be outcome-focused, not feature-focused. "Implement core recycling functionality" is better than "Complete 7 stories" because it focuses on user value.

---

### Challenge 6: Balancing Technical and User-Centric Stories

**The Issue:** US-015 (data encryption) and US-016 (scalability) are important for security and performance, but they don't deliver visible value to students. I initially considered moving them to later sprints, but security cannot be an afterthought.

**How I Addressed It:** I kept US-015 in Must-have with low story points (2). I moved US-016 to Should-have with high story points (8) because scalability testing requires infrastructure setup that can happen after initial functionality is stable.

**Lesson Learned:** Non-functional requirements must be addressed early, but they can be prioritized alongside functional stories. Security cannot be deferred; scalability can be if traffic is initially low.

---

### Challenge 7: Playing Multiple Scrum Roles

**The Issue:** As a single person, I played Product Owner (prioritizing backlog), Scrum Master (facilitating process), and Developer (estimating and task breakdown). This made it difficult to separate stakeholder advocacy from development realism.

**How I Addressed It:** I mentally separated the roles. As Product Owner, I prioritized based on stakeholder value. As Developer, I provided honest estimates and pushed back when the backlog exceeded capacity. This internal negotiation helped me find a balanced sprint plan.

**Lesson Learned:** Even in solo development, separating roles mentally helps maintain objectivity. The Product Owner wants everything; the Developer must say what's realistic.

---

## 6. Traceability to Prior Assignments

| Assignment | Artifact | How Used |
|------------|----------|----------|
| Assignment 3 | System Specification, C4 Architecture | Provided system scope and component boundaries |
| Assignment 4 | Functional Requirements (FR1-FR12) | Direct source for user stories US-001 to US-012 |
| Assignment 4 | Non-Functional Requirements | Source for US-015 (security) and US-016 (scalability) |
| Assignment 5 | Use Cases (UC-001 to UC-008) | Provided interaction flows for user stories |
| Assignment 5 | Test Cases | Used to define acceptance criteria |

---

## 7. GitHub Agile Tools Implementation

| GitHub Tool | Purpose | Link |
|-------------|---------|------|
| **Issues** | Individual user stories with acceptance criteria | [View Issues](https://github.com/Thandeka-debug/SmartBin-Campus-Rewards/issues) |
| **Milestones** | Sprint 1 tracking | [View Milestones](https://github.com/Thandeka-debug/SmartBin-Campus-Rewards/milestones) |
| **Project Board** | Kanban board for sprint progress | [View Project Board](https://github.com/Thandeka-debug/SmartBin-Campus-Rewards/projects/1) |
| **Labels** | Prioritization (MoSCoW) and story type | priority-high, must-have, user-story, etc. |

---

## 8. Agile Manifesto Alignment

| Agile Manifesto Value | Application in SmartBin |
|-----------------------|-------------------------|
| Individuals and interactions over processes and tools | User stories written from stakeholder perspectives |
| Working software over comprehensive documentation | Sprint focuses on delivering functional MVP |
| Customer collaboration over contract negotiation | Prioritization based on stakeholder success metrics |
| Responding to change over following a plan | MoSCoW allows reprioritization as needs evolve |

---


