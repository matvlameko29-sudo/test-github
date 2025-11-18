import re
text = input()
sentences = re.split(r'[.!?]', text)
sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
for sentence in sentences:
    print(sentence)
print(f"Предложений в тексте: {len(sentences)}")