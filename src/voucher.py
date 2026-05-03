from enum import Enum
from datetime import datetime, timedelta
from typing import Optional
import uuid


class VoucherStatus(Enum):
    GENERATED = "generated"
    EMAILED = "emailed"
    SCANNED = "scanned"
    VERIFIED = "verified"
    INVALID = "invalid"
    REDEEMED = "redeemed"
    EXPIRED = "expired"


class Voucher:
    def __init__(self, voucher_id: str, user_id: str, reward_id: str, qr_code: str):
        self._voucher_id = voucher_id
        self._user_id = user_id
        self._reward_id = reward_id
        self._qr_code = qr_code
        self._status = VoucherStatus.GENERATED
        self._generated_at = datetime.now()
        self._expires_at = datetime.now() + timedelta(days=30)
        self._redeemed_at = None

    def get_voucher_id(self) -> str:
        return self._voucher_id

    def get_user_id(self) -> str:
        return self._user_id

    def get_reward_id(self) -> str:
        return self._reward_id

    def get_qr_code(self) -> str:
        return self._qr_code

    def get_status(self) -> VoucherStatus:
        return self._status

    def get_expires_at(self) -> datetime:
        return self._expires_at

    @classmethod
    def generate_voucher(cls, user_id: str, reward_id: str) -> 'Voucher':
        voucher_id = str(uuid.uuid4())
        qr_code = f"QR_{voucher_id[:8]}"
        return cls(voucher_id, user_id, reward_id, qr_code)

    def send_email(self) -> bool:
        if self._status == VoucherStatus.GENERATED:
            self._status = VoucherStatus.EMAILED
            print(f"Email sent with QR code: {self._qr_code}")
            return True
        return False

    def scan_qr_code(self, code: str) -> bool:
        if self.check_expiry():
            self._status = VoucherStatus.EXPIRED
            return False
        if self._qr_code == code:
            self._status = VoucherStatus.SCANNED
            return True
        self._status = VoucherStatus.INVALID
        return False

    def verify_voucher(self) -> bool:
        if self.check_expiry():
            self._status = VoucherStatus.EXPIRED
            return False
        if self._status == VoucherStatus.SCANNED:
            self._status = VoucherStatus.VERIFIED
            return True
        return False

    def mark_as_redeemed(self) -> None:
        if self._status == VoucherStatus.VERIFIED:
            self._status = VoucherStatus.REDEEMED
            self._redeemed_at = datetime.now()

    def check_expiry(self) -> bool:
        return datetime.now() > self._expires_at

    def __str__(self) -> str:
        return f"Voucher(id={self._voucher_id}, status={self._status.value})"