# Reflection: Use Case Modeling and Test Case Development

## Challenges in Translating Requirements to Use Cases and Tests

### Challenge 1: Defining the Right Level of Detail for Use Cases

**The Issue:** I struggled with determining how detailed each use case should be. Too little detail makes specifications ambiguous; too much detail makes them rigid and hard to maintain.

**How I Addressed It:** I used the "basic flow" format with clear step-by-step actions, ensuring each step was testable. I included alternative flows to handle exceptions without cluttering the main flow. This balance came from referencing the functional requirements from Assignment 4 and ensuring each requirement was traceable to at least one use case.

**Lesson Learned:** Use cases should be detailed enough for a developer to implement and a tester to validate, but not so detailed that they specify implementation details.

---

### Challenge 2: Determining Include vs. Extend Relationships

**The Issue:** In the use case diagram, I had to decide when to use include relationships (mandatory steps) vs. extend relationships (optional steps). I initially overcomplicated the diagram with too many relationships.

**How I Addressed It:** I simplified by using include relationships only where one use case was always required by another (e.g., "Redeem Reward" always includes "View Points" to check balance). I avoided extend relationships for now to keep the diagram clear for the first version.

**Lesson Learned:** Simplicity in diagrams often communicates better than complexity. Stakeholders don't need every technical nuance in the high-level diagram.

---

### Challenge 3: Translating Non-Functional Requirements into Testable Scenarios

**The Issue:** Non-functional requirements like "scalability" and "security" are harder to test than functional ones. I initially wrote vague test cases like "System handles many users."

**How I Addressed It:** I followed the assignment's advice to be specific. Instead of vague tests, I created measurable scenarios:
- "Simulate 100 concurrent users making 10 requests each"
- "95% of requests complete in <300ms"
- "Send 150 API requests; requests 101-150 return HTTP 429"

This required understanding what numbers actually mean for my system.

**Lesson Learned:** Non-functional tests need specific metrics to be meaningful. Vague tests can't be verified or automated.

---

### Challenge 4: Ensuring Traceability from Stakeholders to Tests

**The Issue:** The assignment requires consistency across Assignments 3, 4, and 5. I needed to ensure my use cases and tests actually addressed the stakeholder concerns identified in Assignment 4.

**How I Addressed It:** I created a mental traceability matrix to ensure every stakeholder need was covered by at least one use case and test scenario.

**Lesson Learned:** Requirements traceability isn't just for large projects. Even for an academic assignment, it ensures nothing falls through the cracks.

---

### Challenge 5: Balancing Comprehensive Testing with Practicality

**The Issue:** I could create hundreds of test cases, but I had to select which tests were most critical.

**How I Addressed It:** I prioritized:
1. Happy path tests (normal successful scenarios)
2. Edge case tests (invalid inputs, boundary conditions)
3. Failure scenario tests (system errors, timeouts)
4. Critical non-functional tests (performance, security)

This gave me enough tests to be comprehensive without being overwhelming.

**Lesson Learned:** Testing strategy matters. It's not about how many tests, but whether they cover critical paths and failure modes.

---

### Challenge 6: Representing the Bin Simulator in Use Cases

**The Issue:** My system includes a "Bin Simulator" component that isn't a human actor. How do I represent automated system-to-system interactions in a use case diagram?

**How I Addressed It:** I kept the bin simulator as an "external system" in the architecture (from Assignment 3) but didn't include it as an actor in the use case diagram since use cases traditionally focus on human-system interactions. Instead, I documented the bin simulator's role in the use case specifications for "Deposit Item" and "Receive Alerts."

**Lesson Learned:** Use case diagrams aren't meant to capture all system components. They focus on user goals. System components belong in the architecture diagram.

---

## Summary

The biggest takeaway from this assignment is that requirements, use cases, and test cases form a chain of increasing specificity:
- Requirements define WHAT the system should do
- Use Cases define HOW users interact with the system
- Test Cases define HOW TO VERIFY it works correctly

Each layer depends on the previous one. If the requirements are vague, use cases become ambiguous and tests become meaningless. This assignment reinforced the importance of getting the foundation right before moving to modeling and testing.

For the SmartBin system, I now have confidence that the requirements are testable, the use cases cover stakeholder needs, and the tests will validate the system's critical functions.
