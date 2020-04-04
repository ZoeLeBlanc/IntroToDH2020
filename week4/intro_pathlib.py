from pathlib import Path

file = Path('PrideandPrejudice.txt')


text = file.read_text()
text = text.replace('man', 'person').replace('woman', 'partner')

# print(text)
file.write_text(text)