import json

class Report:
    @staticmethod
    def format(results, fmt="json"):
        if fmt == "json":
            return json.dumps(results, indent=2)
        elif fmt == "table":
            return Report.to_table(results)
        elif fmt == "markdown":
            return Report.to_markdown(results)
        return results

    @staticmethod
    def to_table(results):
        out = []
        for r in results:
            out.append(f"[{r['severity']}] {r['file']}:{r['line']} -> {r['message']} ({r['rule']})")
        return "\n".join(out)

    @staticmethod
    def to_markdown(results):
        md = ["| Severity | File | Line | Rule | Message |", "|---------|------|------|------|--------|"]
        for r in results:
            md.append(f"| {r['severity']} | {r['file']} | {r['line']} | {r['rule']} | {r['message']} |")
        return "\n".join(md)
