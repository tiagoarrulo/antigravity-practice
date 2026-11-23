"""Hook: run pytest after every file edit, and do not let the agent stop while tests fail.

Wired in .agents/hooks.json (docs: https://antigravity.google/docs/hooks).
  post-edit : PostToolUse on the edit tools. Runs pytest and writes the result to
              .agents/last-test-run.txt. PostToolUse must answer {} on stdout.
  stop      : Stop. If pytest fails, answers {"decision": "continue", "reason": ...}, which the
              docs say is injected as a system message, so the agent keeps working on the failure.
"""

import json
import subprocess
import sys
from pathlib import Path

MAX_STOP_RETRIES = 3


def run_pytest(cwd: Path):
    proc = subprocess.run([sys.executable, "-m", "pytest", "-q", "--no-header", "-p", "no:cacheprovider"],
                          cwd=cwd, capture_output=True, text=True)
    return proc.returncode, (proc.stdout + proc.stderr).strip()


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "post-edit"
    event = json.loads(sys.stdin.read() or "{}")
    workspace = Path((event.get("workspacePaths") or ["."])[0])
    code, output = run_pytest(workspace)
    (workspace / ".agents" / "last-test-run.txt").write_text(output + "\n")

    if mode == "stop" and code != 0 and int(event.get("executionNum") or 0) < MAX_STOP_RETRIES:
        tail = "\n".join(output.splitlines()[-15:])
        print(json.dumps({"decision": "continue",
                          "reason": "pytest is failing. Fix the code (not the tests) before you finish:\n" + tail}))
    else:
        print("{}")


if __name__ == "__main__":
    main()
