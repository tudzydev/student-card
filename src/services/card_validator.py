from typing import List, Dict, Any
from ..models.student_card import  StudentCard

class CardValidator:
    @staticmethod
    def validate_card(card: StudentCard) -> Dict[str, Any]:
        errors = []
        warnings = []

        if not card.student.student_id:
            errors.append("รหัสนกัศึกษําวํา่ งเปล่ํา")

        if len(card.student.student_id) < 8:
            errors.append("รหัสนกัศึกษําตอ้งมีควํามยําวอยํา่ งนอ้ย 8 หลัก"
                          )
        if not card.student.first_name_th or not card.student.last_name_th:
            errors.append("ชื่อ-สกุล ภําษําไทยไม่ครบถว้น")

        if not card.student.first_name_en or not card.student.last_name_en:
            errors.append("ชื่อ-สกุล ภําษําองักฤษไม่ครบถว้น")

        if not card.card_number:
            errors.append("หมํายเลขบตัรวํา่ งเปล่ํา")

        card_digits = card.card_number.replace(" ", "")
        if len(card_digits) != 16:
            errors.append("หมํายเลขบัตรต้องมีควํามยําว 16 หลัก")

        if card.is_expired():
            errors.append("บัตรหมดอํายุแล้ว")
        elif card.get_days_until_expire() < 30:
            warnings.append("บัตรจะหมดอํายุในอีก 30 วัน")

        return {
            "is_valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings,
        }

    @staticmethod
    def validata_card_number(card_number: str) -> bool:
        digits = card_number.replace(" ", "")
        if not digits.isdigit() or len(digits) != 16 :
            return  False

        total = 0
        revers_digits = digits[::-1]

        for i, digit in enumerate(revers_digits):
            n = int(digit)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            total += n

        return total % 10 == 0