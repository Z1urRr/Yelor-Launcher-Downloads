#!/bin/sh
set -eu

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <file> <expected-sha256>" >&2
  exit 2
fi

file=$1
expected=$(printf '%s' "$2" | tr '[:lower:]' '[:upper:]')

if command -v shasum >/dev/null 2>&1; then
  actual=$(shasum -a 256 "$file" | awk '{print toupper($1)}')
elif command -v sha256sum >/dev/null 2>&1; then
  actual=$(sha256sum "$file" | awk '{print toupper($1)}')
else
  echo "No SHA-256 command found." >&2
  exit 2
fi

if [ "$actual" != "$expected" ]; then
  echo "SHA-256 mismatch. Expected $expected, got $actual." >&2
  exit 1
fi

echo "Verified: $file"
echo "SHA-256: $actual"
