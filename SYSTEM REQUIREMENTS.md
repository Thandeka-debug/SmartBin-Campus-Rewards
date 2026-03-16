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
