# Use Case Specifications: SmartBin System

---

## Use Case 1: Register Account

| Field              | Detail                                                                             |
| ------------------ | ---------------------------------------------------------------------------------- |
| **Use Case ID**    | UC-001                                                                             |
| **Use Case Name**  | Register Account                                                                   |
| **Actors**         | Student                                                                            |
| **Description**    | A new student creates an account to start earning points for recycling.            |
| **Preconditions**  | Student has a valid university email address.                                      |
| **Postconditions** | Student account is created and stored in the database. Verification email is sent. |

### Basic Flow

1. Student opens the mobile app.
2. Student clicks **Register**.
3. System displays registration form.
4. Student enters full name, university email, and password.
5. Student confirms password.
6. Student clicks **Submit**.
7. System validates email domain.
8. System checks email is not already registered.
9. System creates account with 0 points.
10. System sends verification email.
11. System displays success message.

### Alternative Flows

| Flow | Condition            | Action                                   |
| ---- | -------------------- | ---------------------------------------- |
| A1   | Invalid email domain | Display error: "Use university email."   |
| A2   | Email exists         | Display error: "Account already exists." |
| A3   | Weak password        | Display password requirements            |
| A4   | Password mismatch    | Display error                            |

---

## Use Case 2: Login / Authenticate

| Field              | Detail                                           |
| ------------------ | ------------------------------------------------ |
| **Use Case ID**    | UC-002                                           |
| **Use Case Name**  | Login / Authenticate                             |
| **Actors**         | Student                                          |
| **Description**    | Student logs into the system to access features. |
| **Preconditions**  | Registered account exists                        |
| **Postconditions** | User session created                             |

### Basic Flow (Email Login)

1. Open app
2. Enter email + password
3. Click **Login**
4. System validates credentials
5. Session created
6. Redirect to dashboard

### Basic Flow (QR Login)

1. Scan bin QR
2. Scan student ID
3. System validates identity
4. Session created

### Alternative Flows

| Flow | Condition         | Action              |
| ---- | ----------------- | ------------------- |
| A1   | Invalid login     | Show error          |
| A2   | Not verified      | Prompt verification |
| A3   | Too many attempts | Lock account        |
| A4   | Invalid ID        | Use email login     |

---

## Use Case 3: Deposit Recyclable Item

| Field              | Detail                                            |
| ------------------ | ------------------------------------------------- |
| **Use Case ID**    | UC-003                                            |
| **Actors**         | Student                                           |
| **Description**    | Student deposits recyclable item and earns points |
| **Preconditions**  | Logged in, bin available                          |
| **Postconditions** | Points updated, transaction saved                 |

### Basic Flow

1. Scan bin QR
2. System authenticates user
3. Select item type
4. System calculates points
5. Points added
6. Transaction recorded
7. Bin fill level updated
8. Confirmation shown

### Alternative Flows

| Flow | Condition     | Action      |
| ---- | ------------- | ----------- |
| A1   | Bin full      | Show error  |
| A2   | Invalid QR    | Retry       |
| A3   | Network issue | Retry       |
| A4   | Cancel        | End process |

---

## Use Case 4: View Points Balance

| Field              | Detail                        |
| ------------------ | ----------------------------- |
| **Use Case ID**    | UC-004                        |
| **Actors**         | Student                       |
| **Description**    | View current and total points |
| **Preconditions**  | Logged in                     |
| **Postconditions** | No change                     |

### Basic Flow

1. Open app
2. View balance
3. Open details page
4. View stats and history

### Alternative Flows

| Flow | Condition   | Action             |
| ---- | ----------- | ------------------ |
| A1   | Offline     | Show cached data   |
| A2   | Zero points | Show encouragement |

---

## Use Case 5: Redeem Reward

| Field              | Detail                             |
| ------------------ | ---------------------------------- |
| **Use Case ID**    | UC-005                             |
| **Actors**         | Student                            |
| **Description**    | Exchange points for reward         |
| **Preconditions**  | Enough points                      |
| **Postconditions** | Points deducted, voucher generated |

### Basic Flow

1. Open rewards
2. Select reward
3. Confirm redemption
4. System checks points
5. Deduct points
6. Generate QR voucher
7. Display confirmation

### Alternative Flows

| Flow | Condition         | Action               |
| ---- | ----------------- | -------------------- |
| A1   | Not enough points | Show required points |
| A2   | Out of stock      | Show unavailable     |
| A3   | Cancel            | No action            |
| A4   | Duplicate use     | Prevent reuse        |

---

## Use Case 6: View Reward Catalog

| Field              | Detail                   |
| ------------------ | ------------------------ |
| **Use Case ID**    | UC-006                   |
| **Actors**         | Student                  |
| **Description**    | Browse available rewards |
| **Preconditions**  | Logged in                |
| **Postconditions** | None                     |

### Basic Flow

1. Open rewards tab
2. System loads rewards
3. Display list
4. Filter/search
5. View details

### Alternative Flows

| Flow | Condition         | Action       |
| ---- | ----------------- | ------------ |
| A1   | No rewards        | Show message |
| A2   | No search results | Show message |

---

## Use Case 7: Monitor Bin Fill Levels

| Field              | Detail                     |
| ------------------ | -------------------------- |
| **Use Case ID**    | UC-007                     |
| **Actors**         | Facilities Admin, IT Admin |
| **Description**    | View bin status            |
| **Preconditions**  | Admin logged in            |
| **Postconditions** | None                       |

### Basic Flow

1. Open dashboard
2. View map
3. Check bin status
4. View details

### Alternative Flows

| Flow | Condition   | Action        |
| ---- | ----------- | ------------- |
| A1   | Bin offline | Show status   |
| A2   | Filter view | Apply filters |

---

## Use Case 8: Receive Fill-Level Alerts

| Field              | Detail                       |
| ------------------ | ---------------------------- |
| **Use Case ID**    | UC-008                       |
| **Actors**         | Facilities Admin             |
| **Description**    | Receive alerts for full bins |
| **Preconditions**  | Alerts enabled               |
| **Postconditions** | Alert logged                 |

### Basic Flow

1. Bin reaches threshold
2. System generates alert
3. Send notification
4. Admin acknowledges
5. System updates status

### Alternative Flows

| Flow | Condition       | Action       |
| ---- | --------------- | ------------ |
| A1   | No response     | Escalate     |
| A2   | Critical level  | Urgent alert |
| A3   | Multiple alerts | Group alerts |

---

