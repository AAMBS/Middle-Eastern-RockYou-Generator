# Middle-Eastern RockYou Wordlist Generator

---

This project presents a **Middle-Eastern localized version of the RockYou wordlist**, a common tool in cybersecurity for password cracking. Developed with **educational intent**, this Python-based project generates a comprehensive dictionary of potential passwords relevant to the Middle East and UAE regions.

This project is licensed under the MIT License - see the [LICENSE](LICENSE.MD) file for details.

---

## Educational Disclaimer

This project is created solely for **educational purposes** to demonstrate the principles of password security, brute-force attacks, and defensive measures. The generated wordlists contain common terms, names, and places that *could* be used as passwords. **Under no circumstances should these wordlists be used to compromise real accounts or systems.** Using these wordlists for malicious activities is illegal and unethical. Users are responsible for ensuring their actions comply with all applicable laws and ethical guidelines. **Protect your online accounts with strong, unique passwords!**

---

## Project Overview

The core of this project is a **Python script** that intelligently randomizes and combines a variety of elements specific to the Middle East and UAE. These elements include:

* **Diverse Data Sources:** Incorporates extensive lists of personal names (Middle Eastern, South Asian, Western), family names, city names (UAE-specific, international), common words (including Arabic terms), sports teams, UAE-specific references, pet names, emotions, and more.
* **Multiple Languages/Regional Data:** Leveraging popular names, common Arabic phrases, and significant places (cities, landmarks) from the Middle East and UAE.
* **Common Names & Phrases:** Utilizing common words, pet names, love expressions, and common terms relevant to the region and globally.
* **Years & Dates:** Incorporating common years (e.g., birth years, significant historical years) and specific recent years (e.g., `2023`, `2024`, `2025`), as well as month names and numerical date formats.
* **Sports Teams & Cultural References:** Integrating popular sports teams and well-known UAE-specific landmarks and entities.

To achieve a highly realistic and diverse wordlist, the generation process incorporates advanced techniques such as:

* **Pattern Weights:** Assigning probabilities to different password structures (e.g., `word+year`, `name+special_char`) to mimic real-world password trends.
* **Common Affixes:** Including common numeric, symbolic, and short word prefixes and suffixes that users might append.
* **Case Variations:** Generating passwords with various casing styles (lowercase, uppercase, capitalized, CamelCase-like) to expand permutations.
* **Leet Speak (Leetmaps):** Implementing `leet` variations (e.g., `a` becoming `4`, `e` becoming `3`) to ensure a wider range of permutations, mimicking common user habits.

The script ensures:

* **Randomization:** Utilizes Python's `random` module to create diverse and unpredictable password combinations.
* **Uniqueness:** Guarantees that no duplicate entries are present in the generated wordlist.
* **Scale:** The current iteration produces up to **1.5 million unique entries**, providing a substantial dictionary for educational demonstrations.

---

## Demonstrative Use Case

To illustrate the practical application of such wordlists (and highlight the risks associated with weak passwords), a responsible demonstration was conducted:

1.  A **dummy PDF file** (containing no sensitive information) was protected with a randomly generated password sourced directly from this custom wordlist.
2.  **John the Ripper**, a popular password cracking tool, was used to extract the hash from the dummy PDF file.
3.  The generated Middle-Eastern wordlist was then successfully employed with John the Ripper to **crack the PDF's password**.

This demonstration serves to show how attackers might leverage common password patterns and regional specificity, underscoring the importance of strong, unique passwords for personal and organizational security.

---

## Blue Team / Defensive Elements (Conceptual & Practical)

Beyond demonstrating offensive capabilities, this project also emphasizes crucial **Blue Team** (defensive) principles and practices that should accompany any offensive security testing:

* **Live Monitoring/Auditing:** Highlighting the importance of implementing systems for continuous monitoring and auditing of file access and system activity, crucial for detecting and responding to unauthorized actions.
* **AppArmor Scripting:** Demonstrating the strategic use of **AppArmor** to restrict a tool's permissions (e.g., ensuring John the Ripper has **zero access** to sensitive files during a test). This showcases the practical application of the principle of least privilege in securing systems.
* **File Permission Hardening:** Emphasizing the critical step of tightening permissions on sensitive files themselves, ensuring that **no unauthorized user** can modify, access, or even view critical data.

These defensive considerations are paramount in a comprehensive cybersecurity strategy, whether in a simulated environment or a real-world scenario.

---

## Getting Started

Follow these steps to get your custom wordlist generated on your system.

### Prerequisites

* **Python 3.x** installed on your computer.

    You can check your Python version by opening a terminal or command prompt and typing:

    ```bash
    python3 --version
    ```
    If Python 3 is not installed, please download it from [python.org](https://www.python.org/downloads/).

### Installation & Execution

1.  **Clone the Repository:**
    Open your terminal or command prompt and clone this repository:

    ```bash
    git clone [https://github.com/your-username/middle-eastern-rockyou-generator.git](https://github.com/your-username/middle-eastern-rockyou-generator.git)
    ```
    *(**Important:** Remember to replace `your-username` with your actual GitHub username.)*

2.  **Navigate to the Project Directory:**
    Change your current directory to the cloned repository folder:

    ```bash
    cd middle-eastern-rockyou-generator
    ```

3.  **Run the Wordlist Generator Script:**
    Execute the Python script to start the password generation process. It will display progress updates in your terminal.

    ```bash
    python3 your_script_name.py
    ```
    *(**Note:** Replace `your_script_name.py` with the actual filename of your Python script, for example, `ArbRock_Random.py` if that is its name.)*

4.  **Locate Your Wordlist:**
    Once the script completes, the generated wordlist will be saved as a text file in the same directory. By default, this file is named:
    * **`ArbRock_Random.txt`**

### Using the Generated Wordlist

* **Local Use:** If you run the generator on your Kali Linux machine (or another Linux distribution used for security testing), the `ArbRock_Random.txt` file will be directly available in the directory where you ran the script.
* **Transfer to Kali (if generated elsewhere):** If you generated the wordlist on a different operating system (e.g., Windows, macOS), you can easily transfer the `ArbRock_Random.txt` file to your Kali Linux VM using:
    * **Shared Folders:** Configure a shared folder between your host OS and your Kali VM in your virtualization software (VirtualBox, VMware).
    * **SCP (Secure Copy Protocol):** If SSH is set up on Kali, you can use `scp` from your host machine.
    * **USB Drive / Cloud Storage:** Copy the file via external media or cloud services.

Once transferred, you can then integrate `ArbRock_Random.txt` into password cracking tools like John the Ripper (e.g., `john --wordlist=ArbRock_Random.txt --format=raw-md5 hash.txt`) or Hashcat, just as you would with any other wordlist (like `rockyou.txt`).

---

## Configuration & Customization

You can easily adjust the generation parameters directly within the Python script (`your_script_name.py`) to suit your specific needs.

Open the script in any text editor and look for the `--- Configuration ---` section. Here you can modify:

* **`output_filename`**: Change this string to specify a different name for your generated wordlist file.
* **`target_password_count`**: Modify this integer to set the desired number of unique passwords you want to generate.
* **`pattern_weights`**: This dictionary allows you to fine-tune the prevalence of each password pattern. Increase a pattern's weight to make it appear more frequently, or decrease it for less frequent inclusion.
* **Base Data Lists:** Feel free to expand, adjust, or remove entries from the `family_names`, `personal_names`, `city_names`, `common_passwords`, `common_words`, `sports_teams`, `uae_references`, etc. Adding more relevant local data (e.g., specific to a certain country or region you are targeting) will significantly improve the effectiveness of the wordlist for your specific use case.

---

## Contributing

Contributions are always welcome! If you have ideas for new password patterns, additional data to include in the lists (especially for underrepresented regions or specific cultural references), or improvements to the code, feel free to:

1.  Fork this repository.
2.  Create your feature branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
