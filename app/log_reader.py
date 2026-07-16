from pathlib import Path

log_path = Path("logs/sample.log")

with open(log_path, "r") as file:
    lines = file.readlines()

print(f"Total log lines: {len(lines)}")

print("\nLast 10 log entries:\n")

for line in lines[-10:]:
    print(line.strip())