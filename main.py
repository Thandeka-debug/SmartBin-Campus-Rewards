"""
SmartBin REST API - FastAPI Application
"""
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

from services.user_service import UserService
from services.reward_service import RewardService
from services.smart_bin_service import SmartBinService

# Initialize FastAPI app
app = FastAPI(
    title="SmartBin API",
    description="REST API for SmartBin Campus Sustainability Rewards System",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
user_service = UserService()
reward_service = RewardService()
bin_service = SmartBinService()

# ==================== Request/Response Models ====================

class CreateUserRequest(BaseModel):
    user_id: str
    email: str
    name: str
    role: str = "student"

class UserResponse(BaseModel):
    user_id: str
    email: str
    name: str
    role: str
    points_balance: int
    status: str

class CreateRewardRequest(BaseModel):
    reward_id: str
    name: str
    point_cost: int
    inventory: int

class RewardResponse(BaseModel):
    reward_id: str
    name: str
    point_cost: int
    inventory_count: int
    status: str

class RedeemRequest(BaseModel):
    user_id: str
    reward_id: str

class RedeemResponse(BaseModel):
    voucher_id: str
    qr_code: str
    points_deducted: int
    remaining_points: int

class CreateBinRequest(BaseModel):
    bin_id: str
    location: str

class BinResponse(BaseModel):
    bin_id: str
    location: str
    fill_level: int
    status: str
    status_color: str

class DepositRequest(BaseModel):
    user_id: str
    bin_id: str
    item_type: str

class DepositResponse(BaseModel):
    transaction_id: str
    points_earned: int
    bin_fill_level: int
    message: str

class UpdateFillLevelRequest(BaseModel):
    fill_level: int

# ==================== User Endpoints ====================

@app.post("/api/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED, tags=["Users"])
async def create_user(request: CreateUserRequest):
    try:
        user = user_service.create_user(request.user_id, request.email, request.name, request.role)
        return UserResponse(
            user_id=user.get_user_id(),
            email=user.get_email(),
            name=user.get_name(),
            role=user.get_role().value,
            points_balance=user.get_points_balance(),
            status=user.get_status().value
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/api/users", response_model=List[UserResponse], tags=["Users"])
async def get_all_users():
    users = user_service.get_all_users()
    return [
        UserResponse(
            user_id=u.get_user_id(),
            email=u.get_email(),
            name=u.get_name(),
            role=u.get_role().value,
            points_balance=u.get_points_balance(),
            status=u.get_status().value
        ) for u in users
    ]

@app.get("/api/users/{user_id}", response_model=UserResponse, tags=["Users"])
async def get_user_by_id(user_id: str):
    try:
        user = user_service.get_user_by_id(user_id)
        return UserResponse(
            user_id=user.get_user_id(),
            email=user.get_email(),
            name=user.get_name(),
            role=user.get_role().value,
            points_balance=user.get_points_balance(),
            status=user.get_status().value
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.delete("/api/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Users"])
async def delete_user(user_id: str):
    try:
        user_service.delete_user(user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

# ==================== Reward Endpoints ====================

@app.post("/api/rewards", response_model=RewardResponse, status_code=status.HTTP_201_CREATED, tags=["Rewards"])
async def create_reward(request: CreateRewardRequest):
    try:
        reward = reward_service.create_reward(request.reward_id, request.name, request.point_cost, request.inventory)
        return RewardResponse(
            reward_id=reward.get_reward_id(),
            name=reward.get_name(),
            point_cost=reward.get_point_cost(),
            inventory_count=reward.get_inventory_count(),
            status=reward.get_status().value
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/api/rewards", response_model=List[RewardResponse], tags=["Rewards"])
async def get_all_rewards():
    rewards = reward_service.get_all_rewards()
    return [
        RewardResponse(
            reward_id=r.get_reward_id(),
            name=r.get_name(),
            point_cost=r.get_point_cost(),
            inventory_count=r.get_inventory_count(),
            status=r.get_status().value
        ) for r in rewards
    ]

@app.get("/api/rewards/available", response_model=List[RewardResponse], tags=["Rewards"])
async def get_available_rewards():
    rewards = reward_service.get_available_rewards()
    return [
        RewardResponse(
            reward_id=r.get_reward_id(),
            name=r.get_name(),
            point_cost=r.get_point_cost(),
            inventory_count=r.get_inventory_count(),
            status=r.get_status().value
        ) for r in rewards
    ]

@app.post("/api/rewards/redeem", response_model=RedeemResponse, tags=["Rewards"])
async def redeem_reward(request: RedeemRequest):
    try:
        result = reward_service.redeem_reward(request.user_id, request.reward_id)
        return RedeemResponse(
            voucher_id=result["voucher_id"],
            qr_code=result["qr_code"],
            points_deducted=result["points_deducted"],
            remaining_points=result["remaining_points"]
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/api/rewards/{reward_id}/publish", response_model=RewardResponse, tags=["Rewards"])
async def publish_reward(reward_id: str):
    try:
        reward = reward_service.publish_reward(reward_id)
        return RewardResponse(
            reward_id=reward.get_reward_id(),
            name=reward.get_name(),
            point_cost=reward.get_point_cost(),
            inventory_count=reward.get_inventory_count(),
            status=reward.get_status().value
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

# ==================== SmartBin Endpoints ====================

@app.post("/api/bins", response_model=BinResponse, status_code=status.HTTP_201_CREATED, tags=["Bins"])
async def create_bin(request: CreateBinRequest):
    try:
        bin = bin_service.create_bin(request.bin_id, request.location)
        return BinResponse(
            bin_id=bin.get_bin_id(),
            location=bin.get_location(),
            fill_level=bin.get_fill_level(),
            status=bin.get_status().value,
            status_color=bin.get_status_color()
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/api/bins", response_model=List[BinResponse], tags=["Bins"])
async def get_all_bins():
    bins = bin_service.get_all_bins()
    return [
        BinResponse(
            bin_id=b.get_bin_id(),
            location=b.get_location(),
            fill_level=b.get_fill_level(),
            status=b.get_status().value,
            status_color=b.get_status_color()
        ) for b in bins
    ]

@app.get("/api/bins/{bin_id}", response_model=BinResponse, tags=["Bins"])
async def get_bin_by_id(bin_id: str):
    try:
        bin = bin_service.get_bin_by_id(bin_id)
        return BinResponse(
            bin_id=bin.get_bin_id(),
            location=bin.get_location(),
            fill_level=bin.get_fill_level(),
            status=bin.get_status().value,
            status_color=bin.get_status_color()
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.put("/api/bins/{bin_id}/fill-level", response_model=BinResponse, tags=["Bins"])
async def update_fill_level(bin_id: str, request: UpdateFillLevelRequest):
    try:
        bin = bin_service.update_bin_fill_level(bin_id, request.fill_level)
        return BinResponse(
            bin_id=bin.get_bin_id(),
            location=bin.get_location(),
            fill_level=bin.get_fill_level(),
            status=bin.get_status().value,
            status_color=bin.get_status_color()
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/bins/deposit", response_model=DepositResponse, tags=["Bins"])
async def deposit_item(request: DepositRequest):
    try:
        result = bin_service.deposit_item(request.user_id, request.bin_id, request.item_type)
        return DepositResponse(
            transaction_id=result["transaction_id"],
            points_earned=result["points_earned"],
            bin_fill_level=result["bin_fill_level"],
            message=result["message"]
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/bins/{bin_id}/empty", response_model=BinResponse, tags=["Bins"])
async def empty_bin(bin_id: str):
    try:
        bin = bin_service.empty_bin(bin_id)
        return BinResponse(
            bin_id=bin.get_bin_id(),
            location=bin.get_location(),
            fill_level=bin.get_fill_level(),
            status=bin.get_status().value,
            status_color=bin.get_status_color()
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/api/bins/needs-emptying", response_model=List[BinResponse], tags=["Bins"])
async def get_bins_needing_emptying(threshold: int = 80):
    bins = bin_service.get_bins_needing_emptying(threshold)
    return [
        BinResponse(
            bin_id=b.get_bin_id(),
            location=b.get_location(),
            fill_level=b.get_fill_level(),
            status=b.get_status().value,
            status_color=b.get_status_color()
        ) for b in bins
    ]

# ==================== Root Endpoint ====================

@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "Welcome to SmartBin API",
        "docs": "/docs",
        "redoc": "/redoc",
        "version": "1.0.0"
    }