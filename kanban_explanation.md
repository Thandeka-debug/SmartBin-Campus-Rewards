# Kanban Board Explanation

## What is a Kanban Board?

A Kanban board is a visual project management tool that helps teams track work as it moves through different stages of a workflow. The word "Kanban" comes from Japanese, meaning "visual card" or "sign board."

## How My Kanban Board Visualizes Workflow

My SmartBin Sprint Board uses the following columns:

| Column | Purpose |
|--------|---------|
| **Blocked** | Tasks that cannot proceed due to dependencies |
| **Todo** | Tasks planned but not yet started |
| **In Progress** | Tasks currently being worked on |
| **Testing** | Completed code awaiting quality assurance |
| **Done** | Fully completed and verified tasks |

## Work-in-Progress (WIP) Limits

| Column | WIP Limit | Justification |
|--------|-----------|---------------|
| In Progress | 3 tasks | Single developer cannot work on more than 3 tasks simultaneously |
| Testing | 2 tasks | Testing requires focus; too many indicates quality issues |
| Blocked | No limit | Blocked tasks need visibility but shouldn't count against WIP |

## How the Board Supports Agile Principles

| Agile Principle | How My Board Supports It |
|----------------|--------------------------|
| Continuous delivery | Tasks move through columns to Done |
| Adaptability | Easy to reprioritize by moving tasks |
| Transparency | Everyone can see what is being worked on |
| Customer focus | Each task links to a user story |
