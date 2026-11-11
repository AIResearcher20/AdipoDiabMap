import pandas as pd


def load_gwas(path):
    df = pd.read_csv(path, sep="\t")
    return df


def keep_significant(df, p_cutoff=5e-8):
    return df[df["P"] < p_cutoff].copy()


def shared_variants(bmi, t2d):
    merged = bmi.merge(
        t2d,
        on="SNP",
        suffixes=("_bmi", "_t2d"),
    )
    return merged
