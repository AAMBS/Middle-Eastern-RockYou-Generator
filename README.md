# Middle-Eastern RockYou Wordlist Generator

---

This project presents a **Middle-Eastern localized version of the RockYou wordlist**, a common tool in cybersecurity for password cracking. Developed with **educational intent**, this Python-based project generates a comprehensive dictionary of potential passwords relevant to the Middle East and UAE regions.

This project is licensed under the MIT License - see the [LICENSE.MD](LICENSE.MD) file for details.

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

How to Run Your Wordlist Generator
Follow these steps to get your custom password wordlist generated on your system.

1. Prerequisites
Before you start, ensure you have Python 3.x installed on your computer.

You can check your Python version by opening a terminal or command prompt and typing:

``Bash

python3 --version
If Python 3 is not installed, please download it from python.org.

2. Get the Code
First, you need to download the project files to your local machine.

Open your terminal or command prompt and use git clone to download the repository:

``Bash

git clone https://github.com/your-username/middle-eastern-rockyou-generator.git
(Important: Remember to replace your-username with your actual GitHub username.)

3. Navigate to the Project Directory
Once the repository is cloned, change your current directory to the project folder:

``Bash

cd middle-eastern-rockyou-generator
4. Run the Wordlist Generator Script
Now, you can execute the Python script. This will start the password generation process.

Bash

python3 your_script_name.py
(If you have named your Python script something different, replace your_script_name.py with its actual filename, e.g., python3 generate_wordlist.py or python3 ArbRock_Random.py if that's what you decided.)

The script will display progress updates in your terminal as it generates passwords.

5. Find the Generated Wordlist
After the script finishes (it will print a "Generation complete" message), your custom wordlist will be saved as a text file in the same directory where you ran the script.

By default, the output file is named:

ArbRock_Random.txt

6. Customization (Optional)
If you wish to change the number of passwords generated, the output filename, or adjust the generation patterns, you can do so by editing the Python script directly.

Open the your_script_name.py file in any text editor and look for the --- Configuration --- section at the top to modify these parameters.
