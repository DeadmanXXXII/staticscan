import argparse
from staticscan.core.scanner import StaticScanner

def main():
    parser = argparse.ArgumentParser(description="🔎 StaticScan - Red Team Static Code Analyzer")
    parser.add_argument("target", help="File or directory to scan")
    parser.add_argument("--fmt", choices=["json", "table", "markdown"], default="table", help="Output format")
    parser.add_argument("--severity", nargs="+", choices=["low", "medium", "high"], help="Filter by severity")
    parser.add_argument("--ruleset", nargs="+", help="Filter by language ruleset (python, javascript, etc.)")
    parser.add_argument("--output", "-o", help="Save output to a file")
    args = parser.parse_args()

    scanner = StaticScanner()
    results = scanner.run(
        path=args.target,
        fmt=args.fmt,
        severity=args.severity,
        ruleset=args.ruleset
    )

    print(results)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(results)
        print(f"\n📄 Report saved to {args.output}")

if __name__ == "__main__":
    main()
