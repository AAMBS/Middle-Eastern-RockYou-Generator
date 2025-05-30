# Middle-Eastern RockYou Wordlist Generator

---

This project presents a **Middle-Eastern localized version of the RockYou wordlist**, a common tool in cybersecurity for password cracking. Developed with **educational intent**, this Python-based project generates a comprehensive dictionary of potential passwords relevant to the Middle East and UAE regions.

---

## Educational Disclaimer

This project is created solely for **educational purposes** to demonstrate the principles of password security, brute-force attacks, and defensive measures. The generated wordlists contain common terms, names, and places that *could* be used as passwords. **Under no circumstances should these wordlists be used to compromise real accounts or systems.** Using these wordlists for malicious activities is illegal and unethical. Users are responsible for ensuring their actions comply with all applicable laws and ethical guidelines. **Protect your online accounts with strong, unique passwords!**

---

## Project Overview

The core of this project is a **Python script** that intelligently randomizes and combines a variety of elements specific to the Middle East and UAE. These elements include:

* **Multiple languages:** Incorporating Arabic and potentially other regional languages.
* **Common names:** Popular names from the Middle East.
* **Significant places:** Cities, landmarks, and other geographical locations within the Middle East and UAE.
* **Emojis and special characters:** To simulate common password patterns.

To achieve a highly realistic and diverse wordlist, the generation process incorporates advanced techniques such as:

* **Pattern Weights:** Assigning probabilities to different password structures (e.g., `word+year`, `name+special_char`).
* **Common Affixes:** Including common prefixes and suffixes that users might append to words.
* **Pet Names:** Integrating popular pet names.
* **Special Characters:** A wide range of special characters are strategically included.
* **Years & Special Years:** Incorporating common years (e.g., birth years, significant historical years) and specific years (e.g., `2023`, `2024`).
* **Months:** Including full month names and their abbreviations.
* **Love Expressions:** Common terms of endearment or love-related phrases.
* **Case Variations:** Generating passwords with both lowercase and uppercase letters, and combinations thereof.
* **Leet Speak (Leetmaps):** Implementing `leet` variations (e.g., `a` becoming `4`, `e` becoming `3`) to ensure a wider range of permutations, mimicking common user habits.

The script ensures:

* **Randomization:** Utilizes Python's `random` module to create diverse and unpredictable password combinations.
* **Uniqueness:** Guarantees that no duplicate entries are present in the generated wordlist.
* **Scale:** The current iteration produces **10 million unique entries**, providing a substantial dictionary for educational demonstrations.

---

## Demonstrative Use Case

To illustrate the practical application (and the risks associated with weak passwords), a demonstration was conducted:

1.  A **dummy PDF file** (containing no sensitive information) was protected with a randomly generated password from the custom wordlist.
2.  **John the Ripper**, a popular password cracking tool, was used to hash the PDF file.
3.  The generated Middle-Eastern wordlist was then employed to **successfully crack the PDF's password** using John the Ripper.

---

## Blue Team / Defensive Elements

Beyond demonstrating offensive capabilities, this project also incorporates crucial **Blue Team** (defensive) elements:

* **Live Monitoring/Auditing:** Implementation of a system for continuous monitoring and auditing of file access, crucial for detecting unauthorized activities.
* **AppArmor Scripting:** Strategic use of **AppArmor** to restrict John the Ripper's permissions, specifically ensuring it has **zero access** to the sensitive PDF file. This highlights the importance of principle of least privilege.
* **File Permission Hardening:** Further implementation plans include tightening permissions on the PDF file itself, ensuring that **no unauthorized user** has access to modify or even touch the file.

---

## Getting Started

*(Instructions on how to set up and run the Python script, prerequisites, etc., will go here. You'll need to fill this section in once your code is ready.)*

```bash
# Example (you'll replace this with actual instructions)
git clone [https://github.com/your-username/middle-eastern-rockyou.git](https://github.com/your-username/middle-eastern-rockyou.git)
cd middle-eastern-rockyou
pip install -r requirements.txt
python generate_wordlist.py
