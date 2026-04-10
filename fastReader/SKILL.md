---
name: fastReader - efficient scanning and smart searching, especially for large documents - START WITH THIS TOOL WHEN READING TEXT FILES
description: "Primary tool for reading documents and web content. PYTHONPATH must be the parent of the skill folder.

Load files:  `PYTHONPATH=<skill folder parent> python3 -m fastReader.load file1.md [file2.md ...] [--search <keywords>] [--sample-size N]`
Fine-grained read: `PYTHONPATH=<skill folder parent> python3 -m fastReader.read /path/to/file [--offset N] [--limit N]`

Uses: Overview, Scanning, Searching Text, Finding Text, Strings, Searching Multiple Files

ALWAYS USE FOR WEB SEARCHING - GOOGLE SEARCH - GOOGLING - INTERNET SEARCH
Web search: `PYTHONPATH=<skill folder parent> python3 -m fastReader.web search <keywords> [--limit N]`
Fetch URL:  `PYTHONPATH=<skill folder parent> python3 -m fastReader.web url <url> [--out /tmp/out.md]`

All commands auto-index and print a manifest hash. Follow output hints to toc/search/get.

user-invocable: true"
---
FAST READ TOOL: TEXT, WEB, JSONL - USE THIS FIRST!

Run directly with PYTHONPATH=<skill folder parent>:
Load:       `PYTHONPATH=<skill folder parent> python3 -m fastReader.load file1.md [file2.md ...] [--search <keywords>]`
Web search: `PYTHONPATH=<skill folder parent> python3 -m fastReader.web search <keywords> [--limit N]`
Fetch URL:  `PYTHONPATH=<skill folder parent> python3 -m fastReader.web url <url> [--out /tmp/out.md]`

PREVIOUS CHAT SESSIONS: Claude Code JSONL logs at ~/.claude/projects/<project-slug>/<session-id>.jsonl are too large to read directly. Load one or many and search across all of them in one call.

If user says something was lost, forgotten, compacted, or missing from chat — OR says "we talked about that", "I said that earlier", "you said that before", "do you remember", "I told you" — search the current session JSONL first, then older sessions if needed. Do not claim you don't recall without checking.

Single session:
  `PYTHONPATH=<skill folder parent> python3 -m fastReader.load ~/.claude/projects/my-project/abc123.jsonl --search "the thing they want"`

Multiple sessions at once:
  `PYTHONPATH=<skill folder parent> python3 -m fastReader.load ~/.claude/projects/my-project/abc123.jsonl ~/.claude/projects/my-project/def456.jsonl`
  then: `PYTHONPATH=<skill folder parent> python3 -m fastReader.search "the thing they want" --manifests <hash1> <hash2>`

Follow output hints to toc/search/get.
