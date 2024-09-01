

def sort_by_age(people):
    return sorted(people, key=lambda x: x[1])


if __name__ == "__main__":
    people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
    print("sort_by_age(people):", sort_by_age(people))  
