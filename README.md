#BookBot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

BookBot is a Python project from [boot.dev](https://boot.dev) that analyzes text files to provide word and character frequency statistics.

## Usage

To run BookBot, use the following command:

```bash
uv run main.py <path_to_book.txt>
```

### Functionality
- **Word Count**: Outputs the total number of words in the provided text file.
- **Character Frequency**: Lists all characters used in the text and their frequency, sorted by usage (most frequent first).

### Prerequisites
- Python 3.x
- [uv](https://github.com/astral-sh/uv) for dependency management

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Steffen025/bookbot.git
   cd bookbot
   ```
2. Ensure `uv` is installed. Follow the instructions [here](https://github.com/astral-sh/uv) if needed.
3. Place your text file (e.g., `book.txt`) in the project directory or provide its path.

### Example
```bash
uv run main.py books/book.txt
```

This will output:
- Total word count
- A sorted list of characters and their frequencies