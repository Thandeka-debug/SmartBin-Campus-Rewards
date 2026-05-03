# System Specification: SmartBin

## 1. Introduction
- **Project Title:** SmartBin: A Campus Sustainability Rewards System
- **Domain:** Internet of Things (IoT) / Smart Campus / Sustainability. This system operates within the context of a university campus, focusing on student engagement and environmental monitoring.
- **Problem Statement:** University campuses generate significant amounts of recyclable waste, but current recycling bins are passive. Students lack a direct incentive to recycle properly, and facilities management has no real-time data on bin status. This system aims to increase recycling rates by introducing a gamified reward system and improve operational efficiency by providing fill-level monitoring.
- **Individual Scope:** This project is feasible for one person over a semester by simulating the hardware components. The "Smart Bin" will be represented by a simple script or a mock API client that sends data to the backend. The focus will be on the backend API, database design, and a basic mobile/web frontend, demonstrating a complete, end-to-end system.

## 2. Functional Requirements (User Stories)
- As a **Student**, I want to register for an account so that I can start earning points.
- As a **Student**, I want to scan a QR code on a bin to identify myself before recycling.
- As a **Student**, I want to receive points instantly when I deposit an item.
- As a **Student**, I want to view my total points and redemption history.
- As a **Student**, I want to see a catalog of rewards I can redeem my points for.
- As an **Admin**, I want to view the current fill-level of all bins on a map/dashboard.
- As an **Admin**, I want to add, update, or remove rewards from the catalog.
- As a **System**, I want to simulate a bin's fill level increasing over time.

## 3. Non-Functional Requirements
- The backend API should respond to requests in under 300ms.
- User data and point totals must be secure and persisted in a database.
- The system architecture should be modular, allowing the simulated "bin" component to be easily replaced with a real hardware client in the future.
- The mobile interface should be simple and intuitive.

## 4. Core Components (End-to-End)
1.  **Mobile/Web Client:** The user interface for students and admins.
2.  **Backend API:** The central server (e.g., using Node.js/Express or Python/Flask) that handles all business logic.
3.  **Database:** (e.g., PostgreSQL or MongoDB) to store user profiles, points, transactions, and reward inventory.
4.  **Smart Bin Simulator:** A simple script (e.g., in Python) that acts as an IoT device, sending "item deposited" and "fill level" data to the API.
