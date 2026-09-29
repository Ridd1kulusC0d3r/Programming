#!/usr/bin/env bash
set -euo pipefail

printf 'user=%s\n' "${USER:-unknown}"
printf 'shell=%s\n' "${SHELL:-unknown}"
printf 'kernel=%s\n' "$(uname -s)"
printf 'architecture=%s\n' "$(uname -m)"
