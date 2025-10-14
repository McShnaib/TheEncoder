"""
SPSS Prep Tool - Package for automating SPSS data preparation.

A Streamlit web application for preparing Google Forms Excel exports for IBM SPSS analysis.
"""

__version__ = "1.2.0"
__author__ = "SPSS Prep Tool Contributors"
__email__ = "your-email@example.com"
__license__ = "MIT"
__url__ = "https://github.com/your-org/spss-prep-tool"

__all__ = ["encoder", "sps_generator", "utils", "app"]


def main():
    """Entry point for the SPSS Prep Tool application."""
    import sys
    import subprocess
    from pathlib import Path
    
    # Get the path to app.py in the same directory
    app_path = Path(__file__).parent / "app.py"
    
    # Run streamlit with the app
    sys.exit(subprocess.call(["streamlit", "run", str(app_path)] + sys.argv[1:]))


