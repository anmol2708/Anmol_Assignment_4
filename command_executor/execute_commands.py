import subprocess
import json


def execute_commands(commands: list) -> list:
    """
    Executes a list of OS commands and returns results as a list of dicts.
    - Deduplicates commands (preserves first occurrence order)
    - Continues execution even if a command fails
    """
    seen = set()
    unique_commands = []
    for cmd in commands:
        if cmd not in seen:
            seen.add(cmd)
            unique_commands.append(cmd)

    results = []

    for cmd in unique_commands:
        try:
            proc = subprocess.run(
                cmd,
                shell=True,
                capture_output=True,
                text=True
            )
            if proc.returncode == 0:
                results.append({
                    cmd: {
                        "output": proc.stdout.strip(),
                        "error": proc.stderr.strip(),
                        "status": "success"
                    }
                })
            else:
                results.append({
                    cmd: {
                        "output": proc.stdout.strip(),
                        "error": proc.stderr.strip() or f"Command exited with return code {proc.returncode}",
                        "status": "Failed"
                    }
                })
        except Exception as e:
            results.append({
                cmd: {
                    "output": "",
                    "error": f"Not able to execute the command: {str(e)}",
                    "status": "Failed"
                }
            })

    return results


if __name__ == "__main__":
    # Sample list of commands (including duplicates to test deduplication)
    commands = ["ls", "pwd", "df", "ls", "invalid_cmd_xyz", "whoami"]

    output = execute_commands(commands)
    print(json.dumps(output, indent=4))
