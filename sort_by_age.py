
def sort_by_age(people):
    return sorted(people, key=lambda x: x[1])


people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
print(f"Sorted by age: {sort_by_age(people)}")
