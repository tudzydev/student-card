from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime

@dataclass()
class Student:
    """Model สํา หรับเก็บขอ้ มูลนกัศึกษํา"""
    student_id: str
    first_name_th: str
    last_name_th: str
    first_name_en: str
    last_name_en: str
    faculty: str
    gener: str
    photo_path: str = "assets/photos/default.jpg"
    university_th: str = "มหําวิทยําลัยรําชภัฏนครปฐม"
    university_en: str = "NAKORN PATHOM RAJBHAT UNIVERSITY"
    created_at: datetime = field(default_factory=datetime.now)

    def get_full_name_th(self) -> str:
        return f"{self.first_name_th} {self.last_name_th}"

    def get_full_name_en(self) -> str:
        return  f"{self.first_name_en} {self.last_name_en}"

    def get_prefix_th(self,gender) -> str:
        if(gender == "ชาย"):
            return "นาย"
        else:
            return "นางสําว"

    def get_prefix_en(self, gender) -> str:
        if(gender == "male"):
            return "Mister"
        else:
            return "Miss"

    def to_dict(self) -> dict:
        return {
            "student_id": self.student_id,
            "first_name_th": self.first_name_th,
            "last_name_th": self.last_name_th,
            "first_name_en": self.first_name_en,
            "last_name_en": self.last_name_en,
            "faculty": self.faculty,
            "photo_path": self.photo_path,
            "full_name_th": self.get_full_name_th(),
            "full_name_en": self.get_full_name_en(),
            "university_th": self.university_th,
            "university_en": self.university_en,
        }

    def __str__(self) -> str:
        return f"Student({self.student_id}: {self.get_full_name_th()})"
    
    def __repr__(self) -> str:
        return self.__str__()