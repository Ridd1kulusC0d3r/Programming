# Programming

> Multi-language learning lab focused on software engineering, automation, tooling and security-oriented development.

[![Quality](https://github.com/Ridd1kulusC0d3r/Programming/actions/workflows/quality.yml/badge.svg)](https://github.com/Ridd1kulusC0d3r/Programming/actions/workflows/quality.yml)

This repository is my structured programming workspace: notes, exercises, small utilities and progressively more complete projects across multiple languages.

## Languages

| Language | Focus | Path |
|---|---|---|
| Python | automation, scripting, data processing | [Python](./Python/) |
| Go | CLIs, concurrency, networking foundations | [Go](./Go/) |
| TypeScript | typed applications and tooling | [TypeScript](./TypeScript/) |
| JavaScript | language fundamentals and runtime APIs | [JavaScript](./JavaScript/) |
| Shell | Linux automation and operational workflows | [Shell](./Shell/) |

## Repository model

Each language follows the same learning progression:

```text
fundamentals -> exercises -> scripts -> mini-projects -> portfolio projects
```

Existing Python course material has been preserved. New content should prefer descriptive names, small focused directories and a README whenever a folder represents a complete topic or project.

## Structure

```text
Programming/
├── Python/
├── Go/
├── TypeScript/
├── JavaScript/
├── Shell/
├── docs/
│   └── ROADMAP.md
├── repos/
│   └── sitemap.md
├── .github/
│   └── workflows/
│       └── quality.yml
├── CONTRIBUTING.md
├── Meu_guia_de_estudos.md
└── README.md
```

## Learning priorities

1. **Programming fundamentals**: variables, control flow, functions, data structures and error handling.
2. **Software construction**: modules, packages, testing, dependency management and documentation.
3. **Automation**: filesystem, processes, APIs, structured data and CLI tooling.
4. **Engineering practice**: Git, code review, CI, debugging and maintainability.
5. **Portfolio projects**: useful tools that combine multiple concepts instead of isolated syntax drills.

See [the roadmap](./docs/ROADMAP.md) for the progression and [the study guide](./Meu_guia_de_estudos.md) for learning resources.

## Quality checks

The repository runs lightweight GitHub Actions checks for Python, Go, TypeScript, JavaScript and Shell.

## Contribution conventions

See [CONTRIBUTING.md](./CONTRIBUTING.md).

---

Built as a continuous learning repository: small experiments are welcome, but every new directory should make the repository easier to understand than it was before.
