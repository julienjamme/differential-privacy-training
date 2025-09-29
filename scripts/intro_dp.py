import polars as pl
import opendp.prelude as dp
from utils import build_data_reunion, PARQ_POP_974

if __name__ == "__main__":
    # reunion = build_data_reunion() # une seule fois par session
    reunion = pl.read_parquet(PARQ_POP_974)
    print(reunion.head())
    print(reunion.shape)
    print(reunion.columns)
    print(reunion.dtypes)

    reunion.group_by(["code", "libelle", "AGE_CAT"]).len()

    # Activer les fonctionnalités expérimentales d'OpenDP si nécessaire
    dp.enable_features("contrib")

    # Créer un contexte DP sur les données (ici epsilon=1)
    context = dp.Context.compositor(
        data=reunion.lazy(),    # utilisation du LazyFrame polars
        privacy_unit=dp.unit_of(contributions=1),
        privacy_loss=dp.loss_of(epsilon=1.0),
        # privacy_loss=dp.loss_of(epsilon=1.0 / 4, delta=1e-7),
        split_evenly_over=10
        # margins=[dp.polars.Margin(max_length=len(reunion))]
    )

    query_pop_tot = context.query().select(dp.len())
    query_pop_tot.summarize(alpha=0.05)
    print(
        "len_orig:", reunion.shape[0],
        "len_pert:", query_pop_tot.release().collect().item()
    )

    # Construire la requête de comptage par sexe (supposant colonne 'sex')
    query_pop_com_age = context.query().group_by("code", "libelle", "AGE_CAT").agg(dp.len())

    # Appliquer et récupérer la version protégée
    dp_result = query_pop_com_age.release().collect()

    print(dp_result)
