```markdown
# Use Case Specifications: SmartBin System

## Use Case 1: Register Account

| Field | Detail |
|-------|--------|
| **Use Case ID** | UC-001 |
| **Use Case Name** | Register Account |
| **Actors** | Student |
| **Description** | A new student creates an account to start earning points for recycling. |
| **Preconditions** | Student has a valid university email address. |
| **Postconditions** | Student account is created and stored in the database. Verification email is sent. |

### Basic Flow
1. Student opens the mobile app.
2. Student clicks "Register" button.
3. System displays registration form.
4. Student enters full name, university email, and password.
5. Student confirms password.
6. Student clicks "Submit".
7. System validates email is from university domain (@university.edu).
8. System checks email is not already registered.
9. System creates user account with initial points balance of 0.
10. System sends verification email with unique link.
11. System displays success message: "Verification email sent. Please check your inbox."

### Alternative Flows
| Flow | Condition | Action |
|------|-----------|--------|
| A1 | Invalid email domain | System displays error: "Please use your university email address." |
| A2 | Email already exists | System displays error: "Account already exists. Please login." |
| A3 | Password doesn't meet requirements | System displays requirements (min 8 chars, 1 number, 1 special). |
| A4 | Password confirmation doesn't match | System displays error: "Passwords do not match." |

---

## Use Case 2: Login / Authenticate

| Field | Detail |
|-------|--------|
| **Use Case ID** | UC-002 |
| **Use Case Name** | Login / Authenticate |
| **Actors** | Student |
| **Description** | Student authenticates to access their account and perform actions. |
| **Preconditions** | Student has registered account. |
| **Postconditions** | Student is logged in and session is created. |

### Basic Flow (Email/Password)
1. Student opens the mobile app.
2. System displays login screen.
3. Student enters email and password.
4. Student clicks "Login".
5. System validates credentials against database.
6. System creates authenticated session with JWT token.
7. System redirects to home screen with user's point balance.

### Basic Flow (QR Code Scan)
1. Student opens mobile app camera.
2. Student scans bin QR code.
3. System identifies bin and prompts for authentication.
4. Student scans student ID card QR code.
5. System validates student ID against database.
6. System creates authenticated session and proceeds to deposit flow.

### Alternative Flows
| Flow | Condition | Action |
|------|-----------|--------|
| A1 | Invalid credentials | System displays error: "Email or password incorrect." |
| A2 | Account not verified | System displays error: "Please verify your email before logging in." |
| A3 | Too many failed attempts | System locks account for 15 minutes after 5 failed attempts. |
| A4 | Invalid student ID card | System displays error: "Invalid ID. Please use email login." |

---

## Use Case 3: Deposit Recyclable Item

| Field | Detail |
|-------|--------|
| **Use Case ID** | UC-003 |
| **Use Case Name** | Deposit Recyclable Item |
| **Actors** | Student |
| **Description** | Student scans a bin QR code, selects item type, and receives points for recycling. |
| **Preconditions** | Student is authenticated (logged in). Bin has capacity available. |
| **Postconditions** | Student's points balance increases. Transaction is recorded. Bin fill level increases. |

### Basic Flow
1. Student approaches a SmartBin.
2. Student scans the bin's QR code using the mobile app.
3. System authenticates the student (via UC-002).
4. System displays item type selection screen (Plastic Bottle, Aluminum Can, Glass, Paper).
5. Student selects the item type they are depositing.
6. System calculates points based on item type (Plastic: 10, Can: 8, Glass: 12, Paper: 5).
7. System awards points to student's account.
8. System records transaction with timestamp, item type, and points.
9. System updates bin fill level (increases by 2% for each deposit).
10. System displays success message: "You earned 10 points! New balance: X points."
11. System sends push notification confirming deposit.

### Alternative Flows
| Flow | Condition | Action |
|------|-----------|--------|
| A1 | Bin is full (95%+) | System displays error: "This bin is full. Please use another bin." |
| A2 | Invalid QR code | System displays error: "Invalid bin. Please scan again." |
| A3 | Network timeout | System retries up to 3 times; displays error if fails. |
| A4 | Item type selection cancelled | Use case ends with no points awarded. |

---

## Use Case 4: View Points Balance

| Field | Detail |
|-------|--------|
| **Use Case ID** | UC-004 |
| **Use Case Name** | View Points Balance |
| **Actors** | Student |
| **Description** | Student checks current point total and lifetime points earned. |
| **Preconditions** | Student is authenticated. |
| **Postconditions** | Student views current balance; no system state change. |

### Basic Flow
1. Student opens the mobile app.
2. Home screen displays current point balance.
3. Student clicks "Points" tab for detailed view.
4. System displays:
   - Current points available
   - Lifetime points earned
   - Points needed for next reward tier
   - Recent transactions summary
5. Student reviews information.

### Alternative Flows
| Flow | Condition | Action |
|------|-----------|--------|
| A1 | Offline mode | System displays cached balance with note: "Last updated [time]" |
| A2 | Zero balance | System displays message: "Start recycling to earn points!" |

---

## Use Case 5: Redeem Reward

| Field | Detail |
|-------|--------|
| **Use Case ID** | UC-005 |
| **Use Case Name** | Redeem Reward |
| **Actors** | Student |
| **Description** | Student exchanges accumulated points for a reward voucher. |
| **Preconditions** | Student is authenticated. Student has sufficient points. Reward is available. |
| **Postconditions** | Student's points are deducted. Reward voucher (QR code) is generated. Transaction is recorded. |

### Basic Flow
1. Student opens the mobile app.
2. Student clicks "Rewards" tab.
3. System displays reward catalog (via UC-006).
4. Student selects a reward.
5. System displays reward details and point cost.
6. Student clicks "Redeem".
7. System checks student has sufficient points.
8. System deducts points from student's balance.
9. System generates unique QR code voucher.
10. System records redemption transaction.
11. System displays voucher with QR code and expiration date.
12. System sends confirmation email with voucher details.

### Alternative Flows
| Flow | Condition | Action |
|------|-----------|--------|
| A1 | Insufficient points | System displays: "You need X more points to redeem this reward." |
| A2 | Reward out of stock | System displays: "This reward is currently unavailable." |
| A3 | Redemption cancelled | Student cancels before confirmation; points not deducted. |
| A4 | Duplicate redemption attempt | System prevents using same QR code twice. |

---

## Use Case 6: View Reward Catalog

| Field | Detail |
|-------|--------|
| **Use Case ID** | UC-006 |
| **Use Case Name** | View Reward Catalog |
| **Actors** | Student |
| **Description** | Student browses available rewards to see options for redemption. |
| **Preconditions** | Student is authenticated. |
| **Postconditions** | Student views reward catalog; no system state change. |

### Basic Flow
1. Student opens the mobile app.
2. Student clicks "Rewards" tab.
3. System fetches available rewards from database.
4. System displays catalog with:
   - Reward name and image
   - Point cost
   - Brief description
   - Availability status (in stock, limited, out of stock)
5. Student can search by name or filter by point range.
6. Student clicks on a reward to view full details.

### Alternative Flows
| Flow | Condition | Action |
|------|-----------|--------|
| A1 | No rewards available | System displays: "No rewards available at this time." |
| A2 | Search returns no results | System displays: "No rewards match your search." |

---

## Use Case 7: Monitor Bin Fill Levels

| Field | Detail |
|-------|--------|
| **Use Case ID** | UC-007 |
| **Use Case Name** | Monitor Bin Fill Levels |
| **Actors** | Facilities Admin, IT Administrator |
| **Description** | Admin views real-time fill levels of all bins on campus. |
| **Preconditions** | Admin is authenticated with admin privileges. |
| **Postconditions** | Admin sees current bin status; no system state change. |

### Basic Flow
1. Admin logs into web admin panel.
2. Admin clicks "Bin Monitoring" dashboard.
3. System displays map view with all bin locations.
4. System shows each bin with:
   - Bin ID and location name
   - Current fill percentage
   - Color indicator (green <60%, yellow 60-80%, red >80%)
   - Last updated timestamp
5. Admin clicks on individual bin for detailed view.
6. System displays fill history chart for that bin.
7. Admin reviews information.

### Alternative Flows
| Flow | Condition | Action |
|------|-----------|--------|
| A1 | Bin offline | System marks bin as "Offline" with last known data. |
| A2 | Filter by location | Admin selects campus area to filter bins. |

---

## Use Case 8: Receive Fill-Level Alerts

| Field | Detail |
|-------|--------|
| **Use Case ID** | UC-008 |
| **Use Case Name** | Receive Fill-Level Alerts |
| **Actors** | Facilities Admin |
| **Description** | System proactively notifies admin when bins reach critical fill levels. |
| **Preconditions** | Admin has notification preferences configured. Bins are reporting data. |
| **Postconditions** | Admin is notified. System logs the alert. |

### Basic Flow
1. Bin simulator reports fill level of 85% (critical).
2. System detects fill level exceeds 80% threshold.
3. System creates alert with bin ID, location, fill level.
4. System sends push notification to Facilities Admin mobile app.
5. System sends email with alert details.
6. Admin acknowledges alert in the app.
7. System marks alert as "Acknowledged" and records acknowledgment time.
8. System updates alert status to "In Progress".

### Alternative Flows
| Flow | Condition | Action |
|------|-----------|--------|
| A1 | Alert not acknowledged within 2 hours | System escalates to secondary admin contact. |
| A2 | Fill level reaches 95% | System sends urgent alert with higher priority. |
| A3 | Multiple bins alert simultaneously | System groups alerts by location and priority. |
