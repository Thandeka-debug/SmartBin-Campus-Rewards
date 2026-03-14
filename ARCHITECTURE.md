classDiagram
%% Combined SmartBin Architecture (Levels 1-4)

%% Level 1: System Context
class Student {
    <<Person>>
    "Wants to recycle and earn rewards"
}
class FacilitiesAdmin {
    <<Person>>
    "Monitors bin status and manages rewards"
}
class SmartBinSystem {
    <<System>>
    "Earn points for recycling, monitor bins"
}
class CampusIDService {
    <<External System>>
    "Auth for student IDs"
}
class PushNotificationService {
    <<External System>>
    "Sends alerts for bin status and rewards"
}

%% Level 2: Containers
class MobileApp {
    <<Container>>
    "Flutter/React Native, scan QR, view points, admin dashboard"
}
class WebAdminPanel {
    <<Container>>
    "React, monitor bins, manage rewards"
}
class BackendAPI {
    <<Container>>
    "Node.js/Express, business logic: users, points, rewards, bin data"
}
class Database {
    <<ContainerDB>>
    "PostgreSQL, stores profiles, points, transactions, bins, rewards"
}
class BinSimulator {
    <<Container>>
    "Python script, simulates IoT events"
}

%% Level 3: Components (Backend API)
class UserController {
    <<Component>>
    "User registration, login, profile"
}
class PointsController {
    <<Component>>
    "Award points, check balance, history"
}
class RewardsController {
    <<Component>>
    "Manage reward catalog and redemption"
}
class BinController {
    <<Component>>
    "Receive bin simulator events"
}
class AuthMiddleware {
    <<Component>>
    "JWT token verification"
}
class ServiceLayer {
    <<Component>>
    "Business logic orchestrator"
}
class RepositoryLayer {
    <<Component>>
    "Database access abstraction"
}

%% Level 4: Classes inside Points Controller
class PointsService {
    -pointsRepository: PointsRepository
    -userRepository: UserRepository
    -transactionRepository: TransactionRepository
    +calculatePoints(itemType: String): int
    +addPoints(userId: String, points: int): Transaction
}
class PointsRepository {
    +findByUserId(userId: String): UserPoints
}
class TransactionRepository {
    +create(transaction: Transaction): Transaction
}
class UserRepository {
    +findById(userId: String): User
}
class PointsValidator {
    +validateItemType(itemType: String): boolean
}
class Transaction {
    +id: String
    +userId: String
    +points: int
    +type: "EARN"|"REDEEM"
}
class UserPoints {
    +userId: String
    +currentBalance: int
}

%% Relationships Level 1
Student --> SmartBinSystem : "interacts with"
FacilitiesAdmin --> SmartBinSystem : "manages"
SmartBinSystem --> CampusIDService : "verifies identity"
SmartBinSystem --> PushNotificationService : "sends notifications"

%% Relationships Level 2
Student --> MobileApp : "uses"
FacilitiesAdmin --> WebAdminPanel : "uses"
MobileApp --> BackendAPI : "API calls"
WebAdminPanel --> BackendAPI : "API calls"
BinSimulator --> BackendAPI : "sends events"
BackendAPI --> Database : "reads/writes"

%% Relationships Level 3
MobileApp --> UserController : "login/register"
MobileApp --> PointsController : "get balance"
MobileApp --> RewardsController : "redeem points"
BinSimulator --> BinController : "deposit events"
UserController --> ServiceLayer : "uses"
PointsController --> ServiceLayer : "uses"
RewardsController --> ServiceLayer : "uses"
BinController --> ServiceLayer : "uses"
ServiceLayer --> RepositoryLayer : "uses"
RepositoryLayer --> Database : "accesses"
UserController --> AuthMiddleware : "protected by"
PointsController --> AuthMiddleware : "protected by"
RewardsController --> AuthMiddleware : "protected by"

%% Relationships Level 4
PointsController --> PointsService : "uses"
PointsService --> PointsRepository : "uses"
PointsService --> TransactionRepository : "uses"
PointsService --> UserRepository : "uses"
PointsService --> PointsValidator : "uses"
PointsService ..> Transaction : "creates"
PointsRepository ..> UserPoints : "persists"
TransactionRepository ..> Transaction : "persists"
UserPoints --> Transaction : "references"
