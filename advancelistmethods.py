submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
submitted_attended = []
#Task 1
print(submitted is attended)
#Task 2
submitted_attended = set(submitted) & set(attended)
print(submitted_attended)
#Task 3
attended.remove("Charlie")
attended.remove("Frank")
print(attended)

