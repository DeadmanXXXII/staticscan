import importlib
import pkgutil
import os

def load_rules(rules_dir="staticscan/rules"):
    """
    Dynamically load all rule modules from rules_dir.
    Supports multiple rule files per language.
    """
    rules = {}
    package = "staticscan.rules"

    if not os.path.exists(rules_dir):
        return rules

    for _, module_name, _ in pkgutil.iter_modules([rules_dir]):
        if module_name.startswith("rules_"):
            lang = module_name.split("_")[1]
            module = importlib.import_module(f"{package}.{module_name}")
            rules.setdefault(lang, []).extend(getattr(module, "RULES", []))
    return rules
