import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from src.models.student import Student
from src.models.student_card import StudentCard
from src.services.card_service import CardService
from src.views.card_renderor import CardRenderer

def main():
    print("=" * 60)
    print("ระบบจัดกํารบัตรนักศึกษํา - มหําวิทยําลัยรําชภัฏนครปฐม")
    print("=" * 60)

service = CardService()
student_data = {
    "student_id": "67123456",
    "first_name_th": "ลิซ่ํา",
    "last_name_th": "Blackpink",
    "first_name_en": "Lisa",
    "last_name_en": "Blackpink",
    "faculty": "คณะวิทยําศําสตร์และเทคโนโลยี",
    "photo_path": "assets/photos/lisa.jpg",
    "gener": "female",
}

student = service.create_student(**student_data)
print(f"\n✅ สร้ํางนักศึกษํา: {student}")

card = service.create_card(student, expire_years=4, card_type="VISA")
print(f"✅ สร้ํางบัตร: {card}")

validation = service.validate_card(card)
print(f"\n📋 ผลกํารตรวจสอบบัตร:")
print(f" Valid: {validation['is_valid']}")

if validation['errors']:
    print(f" Errors: {validation['errors']}")
if validation['warnings']:
    print(f" Warnings: {validation['warnings']}")

print(f"\n📄 ข้อมูลบัตร:")
print(f" Card Number: {card.formatted_card_number}")
print(f" CVV: {card.cvv}")
print(f" Issue Date: {card.issue_date.strftime('%d/%m/%Y')}")
print(f" Expire Date: {card.expire_date_thai}")
print(f" Days Until Expire: {card.get_days_until_expire()}")

renderer = CardRenderer(card)
print(f"\n{renderer.render_text()}")

html_content = renderer.render_html()
output_file = "student_card.html"
with open(output_file, "w", encoding="utf-8") as f:f.write(html_content)
print(f"✅ สร้ํางไฟล์ HTML: {output_file}")

stats = service.get_statistics()
print(f"\n สถิติ:")
print(f" Total Cards: {stats['total_cards']}")
print(f" Active Cards: {stats['active_cards']}")
print(f" Expired Cards: {stats['expired_cards']}")

if __name__ == "__main__":
    main()