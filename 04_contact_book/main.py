def main():
    while True:
        print("""
1. Add
2. Edit
3. Delete
4. Search
5. Show All
6. Exit
""")
        choice = input("Choose: ")

        match choice:
            case "1":
                print("Add")
            case "2":
                print("Edit")
            case "3":
                print("Delete")
            case "4":
                print("Search")
            case "5":
                print("Show All")
            case "6":
                break
            case _:
                print("Invalid choice.")


if __name__ == "__main__":
    main()
