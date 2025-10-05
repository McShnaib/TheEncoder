"""
Utility functions for SPSS preparation tool.
Includes variable name sanitization, path handling, and detection heuristics.
"""

import re
import os
from typing import List, Optional, Dict

# Export strip_bidi_characters for use in other modules
__all__ = ['sanitize_variable_name', 'generate_unique_var_names', 'format_spss_path', 
           'is_likely_likert', 'is_multi_response', 'escape_spss_string', 'strip_bidi_characters']


def sanitize_variable_name(name: str, max_length: int = 64, fallback_prefix: str = "var") -> str:
    """
    Sanitize a column name to be SPSS-compatible.
    
    Rules:
    - Must start with a letter
    - Can only contain letters, digits, and underscores
    - Maximum length of 64 characters (SPSS limit)
    - No spaces or special characters
    - For non-ASCII names (e.g., Arabic), returns fallback_prefix
    
    Args:
        name: Original column name
        max_length: Maximum allowed length (default 64)
        fallback_prefix: Prefix to use if name has no ASCII chars (default "var")
        
    Returns:
        Sanitized variable name
    """
    # Replace spaces and special chars with underscore
    sanitized = re.sub(r'[^a-zA-Z0-9_]', '_', name)
    
    # Remove consecutive underscores
    sanitized = re.sub(r'_+', '_', sanitized)
    
    # Strip leading/trailing underscores
    sanitized = sanitized.strip('_')
    
    # If empty or only underscores (e.g., Arabic text), use fallback
    if not sanitized:
        return fallback_prefix
    
    # Ensure it starts with a letter
    if not sanitized[0].isalpha():
        sanitized = 'v_' + sanitized
    
    # Truncate to max length
    sanitized = sanitized[:max_length]
    
    # Remove trailing underscores
    sanitized = sanitized.rstrip('_')
    
    return sanitized


def generate_unique_var_names(column_names: List[str], max_length: int = 64) -> Dict[str, str]:
    """
    Generate unique SPSS-compatible variable names for a list of column names.
    Handles non-ASCII names (e.g., Arabic) by assigning unique sequential names.
    
    Args:
        column_names: List of original column names
        max_length: Maximum length for variable names
        
    Returns:
        Dictionary mapping original names to sanitized unique names
    """
    name_map = {}
    used_names = set()
    var_counter = 1
    
    for original_name in column_names:
        # Try to sanitize normally
        sanitized = sanitize_variable_name(original_name, max_length, fallback_prefix=f"var{var_counter}")
        
        # If this name was a fallback or already used, make it unique
        if sanitized in used_names or sanitized.startswith('var') and len(sanitized) <= 6:
            # Generate unique name
            while f"var{var_counter}" in used_names:
                var_counter += 1
            sanitized = f"var{var_counter}"
            var_counter += 1
        elif sanitized == sanitize_variable_name(original_name, max_length, fallback_prefix="var"):
            # This was likely a fallback, assign unique number
            while f"var{var_counter}" in used_names:
                var_counter += 1
            sanitized = f"var{var_counter}"
            var_counter += 1
        
        used_names.add(sanitized)
        name_map[original_name] = sanitized
    
    return name_map


def format_spss_path(path: str) -> str:
    """
    Format a file path for use in SPSS syntax.
    Converts to absolute path and escapes backslashes for Windows.
    
    Args:
        path: File path (relative or absolute)
        
    Returns:
        SPSS-compatible path string with escaped backslashes
    """
    abs_path = os.path.abspath(path)
    # Double backslashes for SPSS on Windows
    spss_path = abs_path.replace('\\', '\\\\')
    return spss_path


def is_likely_likert(unique_values: List[str]) -> bool:
    """
    Heuristic to detect if a column contains Likert-scale data.
    
    Criteria:
    - Between 3 and 7 unique values
    - Contains common Likert keywords
    
    Args:
        unique_values: List of unique string values in column
        
    Returns:
        True if likely Likert scale, False otherwise
    """
    if not (3 <= len(unique_values) <= 7):
        return False
    
    # Common Likert scale keywords (case-insensitive)
    likert_keywords = [
        'strongly disagree', 'disagree', 'neutral', 'agree', 'strongly agree',
        'never', 'rarely', 'sometimes', 'often', 'always',
        'very dissatisfied', 'dissatisfied', 'satisfied', 'very satisfied',
        'not at all', 'slightly', 'moderately', 'very', 'extremely',
        'poor', 'fair', 'good', 'very good', 'excellent',
        'low', 'medium', 'high',
        'yes', 'no', 'maybe'
    ]
    
    # Check if any value matches Likert keywords
    values_lower = [str(v).lower().strip() for v in unique_values]
    for keyword in likert_keywords:
        if keyword in values_lower:
            return True
    
    return False


def is_multi_response(value: str) -> bool:
    """
    Check if a value appears to be a multi-response (contains comma or semicolon).
    
    Args:
        value: String value to check
        
    Returns:
        True if value contains comma or semicolon separators
    """
    if not isinstance(value, str):
        return False
    return ',' in value or ';' in value


def strip_bidi_characters(text: str) -> str:
    """
    Remove Unicode bidirectional formatting characters that break SPSS syntax.
    These invisible characters (LTR/RTL marks, embeddings, overrides) are often
    inserted with Arabic text but cause SPSS parsing errors.
    
    Args:
        text: Text potentially containing bidi characters
        
    Returns:
        Clean text with bidi characters removed
    """
    # Unicode bidirectional formatting characters to remove
    bidi_chars = [
        '\u200E',  # LEFT-TO-RIGHT MARK
        '\u200F',  # RIGHT-TO-LEFT MARK
        '\u202A',  # LEFT-TO-RIGHT EMBEDDING
        '\u202B',  # RIGHT-TO-LEFT EMBEDDING
        '\u202C',  # POP DIRECTIONAL FORMATTING
        '\u202D',  # LEFT-TO-RIGHT OVERRIDE
        '\u202E',  # RIGHT-TO-LEFT OVERRIDE
        '\u2066',  # LEFT-TO-RIGHT ISOLATE
        '\u2067',  # RIGHT-TO-LEFT ISOLATE
        '\u2068',  # FIRST STRONG ISOLATE
        '\u2069',  # POP DIRECTIONAL ISOLATE
    ]
    
    clean_text = text
    for char in bidi_chars:
        clean_text = clean_text.replace(char, '')
    
    return clean_text


def escape_spss_string(text: str) -> str:
    """
    Escape a string for use in SPSS syntax (VALUE LABELS).
    Single quotes are escaped by doubling them.
    Also strips bidirectional Unicode control characters.
    
    Args:
        text: Original text
        
    Returns:
        Escaped text safe for SPSS
    """
    # Strip bidirectional formatting characters
    clean_text = strip_bidi_characters(text)
    # Replace single quotes with two single quotes (SPSS convention)
    return clean_text.replace("'", "''")

