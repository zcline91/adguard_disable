# Adguard Disable

This simple script is for disabling Adguard for a short amount of time through the API.

## Setup

1. Install the requirements: `pip install -r requirements.txt`
2. Add a file `.env` with contents

    ```text
    AUTH_HEADER=<header>
    ADGUARD_URL=<url>
    ```

    where `<url>` is the full url, e.g. beginning http://, for the Adguard instance, and `<header>` is the output of

    ```bash
    echo -n "<username>:<password>" | base64
    ```

    for a user on Adguard.
3. Check that everything is correct by running the command: `python3 .\disable_adguard.py`.
4. Compile to a single portable executable (for your machine's architecture):

   ```bash
   pyinstaller --onefile --console --add-data ".env;." ./disable_adguard.py
   ```

5. Move the resulting file in `/dist` to wherever is convenient when you (or someone in your household) want to temporarily disable Adguard.
