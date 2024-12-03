import sys
import importlib.util

def is_standard_lib(module_name: str) -> bool:
    """Check if a module is part of the Python standard library."""
    if module_name in sys.builtin_module_names:
        return True
    spec = importlib.util.find_spec(module_name)
    return spec is not None and spec.origin in ["built-in", "frozen"]


def sort_imports(code: str, slug: str = "") -> str:
    """Sort imports according to specified rules."""
    standard_imports = []
    third_party_imports = []
    app_specific_imports = []

    for line in code.splitlines():
        line = line.strip()
        if not line.startswith("import") and not line.startswith("from"):
            continue
        
        first_dot = True if line.split()[1][0] == "." else False
        module_name = line.split()[1].split(".")[0]

        if is_standard_lib(module_name):
            standard_imports.append(line)
        elif first_dot or module_name==slug:
            if first_dot:
                line += "  # TODO: Refactor relative import '.file' to an absolute import."
            app_specific_imports.append(line)
        else:
            third_party_imports.append(line)

    def sort_group(group):
        return sorted(group, key=lambda s: s.lower())

    sorted_code = "\n".join(
        sort_group(standard_imports)
        + [""]
        + sort_group(third_party_imports)
        + [""]
        + sort_group(app_specific_imports)
    ).strip()
    return sorted_code
