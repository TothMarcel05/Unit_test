def categorize_by_age(age):
    if 0 <= age <=9:
        return "Child"
    elif 10 <= age <= 18:
        return "Teenager"
    elif 19 <= age <= 65:
        return "Adult"
    elif 65 < age <= 125:
        return "Golden Age"
    else:
        return f"This is not a valid age: {age}!"