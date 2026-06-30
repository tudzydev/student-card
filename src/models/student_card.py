from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Optional
import random
from .student import Student

@dataclass
class StudentCard:
    student: Student

    card_number: str = field(default_factory=lambda:
    StudentCard._generate_card_number())

    cvv: str = field(default_factory=lambda:
    StudentCard._generate_cvv())

    issue_date: datetime = field(default_factory=datetime.now)
    expire_years: int = 4
    card_type: str = "VISA"

    @staticmethod
    def _generate_card_number() -> str:
        return f"{random.randint(100,999)}"

    @staticmethod
    def _generate_card_number() -> str:
        prefix = "1234"
        middle = f"{random.randint(1000, 9999)}"
        random1 = f"{random.randint(1000, 9999)}"
        random2 = f"{random.randint(1000, 9999)}"
        return f"{prefix} {middle} {random1} {random2}"

    @staticmethod
    def _generate_cvv() -> str:
        return f"{random.randint(100,999)}"

    @property
    def expire_date(self) -> datetime:
        return self.issue_date + timedelta(days=self.expire_years * 365)

    @property
    def expire_date_thai(self) -> str:
        thai_year = self.expire_date.year + 543 - 2000
        return f"{self.expire_date.strftime('%m')}/{thai_year}"

    @property
    def formatted_card_number(self) -> str:
         return self.card_number

    def is_expired(self) -> bool:
        return datetime.now() > self.expire_date

    def is_valid(self) -> bool:
        return not self.is_expired()

    def get_days_until_expire(self) -> int:
        delta = self.expire_date - datetime.now()
        return max(0, delta.days)

    def to_dict(self) -> dict:
        return {
            "card_number": self.card_number,
            "cvv": self.cvv,
            "issue_date": self.issue_date.isoformat(),
            "expire_date": self.expire_date.isoformat(),
            "expire_date_thai": self.expire_date_thai,
            "card_type": self.card_type,
            "is_valid": self.is_valid(),
            "days_until_expire": self.get_days_until_expire(),
            "student": self.student.to_dict(),
        }

    def __str__(self) -> str:
        return f"Card({self.card_number} - {self.student.student_id})"