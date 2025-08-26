# staticscan
Source code analysis with telescopic ruleset.

---

1️⃣ Scanning a single file

You can point staticscan at a file path:

python cli.py /path/to/myfile.py

It will automatically detect the language from the extension (.py → Python).

It will load all rules for that language.

Output will show any matches with line numbers, severity, and rule IDs.


You can also save the output:
```
python cli.py /path/to/myfile.py --fmt json --output report.json
```

---

2️⃣ Scanning a directory

Point it at a directory:

python cli.py /path/to/project/

staticscan recursively walks the directory tree.

Each file is checked based on its extension.

Multiple languages in the same directory are automatically handled.


Example: a project with .py, .js, .php files:

Python files → Python rules

JavaScript files → JS rules

PHP files → PHP rules


No need to limit to a single language; the scanner automatically supports multi-language workflows.


---

3️⃣ Filtering by language

If you want to scan only certain languages in a mixed project:
```
python cli.py /path/to/project --ruleset python javascript
```
Only Python and JavaScript rules will be applied.

All other files will be ignored.



---

4️⃣ Filtering by severity

You can scan everything but only report certain severities:

python cli.py /path/to/project --severity high medium

Low-severity matches are ignored.



---

5️⃣ Combined workflow example

Scan a mixed-language project, only Python and Rust rules, only high-severity issues, save output to JSON:
```
python cli.py /path/to/project --ruleset python rust --severity high --fmt json --output report.json
```
✅ Detects Python and Rust files

✅ Applies rules only for those languages

✅ Filters by high severity

✅ Saves a report



---

Summary

Supports multiple languages in a single workflow.

Language detection is automatic via file extension.

Filters let you restrict which languages or severities are reported.

Works for single files or whole directories.



---
