# C4 Architecture for SmartBin

This document outlines the architecture of the SmartBin system using the C4 model.

## Level 1: System Context Diagram
This diagram shows the big picture: our system and the people/systems it interacts with.

```mermaid
C4Context
  title System Context diagram for SmartBin System

  Person(student, "Student", "A university student who wants to recycle and earn rewards.")
  Person(admin, "Facilities Admin", "An employee who monitors bin status and manages rewards.")

  System(smartbin, "SmartBin System", "Allows students to earn points for recycling and staff to monitor bin levels.")

  System_Ext(id_auth, "Campus ID Service", "External authentication for student IDs (to be simulated).")
  System_Ext(push_notif, "Push Notification Service", "Sends alerts for bin status and new rewards.")

  Rel(student, smartbin, "Scans QR code, views points, redeems rewards")
  Rel(admin, smartbin, "Monitors bins, manages reward catalog")
  Rel(smartbin, id_auth, "Verifies student identity")
  Rel(smartbin, push_notif, "Sends notifications")
