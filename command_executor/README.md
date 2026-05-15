# Command Executor

A Python utility that executes a list of OS commands and returns structured output as a list of dictionaries.

## Features

- Executes any valid OS command (`ls`, `pwd`, `df`, `whoami`, etc.)
- Automatically deduplicates commands (preserves first occurrence order)
- Never exits on failure — continues executing remaining commands
- Returns structured JSON output with `output`, `error`, and `status` fields

## Project Structure

```
command_executor/
├── execute_commands.py   # Main script
├── requirements.txt      # Dependencies (stdlib only)
└── README.md             # This file
```

## Usage

```python
from execute_commands import execute_commands

commands = ["ls", "pwd", "df", "invalid_cmd", "whoami"]
results = execute_commands(commands)

import json
print(json.dumps(results, indent=4))
```

## Sample Output

```json
[
    {
        "ls": {
            "output": "execute_commands.py",
            "error": "",
            "status": "success"
        }
    },
    {
        "invalid_cmd": {
            "output": "",
            "error": "/bin/sh: 1: invalid_cmd: not found",
            "status": "Failed"
        }
    }
]
```

## Run Directly

```bash
python execute_commands.py
```

## Requirements

No external libraries needed — uses Python's built-in `subprocess` and `json` modules.
