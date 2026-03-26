# Use Case Diagram: SmartBin System

## Diagram

```mermaid
graph TB
    subgraph Actors
        User[System User]
        Student[Student]
        FacilitiesAdmin[Facilities Admin]
        SustainabilityOfficer[Sustainability Officer]
        ITAdmin[IT Administrator]
        FinanceOffice[Finance Office]
        DiningServices[Dining Services]
    end

    %% Generalization - Student is a type of System User
    User --> Student

    subgraph SmartBin System
        Register[Register Account]
        Login[Login / Authenticate]
        ScanBin[Scan Bin QR Code]
        DepositItem[Deposit Recyclable Item]
        ViewPoints[View Points Balance]
        ViewHistory[View Transaction History]
        ViewLeaderboard[View Leaderboard]
        RedeemReward[Redeem Reward]
        ViewRewardCatalog[View Reward Catalog]
        MonitorBins[Monitor Bin Fill Levels]
        ReceiveAlerts[Receive Fill-Level Alerts]
        ManageRewards[Manage Reward Catalog]
        ViewAnalytics[View Recycling Analytics]
        GenerateReports[Generate Sustainability Reports]
        ManageBudget[Manage Reward Budget]
        VerifyVoucher[Verify Redemption Voucher]
    end

    Student --> Register
    Student --> Login
    Student --> ScanBin
    Student --> DepositItem
    Student --> ViewPoints
    Student --> ViewHistory
    Student --> ViewLeaderboard
    Student --> RedeemReward
    Student --> ViewRewardCatalog

    FacilitiesAdmin --> MonitorBins
    FacilitiesAdmin --> ReceiveAlerts

    SustainabilityOfficer --> ViewAnalytics
    SustainabilityOfficer --> GenerateReports

    ITAdmin --> MonitorBins
    ITAdmin --> ReceiveAlerts

    FinanceOffice --> ManageBudget
    FinanceOffice --> GenerateReports

    DiningServices --> ManageRewards
    DiningServices --> VerifyVoucher

    %% Include relationships
    RedeemReward -.-> |<<includes>>| ViewRewardCatalog
    RedeemReward -.-> |<<includes>>| ViewPoints
    DepositItem -.-> |<<includes>>| ViewPoints
    ScanBin -.-> |<<includes>>| Login
    GenerateReports -.-> |<<includes>>| ViewAnalytics
    VerifyVoucher -.-> |<<includes>>| ViewPoints
