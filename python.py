def validate_password(password):
    if len(password) != 10:
        return "Invalid password"
    for i in range(7):
        consecutive_chars = password[i:i+4]
        if consecutive_chars.isalpha() or consecutive_chars.isdigit():
            return "Weak"
    return "Strong"

password = "AbcDefGhiJ"
result1 = validate_password(password)

print(result1)