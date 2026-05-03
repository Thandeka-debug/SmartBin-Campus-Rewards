# Reflection: Agile User Stories, Backlog, and Sprint Planning

## Agile Principles Applied

This reflection is informed by the [Agile Manifesto](https://agilemanifesto.org/) and the [Scrum Guide](https://scrumguides.org/).

| Agile Principle | Application in SmartBin |
|-----------------|-------------------------|
| Individuals and interactions over processes and tools | User stories focus on stakeholder needs, not technical specifications |
| Working software over comprehensive documentation | MVP sprint focuses on delivering functional recycling loop |
| Customer collaboration over contract negotiation | Stories prioritized based on stakeholder success metrics |
| Responding to change over following a plan | MoSCoW prioritization allows flexibility |

## Challenge 1: Balancing Must-have Stories with Time Constraints

**The Issue:** When prioritizing the product backlog using MoSCoW, I initially marked 12 stories as "Must-have." However, with a 2-week sprint capacity of approximately 24 story points, I had to reduce the Must-have list to 8 stories totaling 24 points.

**How I Addressed It:** I reviewed each story against the stakeholder success metrics from Assignment 4. Stories that directly enabled core user journeys (registration, login, deposit, redeem) remained Must-have. Stories like "View transaction history" and "Leaderboard" were moved to Should-have.

**Lesson Learned:** The Product Owner must constantly balance stakeholder desires with development capacity.

## Challenge 2: Estimating Story Points Accurately

**The Issue:** Assigning story points using the Fibonacci sequence (1, 2, 3, 5, 8) was difficult because I had to consider complexity, not just time.

**How I Addressed It:** I set US-004 (View point balance) as a 1-point baseline because it's a simple database read. I then estimated other stories relative to this baseline. Stories with external integrations (like push notifications) received higher estimates.

**Lesson Learned:** Story points should measure relative complexity, not absolute time.

## Challenge 3: Breaking Stories into Small, Testable Tasks

**The Issue:** When breaking US-003 into tasks, I initially created 3 large tasks. This made tracking progress difficult.

**How I Addressed It:** I broke each story into smaller tasks that could be completed in 2-4 hours. For US-003, I created 7 tasks. This allows daily stand-ups to track meaningful progress.

**Lesson Learned:** Tasks should be small enough that "in progress" doesn't last more than a day.

## Challenge 4: Aligning Agile with Previous Assignments

**The Issue:** Assignments 3-5 were structured for traditional requirements engineering. Translating this into Agile user stories required mental shifts.

**How I Addressed It:** I mapped each user story back to a functional requirement from Assignment 4 and a use case from Assignment 5. This traceability helped me ensure no critical functionality was missed.

**Lesson Learned:** Agile doesn't mean abandoning documentation. Traceability helps maintain consistency.

## Challenge 5: Defining the Sprint Goal

**The Issue:** I had to define a sprint goal that was ambitious but achievable. Initially, I wanted to include analytics stories in the first sprint, but this would have added too many story points.

**How I Addressed It:** I focused on the "core recycling loop" - register → login → deposit → view points → redeem. This delivers end-to-end value to students.

**Lesson Learned:** Sprint goals should be outcome-focused, not feature-focused.

## Challenge 6: Balancing Technical and User-Centric Stories

**The Issue:** US-015 (data encryption) and US-016 (scalability) are important for security and performance, but they don't deliver visible value to students.

**How I Addressed It:** I kept US-015 in Must-have with low story points (2). I moved US-016 to Should-have with high story points (8) because scalability testing can happen after initial functionality is stable.

**Lesson Learned:** Security cannot be deferred; scalability can be if traffic is initially low.

## Challenge 7: Playing Multiple Scrum Roles

**The Issue:** As a single person, I played Product Owner (prioritizing backlog), Scrum Master (facilitating process), and Developer (estimating and task breakdown).

**How I Addressed It:** I mentally separated the roles. As Product Owner, I prioritized based on stakeholder value. As Developer, I provided honest estimates and pushed back when the backlog exceeded capacity.

**Lesson Learned:** Even in solo development, separating roles mentally helps maintain objectivity.

## Agile Manifesto Alignment

| Agile Manifesto Value | How It Applies to SmartBin |
|-----------------------|----------------------------|
| Individuals and interactions over processes and tools | User stories written from stakeholder perspectives |
| Working software over comprehensive documentation | Sprint focuses on delivering functional MVP |
| Customer collaboration over contract negotiation | Prioritization based on stakeholder success metrics |
| Responding to change over following a plan | MoSCoW allows reprioritization as needs evolve |

## Summary

The Agile transformation required translating traditional requirements into user stories, prioritizing with MoSCoW, estimating with story points (Fibonacci sequence), and planning a sprint that balances technical and user-centric stories. The final sprint plan delivers a functional MVP that addresses the highest-priority stakeholder concerns.
