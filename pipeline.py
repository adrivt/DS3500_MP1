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
from data_loaders import load_data


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
    path = Path(filepath)
    if not path.is_file():
        logger.error(f"Input file not found or is not a file: {filepath}")
        return False
    logger.info(f"Input file validated: {filepath}")
    return True


def main():
    """Main pipeline function."""
    args = parse_arguments()
    setup_logging(args.verbose)
    logger.debug(f"Parsed arguments: {args}")
    if not validate_input(args.input):
        sys.exit(1) 
    try: 
        data=load_data(args.input)
    except ValueError as e:
        logger.error(f"Failed to load data: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
