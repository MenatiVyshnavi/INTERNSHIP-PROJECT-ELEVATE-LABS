from zxcvbn import zxcvbn
import math

def calc_entropy(pw: str) -> float:
    pool = 0
    if any(c.islower() for c in pw):
        pool += 26
    if any(c.isupper() for c in pw):
        pool += 26
    if any(c.isdigit() for c in pw):
        pool += 10
    # approximate symbol count
    if any(not c.isalnum() for c in pw):
        pool += 32
    if pool == 0:
        return 0.0
    return round(len(pw) * math.log2(pool), 2)

def leet_variations(word: str):
    subs = {'a':'@', 'A':'@', 'o':'0', 'O':'0', 'e':'3', 'E':'3', 's':'$', 'S':'$',
            'i':'1', 'I':'1', 't':'7', 'T':'7'}
    variations = set()
    variations.add(word)
    # single substitutions
    for k,v in subs.items():
        variations.add(word.replace(k, v))
    # capitalized and reversed
    variations.add(word.title())
    variations.add(word[::-1])
    return variations

print("===== PASSWORD STRENGTH ANALYZER =====")
password = input("Enter a password to check its strength: ")

# zxcvbn analysis
result = zxcvbn(password)
score = result['score']

# entropy calculation
entropy = calc_entropy(password)

print("\nPassword Strength Score (0-4):", score)
print(f"Estimated entropy (bits): {entropy}")
if entropy < 28 or score <= 1:
    print("🔴 Weak password. Try making it longer and include mixed character types.")
elif entropy < 50 or score == 2:
    print("🟡 Medium strength. Add more length or unique characters.")
else:
    print("🟢 Strong password! Good length and variety.")

print("\nFeedback (zxcvbn):")
for msg in result['feedback']['suggestions']:
    print("-", msg)

# Wordlist generator with leet & patterns
print("\n===== CUSTOM WORDLIST GENERATOR =====")
name = input("Enter your first name (or Enter any name): ").strip()
pet = input("Enter pet's name (or type None): ").strip()
year = input("Enter birth year (or Enter your favorite number): ").strip()

base_words = [w for w in [name, pet] if w]
# include parts of name (first 3 letters) optionally
if name and len(name) >= 3:
    base_words.append(name[:3])
if pet and len(pet) >= 3:
    base_words.append(pet[:3])

suffixes = ['', '123', '2025', '!', '@', '#']
wordlist = set()

for w in base_words:
    # basic variants
    for v in leet_variations(w):
        for s in suffixes:
            wordlist.add(v + s)
            if year:
                wordlist.add(v + year)
                wordlist.add(v + s + year)

# mix name+pet combinations
if name and pet:
    combos = [name+pet, pet+name, name+pet+year, pet+name+year]
    for c in combos:
        for v in leet_variations(c):
            wordlist.add(v)

# ensure we don't create a huge list
wordlist = list(wordlist)[:200]  # limit to first 200 items

print("\nGenerated Wordlist (sample):")
for w in wordlist[:30]:
    print(w)
print(f"\nTotal generated (limited): {len(wordlist)}")

# save to file
filename = "wordlist_amrutha.txt"
with open(filename, "w") as f:
    for w in wordlist:
        f.write(w + "\n")

print(f"\nWordlist saved to '{filename}'")
print("Project completed successfully!")

