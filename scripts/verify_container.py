"""Build-independent smoke test for the hardened reference container."""

from __future__ import annotations

import json
import subprocess
import time
import urllib.request


IMAGE = "panelforge-reference:ci"
CONTAINER = "panelforge-reference-ci"
URL = "http://127.0.0.1:4174/api/health"


def docker(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["docker", *args],
        check=check,
        capture_output=True,
        text=True,
    )


def main() -> int:
    docker("rm", "--force", CONTAINER, check=False)
    docker(
        "run",
        "--detach",
        "--name",
        CONTAINER,
        "--publish",
        "127.0.0.1:4174:4173",
        "--read-only",
        "--tmpfs",
        "/tmp",
        "--tmpfs",
        "/var/lib/panelforge:uid=10001,gid=10001,mode=700",
        "--env",
        "PANELFORGE_SESSION_SECRET=ci-container-secret",
        "--health-interval=2s",
        "--health-timeout=3s",
        "--health-retries=5",
        IMAGE,
    )
    try:
        deadline = time.monotonic() + 30
        health = ""
        while time.monotonic() < deadline:
            try:
                with urllib.request.urlopen(URL, timeout=2) as response:
                    if response.status == 200:
                        break
            except OSError:
                time.sleep(1)
        else:
            raise RuntimeError("container health endpoint did not respond")

        while time.monotonic() < deadline:
            inspect = docker(
                "inspect",
                "--format",
                "{{json .State.Health}}",
                CONTAINER,
            )
            health = json.loads(inspect.stdout).get("Status", "")
            if health == "healthy":
                break
            time.sleep(1)
        else:
            raise RuntimeError(f"container health status was {health!r}")

        user = docker("inspect", "--format", "{{.Config.User}}", CONTAINER).stdout.strip()
        if user != "panelforge":
            raise RuntimeError(f"container user was {user!r}")
        print("Container smoke passed: API healthy and runtime user is panelforge.")
    finally:
        docker("rm", "--force", CONTAINER, check=False)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
