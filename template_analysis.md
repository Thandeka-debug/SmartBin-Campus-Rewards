# GitHub Project Templates Analysis

## Template Comparison Table

| Template | Columns | Automation Features | Suitability for Agile |
|----------|---------|---------------------|----------------------|
| **Basic Kanban** | Todo, In Progress, Done | None - manual movement only | Basic Agile tracking for small teams |
| **Automated Kanban** | Todo, In Progress, Done | Auto-moves issues to "Done" when PR is merged | Full Agile support with automation |
| **Bug Triage** | Needs Triage, In Progress, Done | Auto-labels bugs; auto-assigns based on rules | Bug-focused Agile workflow |
| **Team Planning** | Backlog, Ready, In Progress, In Review, Done | Custom workflows; dependency tracking | Advanced Agile for larger teams |

## Selected Template: Automated Kanban

### Justification

I selected the **Automated Kanban** template for the SmartBin system because:

1. **Sprint Tracking Support** - The template includes basic columns (Todo, In Progress, Done) needed for sprint tracking from Assignment 6

2. **Built-in Automation** - When a pull request is merged, the associated issue automatically moves to "Done". This reduces manual work and keeps the board accurate

3. **Alignment with Agile** - The automated workflow supports continuous delivery principles

4. **Customizable** - The template allows adding new columns without breaking existing automation

5. **Traceability** - Linked issues and pull requests maintain traceability from user stories to code changes

### Why Not Other Templates?

| Template | Reason for Rejection |
|----------|----------------------|
| Basic Kanban | No automation; requires manual status updates for every task |
| Bug Triage | Focuses only on bugs; SmartBin has user stories and tasks, not just bugs |
| Team Planning | Too complex for a single developer; designed for multiple team members with review stages |

### Custom Columns Added in This Assignment (Assignment 7)

For Assignment 7, I customized the Automated Kanban template by adding **2 new columns**:

| New Column | Purpose | Placement |
|------------|---------|-----------|
| **Blocked** | Tasks that cannot proceed due to dependencies or external issues | Placed after "In Progress" to visualize bottlenecks |
| **Testing** | Completed code awaiting quality assurance and verification | Placed between "In Progress" and "Done" to ensure QA before completion |

These custom columns were added to better reflect the SmartBin development workflow, where code needs testing before being marked done, and tasks can become blocked due to dependencies.

### Final Column Structure

After customization, my board has these columns:

| Order | Column Name | Type |
|-------|-------------|------|
| 1 | Todo | Default from template |
| 2 | In Progress | Default from template |
| 3 | Blocked | **NEW - Added in Assignment 7** |
| 4 | Testing | **NEW - Added in Assignment 7** |
| 5 | Done | Default from template |
