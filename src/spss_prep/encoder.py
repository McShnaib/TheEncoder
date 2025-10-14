"""
Encoding functions for converting categorical data to numeric codes.
Handles detection, mapping creation, and application of encodings.
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Any, Optional
from collections import Counter
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ColumnConfig:
    """Configuration for encoding a single column."""
    
    def __init__(
        self,
        column_name: str,
        unique_values: List[str],
        encoding_type: str = 'Ordinal',
        start_value: int = 1,
        direction: str = 'Ascending',
        treat_missing: bool = True,
        sanitized_name: Optional[str] = None
    ):
        self.column_name = column_name
        self.unique_values = unique_values  # Ordered list
        self.encoding_type = encoding_type  # 'Ordinal', 'Nominal', 'Scale', 'Ignore'
        self.start_value = start_value
        self.direction = direction  # 'Ascending' or 'Descending'
        self.treat_missing = treat_missing
        self.sanitized_name = sanitized_name or column_name
        
    def get_mapping(self) -> Dict[str, int]:
        """
        Generate the encoding mapping based on configuration.
        
        Returns:
            Dictionary mapping original values to numeric codes
        """
        if self.encoding_type == 'Ignore':
            return {}
        
        # Scale variables (continuous numeric) don't need encoding
        if self.encoding_type == 'Scale':
            return {}
        
        mapping = {}
        n_values = len(self.unique_values)
        
        if self.direction == 'Ascending':
            # First item gets smallest number
            for idx, value in enumerate(self.unique_values):
                mapping[value] = self.start_value + idx
        else:  # Descending
            # First item gets largest number
            for idx, value in enumerate(self.unique_values):
                mapping[value] = self.start_value + (n_values - 1 - idx)
        
        return mapping


def detect_columns(df: pd.DataFrame) -> Dict[str, Dict[str, Any]]:
    """
    Detect unique values and metadata for each column in the dataframe.
    
    Args:
        df: Input dataframe
        
    Returns:
        Dictionary with column metadata including unique values, counts, etc.
    """
    column_info = {}
    
    for col in df.columns:
        # Get non-null values
        values = df[col].dropna()
        
        # Check if already numeric
        numeric_ratio = 0
        try:
            numeric_converted = pd.to_numeric(values, errors='coerce')
            numeric_ratio = numeric_converted.notna().sum() / len(values) if len(values) > 0 else 0
        except:
            numeric_ratio = 0
        
        # Get unique values sorted by frequency
        value_counts = Counter(values)
        unique_values = [str(val) for val, _ in value_counts.most_common()]
        
        # Check for multi-response indicators
        has_multi_response = any(
            ',' in str(val) or ';' in str(val) 
            for val in unique_values
        )
        
        column_info[col] = {
            'unique_values': unique_values,
            'n_unique': len(unique_values),
            'n_missing': df[col].isna().sum(),
            'is_numeric': numeric_ratio > 0.8,
            'has_multi_response': has_multi_response,
            'value_counts': dict(value_counts)
        }
        
    return column_info


def apply_encoding(
    df: pd.DataFrame,
    configs: Dict[str, ColumnConfig]
) -> Tuple[pd.DataFrame, Dict[str, Dict[str, int]]]:
    """
    Apply encoding configurations to the dataframe.
    
    Args:
        df: Input dataframe
        configs: Dictionary mapping column names to ColumnConfig objects
        
    Returns:
        Tuple of (encoded_dataframe, mappings_dict)
    """
    encoded_df = df.copy()
    all_mappings = {}
    
    for col_name, config in configs.items():
        if config.encoding_type == 'Ignore':
            continue
            
        mapping = config.get_mapping()
        all_mappings[col_name] = mapping
        
        # Apply mapping
        encoded_df[col_name] = df[col_name].map(lambda x: mapping.get(str(x), np.nan) if pd.notna(x) else np.nan)
        
        logger.info(f"Encoded column '{col_name}' with {len(mapping)} mappings")
    
    return encoded_df, all_mappings


def save_encoded_excel(df: pd.DataFrame, output_path: str, sheet_name: str = 'Sheet1') -> None:
    """
    Save encoded dataframe to Excel file in a format compatible with SPSS.
    Uses xlsxwriter engine for better SPSS compatibility.
    
    Args:
        df: Encoded dataframe
        output_path: Path to output Excel file
        sheet_name: Name of sheet to create
    """
    # Use xlsxwriter for better SPSS compatibility
    # Write with proper formatting to ensure SPSS can read it
    with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name=sheet_name, index=False)
        
        # Get workbook and worksheet objects
        workbook = writer.book
        worksheet = writer.sheets[sheet_name]
        
        # Set column widths for readability
        for idx, col in enumerate(df.columns):
            max_len = max(
                df[col].astype(str).apply(len).max(),
                len(str(col))
            )
            worksheet.set_column(idx, idx, min(max_len + 2, 50))
    
    logger.info(f"Saved encoded Excel to: {output_path}")


