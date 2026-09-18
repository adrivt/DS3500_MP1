"""
Data Processing Pipeline - CLI Template

DS 3500 - MP1

Usage:
    python pipeline.py --input data.csv --output clean.csv
    python pipeline.py --input data.csv --output results.json --format json --verbose
"""

import argparse
import logging
import sys
from pathlib import Path


logger = logging.getLogger(__name__)


def setup_logging(verbose=False):
    """Configure logging for the pipeline."""
    level = logging.DEBUG if verbose else logging.INFO #if verbose, then DEBUG, else INFO
    
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)-8s %(message)s",
        datefmt="%H:%M:%S"
    )


def parse_arguments():
    """Parse command-line arguments."""
    #we first create the parser. 
    parser = argparse.ArgumentParser(
    description="MP1 Data Processing Pipeline"
    ) 
    #with it, we create the arguments we want to accept.
    parser.add_argument(
    "--input", "-i",
    required=True,
    help="Path to the input file")
    
    parser.add_argument(
    "--output", "-o",
    required=True,
    help="Path to the output file"
    )
    
    parser.add_argument(
        "--format", "-f",
        default="csv",
        choices=["csv", "json"],
        help="Output file format (default: csv)")
    
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose logging"
    )
    
    return parser.parse_args()


def validate_input(filepath):
    """Check whether the input path exists and is a file."""
    pass  # TODO: implement


def main():
    """Main pipeline function."""
    pass  # TODO: implement


if __name__ == "__main__":
    main()
