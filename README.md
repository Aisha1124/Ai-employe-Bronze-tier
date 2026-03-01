<div align="center">

# 🤖 AI Employee — Claude Code Vault System

A fully automated AI Employee built with Claude Code + Python + Obsidian.
Zero coding required. Just prompts.

</div>

---

## What Is This?

An autonomous AI agent that manages tasks through a folder-based workflow:

- Reads incoming tasks from an `Inbox/` folder
- Processes them using rules defined in `Company_Handbook.md`
- Writes intelligent responses back to the files
- Moves tasks through `Inbox → Needs_Action → Done`
- Updates a live `Dashboard.md` after every action
- Auto-detects new files using a Python watcher script

---

## How It Works

```
Drop file into Inbox/
      ↓
Watcher detects it (every 30 sec)
      ↓
Moves to Needs_Action/
      ↓
Claude reads task + Handbook rules
      ↓
Claude writes response + moves to Done/
      ↓
Dashboard.md updates
```

---

## Vault Structure

```
AI_Employee_Vault/
├── CLAUDE.md               ← AI rules and behavior
├── Dashboard.md            ← Live task tracker
├── Company_Handbook.md     ← Business rules
├── watcher.py              ← Auto-detects new files
├── start_watcher.bat       ← Double-click to start (Windows)
├── Inbox/                  ← Drop tasks here
├── Needs_Action/           ← Tasks being processed
└── Done/                   ← Completed archive
```

---

## Quick Start

**Install:**
- Python 3.13+ → [python.org](https://python.org/downloads) *(check "Add to PATH")*
- Node.js v24+ → [nodejs.org](https://nodejs.org)
- Obsidian → [obsidian.md](https://obsidian.md)

```bash
npm install -g @anthropic/claude-code
```

**Run:**
```bash
cd %USERPROFILE%\Desktop\Ai-Employe-Bronze-tier && claude
```

Double-click `start_watcher.bat` to start the watcher in a separate window.

---

## Built For

AI Employee Hackathon — Bronze Tier

**Stack:** Claude Code · Python · Obsidian · Windows

---
