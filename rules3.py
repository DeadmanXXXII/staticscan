RULES.update({
    "kotlin": [
        {"regex": r"Runtime\.getRuntime\(\)\.exec\(", "desc": "Command execution risk", "cwe": "CWE-78"},
        {"regex": r"ObjectInputStream\(", "desc": "Insecure Java object deserialization", "cwe": "CWE-502"},
        {"regex": r"allowMainThreadQueries\(", "desc": "SQLite DB operations on main thread", "cwe": "CWE-666"},
        {"regex": r"setJavaScriptEnabled\(true\)", "desc": "Enabling JS in WebView (XSS risk)", "cwe": "CWE-79"},
        {"regex": r"KeyStore\.getInstance\(\"JKS\"\)", "desc": "Use of JKS keystore (weak, legacy)", "cwe": "CWE-327"},
        {"regex": r"ignoreSslErrors\(", "desc": "Ignoring SSL/TLS errors", "cwe": "CWE-295"},
        {"regex": r"HttpURLConnection\.setHostnameVerifier\(.*\)", "desc": "Custom hostname verifier (potential SSL bypass)", "cwe": "CWE-295"},
        {"regex": r"File\(.*\)\.writeText\(", "desc": "Potential insecure file write", "cwe": "CWE-73"}
    ],
    "r": [
        {"regex": r"eval\(", "desc": "Arbitrary code execution risk", "cwe": "CWE-94"},
        {"regex": r"parse\(text\s*=", "desc": "Dynamic code parsing/execution", "cwe": "CWE-94"},
        {"regex": r"system\(", "desc": "OS command execution risk", "cwe": "CWE-78"},
        {"regex": r"shell\(", "desc": "Shell command execution risk", "cwe": "CWE-78"},
        {"regex": r"download\.file\(", "desc": "Unvalidated external file download", "cwe": "CWE-829"},
        {"regex": r"read\.csv\([^)]*http", "desc": "Loading CSV directly from remote URL", "cwe": "CWE-829"},
        {"regex": r"RCurl::getURL\(", "desc": "Unvalidated external data fetch", "cwe": "CWE-829"},
        {"regex": r"save\(.*file\s*=\s*\".*\.RData\"", "desc": "Insecure RData serialization", "cwe": "CWE-502"}
    ],
    "rust": [
        {"regex": r"unsafe\s*\{", "desc": "Use of unsafe Rust block", "cwe": "CWE-120"},
        {"regex": r"std::process::Command::new\(", "desc": "Command injection risk", "cwe": "CWE-78"},
        {"regex": r"unwrap\(", "desc": "Unwrapping Result/Option without handling errors", "cwe": "CWE-754"},
        {"regex": r"expect\(", "desc": "Using expect() without error handling", "cwe": "CWE-754"},
        {"regex": r"std::fs::write\(", "desc": "File write operation (check for path traversal)", "cwe": "CWE-73"},
        {"regex": r"std::fs::read_to_string\(", "desc": "File read operation (potential sensitive data exposure)", "cwe": "CWE-200"},
        {"regex": r"openssl::ssl::SslConnector::builder\(.*verify_none", "desc": "Disabling SSL verification in Rust OpenSSL", "cwe": "CWE-295"},
        {"regex": r"let\s+password\s*=\s*\".+\"", "desc": "Hardcoded password in Rust code", "cwe": "CWE-798"}
    ]
})
