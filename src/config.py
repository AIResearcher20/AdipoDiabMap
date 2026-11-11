"""Central configuration for AdipoDiabMap."""

# Tissues of interest in GTEx
TISSUES = [
    "Adipose_Visceral_Omentum",
    "Adipose_Subcutaneous",
    "Pancreas",
    "Liver",
    "Muscle_Skeletal",
]

# GWAS traits
TRAITS = {
    "BMI": "body mass index",
    "T2D": "type 2 diabetes",
}

# Colocalization threshold
COLOC_PP_H4_THRESHOLD = 0.8

# Pathways of interest
PATHWAYS = [
    "Insulin signaling",
    "Lipid metabolism",
    "Adipogenesis",
    "Inflammation",
    "Glucose homeostasis",
]
