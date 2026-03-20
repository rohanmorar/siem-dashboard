### [2026-03-19] Hardcoded indexes vs regex
**Mistake:** Originally used parts[0], parts[12] etc to extract fields.
**Problem:** Fragile — breaks silently if log format changes.
**Resolution:** Use regex to search for patterns instead of positions.
**Lesson:** Never rely on fixed indexes for log parsing. Search for meaning, not position.

### [2026-03-19] Redundant hardcoded word count check
**Mistake:** Used len(line.split()) < 13 to skip malformed lines.
**Problem:** Hardcoded number tied to old index-based approach. Meaningless after switching to regex.
**Resolution:** Removed entirely. Regex match failures handle malformed lines instead.
**Lesson:** When you refactor, audit every line — old code can linger and cause confusion.

## Regex Patterns

### Pattern 1: IP address
re.search(r`from (\d+\.\d+\.\d+\.\d+)`, line)

- `from ` — literal word "from " in the line
- `(\d+\.\d+\.\d+\.\d+)` — captures the IP address
- `\d+` — one or more digits
- `\.` — literal dot (without backslash, . means any character)
- Returns: 192.168.1.100

### Pattern 2: Username
re.search(r`for (?:invalid user )?(\w+) from`, line)

- `for ` — literal word "for "
- `(?:invalid user )?` — optionally matches "invalid user "
  - `?:` — don't capture this group
  - `?` at the end — the whole group is optional
- `(\w+)` — captures the username
- ` from` — anchors the end of the pattern
- Returns: admin (failed lines), rohan (accepted lines)

### Pattern 3: Timestamp
re.search(r`^(\w+\s+\d+\s+[\d:]+)`, line)

- `^` — start of the line
- `\w+` — month e.g. Jan
- `\s+` — whitespace
- `\d+` — day e.g. 15
- `\s+` — whitespace
- `[\d:]+` — time e.g. 10:23:01 (digits or colons)
- Returns: Jan 15 10:23:01

### Key distinction: ?: vs ?
- `?:` at the START of a group — non-capturing (don't store this match)
- `?` at the END of a group — optional (this group may or may not exist)
- They are independent — you can use either, both, or neither

### [2026-03-19] SyntaxWarning from NOTES.md
**Cause:** \d in NOTES.md was interpreted as a Python escape sequence.
**Resolution:** Wrap all regex patterns in backticks in markdown files.
**Lesson:** Python warns about invalid escape sequences — always use raw strings r'' in actual code.