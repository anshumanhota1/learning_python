def calculate_love_score(name1, name2):
    # Step 1: Combine and lowercase the names
    combined_names = (name1 + name2).lower()

    # Step 2: Count letters in 'TRUE'
    true_count = sum(combined_names.count(letter) for letter in "true")
    
    # Step 3: Count letters in 'LOVE'
    love_count = sum(combined_names.count(letter) for letter in "love")
    
    # Step 4: Combine counts to form the score
    love_score = int(f"{true_count}{love_count}")
    
    # Step 5: Print the result
    print(f"Your love score is: {love_score}")


calculate_love_score("Anshuman", "Swapanarani")