class std_card:
  def __init__(self, std_id, name, faculty, major):
    self.std_id = std_id,
    self.name = name,
    self.faculty = faculty,
    self.major = major,

  def display(self):
    print("===== Student ID Card =====")
    print(f"Student ID : {self.std_id}")
    print(f"Name       : {self.name}")
    print(f"Faculty    : {self.faculty}")
    print(f"Major      : {self.major}")

std1 = std_card(
    "674259009",
    "Narongsak Pumpasert",
    "SciTech",
    "Software Engneering"
)

print(std1.display())