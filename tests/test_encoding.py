"""
Unit tests for encoding and utility functions.
Run with: pytest tests/
"""

import pytest
import pandas as pd
from utils import sanitize_variable_name, format_spss_path, is_likely_likert, escape_spss_string, strip_bidi_characters
from encoder import ColumnConfig, detect_columns, apply_encoding
from sps_generator import generate_value_labels_block


class TestSanitizeVariableName:
    """Tests for variable name sanitization."""
    
    def test_basic_sanitization(self):
        """Test basic character replacement."""
        assert sanitize_variable_name("My Question 1") == "My_Question_1"
        assert sanitize_variable_name("Price ($)") == "Price"
        assert sanitize_variable_name("First-Name") == "First_Name"
    
    def test_starts_with_letter(self):
        """Test that names start with a letter."""
        assert sanitize_variable_name("123abc").startswith("v_")
        # Updated: leading underscores are stripped, so "_test" becomes "test"
        assert sanitize_variable_name("_test") == "test"
        # Empty after stripping should return fallback
        assert sanitize_variable_name("___") == "var"
    
    def test_max_length(self):
        """Test truncation to max length."""
        long_name = "a" * 100
        sanitized = sanitize_variable_name(long_name, max_length=64)
        assert len(sanitized) <= 64
    
    def test_consecutive_underscores(self):
        """Test removal of consecutive underscores."""
        assert sanitize_variable_name("test___name") == "test_name"
        assert sanitize_variable_name("a__b__c") == "a_b_c"
    
    def test_special_characters(self):
        """Test handling of special characters."""
        assert sanitize_variable_name("email@domain.com") == "email_domain_com"
        assert sanitize_variable_name("50% complete") == "v_50_complete"


class TestStripBidiCharacters:
    """Tests for Unicode bidirectional character stripping."""
    
    def test_ltr_mark_removal(self):
        """Test removal of LEFT-TO-RIGHT marks."""
        text_with_ltr = "Sheet\u200E1\u200E"
        assert strip_bidi_characters(text_with_ltr) == "Sheet1"
    
    def test_rtl_mark_removal(self):
        """Test removal of RIGHT-TO-LEFT marks."""
        text_with_rtl = "var\u200F1\u200F"
        assert strip_bidi_characters(text_with_rtl) == "var1"
    
    def test_mixed_bidi_removal(self):
        """Test removal of multiple bidi character types."""
        text_with_mixed = "\u202Avar\u200E1\u202C"
        assert strip_bidi_characters(text_with_mixed) == "var1"
    
    def test_arabic_text_preserved(self):
        """Test that Arabic text is preserved while bidi marks are removed."""
        text = "\u200Fموافق\u200E"
        result = strip_bidi_characters(text)
        assert result == "موافق"
        assert "\u200F" not in result
        assert "\u200E" not in result
    
    def test_no_bidi_characters(self):
        """Test text without bidi characters is unchanged."""
        assert strip_bidi_characters("Hello World") == "Hello World"
        assert strip_bidi_characters("123") == "123"


class TestEscapeSPSSString:
    """Tests for SPSS string escaping."""
    
    def test_single_quote_escaping(self):
        """Test that single quotes are doubled."""
        assert escape_spss_string("It's great") == "It''s great"
        assert escape_spss_string("can't") == "can''t"
    
    def test_no_escaping_needed(self):
        """Test strings without quotes."""
        assert escape_spss_string("Normal text") == "Normal text"
        assert escape_spss_string("123") == "123"
    
    def test_bidi_removal_in_escape(self):
        """Test that bidi characters are removed during escaping."""
        text_with_bidi = "It\u200E's\u200F great"
        assert escape_spss_string(text_with_bidi) == "It''s great"


class TestIsLikelyLikert:
    """Tests for Likert scale detection."""
    
    def test_likert_detection_positive(self):
        """Test detection of common Likert scales."""
        assert is_likely_likert(['Strongly Disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly Agree'])
        assert is_likely_likert(['Never', 'Rarely', 'Sometimes', 'Often', 'Always'])
        assert is_likely_likert(['Low', 'Medium', 'High'])
    
    def test_likert_detection_negative(self):
        """Test rejection of non-Likert data."""
        assert not is_likely_likert(['Apple', 'Banana', 'Cherry'])
        assert not is_likely_likert(['Yes', 'No'])  # Only 2 values
        assert not is_likely_likert(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])  # Too many


class TestColumnConfig:
    """Tests for ColumnConfig mapping generation."""
    
    def test_ascending_mapping(self):
        """Test ascending direction mapping."""
        config = ColumnConfig(
            column_name='q1',
            unique_values=['Low', 'Medium', 'High'],
            encoding_type='Ordinal',
            start_value=1,
            direction='Ascending'
        )
        mapping = config.get_mapping()
        assert mapping == {'Low': 1, 'Medium': 2, 'High': 3}
    
    def test_descending_mapping(self):
        """Test descending direction mapping."""
        config = ColumnConfig(
            column_name='q1',
            unique_values=['Low', 'Medium', 'High'],
            encoding_type='Ordinal',
            start_value=1,
            direction='Descending'
        )
        mapping = config.get_mapping()
        assert mapping == {'Low': 3, 'Medium': 2, 'High': 1}
    
    def test_custom_start_value(self):
        """Test custom starting value."""
        config = ColumnConfig(
            column_name='q1',
            unique_values=['A', 'B', 'C'],
            encoding_type='Nominal',
            start_value=10,
            direction='Ascending'
        )
        mapping = config.get_mapping()
        assert mapping == {'A': 10, 'B': 11, 'C': 12}
    
    def test_ignore_type(self):
        """Test that Ignore type returns empty mapping."""
        config = ColumnConfig(
            column_name='q1',
            unique_values=['A', 'B'],
            encoding_type='Ignore'
        )
        mapping = config.get_mapping()
        assert mapping == {}


class TestDetectColumns:
    """Tests for column detection."""
    
    def test_basic_detection(self):
        """Test basic column detection."""
        df = pd.DataFrame({
            'Q1': ['Agree', 'Disagree', 'Agree', 'Neutral'],
            'Q2': ['Yes', 'No', 'Yes', 'Yes']
        })
        
        info = detect_columns(df)
        
        assert 'Q1' in info
        assert 'Q2' in info
        assert info['Q1']['n_unique'] == 3
        assert info['Q2']['n_unique'] == 2
    
    def test_missing_values(self):
        """Test detection of missing values."""
        df = pd.DataFrame({
            'Q1': ['A', None, 'B', None, 'C']
        })
        
        info = detect_columns(df)
        assert info['Q1']['n_missing'] == 2


class TestGenerateValueLabelsBlock:
    """Tests for SPSS VALUE LABELS generation."""
    
    def test_simple_value_labels(self):
        """Test generation of simple value labels."""
        mappings = {
            'q1': {'Disagree': 1, 'Neutral': 2, 'Agree': 3}
        }
        original_names = {'q1': 'Q1'}
        
        block = generate_value_labels_block(mappings, original_names)
        
        assert 'VALUE LABELS' in block
        assert 'q1' in block
        assert "1 'Disagree'" in block
        assert "2 'Neutral'" in block
        assert "3 'Agree'" in block
        assert block.endswith('.')
    
    def test_multiple_variables(self):
        """Test multiple variables in VALUE LABELS."""
        mappings = {
            'q1': {'Low': 1, 'High': 2},
            'q2': {'Yes': 1, 'No': 2}
        }
        original_names = {'q1': 'Q1', 'q2': 'Q2'}
        
        block = generate_value_labels_block(mappings, original_names)
        
        assert 'q1' in block
        assert 'q2' in block
        assert block.count('.') == 1  # Only one period at the end
        assert block.count('/') == 1  # Forward slash between variables
    
    def test_escaping_in_labels(self):
        """Test that quotes are escaped in labels."""
        mappings = {
            'q1': {"It's good": 1, "It's bad": 2}
        }
        original_names = {'q1': 'Q1'}
        
        block = generate_value_labels_block(mappings, original_names)
        
        # Should have doubled quotes
        assert "It''s good" in block
        assert "It''s bad" in block


class TestApplyEncoding:
    """Tests for applying encoding to dataframes."""
    
    def test_basic_encoding(self):
        """Test basic encoding application."""
        df = pd.DataFrame({
            'Q1': ['Low', 'Medium', 'High', 'Low']
        })
        
        config = ColumnConfig(
            column_name='Q1',
            unique_values=['Low', 'Medium', 'High'],
            encoding_type='Ordinal',
            start_value=1,
            direction='Ascending'
        )
        
        encoded_df, mappings = apply_encoding(df, {'Q1': config})
        
        assert encoded_df['Q1'].tolist() == [1.0, 2.0, 3.0, 1.0]
        assert 'Q1' in mappings
    
    def test_missing_values_preserved(self):
        """Test that missing values are preserved."""
        df = pd.DataFrame({
            'Q1': ['Low', None, 'High']
        })
        
        config = ColumnConfig(
            column_name='Q1',
            unique_values=['Low', 'High'],
            encoding_type='Ordinal',
            start_value=1,
            direction='Ascending'
        )
        
        encoded_df, _ = apply_encoding(df, {'Q1': config})
        
        assert pd.isna(encoded_df['Q1'].iloc[1])


if __name__ == '__main__':
    pytest.main([__file__, '-v'])

