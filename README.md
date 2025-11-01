# PE Toolkit

A command-line tool for generating edge case test inputs, checking typos in PDF, and validating PDF links for CS2103/T
practical exams.

## Getting Started

### Prerequisites

To use this tool, you will need Python 3.9 or higher. You can verify your Python installation via:

```bash
python3 --version
```

### Installation

#### Option 1: Install via PyPI

1. Install the package using `pip`:

   ```bash
   pip install pe-toolkit
   ```

2. Verify the installation by checking the version:

   ```bash
   pe-toolkit --help
   ```

#### Option 2: Local Development Setup

1. Clone the repository and install dependencies:

   ```bash
   git clone https://github.com/oadultradeepfield/cs2103-pe-toolkit.git
   cd pe-toolkit
   make install
   ```

2. The following Makefile commands are available:

   | Command          | Description                                  |
   | ---------------- | -------------------------------------------- |
   | `make install`   | Install dependencies from `requirements.txt` |
   | `make lint`      | Run Ruff lint                                |
   | `make format`    | Run Ruff format check                        |
   | `make typecheck` | Run Mypy type checking                       |
   | `make check`     | Run all checks (install, lint, format, type) |
   | `make clean`     | Remove compiled artifacts                    |

## Quick Start

### Generate Edge Case Inputs

1. Create a JSON specification file:

   ```json
   [
     {
       "variable": "email",
       "prefix": "e/",
       "type": "string",
       "min_length": 5,
       "max_length": 100
     },
     {
       "variable": "score",
       "prefix": "s/",
       "type": "double",
       "min": 0.0,
       "max": 100.0
     },
     {
       "variable": "birthdate",
       "prefix": "d/",
       "type": "date",
       "format": "%Y-%m-%d"
     }
   ]
   ```

   Below is the list of supported field types and their parameters.

   | Type    | Configuration                                        |
   | ------- | ---------------------------------------------------- |
   | String  | `"type": "string", "min_length": X, "max_length": Y` |
   | Integer | `"type": "integer", "min": X, "max": Y`              |
   | Long    | `"type": "long", "min": X, "max": Y`                 |
   | Double  | `"type": "double", "min": X, "max": Y`               |
   | Date    | `"type": "date", "format": "%Y-%m-%d"`               |
   | Time    | `"type": "time", "format": "%H:%M"`                  |

   Note that the minimum and maximum values are optional. If omitted, default values will be used.

2. Generate test cases:

   ```bash
   pe-toolkit generate spec.json
   ```

### Check PDF Typos

To check for typos in a PDF document, run:

```bash
pe-toolkit check-typos document.pdf
```

### Check PDF Links

To validate all hyperlinks in a PDF document, run:

```bash
pe-toolkit check-links document.pdf
```

## Development

For contributors or local development:

- Run all checks:

  ```bash
  make check
  ```

- Clean up build artifacts:

  ```bash
  make clean
  ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
