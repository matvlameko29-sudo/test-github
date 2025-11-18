def create_abbreviation(text):
    words = text.split()
    abbreviation = ""
    for word in words:
        if len(word) >= 3:
            abbreviation += word[0].upper()
    return abbreviation
print(create_abbreviation("New York City"))  # NYC

print(create_abbreviation("Yanka Kupala State University of Grodno"))  # YKSUG
