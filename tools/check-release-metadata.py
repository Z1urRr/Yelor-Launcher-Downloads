#!/usr/bin/env python3
import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HASH_LINE = re.compile(r"^([0-9A-F]{64})  ([^/\\]+)$")
BINARY_SUFFIXES = (".exe", ".dmg", ".app.zip", ".app.tar.gz")


def fail(message: str) -> None:
    raise ValueError(message)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_checksums() -> dict[str, str]:
    checksums: dict[str, str] = {}
    for line in read_text(ROOT / "SHA256SUMS.txt").splitlines():
        if not line:
            continue
        match = HASH_LINE.fullmatch(line)
        if not match:
            fail(f"Invalid SHA256SUMS line: {line!r}")
        digest, filename = match.groups()
        if filename in checksums:
            fail(f"Duplicate checksum entry: {filename}")
        checksums[filename] = digest
    return checksums


def verify_manifest(checksums: dict[str, str]) -> list[str]:
    manifest = json.loads(read_text(ROOT / "release-manifest.json"))
    if manifest.get("product") != "Yelor Launcher":
        fail("Unexpected product name")
    if manifest.get("version") != "0.1.4":
        fail("Unexpected release version")
    if manifest.get("channel") != "public-preview":
        fail("Unexpected release channel")
    date.fromisoformat(manifest["published_at"])

    artifacts = manifest.get("artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        fail("Manifest artifacts must be a non-empty list")

    filenames: list[str] = []
    for artifact in artifacts:
        filename = artifact.get("filename")
        digest = artifact.get("sha256")
        size = artifact.get("size")
        if not isinstance(filename, str) or Path(filename).name != filename:
            fail(f"Unsafe artifact filename: {filename!r}")
        if not isinstance(digest, str) or not re.fullmatch(r"[0-9A-F]{64}", digest):
            fail(f"Invalid artifact digest: {filename}")
        if not isinstance(size, int) or size <= 0:
            fail(f"Invalid artifact size: {filename}")
        if checksums.get(filename) != digest:
            fail(f"Manifest/checksum mismatch: {filename}")
        filenames.append(filename)

    if len(filenames) != len(set(filenames)):
        fail("Manifest contains duplicate artifact filenames")
    if set(filenames) != set(checksums):
        fail("Manifest and SHA256SUMS artifact sets differ")
    return filenames


def verify_docs(filenames: list[str]) -> None:
    required_docs = [
        ROOT / "README.md",
        ROOT / "RELEASE_NOTES_0.1.4.md",
        ROOT / "OPEN_SOURCE.md",
        ROOT / "SECURITY.md",
        ROOT / "SUPPORT.md",
        ROOT / "docs" / "INSTALLATION.md",
        ROOT / "docs" / "VERIFY_DOWNLOAD.md",
        ROOT / "docs" / "TROUBLESHOOTING.md",
    ]
    for path in required_docs:
        if not path.is_file():
            fail(f"Missing documentation file: {path.relative_to(ROOT)}")

    combined_release_docs = read_text(ROOT / "README.md") + read_text(
        ROOT / "RELEASE_NOTES_0.1.4.md"
    )
    for filename in filenames:
        if filename not in combined_release_docs:
            fail(f"Artifact is absent from public release docs: {filename}")

    local_link = re.compile(r"\[[^\]]+\]\((?!https?://|#)([^)]+)\)")
    for path in required_docs:
        for target in local_link.findall(read_text(path)):
            clean_target = target.split("#", 1)[0]
            if clean_target and not (path.parent / clean_target).resolve().exists():
                fail(f"Broken local link in {path.relative_to(ROOT)}: {target}")


def verify_public_tree() -> None:
    ET.parse(ROOT / "docs" / "assets" / "banner.svg")
    tracked_output = subprocess.check_output(
        ["git", "ls-files", "-z"], cwd=ROOT, text=False
    )
    for raw_path in tracked_output.split(b"\0"):
        if not raw_path:
            continue
        relative_path = Path(raw_path.decode("utf-8"))
        if relative_path.name.lower().endswith(BINARY_SUFFIXES):
            fail(f"Release binary must not be committed to Git: {relative_path}")


def main() -> int:
    try:
        checksums = parse_checksums()
        filenames = verify_manifest(checksums)
        verify_docs(filenames)
        verify_public_tree()
    except (
        KeyError,
        OSError,
        ValueError,
        json.JSONDecodeError,
        ET.ParseError,
        subprocess.SubprocessError,
    ) as exc:
        print(f"Release metadata verification failed: {exc}", file=sys.stderr)
        return 1

    print(f"Verified {len(filenames)} public artifacts and repository metadata.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
