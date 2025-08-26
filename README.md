# staticscan
Source code analysis with telescopic ruleset.

A very small static code analysis cli tool.
Also works on a smartphone. 
No massive installs, downloads or compiles.
This is a precompute vulnerability scanner for source code.

## Requirements
```python
PyYAML>=6.0
```


## Languages:
```python
def map_ext_to_lang(self, ext):
    ext_map = {
        # Scripting / high-level languages
        ".py": "python",
        ".js": "javascript",
        ".php": "php",
        ".rb": "ruby",
        ".pl": "perl",
        ".R": "r",

        # JVM / Kotlin
        ".java": "java",
        ".kt": "kotlin",
        ".scala": "scala",

        # Rust
        ".rs": "rust",

        # C-family languages
        ".c": "c",
        ".h": "c",          # header file
        ".cpp": "cpp",
        ".hpp": "cpp",      # header file
        ".cc": "cpp",
        ".cxx": "cpp",
        ".cs": "csharp",
        
        # Configuration / markup
        ".json": "json",
        ".yaml": "yaml",
        ".yml": "yaml",
        ".xml": "xml",
        ".toml": "toml",
        ".ini": "ini",

        # Shell / scripts
        ".sh": "shell",
        ".bat": "batch",
        ".ps1": "powershell",
    }
    return ext_map.get(ext.lower(), None)
```

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
