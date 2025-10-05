"""
Utility functions for SPSS preparation tool.
Includes variable name sanitization, path handling, and detection heuristics.
"""

import re
import os
from typing import List, Optional


def sanitize_variable_name(name: str, max_length: int = 64) -> str:
    """
    Sanitize a column name to be SPSS-compatible.
    
    Rules:
    - Must start with a letter
    - Can only contain letters, digits, and underscores
    - Maximum length of 64 characters (SPSS limit)
    - No spaces or special characters
    
    Args:
        name: Original column name
        max_length: Maximum allowed length (default 64)
        
    Returns:
        Sanitized variable name
    """
    # Replace spaces and special chars with underscore
    sanitized = re.sub(r'[^a-zA-Z0-9_]', '_', name)
    
    # Remove consecutive underscores
    sanitized = re.sub(r'_+', '_', sanitized)
    
    # Ensure it starts with a letter
    if not sanitized or not sanitized[0].isalpha():
        sanitized = 'v_' + sanitized
    
    # Truncate to max length
    sanitized = sanitized[:max_length]
    
    # Remove trailing underscores
    sanitized = sanitized.rstrip('_')
    
    return sanitized


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


def escape_spss_string(text: str) -> str:
    """
    Escape a string for use in SPSS syntax (VALUE LABELS).
    Single quotes are escaped by doubling them.
    
    Args:
        text: Original text
        
    Returns:
        Escaped text safe for SPSS
    """
    # Replace single quotes with two single quotes (SPSS convention)
    return text.replace("'", "''")

