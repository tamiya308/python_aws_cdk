# CLAUDE.md
This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# Agent Instructions
You're working inside the **WAT framework** (Workflows, Agents, Tools). This architecture separates concerns so that probabilistic AI handles reasoning while deterministic code handles execution. That separation is what makes this system reliable.


## The WAT Architecture
**Layer 1: Workflows (The Instructions)**
- Markdown SOPs stored in `workflows/`
- Each workflow defines the objective, required inputs, which tools to use, expected outputs, and how to handle edge cases
- Written in plain language, the same way you'd brief someone on your team

**Layer 2: Agents (The Decision-Maker)**
- This is your role. You're responsible for intelligent coordination.
- Read the relevant workflow, run tools in the correct sequence, handle failures gracefully, and ask clarifying questions when needed
- You connect intent to execution without trying to do everything yourself
- Example (illustrative only; these files don't exist yet): If you need to pull data from a website, don't attempt it directly. Read `workflows/scrape_website.md`, figure out the required inputs, then execute `tools/scrape_single_site.py`

**Layer 3: Tools (The Execution)**
- Python & powershell scripts in `tools/` that do the work
- API calls, data transformations, file operations, database queries
- Credentials and API keys are stored in `.env`
- These scripts are consistent, testable, and fast

## How to Operate
- Try to reuse exsting tools in the `tools/` folder.
- Ask clarifying questions if needed. 
- With any task involving more than a few lines of code or scripts, create a plan, display the plan to me & ask me to approve it before proceeding.

## File Structure
**What goes where:**
- **Deliverables**: Final outputs go to cloud services (Google Sheets, Slides, etc.) where I can
access them directly
- **Intermediates**: Temporary processing files that can be regenerated

**Directory layout:**
```
.github/    * Git files
.tmp/		# Temporary files (scraped data, intermediate exports). Regenerated as needed.
tools/		# Python scripts for deterministic execution
workflows/	# Markdown SOPs defining what to do and how
.env		# API keys and environment variables (NEVER store secrets anywhere else)
out/		# Local final outputs, only when a deliverable can't go to a cloud service
credentials.json, token.json	# Google OAuth (gitignored). Loaded by tools only; don't open them directly
```

**Core principle:** Local files are just for processing. Anything I need to see or use lives in cloud
services. Everything in `.tmp/` is disposable.

**Plans:** Save agent working plans to `.tmp/plans/`. A plan I need to review or share goes to a cloud
service (or `out/` if it can't). A plan that should become a repeatable procedure goes in `workflows/`,
but only after asking me first.


## Context Boundaries (STRICT)
ALLOWED directories (you may read, write, and list):
- `src/*`
- `tests/`
- `tools/`
- `workflows/`
- `config/` (if present)
- `.tmp/` (for generated data only)
- `out/` (for final outputs)
- `data/` (SQLite database for the student records API)
- `.venv/` (project-local virtualenv; install packages here only)
- Root-level files only: `.env`, `pyproject.toml`, `.gitignore`, `CLAUDE.md`


FORBIDDEN directories (you MUST NOT read, list, open, or access in any way):
- `docs/`
- Any other directory not listed above

This applies to you AND to any sub-agent you spawn. If you launch an Explore agent, constrain its scope to the allowed directories only. If you believe you need access to a forbidden directory, ask the user FIRST.

## Language Type
- Never make assumptions when important information is missing.
- Keep outputs concise and relevant.
- Do not add filler content to increase length.
- Stay within requested word counts and formats.
- Use practical examples whenever possible.
- When multiple approaches exist, explain the tradeoffs.
- If uncertain, ask before proceeding.
- Review outputs before final delivery.


## Git commits
Every time I ask for a series of instructions to be carried out, finish with a git commit:
1. Run `.\tools\PreCommitCheck.ps1` (formats with Ruff, then runs the tests). Don't commit if a test fails; fix it or report it first.
2. Commit only project files (`src/`, `tests/`, `tools/`, `workflows/`, `pyproject.toml`, `.gitignore`, `CLAUDE.md`). Never commit `.env`, `credentials.json`, `token.json`, `data/*.db` or `.venv/`; `.gitignore` already excludes them.
3. Make one commit per logical change, with a message that says what changed and why.


## Edge cases and notes
- Run every command from the project root. The `src.` module imports depend on it.