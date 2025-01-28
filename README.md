# Binary and Hexadecimal Translator

This is a Python script that provides a simple interface for converting between binary, hexadecimal, and human-readable text. It also allows users to convert text into binary or hexadecimal.

## Features
- Convert binary input to human-readable text.
- Convert hexadecimal input to human-readable text.
- Convert text input to binary.
- Convert text input to hexadecimal.
- Clear the terminal screen (supports Windows, macOS, and Linux).

## Requirements
- Python 3.x

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/seenumehta/binary-hex-translator.git
    ```
2. Navigate to the project directory:
    ```bash
    cd binary-hex-translator
    ```

## Usage
Run the script with the following command-line arguments:

### Options
| Option                 | Description                                   | Example                                 |
|------------------------|-----------------------------------------------|-----------------------------------------|
| `-b` or `--binary`    | Convert binary input to text.                | `python translator.py -b "01001000 01100101"` |
| `-x` or `--hex`       | Convert hexadecimal input to text.           | `python translator.py -x "48 65"`            |
| `-tb` or `--text_to_binary` | Convert text input to binary.           | `python translator.py -tb "Hello"`          |
| `-tx` or `--text_to_hex`    | Convert text input to hexadecimal.      | `python translator.py -tx "Hello"`          |
| `-c` or `--clear`     | Clear the terminal screen.                   | `python translator.py -c`                     |

### Example Commands
1. Convert binary to text:
    ```bash
    python translator.py -b "01001000 01100101 01101100 01101100 01101111"
    ```
   Output:
   ```
   Binary to Text: Hello
   ```

2. Convert hexadecimal to text:
    ```bash
    python translator.py -x "48 65 6c 6c 6f"
    ```
   Output:
   ```
   Hexadecimal to Text: Hello
   ```

3. Convert text to binary:
    ```bash
    python translator.py -tb "Hello"
    ```
   Output:
   ```
   Text to Binary: 01001000 01100101 01101100 01101100 01101111
   ```

4. Convert text to hexadecimal:
    ```bash
    python translator.py -tx "Hello"
    ```
   Output:
   ```
   Text to Hexadecimal: 48 65 6c 6c 6f
   ```

5. Clear the terminal screen:
    ```bash
    python translator.py -c
    ```

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributions
Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

