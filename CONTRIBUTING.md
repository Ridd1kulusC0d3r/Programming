# Contributing

This repository is primarily a learning lab, but changes should still follow basic engineering hygiene.

## Naming

- Prefer English, lowercase directory names for new project folders.
- Use descriptive file names.
- Avoid names such as `test1`, `new`, `final-final` and their inevitable descendants.

## New projects

A project directory should contain:

- a short `README.md`
- source code
- dependency/build metadata when needed
- tests when the project has meaningful logic
- no secrets, tokens, credentials or generated build artifacts

## Commits

Prefer small commits with clear messages:

```text
feat(go): add concurrent checker
docs(python): document packaging notes
fix(shell): handle missing environment variable
```

## Pull requests

Describe:

1. what changed
2. why it changed
3. how it was tested

The repository should become easier to navigate with each contribution.
