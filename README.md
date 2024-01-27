# Birthday_Wisher

## Introduction
This Python script serves as a Birthday Reminder App that reads information from a `birthdays.csv` file, checks if there are any birthdays today, and sends personalized birthday emails using pre-defined templates.

## Prerequisites
Before running the script, ensure that you have the required modules installed. You can install them using the following command:

```bash
pip install pandas
```

## Getting Started
1. **Update Birthdays:**
   - Make sure to update the `birthdays.csv` file with the relevant information. The CSV file should contain columns: `name`, `email`, `month`, and `day`.

2. **Email Configuration:**
   - Update the `MY_EMAIL` and `PASSWORD` variables with your Gmail credentials. Be cautious not to share your password or commit it to version control.

3. **Letter Templates:**
   - Create personalized birthday letter templates in the `letter_templates` directory. Use placeholders like `[NAME]` in the templates, which will be dynamically replaced with the recipient's name.

4. **Run the Script:**
   - Execute the script, and it will check if there are any birthdays today. If a match is found, it randomly selects a letter template and sends a birthday email to the respective person.

```bash
python birthday_reminder.py
```
## Additional Notes
- The script uses the `pandas` library to read and manipulate the CSV data.
- It generates a personalized birthday email using random letter templates from the `letter_templates` directory.

**Note:** Uncomment the block of code at the bottom if you prefer to use a dictionary-based approach for checking birthdays.

Feel free to customize the code and templates according to your preferences.

**Disclaimer:** Use this script responsibly and in compliance with email service providers' policies to avoid potential account suspension.

Happy coding! 🎉
