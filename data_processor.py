# data_processor.py
import logging
import pandas as pd

logger = logging.getLogger(__name__)

def remove_duplicates(df):
    before=len(df)
    df=df.drop_duplicates()
    after=len(df)
    logger.debug("Rows removed: %s", before-after)
    return df

def handle_missing(df, axis="rows"):
    """Drop rows or columns containing missing values."""
    #before 
    beforecols=len(df.columns)
    beforerows=len(df)
    
    try:
        if axis not in ("rows", "columns"):
            raise ValueError(f"Unsupported axis: {axis}")
        df = df.dropna(axis=1) if axis == "columns" else df.dropna()
    except ValueError as e:
        logger.error(e, "Unsupported axis")
        raise
    removed = beforecols - len(df.columns) if axis == "columns" else beforerows - len(df)
    logger.debug(f"Removed {removed} {axis}")
    return df


def remove_outliers(df, columns, method, threshold):
    """Remove outliers from the specified numeric columns."""
    pass


def process_data(df, config):
    """Apply the processing steps enabled in the configuration."""
    pass


def create_cleaning_report(df_before, df_after):
    """Return a dictionary summarizing the cleaning results."""
    pass
