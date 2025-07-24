
import os
import random
import string
import unicodedata # Not directly used in the provided code, but often useful for normalizing strings.
import re # For WordWord capitalization (CamelCase-like)

# ==============================================================================
# ArbRock Passlist Generator - Custom Targeted Password Wordlist Generator
# ==============================================================================
# Author: AAMBS & Balsinglawi
# License: MIT License (A common open-source license. Consider adding a LICENSE file)
#          (You can explicitly state this or add a separate LICENSE.md file)
#
# Description:
# This script generates a highly customized password wordlist based on various common
# password patterns, regional data (e.g., UAE-centric names, cities, common phrases),
# and common password variations (leet speak, case changes, affixes).
#
# Purpose:
# The primary goal is to create a more effective wordlist for password cracking
# and penetration testing by mimicking how real users construct their passwords,
# rather than relying on purely random character combinations. It leverages known
# human tendencies (using personal info, common words, simple number/symbol additions)
# and regional popularity.
#
# Usage:
# 1. Ensure you have Python 3 installed.
# 2. (Optional but recommended) Create a virtual environment:
#    `python3 -m venv venv`
#    `source venv/bin/activate` (Linux/macOS) or `.\venv\Scripts\activate` (Windows)
# 3. No specific libraries to install via pip for this script beyond standard Python.
# 4. Run the script: `python3 your_script_name.py`
# 5. The generated passwords will be saved to the file specified in `output_filename`.
#
# Configuration:
# Adjust `target_password_count` and `pattern_weights` in the CONFIGURATION section
# to control the size and composition of the generated wordlist.
# ==============================================================================


# --- Base Data Lists ---
# These lists are the foundational building blocks for generating passwords.
# They are expanded with relevant local (e.g., UAE, Indian subcontinent, Filipino)
# and international common data to reflect diverse user bases.
# ==============================================================================
family_names = [
    "AlAbdullah", "AlMansoori", "AlMarri", "AlMazrouei", "AlNuaimi", "AlFalasi",
    "AlQubaisi", "AlKusaibi", "AlRomaithi", "AlAli", "AlGhfuli",
    "AlMussabi", "AlShehhi", "AlBalooshi", "AlMuhairi", "AlOwais", "AlDhaheri",
    "AlSuwaidi", "AlJunaibi", "AlKaabi", "AlShamsi", # UAE/GCC specific
    "Khan", "Singh", "Sharma", "Patel", "Kumar", "Ali", "Shah", "Ahmed", "Rizvi",
    "Chowdhury", "Bhatia", "Siddiqui", "Malik", "Rahman", "Hussain", "Qureshi",
    "Desai", "Joshi", "Chatterjee", "Gupta", "Mehta", "Saxena", "Ismail", "Shaikh", # Indian/Pakistani/South Asian
    "Santos", "Cruz", "Reyes", "Ramos", "Mendoza", "Gonzales", "Garcia", "Aquino",
    "Fernandez", "Dela Cruz", "Villanueva", "Bautista", "Santiago", "Tolentino", # Filipino/Hispanic
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Wilson",
    "Taylor", "Anderson", "Thomas", "Harris", "Martin", "Thompson", "Moore", # Western common
    "Ibrahim", "Mohammed", "Abdullah", "Mahmoud", "Hassan", "Hussein", "Khalid",
    "Saleh", "Othman", "Mubarak", "Suleiman", "Habib", "Nasser", "Saeed", "Salim" # General Arabic/Muslim
]
personal_names = [
    "Mohammed", "Ahmed", "Ali", "Omar", "Abdullah", "Saeed", "Khalid", "Rashid",
    "Hamad", "Yusuf", "Ibrahim", "Hassan", "Hasan", "Fatima", "Aisha", "Mariam",
    "Noura", "Hessa", "Moza", "Latifa", "Amna", "Hind", "Meera", "Shamsa", "Maitha", # UAE/GCC specific
    "Raj", "Rahul", "Amit", "Arjun", "Sunil", "Vikram", "Ravi", "Anand", "Deepak",
    "Priya", "Neha", "Anjali", "Kavita", "Sunita", "Pooja", "Divya", "Sneha", # Indian
    "Juan", "Jose", "Miguel", "Maria", "Rosa", "Lourdes", "Juana", "Margarita", # Hispanic
    "John", "David", "Michael", "James", "Robert", "Mary", "Sarah", "Emma", "Emily" # Western common
]
city_names = [
    "Dubai", "AbuDhabi", "Sharjah", "Ajman", "Fujairah", "RAK", "UAQ", "AlAin",
    "KhorFakkan", "Dibba", "MadinatZayed", "Ruwais", "Liwa", "Dhaid", "Hatta", # UAE specific
    "Mumbai", "Delhi", "Karachi", "Lahore", "Manila", "Cairo", "Riyadh", "Doha",
    "Tehran", "Kabul", "Amman", "Beirut", "London", "NewYork", "Toronto", "Sydney",
    "Toronto", 'Quebec', 'Tokyo', 'Kyoto', 'Osaka' # International major cities
]
common_passwords = [
    "123456", "qwerty", "password", "abc123", "letmein", "admin", "welcome",
    "monkey", "sunshine", "princess", "superman", "hello", "iloveyou", "pass",
    "football", "dragon", "baseball", "123123", "654321", "trustno1", "hunter",
    "jordan23", "111111", "222222", "333333", "monkey123", "love123", "passw0rd",
    "abcd1234", "qwerty123", "1q2w3e4r", "zxcvbnm", "asdfghjkl", "123qwe", "abcdef",
    "qazwsx", "1234qwer", "1q2w3e", "qweasd", "killer", "forever", "12345678",
    "password1", "loveyou", "whatever", "hello123", "mypass", "123321", "qwe123",
    "dragon1", "flower", "babygirl", "angel", "lovely", "devil", "jinx", "blessed",
    "success", "winner", "champion", "master", "secret", "shadow", "diamond", "star" # A mix of very common and simple words
]
common_words = [
    "habibi", "marhaba", "salam", "shukran", "inshallah", "yalla", "khalas",
    "habibti", "mashallah", "alhamdulillah", "wallah", "mabrook", "hasanat",
    "hayati", "sadiq", "sadiqi", "noor", "jameel", "aziz", "afwan", "sabah",
    "masaa", "layla", # Arabic common words
    "expo2020", "burjkhalifa", "palmjumeirah", "emirates",
    "etihad", "sheikh", "desert", "camel", "falcon", "dune", "abudhabi2030", # UAE specific terms
    "love", "life", "happy", "peace", "freedom", "hope", "dream", "faith", "best",
    "football", "soccer", "cricket", "tennis", "uae", "emirates", "arab", "muslim",
    "islam", "friend", "family", "money", "work", "home", "heart", "smile", "cool" # General English/common concepts
]
sports_teams = [
    "AlAhli", "AlWasl", "AlNasr", "AlJazira", "AlWahda", "AlSharjah", "AlDhafra",
    "EmiratesFC", "Shabab", "AlAin", # UAE Football Teams
    "Barcelona", "RealMadrid", "ManchesterUnited",
    "Liverpool", "Chelsea", "Arsenal", "Bayern", "PSG", "Juventus", "ACMilan", # Major European Football
    "CSK", "MumbaiIndians", "RCB", "KKR", "DelhiCapitals", # IPL Cricket Teams
    "Lakers", "Bulls" # NBA Teams
]
uae_references = [
    "Expo2020", "BurjKhalifa", "PalmJumeirah", "BurjAlArab", "Ferrari", "YasIsland",
    "GlobalVillage", "DubaiMall", "Emirates", "Etihad", "National", "UAE",
    "DubaiCreek", "SheikhZayed", "Corniche", "MarinaBeach", "JBR", "DesertSafari",
    "Atlantis", "KhalifaUniversity", "NYUAD", "AUS", "ZayedUniversity", "UAEU",
    "ADNOC", "Aramex", "Careem", "NoonAcademy", "SouqAl", "DubaiRun", "AbuDhabiGP", "UAE" # More UAE specific references
]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
years = [str(y) for y in range(1970, 2027)] # Range of common birth/creation years
special_years = ["2000", "2010", "2015", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025", '1990', '1995', '1998', '1999'] # Frequently used years
love_expressions = ["love", "heart", "forever", "always", "mylove", "4ever", "143", "ily", "iloveu", "habibi", "hayati"]
pet_names = ["kitty", "cat", "dog", "puppy", "tiger", "lion", "eagle", "falcon", "wolf", "horse", "luna", "happy", 'milk', 'brownsugar', 'sugar', 'cupcake', "bella", "max", "charlie"]
emotions = ["happy", "smile", "lucky", "blessed", "cool", "best", "sweet", "cute", "strong", "free"]
special_chars = ["!", "@", "#", "$", "%", "^", "&", "*", "?", "_", "-"] # Common special characters
common_affixes = ["1", "123", "!", "!!", "?", ".", "_", "#", "786", "007", "2023", "2024", "2025", "01", "10", "99"] # Common numeric/symbolic suffixes/prefixes
digits = string.digits
lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase
letters = string.ascii_letters
# --- End of Base Data Lists ---


# --- Configuration ---
# These parameters control the overall generation process.
# ==============================================================================
output_filename = "ArbRock.txt" # The name of the output wordlist file.
target_password_count = 1500000 # The desired number of unique passwords to generate.

# Relative weights for different password patterns.
# A higher weight means that pattern type will be generated more frequently.
# These weights are tuned to favor common, realistic password structures.
pattern_weights = {
    1: 5,   # Phone Numbers (less common as full password)
    2: 25,  # Name + Suffix (very common)
    3: 15,  # City + Suffix (common, especially for local users)
    4: 20,  # Common Passwords Base (e.g., "password" with variations)
    5: 25,  # Common Word + Suffix (very common)
    6: 15,  # Combination 1 (e.g., Name+Year, Word+Symbol)
    7: 10,  # Pet/Emotion based (common for personal passwords)
    8: 15,  # Combination 2 (e.g., Name+Name, Name+LoveWord)
    9: 15,  # Sport/Reference based (common hobbies/local interests)
    10: 15, # Dates / Simple Random / Alternating (various common formats)
    11: 10, # Repetition Pattern (e.g., "wordword", "wordword123")
}
# --- End Configuration ---


# --- Helper Functions for Variations ---
# These functions apply common transformations to base words/strings
# to create more diverse and realistic password candidates.
# ==============================================================================
leet_map = {
    'a': ['4', '@'], 'e': ['3'], 'i': ['1', '!', '|'],
    'o': ['0'], 's': ['5', '$', 'z'], 't': ['7', '+'],
    'l': ['1'], 'z': ['2'], 'g': ['9', '6']
}

def apply_leet(word, intensity=0.3):
    """
    Applies random leet speak substitutions to a word based on intensity.
    Example: 'password' -> 'p4ssw0rd'
    """
    new_word = list(word.lower()) # Work with lowercase list for easier modification
    applied = False
    for i, char in enumerate(new_word):
        if char in leet_map and random.random() < intensity:
            new_word[i] = random.choice(leet_map[char])
            applied = True
    return "".join(new_word) if applied else word # Return original if no change occurred

def apply_case_variation(word):
    """
    Applies various common casing styles to a word.
    Styles include: lowercase, Capitalized, UPPERCASE, original, and CamelCase-like.
    Example: 'password' -> 'Password', 'PASSWORD', 'PaSsWoRd', 'password'
    """
    if not word: return ""
    style = random.randint(1, 6) # Randomly choose one of the styles
    if style == 1: return word.lower()
    elif style == 2: return word.capitalize()
    elif style == 3: return word.upper()
    # style 4 returns original case (handled by falling through to default)
    elif style == 5: # Simple WordWord (attempts CamelCase parts if possible)
        # Finds sequences of letters/digits to capitalize them individually
        parts = re.findall('[A-Z]?[a-z]+|[A-Z]+(?![a-z])|\d+', word)
        # If multiple parts are found (e.g., "myword"), join them as MyWord
        return "".join(p.capitalize() for p in parts) if len(parts) > 1 else word.capitalize()
    # For style 6 or if no specific style matches, return original word
    return word

def add_random_affix(word):
    """
    Adds a random common prefix or suffix to a word.
    Example: 'hello' -> 'hello123', '123hello', 'hello!'
    """
    if random.random() < 0.3: # ~30% chance to add an affix
        affix = random.choice(common_affixes)
        # 50% chance to be a suffix, 50% chance to be a prefix
        return word + affix if random.choice([True, False]) else affix + word
    return word
# --- End Helper Functions ---


# --- Main Generation Logic ---
# This is the core loop where passwords are created based on the defined patterns
# and added to a set to ensure uniqueness.
# ==============================================================================
print(f"Generating up to {target_password_count} unique passwords for {output_filename}...")
unique_passwords = set() # Using a set automatically handles uniqueness
last_reported_count = -1 # To track and report progress periodically

# Pre-calculate total weight for efficient pattern selection
total_pattern_weight = sum(pattern_weights.values())

while len(unique_passwords) < target_password_count:
    # Simple progress indicator to show activity for long runs
    current_count = len(unique_passwords)
    if current_count % 50000 == 0 and current_count > last_reported_count:
         print(f"... {current_count} passwords generated ...")
         last_reported_count = current_count

    # Select a password pattern type based on their assigned weights.
    # This ensures patterns with higher weights (e.g., Name+Suffix) are chosen more often.
    rand_val = random.randint(1, total_pattern_weight)
    cumulative_weight = 0
    pattern_type = 1 # Default to the first pattern type
    for pt, weight in pattern_weights.items():
        cumulative_weight += weight
        if rand_val <= cumulative_weight:
            pattern_type = pt
            break

    password = "" # Initialize password for the current iteration

    # Try-except block to gracefully handle any unexpected errors during password
    # generation for a specific pattern, ensuring the loop continues.
    try:
        # --- START Pattern Logic Implementations ---
        # Each 'elif' block implements a distinct password generation pattern,
        # mimicking common human password creation tendencies.

        # Pattern 1: Phone Numbers (e.g., 0501234567)
        if pattern_type == 1:
            prefix = random.choice(["050", "052", "054", "055", "056", "058", "02", "04", "06", "03", "07", "08"]) # Common UAE/GCC prefixes
            password = prefix + ''.join([random.choice(digits) for _ in range(7)]) # 7 random digits for total 10

        # Pattern 2: Name + Suffix (e.g., "Mohammed1990", "Fatima!")
        elif pattern_type == 2:
            base = random.choice(personal_names + family_names) # Random personal or family name
            base = apply_case_variation(base) # Apply casing variations (e.g., capitalize, lowercase)
            if random.random() < 0.2: base = apply_leet(base, intensity=0.4) # Small chance for leet speak

            suffix_type = random.randint(1, 4)
            if suffix_type == 1: suffix = random.choice(years + special_years * 4) # Common years (favors special years)
            elif suffix_type == 2: suffix = str(random.randint(1, 999)) # Small numbers
            elif suffix_type == 3: suffix = str(random.randint(1000, 99999)) # Larger numbers
            else: suffix = random.choice(special_chars) + (random.choice(digits) if random.random()<0.5 else "") # Special char with optional digit

            separator = random.choice(["", "", "_", "."]) if random.random() < 0.4 else "" # Optional separators
            password = base + separator + suffix
            password = add_random_affix(password) # Add additional random affix

        # Pattern 3: City + Suffix (e.g., "Dubai123", "Sharjah!")
        elif pattern_type == 3:
            base = random.choice(city_names) # Random city name
            base = apply_case_variation(base)
            if random.random() < 0.15: base = apply_leet(base, intensity=0.3)

            suffix_type = random.randint(1, 3)
            if suffix_type == 1: suffix = random.choice(years + special_years * 3)
            elif suffix_type == 2: suffix = str(random.randint(1, 999))
            else: suffix = random.choice(special_chars)

            separator = random.choice(["", "_"]) if random.random() < 0.3 else ""
            password = base + separator + suffix
            password = add_random_affix(password)

        # Pattern 4: Common Passwords Base (e.g., "password123", "QWERTY!")
        elif pattern_type == 4:
            base = random.choice(common_passwords) # Select from list of very common passwords
            if random.random() < 0.25: # Add a suffix to the common base
                 suffix = str(random.randint(1, 999)) if random.random() < 0.7 else random.choice(special_chars + common_affixes)
                 base = base + suffix
            if random.random() < 0.15: base = apply_case_variation(base) # Apply case variations
            if random.random() < 0.1: base = apply_leet(base, intensity=0.5) # Apply leet speak
            password = base

        # Pattern 5: Common Word + Suffix (e.g., "monkey2024", "love!")
        elif pattern_type == 5:
            base = random.choice(common_words) # Select from a general list of common words
            base = apply_case_variation(base)
            if random.random() < 0.25: base = apply_leet(base, intensity=0.4)

            suffix_type = random.randint(1, 4)
            if suffix_type == 1: suffix = random.choice(years + special_years * 4)
            elif suffix_type == 2: suffix = str(random.randint(1, 9999))
            elif suffix_type == 3: suffix = random.choice(special_chars) + (str(random.randint(1, 99)) if random.random() < 0.5 else "")
            else: suffix = random.choice(common_affixes)

            separator = random.choice(["", "_", "."]) if random.random() < 0.4 else ""
            password = base + separator + suffix

        # Pattern 6: Combination 1 (e.g., Name+Year, Word+Symbol)
        elif pattern_type == 6:
            first_elem = random.choice(personal_names + common_words + emotions + love_expressions)
            first_elem = apply_case_variation(first_elem)
            if random.random() < 0.1: first_elem = apply_leet(first_elem)

            second_elem = random.choice(special_years * 2 + ["123", "456", "789", "321", "143", "007", "99"] + common_words + love_expressions)
            second_elem = str(second_elem) # Ensure it's a string for concatenation
            if random.random() < 0.3 and not second_elem.isdigit(): # Apply case if not purely numeric
                 second_elem = apply_case_variation(second_elem)
            if random.random() < 0.1 and not second_elem.isdigit(): second_elem = apply_leet(second_elem)

            separator = random.choice(["", "", "_", ".", "-", random.choice(special_chars)]) if random.random() < 0.7 else ""
            password = str(first_elem) + separator + second_elem

        # Pattern 7: Pet/Emotion Based (e.g., "Luna123", "Happy!")
        elif pattern_type == 7:
            base = random.choice(pet_names + emotions)
            base = apply_case_variation(base)
            if random.random() < 0.1: base = apply_leet(base)

            if random.random() < 0.7: # High chance to add suffix
                suffix_choice = random.choice([str(random.randint(1, 999)), random.choice(love_expressions), random.choice(special_years)])
                separator = random.choice(["", "_"]) if random.random() < 0.6 else ""
                password = base + separator + suffix_choice
            else: # Sometimes just the base word
                password = base
            password = add_random_affix(password) # Apply additional affix

        # Pattern 8: Combination 2 (e.g., "JohnMary", "Ahmed&Ali")
        elif pattern_type == 8:
            name1 = random.choice(personal_names)
            name1 = apply_case_variation(name1)
            if random.random() < 0.1: name1 = apply_leet(name1)

            elem2 = random.choice(personal_names + love_expressions + emotions)
            elem2 = apply_case_variation(elem2)
            if random.random() < 0.1: elem2 = apply_leet(elem2)

            separator = random.choice(["", "and", "&", "+", "_", "."]) if random.random() < 0.6 else ""
            password = name1 + separator + elem2

            if random.random() < 0.4: # Chance to add year or affix at the end
                 password += random.choice(special_years + common_affixes)

        # Pattern 9: Sport/Reference Based (e.g., "AlAin2023", "BurjKhalifa!")
        elif pattern_type == 9:
            base = random.choice(sports_teams + uae_references)
            base = apply_case_variation(base)
            if random.random() < 0.2: base = apply_leet(base, intensity=0.5)

            if random.random() < 0.75: # High chance to add suffix
                 suffix = random.choice([str(random.randint(1, 9999))] + special_chars + common_affixes + special_years)
                 password = base + suffix
            else: # Sometimes just the base
                 password = base

        # Pattern 10: Dates / Simple Random / Alternating (e.g., "jan2025", "123abc")
        elif pattern_type == 10:
            pattern_subtype = random.randint(1, 4) # Choose sub-pattern for variety
            if pattern_subtype == 1: # Simple letter+number combination
                letters_part = ''.join(random.choice(lower_letters) for _ in range(random.randint(3, 6)))
                numbers_part = ''.join(random.choice(digits) for _ in range(random.randint(2, 5)))
                password = letters_part + numbers_part
                if random.random() < 0.3: password = apply_case_variation(password)
            elif pattern_subtype == 2: # Dates (various formats like DDMMYY, MMDDYYYY, etc.)
                day = str(random.randint(1, 31)).zfill(2) # Ensure 2 digits (e.g., "01")
                month_num = str(random.randint(1, 12)).zfill(2)
                month_name = random.choice(months)
                month = random.choice([month_num, month_name, month_name.lower()]) # Choose numeric or text month
                year = random.choice([y[-2:] for y in years] + years + years) # Favor full year, sometimes 2-digit year

                separator = random.choice(["", "", ".", "-", "/", "_"]) if random.random() < 0.7 else "" # Optional separators
                date_format = random.randint(1, 6)
                if date_format == 1: password = day + separator + month + separator + year # DD.MM.YYYY
                elif date_format == 2: password = month + separator + day + separator + year # MM.DD.YYYY
                elif date_format == 3: password = year + separator + month + separator + day # YYYY.MM.DD
                elif date_format == 4: password = day + month + year # DDMMYYYY (no separator)
                elif date_format == 5: password = month + day + year # MMDDYYYY (no separator)
                else: password = year + month + day # YYYYMMDD (no separator)

            elif pattern_subtype == 3: # Alternating letter/digit (e.g., "a1b2c3")
                chars = [random.choice(lower_letters), random.choice(digits)]
                password = ''.join(chars[i % 2] for i in range(random.randint(6, 10))) # Mix letters and digits
            elif pattern_subtype == 4: # Simple Random Mix (basic character pool)
                length = random.randint(6, 10)
                char_pool = lower_letters + digits
                if random.random() < 0.3: char_pool += upper_letters # Add uppercase sometimes
                if random.random() < 0.2: char_pool += random.choice(special_chars) # Add special chars sometimes
                password = ''.join(random.choice(char_pool) for _ in range(length))

        # Pattern 11: Repetition Pattern (e.g., "wordword", "catcat123")
        elif pattern_type == 11:
             base_choice = random.choice(common_words + love_expressions + emotions + personal_names + pet_names + city_names + uae_references + [str(random.randint(1,999))])
             base = str(base_choice) # Ensure string base
             if len(base) > 6: base = base[:random.randint(4,6)] # Keep base relatively short for repetition

             password = base * 2 # Repeat the base twice
             password = apply_case_variation(password) # Apply case variations
             if random.random() < 0.3: # Add a common affix or year after repetition
                 password += random.choice(common_affixes + special_years)
        # --- END Pattern Logic Implementations ---

        # Basic password validation: only add if length is reasonable.
        # This prevents extremely short or extremely long, less useful passwords.
        if password and 4 <= len(password) <= 20:
            unique_passwords.add(password) # Add to set (ensures uniqueness)

    except Exception as e:
        # Catch any unexpected errors during generation for a specific password.
        # This prevents the script from crashing due to an odd edge case.
        # It's good practice to log these in a real-world scenario.
        # print(f"Error generating password (pattern {pattern_type}): {e}")
        continue
# --- End Main Generation Logic ---


# --- File Writing ---
# Writes all the unique generated passwords to the specified output file.
# The order of passwords in the file will be arbitrary as they are stored in a set.
# ==============================================================================
print(f"\nGeneration complete. Writing {len(unique_passwords)} passwords to {output_filename}...")

try:
    # Open the file in write mode with UTF-8 encoding for broader character support.
    with open(output_filename, 'w', encoding='utf-8') as f:
        for pwd in unique_passwords:
            f.write(pwd + '\n') # Write each password on a new line
    print(f"Successfully wrote {len(unique_passwords)} passwords to {output_filename}.")
except IOError as e:
    # Handle file writing errors (e.g., permission denied, disk full)
    print(f"Error writing to file {output_filename}: {e}")
except Exception as e:
    # Catch any other unexpected errors during file writing.
    print(f"An unexpected error occurred during file writing: {e}")
# --- End File Writing --
