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
from src import (
    create_cleaning_report,
    load_data,
    process_data,
    save_data,
    setup_logging,
    validate_dataframe,
    validate_input,
)




logger = logging.getLogger(__name__)


def setup_logging(verbose=False):
    """Configure logging for the pipeline."""
    level = logging.DEBUG if verbose else logging.INFO #if verbose, then DEBUG, else INFO
    
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)-8s %(name)s — %(message)s",
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
        "--config", "-conf", 
        required=True,
        help="Path to the YAML configuration file"
    )
    
    parser.add_argument(
    "--output", "-o",
    required=True,
    help="Path to the output file"
    )
    
    
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
    if not validate_input(args.config):
        sys.exit(1)
        
    try: 
        data=load_data(args.input)
        config = load_data(args.config)
    except ValueError as e:
        logger.error(f"Failed to load data: {e}")
        sys.exit(1)
        
    required_columns = config["validation"]["required_columns"]
    numeric_columns = config["validation"]["numeric_columns"]

    rows_before_validation = len(data)
    try:
        data = validate_dataframe(data, required_columns, numeric_columns)
    except ValueError as e:
        logger.error(f"Validation failed: {e}")
        sys.exit(1)
        
    df_before = data.copy()
    
    #Log the number of rows before and after validation at the INFO level.
    logger.info(f"Rows before validation: {rows_before_validation}. Rows after validation: {len(df_before)}")
    
    try:
        df_after = process_data(data, config)
    except ValueError as e:
        logger.error(f"Processing failed: {e}")
        sys.exit(1)

    report = create_cleaning_report(df_before, df_after)
    print(report)
    logger.info(
        f"Processing complete: {report['rows_before']} -> {report['rows_after']} rows"
    )

    output_path = save_data(df_after, args.output)
    logger.info(f"Saved cleaned data to {output_path}")


if __name__ == "__main__":
    main()
