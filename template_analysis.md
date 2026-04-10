# GitHub Project Templates Analysis

## Template Comparison Table

| Template | Columns | Automation Features | Suitability for Agile |
|----------|---------|---------------------|----------------------|
| **Basic Kanban** | Todo, In Progress, Done | None - manual movement only | Basic Agile tracking |
| **Automated Kanban** | Todo, In Progress, Done | Auto-moves issues to "Done" when PR is merged | Full Agile support |
| **Bug Triage** | Needs Triage, In Progress, Done | Auto-labels bugs; auto-assigns | Bug-focused Agile |
| **Team Planning** | Backlog, Ready, In Progress, In Review, Done | Custom workflows; dependency tracking | Advanced Agile with reviews |

## Selected Template: Automated Kanban

### Justification

I have selected the **Automated Kanban** template for the SmartBin system because:

1. **Sprint Tracking Support** - The template includes columns needed for sprint tracking from Assignment 6
2. **Built-in Automation** - When a pull request is merged, issues automatically move to "Done"
3. **Alignment with Agile** - Supports continuous delivery principles
4. **Scalability** - Can be extended with custom columns without breaking automation
5. **Traceability** - Linked issues maintain traceability from user stories to code

### Why Not Other Templates?

| Template | Reason for Rejection |
|----------|----------------------|
| Basic Kanban | No automation; requires manual status updates |
| Bug Triage | Focuses only on bugs; SmartBin has user stories |
| Team Planning | Too complex for a single developer |
