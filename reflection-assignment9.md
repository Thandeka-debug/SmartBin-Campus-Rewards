# Reflection - Assignment 9

## Direct Answers to Assignment Questions

| Question | Answer |
|----------|--------|
| Did I struggle with abstraction? | **Yes** - Challenge 1 below explains my difficulty deciding whether `itemType` should be an entity or enum. |
| Did I struggle with relationships? | **Yes** - Challenge 2 below explains my difficulty determining correct multiplicities (0..* vs 1..*). |
| Did I struggle with method definitions? | **Yes** - Challenge 4 below explains my difficulty ensuring every method traced back to a use case. |

---

## Challenges Faced in Designing the Domain Model and Class Diagram

### Challenge 1: Choosing the Right Level of Abstraction

**The Issue:** Determining which concepts should be entities and which should be attributes was difficult. For example, should `itemType` be a separate entity or an enum attribute of Transaction?

**How I Addressed It:** I considered whether `itemType` has its own behavior or attributes. Since item types only affect point calculation and don't have independent lifecycle, I made it an enum attribute of Transaction.

**Lesson Learned:** An entity should have its own identity and lifecycle. If a concept only has data and no behavior, it's better as an attribute or enum.

---

### Challenge 2: Defining Multiplicity Correctly

**The Issue:** Determining the correct cardinality between entities (e.g., Can a user have zero vouchers? Can a bin have zero alerts?)

**How I Addressed It:** I referred back to the domain logic. A new user starts with no vouchers (0..*). A bin may never trigger an alert if it's always emptied on time (0..*). This matches business rules.

**Lesson Learned:** Multiplicity comes from business rules, not from technical convenience. Always ask: "What are the real-world possibilities?"

---

### Challenge 3: Balancing Inheritance vs. Composition

**The Issue:** Should I create a base `Person` class for User, Admin, Officer, Finance, Dining? Or keep them as a single User class with role enum?

**How I Addressed It:** I chose composition (role enum) over inheritance. The five user types share the same attributes (email, name, password) but have different permissions. A role enum is simpler and more flexible than creating five subclasses.

**Lesson Learned:** Favor composition over inheritance when behaviors differ but data structure is similar. Inheritance adds complexity without enough benefit.

---

### Challenge 4: Mapping Methods to Use Cases

**The Issue:** Ensuring every method in the class diagram traced back to a use case from Assignment 5.

**How I Addressed It:** I created a traceability matrix. For example, `register()` maps to UC-001, `login()` maps to UC-002, `redeemReward()` maps to UC-005, `updateFillLevel()` maps to UC-007.

**Lesson Learned:** The class diagram is the structural implementation of use cases. Each method should fulfill a specific user interaction.

---

### Challenge 5: Aligning Status Enums with State Diagrams

**The Issue:** The state transition diagrams from Assignment 8 defined specific states for each object. I needed to ensure the class diagram's status enums matched exactly.

**How I Addressed It:** I mapped each state diagram to its corresponding class:

| Assignment 8 Object | Class in Assignment 9 | Status Enum Match |
|---------------------|----------------------|-------------------|
| User Account | User | REGISTERED, VERIFIED, ACTIVE, SUSPENDED, DEACTIVATED |
| Recycling Transaction | Transaction | PENDING, PROCESSING, COMPLETED, FAILED |
| Reward | Reward | DRAFT, AVAILABLE, LIMITED, OUT_OF_STOCK, DISCONTINUED |
| Redemption Voucher | Voucher | GENERATED, EMAILED, SCANNED, VERIFIED, INVALID, REDEEMED, EXPIRED |
| SmartBin | SmartBin | OPERATIONAL, REPORTING, WARNING, CRITICAL, OFFLINE, DECOMMISSIONED |
| Alert | Alert | CREATED, SENT, ACKNOWLEDGED, ESCALATED, RESOLVED |

**Lesson Learned:** Structural diagrams (class diagrams) must align with behavioral diagrams (state diagrams). Inconsistent enums would break the design.

---

## How the Class Diagram Aligns with Previous Assignments

| Assignment | Alignment |
|------------|-----------|
| Assignment 4 (Functional Requirements) | Each business rule (BR-001 to BR-010) is enforced by class methods or attributes |
| Assignment 5 (Use Cases) | Each use case (UC-001 to UC-008) maps to one or more class methods |
| Assignment 6 (User Stories) | Each user story (US-001 to US-015) is supported by class capabilities |
| Assignment 8 (State Diagrams) | Status enums exactly match state diagrams for each object |

---

## Trade-offs Made

| Trade-off | Decision | Rationale |
|-----------|----------|-----------|
| Inheritance vs. Composition | Used composition (role enum) | Simpler, more flexible, no need for polymorphic behavior |
| Separate Voucher class vs. attribute of Reward | Created separate Voucher class | Voucher has its own lifecycle (generated, scanned, redeemed, expired) |
| Direct object references vs. ID references | Used ID references (userId, binId) | Avoids circular dependencies in diagram |
| All methods public vs. private | Showed public methods only | Assignment focuses on system interactions, not internal helpers |

---

## Lessons Learned About Object-Oriented Design

1. **Entities have identity** - An entity is defined by its unique identifier, not its attributes.
2. **Enums are powerful** - Fixed sets of states (from state diagrams) map perfectly to enums.
3. **Multiplicity reflects business rules** - Don't guess cardinalities; derive them from requirements.
4. **Methods should be testable** - Each method should have a clear input, output, and side effect.
5. **Class diagrams are blueprints** - They guide implementation but allow flexibility.
6. **Traceability is essential** - Every class, attribute, and method should trace to a requirement or use case.
7. **Simplicity wins** - Composition over inheritance, enums over subclasses, ID references over object references.

---

## Summary

The domain model and class diagram for SmartBin capture 7 core entities with their attributes, methods, relationships, and business rules. The design aligns with all previous assignments, uses composition over inheritance, and matches state diagrams exactly. The main challenges were abstraction level, multiplicity accuracy, and maintaining traceability across 5 assignments.
