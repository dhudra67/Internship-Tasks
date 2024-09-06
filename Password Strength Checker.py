def check_password_strength(user_password):
    strength_score = 0

    if len(user_password) >= 8:
        strength_score += 2

    if any(character.isupper() for character in user_password):
        strength_score += 2

    if any(character.islower() for character in user_password):
        strength_score += 2

    if any(character.isdigit() for character in user_password):
        strength_score += 2

    special_characters = "!@#$%^&*(),.?\":{}|<>"
    if any(character in special_characters for character in user_password):
        strength_score += 2

    return strength_score


user_input = input("Enter a password: ")
password_strength = check_password_strength(user_input)

print(f"Password strength: {password_strength}/10")

if password_strength <= 4:
    print("Weak password")
elif password_strength <= 6:
    print("Moderate password")
else:
    print("Strong password")
