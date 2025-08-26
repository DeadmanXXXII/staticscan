import os
import re
from staticscan.core.loader import load_rules
from staticscan.core.report import Report

class StaticScanner:
    def __init__(self, rules_dir="staticscan/rules"):
        self.rules = load_rules(rules_dir)

    def map_ext_to_lang(self, ext):
        ext_map = {
            ".py": "python",
            ".js": "javascript",
            ".php": "php",
            ".java": "java",
            ".kt": "kotlin",
            ".R": "r",
            ".rs": "rust"
        }
        return ext_map.get(ext.lower(), None)

    def scan_file(self, file_path, severity_filter=None, ruleset_filter=None):
        results = []
        _, ext = os.path.splitext(file_path)
        lang = self.map_ext_to_lang(ext)

        if not lang or lang not in self.rules:
            return results

        if ruleset_filter and lang not in ruleset_filter:
            return results

        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                code = f.read()
        except Exception:
            return results

        for rule in self.rules[lang]:
            if severity_filter and rule.get("severity", "").lower() not in severity_filter:
                continue
            matches = re.finditer(rule["pattern"], code, re.MULTILINE)
            for match in matches:
                results.append({
                    "file": file_path,
                    "language": lang,
                    "rule": rule.get("id"),
                    "severity": rule.get("severity"),
                    "message": rule.get("message"),
                    "line": code[:match.start()].count("\n") + 1
                })
        return results

    def scan_directory(self, path, severity_filter=None, ruleset_filter=None):
        all_results = []
        for root, _, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                all_results.extend(
                    self.scan_file(file_path, severity_filter, ruleset_filter)
                )
        return all_results

    def run(self, path, fmt="json", severity=None, ruleset=None):
        severity_filter = [s.lower() for s in severity] if severity else None
        ruleset_filter = [r.lower() for r in ruleset] if ruleset else None

        results = self.scan_directory(path, severity_filter, ruleset_filter)
        return Report.format(results, fmt)
