# PyYAML Security Update

## Changes Made

Updated PyYAML dependency from version 5.3.1 to 5.4 in `pyproject.toml` to address a critical security vulnerability identified by Dependabot.

## Security Impact

PyYAML versions prior to 5.4 contain a security vulnerability that can be exploited through unsafe YAML loading. While this application intentionally uses unsafe YAML loading for demonstration purposes (in `main.py`), updating to PyYAML 5.4 ensures:

1. The underlying library has security fixes applied
2. Future safe usage of PyYAML will benefit from the security improvements
3. Compliance with security scanning requirements

## Files Modified

- `pyproject.toml`: Updated PyYAML dependency specification from "==5.3.1" to "==5.4"

## Testing

A test file `test_yaml_functionality.py` has been created to verify:
- PyYAML imports correctly
- Basic YAML loading functionality works
- The Flask application can still be imported
- Version requirements are met

## Note on Intentional Vulnerabilities

This application is intentionally vulnerable for security scanning demonstrations. The unsafe YAML loading in `main.py` (line 14) using `yaml.load()` with `yaml.Loader` remains intentionally vulnerable for demo purposes, but now uses a more secure underlying library version.