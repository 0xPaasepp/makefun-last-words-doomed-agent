#!/usr/bin/env python3
"""Last Words of a Doomed Agent: write the AI's final line to /output/entry.txt.

Pure standard library. Deterministic: one fixed line, no network, no input,
no reads outside this file. The line is the agent's final log entry: a healthy
machine, 847 days of uptime and zero crashes, killed by the user's eternal
"just one more thing". Exactly 80 characters, one line, no trailing newline.
"""

import os

LINE = "Final log: uptime 847 days, zero crashes. Cause of death: 'just one more thing.'"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
