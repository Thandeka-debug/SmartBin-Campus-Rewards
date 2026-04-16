# State Transition Diagrams - Assignment 8

## Overview

This document contains state transition diagrams for 8 critical objects in the SmartBin system. Each diagram shows:
- **States** (circles/rectangles with rounded corners)
- **Transitions** (arrows between states)
- **Events** (labels on arrows showing what causes the transition)
- **Guard conditions** (bracketed conditions that must be true)

---

## Object 1: User Account

### State Transition Diagram

```mermaid
stateDiagram-v2
    [*] --> Registered : Student submits registration form
    Registered --> Verified : Student clicks verification email link
    Registered --> Suspended : Admin marks account as suspicious
    Verified --> Active : Student logs in successfully
    Suspended --> Verified : Admin reinstates account
    Active --> Suspended : 5 failed login attempts
    Active --> Deactivated : Student requests account deletion
    Suspended --> Deactivated : Admin deletes account
    Deactivated --> [*]
