# Copilot / AI helper instructions — quick reference

## Project snapshot (why this repo exists) 💡
- Single-developer learning exercises: short, independent Python scripts organized by `dayN/` folders (examples: `day14/copy.py`, `day5/strings.py`).
- No package layout, no tests, and no CI detected — most files are runnable examples and teaching notes.
- Python used interactively (user run examples directly). Recent runs show Python 3.14 in the environment.

---
## Immediate goals for an AI coding agent ✅
1. Keep edits minimal and behavior-preserving: these files are lesson examples — preserve printed output and explanatory comments.  
2. Avoid large structural refactors (packages, CI, renames) unless the human explicitly requests them.  
3. When adding new code, make it import-safe (see "Safe edits" below) and include one-line run examples.

---
## How to run (examples you can use in PRs / code comments) 🔧
- Run a single example (Windows):
  - `python day14/copy.py`
  - or the full-exe form (seen in repo):
    `& C:/Users/vkids/AppData/Local/Programs/Python/Python314/python.exe c:/Users/vkids/python/day14/copy.py`
- There is no test runner or CI — validate by running the edited example(s) locally.

---
## Repository conventions & observable patterns (do this) 📚
- Files are independent, example-focused and usually contain top-level `print()` statements (e.g., `day 1/hello.py`).
- Comment-first pedagogy: preserve and mirror the heavy inline comments when adding examples (see `day5/strings.py`).
- Naming pattern: prefer `dayN/<topic>.py` for new examples. **Note**: existing inconsistencies exist (see "Gotchas").
- Minimal imports / standard library only — do not add external dependencies without explicit approval and a README update.

---
## Gotchas and files to NOT change without asking ⚠️
- Several filename / folder anomalies exist — do **not** auto-rename:
  - `day13/prblms,py` (typo/comma)
  - `day 1/` (contains a space)
  - `day7/booleans` (missing `.py` extension)
  - Mixed casing: `day6/Ascii.py`, `day9/Identity.py`
- Many files execute at import time (top-level prints). When refactoring, preserve exact stdout or add tests that assert the same output.

> Important: any change that renames files, fixes typos in filenames, or changes printed output requires an explicit human review.

---
## Safe-edit checklist (use before committing) ✅
- Run the example you modified: `python <relative-path>` and confirm output unchanged (or document intended change).  
- If you create reusable code, add `if __name__ == "__main__":` to preserve importability. Example:

```py
def demo():
    """Return or print the example output."""
    return "hello"

if __name__ == '__main__':
    print(demo())
```

- Add a one-line usage comment at the top of the file (mirrors existing style).
- DO NOT introduce cross-file imports unless you add clear docstrings and a short usage example.

---
## When to suggest larger changes (and how to propose them)
- Adding tests, CI, or renaming files: create a proposal PR that includes
  - a clear migration plan (list of exact renames and redirects),
  - preserved-originals branch or compatibility wrappers, and
  - smoke-run commands that show unchanged output.

---
## Where to add new content
- New exercise: create `day15/<topic>.py` (follow `dayNN` numbering, no spaces). Include:
  - short description comment, expected output example, and `if __name__ == '__main__'` guard.
- If you add reusable utilities across days, place them in a `lib/` or `shared/` directory and update README with usage examples.

---
## Quick examples from this repo (copyable) 🔍
- Preserve example behavior: `day14/copy.py` prints a copied list — any refactor must keep that output.
- Use comment-heavy, teacher-friendly style as in `day5/strings.py` for new examples.

---
## Decision rules for PRs by an AI agent (short list)
- Safe to auto-commit: whitespace, docstring edits, adding `if __name__ == '__main__'`, small bugfixes that do not change stdout.
- Require human review: renaming files/folders, modifying printed examples, adding third-party dependencies, introducing package-level imports.

---
## Questions for the human reviewer (include in PR descriptions) ❓
- Should we normalize folder/file names (e.g., `day 1` → `day01`) or keep historical typos?  
- Is adding a minimal test harness acceptable, and where should tests live?  

---
If anything above is unclear or you want the agent to follow stricter rules (for example: always add tests, or automatically clean filename typos), tell me which rule to apply and I will update this file.
