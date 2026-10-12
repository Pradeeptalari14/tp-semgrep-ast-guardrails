#!/usr/bin/env python3
"""
Custom Semgrep AST Policy Validator & SARIF Exporter
"""
import subprocess
import json
import sys

def run_semgrep_ast_audit(rules_path: str = "semgrep-rules.yml", target_dir: str = "."):
    cmd = ["semgrep", "scan", "--config", rules_path, "--sarif", "--output=semgrep.sarif", target_dir]
    res = subprocess.run(cmd, capture_output=True, text=True)
    print("Semgrep AST scan completed. Results saved to semgrep.sarif")
    return res.returncode

if __name__ == "__main__":
    run_semgrep_ast_audit()
