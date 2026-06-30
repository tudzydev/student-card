import pytest
from src.models.student import Student

class TestStudent:
    def test_create_student(self):
        student = Student(
            student_id="67123456",
            first_name_th="ลิซ่ํา",
            last_name_th="Blackpink",
            first_name_en="Lisa",
            last_name_en="Blackpink",
            faculty="วิทยําศําสตร์",
            gener="female"
        )

        assert student.student_id == "67123456"
        assert student.get_full_name_th() == "ลิซ่ํา Blackpink"
        assert student.get_full_name_en() == "Lisa Blackpink"

    def test_student_to_dict(self):
        student = Student(
            student_id="67123456",
            first_name_th="ลิซ่ํา",
            last_name_th="Blackpink",
            first_name_en="Lisa",
            last_name_en="Blackpink",
            faculty="วิทยําศําสตร์",
            gener="female"
        )
        data = student.to_dict()
        assert "student_id" in data
        assert "full_name_th" in data
        assert "full_name_en" in data