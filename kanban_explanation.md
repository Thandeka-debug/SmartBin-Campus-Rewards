# Kanban Board Explanation

## What is a Kanban Board?

A Kanban board is a visual project management tool that helps teams track work as it moves through different stages of a workflow. The word "Kanban" comes from Japanese, meaning "visual card" or "sign board." It helps teams see what needs to be done, what is being worked on, and what is completed.

## My Kanban Board Columns

My SmartBin Sprint Board has the following columns:

| Column | Purpose | Origin |
|--------|---------|--------|
| **Backlog** | All tasks that need to be done, not yet scheduled for a sprint | Default from template |
| **Ready** | Tasks that are fully defined and ready to be worked on | Default from template |
| **In Progress** | Tasks currently being worked on | Default from template |
| **Blocked** | Tasks that cannot proceed due to dependencies or issues | **NEW - Added in Assignment 7** |
| **In Review** | Code that has been completed and is awaiting peer review | Default from template |
| **Testing** | Code that has passed review and is awaiting quality assurance | **NEW - Added in Assignment 7** |
| **Done** | Fully completed and verified tasks | Default from template |

## How My Board Visualizes Workflow

The columns represent the complete workflow of a task from start to finish:

1. **Backlog** → Task is identified but not yet scheduled
2. **Ready** → Task is fully defined and ready for the sprint
3. **In Progress** → Developer is actively working on the task
4. **Blocked** → If a dependency arises, task moves here until resolved
5. **In Review** → Code is complete and needs peer review
6. **Testing** → Code has passed review and needs QA verification
7. **Done** → Task is fully complete and verified

This visualization provides:
- **Real-time visibility** into what is being worked on
- **Clear status** of each task at a glance
- **Easy identification** of bottlenecks (tasks stuck in Blocked, In Review, or Testing columns)

## Work-in-Progress (WIP) Limits

To prevent bottlenecks and overload, I have implemented the following WIP limits:

| Column | WIP Limit | Justification |
|--------|-----------|---------------|
| In Progress | 3 tasks | As a single developer, I cannot effectively work on more than 3 tasks simultaneously |
| In Review | 2 tasks | Code review requires focus; too many tasks indicates review bottleneck |
| Testing | 2 tasks | Testing requires focus; too many tasks in Testing indicates quality issues |
| Blocked | No limit | Blocked tasks need visibility, but they are not actively being worked on |

These limits ensure:
- **Focused work** - Complete tasks before starting new ones
- **Reduced context switching** - Less time wasted moving between tasks
- **Early bottleneck detection** - When a column hits its limit, address the blockage

## How the Board Supports Agile Principles

| Agile Principle | How My Kanban Board Supports It |
|----------------|--------------------------------|
| **Continuous delivery** | Tasks move through columns to Done |
| **Adaptability** | Easy to reprioritize by moving tasks between Backlog and Ready |
| **Transparency** | Everyone can see what is Blocked, In Review, In Progress, or Testing |
| **Customer focus** | Each task links to a user story that delivers value to a stakeholder |
| **Continuous improvement** | Reviewing the board during retrospectives identifies workflow improvements |

## Why I Added Blocked and Testing Columns in Assignment 7

For Assignment 7, I added two custom columns to better manage my SmartBin development:

| Column | Reason for Adding |
|--------|-------------------|
| **Blocked** | During development, tasks sometimes depend on other tasks being completed first. The Blocked column makes these dependencies visible and prevents working on tasks that cannot proceed. |
| **Testing** | Before marking a task as Done, code should be tested. The Testing column ensures quality assurance happens after code review and before completion, preventing bugs from reaching production. |

## Why the "In Review" Column Already Existed

The **In Review** column was part of the template I selected. It represents the code review stage, where completed code is reviewed by peers before moving to testing. This is an important quality gate in software development.

## Complete Workflow with All Columns

