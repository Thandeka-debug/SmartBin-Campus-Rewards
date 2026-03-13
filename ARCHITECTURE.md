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

C4Container
  title Container diagram for the SmartBin System

  Person(student, "Student", "A university student who wants to recycle and earn rewards.")
  Person(admin, "Facilities Admin", "An employee who monitors bin status and manages rewards.")

  Container_Boundary(c1, "SmartBin System") {
    Container(mobile_app, "Mobile App", "Flutter / React Native", "Allows students to view points and scan QR codes. Provides admin dashboard.")
    Container(web_app, "Web Admin Panel", "React", "Allows admins to monitor bins and manage rewards.")
    Container(api, "Backend API", "Node.js/Express", "Handles business logic: user management, points, rewards, bin data.")
    ContainerDb(db, "Database", "PostgreSQL", "Stores user profiles, points, transactions, bin status, and reward catalog.")
    Container(bin_sim, "Bin Simulator", "Python Script", "Simulates IoT device behavior. Sends 'item deposited' events and fill-level updates to the API.")
  }

  System_Ext(id_auth, "Campus ID Service", "External Auth")

  Rel(student, mobile_app, "Uses")
  Rel(admin, web_app, "Uses")
  Rel(mobile_app, api, "Makes API calls to", "JSON/HTTPS")
  Rel(web_app, api, "Makes API calls to", "JSON/HTTPS")
  Rel(bin_sim, api, "Sends events to", "JSON/HTTPS")
  Rel(api, db, "Reads/Writes to", "SQL")
  Rel(api, id_auth, "Verifies identity (simulated)")

  UpdateLayoutConfig($c4ShapeInRow="3", $c4BoundaryInRow="1")

C4Component
  title Component diagram for the Backend API Container

  Container_Boundary(api, "Backend API") {
    Component(user_comp, "User Controller", "Route Handler", "Manages user registration, login, and profile.")
    Component(point_comp, "Points Controller", "Route Handler", "Handles point awarding, balance checks, and history.")
    Component(reward_comp, "Rewards Controller", "Route Handler", "Manages reward catalog and redemption logic.")
    Component(bin_comp, "Bin Controller", "Route Handler", "Receives data from bin simulator (fill level, deposits).")
    Component(auth_middleware, "Auth Middleware", "Middleware", "Verifies JWT tokens for protected routes.")

    Component(service, "Service Layer", "Business Logic", "Orchestrates operations, contains core business rules.")
    Component(repo, "Repository Layer", "Data Access", "Abstracts database interactions.")
  }

  ContainerDb(db, "Database", "PostgreSQL", "Stores all system data.")
  Container(mobile_app, "Mobile App", "External Container", "Makes API calls.")
  Container(bin_sim, "Bin Simulator", "External Container", "Sends bin events.")

  Rel(mobile_app, user_comp, "login/register", "JSON/HTTPS")
  Rel(mobile_app, point_comp, "get balance", "JSON/HTTPS")
  Rel(mobile_app, reward_comp, "redeem points", "JSON/HTTPS")
  Rel(bin_sim, bin_comp, "send deposit event", "JSON/HTTPS")

  Rel(user_comp, service, "Uses")
  Rel(point_comp, service, "Uses")
  Rel(reward_comp, service, "Uses")
  Rel(bin_comp, service, "Uses")

  Rel(service, repo, "Uses")
  Rel(repo, db, "Reads/Writes", "SQL")

  Rel(user_comp, auth_middleware, "Protected by")
  Rel(point_comp, auth_middleware, "Protected by")
  Rel(reward_comp, auth_middleware, "Protected by")
