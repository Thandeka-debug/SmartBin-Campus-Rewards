# GitHub Project Templates Analysis

## Template Comparison Table

| Template | Columns | Automation Features | Suitability for Agile |
|----------|---------|---------------------|----------------------|
| **Basic Kanban** | Todo, In Progress, Done | None - manual movement only | Basic Agile tracking for small teams |
| **Automated Kanban** | Todo, In Progress, Done | Auto-moves issues to "Done" when PR is merged | Full Agile support with automation |
| **Bug Triage** | Needs Triage, In Progress, Done | Auto-labels bugs; auto-assigns based on rules | Bug-focused Agile workflow |
| **Team Planning** | Backlog, Ready, In Progress, In Review, Done | Custom workflows; dependency tracking | Advanced Agile for larger teams |

## Selected Template: Team Planning (or Automated Kanban - whichever you used)

Based on my board columns (Backlog, Blocked, Ready, In Progress, Testing, In Review, Done), I am using a template that supports full sprint planning and code review workflows.

### Justification

I selected this template for the SmartBin system because:

1. **Backlog column** - Allows me to store all tasks before sprint planning (from Assignment 6)

2. **Ready column** - Helps identify tasks that are fully defined and ready to work on

3. **In Progress column** - Tracks active development work

4. **In Review column** - Supports code review stage before completion (important for quality)

5. **Done column** - Marks fully completed and verified tasks

6. **Customizable** - The template allows adding new columns without breaking existing workflow

### Custom Columns Added in This Assignment (Assignment 7)

For Assignment 7, I customized the template by adding **2 new columns** to my existing board:

| New Column | Purpose | Placement |
|------------|---------|-----------|
| **Blocked** | Tasks that cannot proceed due to dependencies or external issues | Placed after "In Progress" to visualize bottlenecks |
| **Testing** | Completed code awaiting quality assurance and verification | Placed between "In Review" and "Done" to ensure QA before final completion |

### Final Column Structure

My board now has these columns (in logical workflow order):

| Order | Column Name | Type | Purpose |
|-------|-------------|------|---------|
| 1 | **Backlog** | Default from template | All tasks not yet scheduled |
| 2 | **Ready** | Default from template | Tasks ready to be worked on |
| 3 | **In Progress** | Default from template | Tasks currently being developed |
| 4 | **Blocked** | **NEW - Added in Assignment 7** | Tasks stuck due to dependencies |
| 5 | **In Review** | Default from template | Code awaiting peer review |
| 6 | **Testing** | **NEW - Added in Assignment 7** | Code awaiting quality assurance |
| 7 | **Done** | Default from template | Fully completed and verified tasks |

### Why Not Other Templates?

| Template | Reason for Rejection |
|----------|----------------------|
| Basic Kanban | No automation; no Backlog or In Review columns |
| Automated Kanban | Missing Backlog and In Review columns needed for my workflow |
| Bug Triage | Focuses only on bugs; SmartBin has user stories and tasks |

### How This Board Aligns with Assignment Requirements

| Requirement | How My Board Meets It |
|-------------|----------------------|
| Use a template | I used a template that includes Backlog, Ready, In Progress, In Review, Done |
| Add 2+ new columns | I added **Blocked** and **Testing** columns in Assignment 7 |
| Support Agile workflow | Columns represent complete workflow from Backlog to Done with review and testing stages |
