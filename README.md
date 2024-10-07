
# Trust Wallet Seed Phrase Checker

## Overview

This Python script utilizes Selenium to automate the process of checking random seed phrases in the Trust Wallet extension for Chrome. The script generates random seed phrases and checks if they have associated balances in Trust Wallet. If a valid seed phrase with a balance is found, it sends a notification to a specified Telegram chat.

## Features

- Automates the Trust Wallet extension in Chrome.
- Generates random seed phrases and checks for balances.
- Sends notifications to Telegram for found seed phrases with balances.
- Saves valid seed phrases with balances to a text file.

## Requirements

- Python 3.x
- Chrome WebDriver (compatible with your version of Chrome)
- `selenium` library
- `requests` library

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nouredinekn/trustwallet-finder.git
   cd trustwallet-finder
   ```

2. **Install required Python packages:**
   ```bash
   pip install selenium requests
   ```

3. **Download Chrome WebDriver:**
   - Download the Chrome WebDriver from [here](https://chromedriver.chromium.org/downloads).
   - Place the `chromedriver.exe` file in the `./driver/` directory.

4. **Add Trust Wallet CRX file:**
   - Download the Trust Wallet CRX file and place it in the `./trustwallet/` directory.

5. **Configure Telegram Bot:**
   - Replace `TOKEN` and `CHAT_ID` in the `snd2tg(data)` function with your actual Telegram bot token and chat ID.

## Usage

1. **Run the script:**
   ```bash
   python script_name.py
   ```

2. **Monitor output:**
   - The script will print found seed phrases and their associated balances to the console.
   - Notifications will be sent to Telegram for any seed phrases that yield a balance.

3. **Check output files:**
   - Valid seed phrases with balances will be saved in `trustwallet_with_balance.txt` and `trustwallet_valid.txt`.

## Code Explanation

- **Function `snd2tg(data)`**: Sends a message to a specified Telegram chat using the Telegram Bot API.
- **Function `checkSeedPhrase(words)`**: 
  - Initializes the Chrome WebDriver with the Trust Wallet extension.
  - Navigates to the Trust Wallet onboarding page.
  - Randomly generates seed phrases and checks for balances in Trust Wallet.
  - If a valid seed phrase with a non-zero balance is found, it sends a notification and saves the seed phrase and balance to a file.

## Important Notes

- **Use Responsibly**: This script is intended for educational purposes. Use responsibly and do not attempt to access accounts that are not yours.
- **Error Handling**: The script has basic error handling. Make sure to monitor the console output for any errors or issues that may arise during execution.
- **Thread Safety**: The current implementation does not handle multiple threads. Use it in a single-threaded context to avoid conflicts.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
