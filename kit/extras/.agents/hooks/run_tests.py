"""Hook: run pytest after every file edit, and do not let the agent stop while tests fail.

Wired in .agents/hooks.json (docs: https://antigravity.google/docs/hooks). The App runs hook
commands from inside the .agents folder, so the command there is `python3 hooks/run_tests.py`.
  post-edit : PostToolUse on the edit tools. Runs pytest and writes the result to
              .agents/last-test-run.txt. PostToolUse must answer {} on stdout.
  stop      : Stop. If pytest fails, answers {"decision": "continue", "reason": ...}, which the
              docs say is injected as a system message, so the agent keeps working on the failure.

The tests run with the project's own environment (.venv) when there is one, because that is
where pytest and the service's libraries are installed. Without pytest the hook does not hold
the agent: it writes why to .agents/last-test-run.txt and answers {}.
"""

import json
import subprocess
import sys
from pathlib import Path

MAX_STOP_RETRIES = 3


def project_python(workspace: Path) -> str:
    for candidate in (workspace / ".venv" / "bin" / "python", workspace / ".venv" / "Scripts" / "python.exe"):
        if candidate.exists():
            return str(candidate)
    return sys.executable


def run_pytest(cwd: Path):
    python = project_python(cwd)
    proc = subprocess.run([python, "-m", "pytest", "-q", "--no-header", "-p", "no:cacheprovider"],
                          cwd=cwd, capture_output=True, text=True)
    output = (proc.stdout + proc.stderr).strip()
    if "No module named pytest" in output:
        return None, ("The hook did not run the tests: pytest is not installed for " + python + ".\n"
                      "Create the project's environment first: python3 -m venv .venv, then "
                      ".venv/bin/pip install -r requirements.txt pytest "
                      "(Windows: .venv\\Scripts\\pip).")
    return proc.returncode, output


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "post-edit"
    event = json.loads(sys.stdin.read() or "{}")
    workspace = Path((event.get("workspacePaths") or ["."])[0])
    code, output = run_pytest(workspace)
    (workspace / ".agents" / "last-test-run.txt").write_text(output + "\n")

    if mode == "stop" and code and int(event.get("executionNum") or 0) < MAX_STOP_RETRIES:
        tail = "\n".join(output.splitlines()[-15:])
        print(json.dumps({"decision": "continue",
                          "reason": "pytest is failing. Fix the code (not the tests) before you finish:\n" + tail}))
    else:
        print("{}")


if __name__ == "__main__":
    main()
