# SmartBin: Campus Sustainability Rewards System

## Introduction
SmartBin is a proposed system designed to increase recycling rates on a university campus by gamifying the process. The system simulates a network of "smart" recycling bins that can identify when a user deposits an item, award points to the user's account, and monitor the bin's fill level in real-time. Students can then redeem their accumulated points for small rewards (e.g., coffee vouchers, merchandise) via a mobile application.

## Documentation

### Assignment 3
- [System Specification (SPECIFICATION.md)](SPECIFICATION.md)
- [C4 Architectural Diagrams (ARCHITECTURE.md)](ARCHITECTURE.md)

### Assignment 4
- [Stakeholder Analysis (STAKEHOLDER-ANALYSIS.md)](STAKEHOLDER-ANALYSIS.md)
- [System Requirements (SYSTEM-REQUIREMENTS.md)](SYSTEM-REQUIREMENTS.md)
- [Reflection - Assignment 4 (REFLECTION.md)](REFLECTION.md)

### Assignment 5
- [Use Case Diagram (USE-CASE-DIAGRAM.md)](USE-CASE-DIAGRAM.md)
- [Use Case Specifications (USE-CASE-SPECIFICATIONS.md)](USE-CASE-SPECIFICATIONS.md)
- [Test Cases (TEST-CASES.md)](TEST-CASES.md)
- [Reflection - Assignment 5 (REFLECTION-ASSIGNMENT5.md)](REFLECTION-ASSIGNMENT5.md)

### Assignment 6
- [Agile Planning Document (AGILE-PLANNING-DOCUMENT.md)](AGILE-PLANNING-DOCUMENT.md)
- [User Stories (USER-STORIES.md)](USER-STORIES.md)
- [Product Backlog (PRODUCT-BACKLOG.md)](PRODUCT-BACKLOG.md)
- [Sprint Plan (SPRINT-PLAN.md)](SPRINT-PLAN.md)
- [Reflection - Assignment 6 (REFLECTION-ASSIGNMENT6.md)](REFLECTION-ASSIGNMENT6.md)
- [GitHub Issues](https://github.com/Thandeka-debug/SmartBin-Campus-Rewards/issues)
- [GitHub Project Board](https://github.com/Thandeka-debug/SmartBin-Campus-Rewards/projects/1)
- [GitHub Milestones](https://github.com/Thandeka-debug/SmartBin-Campus-Rewards/milestones)

### Assignment 7
- [Template Analysis (template_analysis.md)](template_analysis.md)
- [Kanban Explanation (kanban_explanation.md)](kanban_explanation.md)
- [Reflection - Assignment 7 (reflection_assignment7.md)](reflection_assignment7.md)
- [Template Comparison Screenshot](template-comparison-screenshot1.png.png)
- [Kanban Board Screenshot - Custom Columns](Kanban_Board_Custom_Columns.png)
- [Kanban Board Screenshot - Final Board](Kanban_Board_Final.png)
- [GitHub Project Board](https://github.com/Thandeka-debug/SmartBin-Campus-Rewards/projects/1)

### Assignment 8
- [State Transition Diagrams (state-transition-diagrams.md)](state-transition-diagrams.md)
- [Activity Diagrams (activity-diagrams.md)](activity-diagrams.md)
- [Reflection - Assignment 8 (reflection-assignment8.md)](reflection-assignment8.md)

### Assignment 9
- [Domain Model (domain-model.md)](domain-model.md)
- [Class Diagram (class-diagram.md)](class-diagram.md)
- [Reflection - Assignment 9 (reflection-assignment9.md)](reflection-assignment9.md)

### Assignment 10
- [Source Code (/src)](src/)
- [Creational Patterns (/creational_patterns)](creational_patterns/)
- [Unit Tests (/tests)](tests/)
- [CHANGELOG.md](CHANGELOG.md)
- [GitHub Issues](https://github.com/Thandeka-debug/SmartBin-Campus-Rewards/issues)

### Assignment 11

**Repository Pattern Implementation**

This assignment adds a repository layer for data persistence with pluggable storage backends.

**Design Decisions:**
- Used **Factory Pattern** for storage abstraction (can switch between memory, database, filesystem)
- Generic `Repository<T, ID>` interface with CRUD operations
- Entity-specific interfaces with custom query methods (e.g., `find_by_email`, `find_by_role`)
- In-memory implementation using Python dictionaries (HashMap)
- Stub implementations provided for future database storage

**Why This Approach:**
- **Separation of Concerns:** Business logic stays separated from storage details
- **Testability:** In-memory repositories enable fast unit tests without external dependencies
- **Scalability:** Switching to a real database later requires only changing the factory parameter
- **Future-Proofing:** New storage backends can be added without modifying existing code

**Factory Pattern Usage:**
```python
from factories.repository_factory import RepositoryFactory

# Create in-memory repository (current)
user_repo = RepositoryFactory.get_user_repository("memory")

# Future: switch to database (just change the parameter)
# user_repo = RepositoryFactory.get_user_repository("database")
