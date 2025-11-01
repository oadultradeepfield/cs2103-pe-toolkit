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

1. To use the PE Toolkit, install the package using `pip`:

   ```bash
   pip install pe-toolkit
   ```

2. Verify the installation by checking the version:

   ```bash
   pe-toolkit --help
   ```

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

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
