# Reflection - Assignment 8

## Challenges in Object State Modeling and Activity Workflow Modeling

### Challenge 1: Choosing the Right Granularity for States

**The Issue:** When creating state transition diagrams, I had to decide how detailed to make the states. Too few states would miss important behavior. Too many states would make the diagram cluttered.

**How I Addressed It:** For each object, I identified the minimum states needed to capture meaningful behavior. For example, the SmartBin object has 6 states: Operational, Reporting, Warning, Critical, Offline, Decommissioned. Each state represents a distinct condition that affects system behavior.

**Lesson Learned:** Granularity should balance completeness with readability. Ask: "Does this state trigger a different system behavior?" If yes, include it.

### Challenge 2: Defining Guard Conditions

**The Issue:** Some transitions depend on conditions being true. For example, a bin transitions to Warning only if fill level is between 80% and 95%.

**How I Addressed It:** I referred back to the functional requirements from Assignment 4. FR8 specifies alert thresholds at 80% and 95%. These numbers became my guard conditions.

**Lesson Learned:** Guard conditions should come directly from requirements. If a requirement doesn't specify a number, add one in the guard condition.

### Challenge 3: Representing Parallel Actions in Activity Diagrams

**The Issue:** Some workflows have actions that happen simultaneously. For example, when an alert is triggered, the system sends both a push notification and an email at the same time.

**How I Addressed It:** I identified parallel actions in the explanation and showed them as concurrent steps in the workflow.

**Lesson Learned:** Parallel actions improve efficiency. In activity diagrams, use fork/join nodes to show concurrency.

### Challenge 4: Mapping Diagrams to Previous Assignments

**The Issue:** The assignment requires traceability to Assignment 4 (functional requirements), Assignment 5 (use cases), and Assignment 6 (user stories).

**How I Addressed It:** I created traceability sections in each diagram showing exactly which FR, UC, and US each diagram maps to.

**Lesson Learned:** Traceability is not automatic. You must explicitly document the links between diagrams and requirements.

### Challenge 5: Aligning Activity Diagrams with Use Case Flows

**The Issue:** Use cases from Assignment 5 have basic flows and alternative flows. Activity diagrams need to show both.

**How I Addressed It:** I used decision diamonds to branch for error conditions. For example, in the Login workflow, if credentials are invalid and attempts < 5, the flow loops back to re-enter credentials.

**Lesson Learned:** Activity diagrams are a natural extension of use cases. The basic flow becomes the main path; alternative flows become decision branches.

### Challenge 6: Choosing Which Objects and Workflows to Model

**The Issue:** The assignment asks for 7-8 objects and 8 workflows. My system has more than that.

**How I Addressed It:** I prioritized objects and workflows that appear in multiple functional requirements, have complex state changes, or are mentioned in stakeholder concerns.

**Lesson Learned:** Not everything needs a diagram. Focus on the core domain objects and workflows that capture the system's complexity.

### Challenge 7: Ensuring Swimlanes Reflect Real Responsibilities

**The Issue:** Activity diagrams require swimlanes to show which actor or system component performs each action.

**How I Addressed It:** I referred to the C4 architecture from Assignment 3 to understand component boundaries. The Bin Simulator, Backend API, Database, and Mobile App each have different responsibilities.

**Lesson Learned:** Swimlanes in activity diagrams should align with containers in the C4 architecture diagram.

## Comparison: State Diagrams vs. Activity Diagrams

| Aspect | State Transition Diagram | Activity Diagram |
|--------|-------------------------|------------------|
| **Focus** | Object lifecycle over time | Process workflow step-by-step |
| **What it shows** | States and transitions | Actions, decisions, parallel flows |
| **Unit of analysis** | A single object | A complete process |
| **Example** | User Account: Registered → Verified → Active | User Registration: Enter details → Validate → Create account |
| **Best for** | Understanding how objects change | Understanding how processes execute |

## Lessons Learned

1. State granularity matters - Too many states confuse; too few states miss important behavior
2. Guard conditions come from requirements - Don't invent numbers; use what's already specified
3. Parallel actions improve efficiency - Activity diagrams can show concurrency
4. Traceability requires explicit documentation - Don't assume connections are obvious
5. Activity diagrams extend use cases - Basic flow = main path, alternative flows = decision branches
6. Prioritize critical objects and workflows - Not everything needs a diagram
7. Swimlanes should align with architecture - Use C4 diagrams as a reference

## How This Assignment Connects to Previous Work

| Assignment | Connection to Assignment 8 |
|------------|---------------------------|
| Assignment 3 | C4 architecture informed swimlanes in activity diagrams |
| Assignment 4 | Functional requirements provided guard conditions and business rules |
| Assignment 5 | Use cases provided basic flows for activity diagrams |
| Assignment 6 | User stories validated that diagrams capture user needs |
| Assignment 7 | Kanban workflow informed process flow thinking |
