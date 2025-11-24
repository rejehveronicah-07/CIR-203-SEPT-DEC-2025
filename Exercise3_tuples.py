patient = ("John Doe", 45, 120, 80)

print(patient[1])
print(patient[3])
print("Tuples are suitable because vitals should not be altered accidentally.")

patient_list = list(patient)
patient_list[3] = 82
patient = tuple(patient_list)
print(patient)

patients = (
    ("John Doe", 45, 120, 80),
    ("Alice Kim", 30, 110, 75),
    ("Mark Lee", 50, 130, 85),
    ("Susan Ray", 38, 118, 78),
    ("Brian Oduor", 60, 140, 90)
)

names = [p[0] for p in patients]
print(names)
