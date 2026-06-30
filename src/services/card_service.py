from typing import List, Optional
from ..models.student import Student
from ..models.student_card import StudentCard
from .card_validator import CardValidator

class CardService:
    def __init__(self):
        self._cards: list[StudentCard] = []
        self._validator = CardValidator()

    def create_student(self, **kwargs) -> Student:
        return Student(**kwargs)

    def create_card(
            self,
            student: Student,
            expire_years: int = 4,
            card_type: str = "VISA"
    ) -> StudentCard:
        card = StudentCard(
            student=student,
            expire_years=expire_years,
            card_type=card_type
        )
        self._cards.append(card)
        return card

    def get_card_by_student_id(self, student_id: str) -> Optional[StudentCard]:
        for card in self._cards:
            if card.student.student_id == student_id:
                return card
        return  None

    def get_all_cards(self) -> List[StudentCard]:
        return self._cards

    def get_active_cards(self) -> List[StudentCard]:
        return [card for card in self._cards if card.is_valid()]

    def validate_card(self, card: StudentCard) -> dict:
        return self._validator.validate_card(card)

    def renew_card(self, card: StudentCard, additional_years: int = 4) -> StudentCard:
        from datetime import datetime
        card.issue_date = datetime.now()
        card.expire_years = additional_years
        return card

    def get_statistics(self) -> dict:
        total = len(self._cards)
        active = len(self.get_active_cards())
        expired = total - active

        return {
            "total_cards": total,
            "active_cards": active,
            "expired_cards": expired,
        }