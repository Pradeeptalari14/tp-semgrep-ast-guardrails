# Semgrep AST Policy Guardrails Studio

> **Production Repository:** `Pradeeptalari14/tp-semgrep-ast-guardrails`  
> **Interactive Studio Workspace:** [https://talaripradeep.info/tools/semgrep-ast-guardrails/](https://talaripradeep.info/tools/semgrep-ast-guardrails/)  
> **Visual Flow Canvas:** [https://talaripradeep.info/studios/flow/?studio=semgrep-ast-guardrails](https://talaripradeep.info/studios/flow/?studio=semgrep-ast-guardrails)

## Overview
Author custom Semgrep AST static analysis policies, taint tracking rules for SQL injection and SSRF, and automated SARIF publishing to GitHub Security tab.

## Primary Specification Manifest: `semgrep-rules.yml`
```yaml
rules:
  - id: detect-tainted-sql-injection
    languages: [python, javascript, go]
    severity: ERROR
    message: "Untrusted user input directly concatenated into SQL query"
    mode: taint
    pattern-sources:
      - pattern: request.args.get(...)
      - pattern: req.query[...]
    pattern-sinks:
      - pattern: db.execute(...)
      - pattern: cursor.execute(...)
```

## Verification & Execution
```bash
# Run local verification
git verify-commit HEAD
```

## License
MIT License. Copyright (c) 2026 Talari Pradeep.
