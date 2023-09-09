# Third party imports
import polars as pl


def preprocess_hotel(df: pl.DataFrame) -> pl.DataFrame:
    """This function preprocess hotel dataframe

    Args:
        df (pl.DataFrame): polars dataframe to preprocess

    Returns:
        pl.DataFrame: preprocessed dataframe
    """
    accommodations_type = "HÔTEL DE TOURISME"
    column_to_concat = ["ADRESSE", "CODE POSTAL", "COMMUNE"]

    df_clean = df.filter(pl.col("TYPE D'HÉBERGEMENT") == accommodations_type) \
                 .fill_null(value="") \
                 .with_columns([
                     pl.col("CLASSEMENT").apply(lambda x: x[:1]) \
                                         .cast(pl.Int64),
                     (pl.col("DATE DE CLASSEMENT") \
                        .str.strptime(pl.Date, format="%d/%m/%Y") \
                        .cast(pl.Utf8)).alias("date"),
                     pl.col("DATE DE CLASSEMENT") \
                       .str.strptime(pl.Date, format="%d/%m/%Y") \
                       .dt.day().cast(pl.Int64).alias("day"),
                     pl.col("DATE DE CLASSEMENT") \
                       .str.strptime(pl.Date, format="%d/%m/%Y") \
                       .dt.month().cast(pl.Int64).alias("month"),
                     pl.col("DATE DE CLASSEMENT") \
                       .str.strptime(pl.Date, format="%d/%m/%Y")\
                       .dt.year().cast(pl.Int64).alias("year"),
                     pl.col("NOM COMMERCIAL").str.to_lowercase(),
                     pl.col("ADRESSE").str.to_lowercase(),
                     pl.col("COMMUNE").str.to_lowercase(),
                     pl.concat_str(column_to_concat, separator="+") \
                       .str.replace_all(r"\s", "+") \
                       .str.replace_all(r"\++", "+") \
                       .str.to_lowercase() \
                       .alias("concat")
                 ])

    return df_clean


def preprocess_adress(df: pl.LazyFrame, source: str) -> pl.LazyFrame:
    """This function preprocess adress dataframe

    Args:
        df (pl.LazyFrame): polars dataframe to preprocess
        source (str): to know which column to concatenate

    Returns:
        pl.LazyFrame: preprocessed dataframe
    """
    if source == "streets":
        column_to_concat = ["numero", "rep", "nom_voie", "code_postal", "nom_commune"]
    elif source == "places":
        column_to_concat = ["nom_lieu_dit", "code_postal", "nom_commune"]

    df_clean = df.fill_null(value="") \
                 .with_columns([
                     pl.concat_str(column_to_concat, separator="+") \
                       .str.replace_all(r"\s", "+") \
                       .str.replace_all(r"\++", "+") \
                       .str.to_lowercase() \
                       .alias("concat")
                 ]) \
                 .collect(streaming=True)
    
    return df_clean
