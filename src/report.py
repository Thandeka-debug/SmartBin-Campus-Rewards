from enum import Enum
from datetime import datetime
from typing import Dict, Any
import uuid


class ReportType(Enum):
    RECYCLING_SUMMARY = "recycling_summary"
    PARTICIPATION_RATES = "participation_rates"
    ENVIRONMENTAL_IMPACT = "environmental_impact"


class ReportStatus(Enum):
    DRAFT = "draft"
    GENERATING = "generating"
    GENERATED = "generated"
    FAILED = "failed"
    DOWNLOADED = "downloaded"
    EMAILED = "emailed"


class Report:
    def __init__(self, report_id: str, report_type: ReportType, generated_by: str):
        self._report_id = report_id
        self._report_type = report_type
        self._date_range_start = None
        self._date_range_end = None
        self._data = None
        self._status = ReportStatus.DRAFT
        self._generated_at = None
        self._generated_by = generated_by

    def get_report_id(self) -> str:
        return self._report_id

    def get_status(self) -> ReportStatus:
        return self._status

    def select_parameters(self, start_date: datetime, end_date: datetime) -> None:
        self._date_range_start = start_date
        self._date_range_end = end_date

    def generate_report(self) -> Dict[str, Any]:
        if self._status != ReportStatus.DRAFT:
            raise Exception("Report already generated")
        
        self._status = ReportStatus.GENERATING
        
        self._data = {
            "report_id": self._report_id,
            "type": self._report_type.value,
            "start_date": str(self._date_range_start),
            "end_date": str(self._date_range_end),
            "total_recycling": 1000,
            "participation_rate": 45,
            "co2_saved": 500
        }
        
        self._status = ReportStatus.GENERATED
        self._generated_at = datetime.now()
        return self._data

    def export_to_csv(self) -> str:
        if self._status != ReportStatus.GENERATED:
            raise Exception("Report not generated yet")
        self._status = ReportStatus.DOWNLOADED
        return f"report_{self._report_id}.csv"

    def export_to_pdf(self) -> str:
        if self._status != ReportStatus.GENERATED:
            raise Exception("Report not generated yet")
        self._status = ReportStatus.DOWNLOADED
        return f"report_{self._report_id}.pdf"

    def send_email(self, stakeholder_email: str) -> bool:
        if self._status != ReportStatus.GENERATED:
            raise Exception("Report not generated yet")
        self._status = ReportStatus.EMAILED
        print(f"Report emailed to {stakeholder_email}")
        return True

    def __str__(self) -> str:
        return f"Report(id={self._report_id}, type={self._report_type.value}, status={self._status.value})"