# import logging
from pathlib import Path
# from typing import Literal
import geopandas as gpd
import numpy as np
import pandas as pd
import polars as pl

# Path vers la racine du projet
PROJECT_DIR: Path = Path(__file__).resolve().parents[1]
# Répertoire pour enregistrer/charger les données
DATA_DIR: Path = PROJECT_DIR / "data"

# Chargement des données La Réunion
DATA_POP_974: Path = DATA_DIR / "population_974.gpkg"
FOND_COMMUNES_974: Path = DATA_DIR / "commune_dep_974_2019.gpkg"
PARQ_POP_974: Path = DATA_DIR / "population_974.parquet"


def build_data_reunion() -> pl.DataFrame:
    gdf = gpd.read_file(DATA_POP_974)
    fond = gpd.read_file(FOND_COMMUNES_974)
    gdf_com = gpd.sjoin(gdf, fond, how="left", predicate="within")
    df = pl.from_pandas(gdf_com.drop(columns="geometry"))
    df.write_parquet(PARQ_POP_974)
    return df
