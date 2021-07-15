# DEFAULT CONFIGURATIONS TO USE IF config.ini NOT ACCESSIBLE

BOM_DATA_DIR = "data/Bom Hierarchy final.csv"
ITEM_DATA_DIR = "data/materials.csv"
ARTICLE_RATES_DIR = "data/articles.csv"

ROYALTY = 0.4
SELLING_DISTRIBUTION = 0.1275
SALES_RETURN = 0.01

FIXED_RATES = {
    "wastage_and_benefits": 0.1,
    "salaries_and_emoluments": 0.1,
    "other_factory_overheads": 0.1,
    "admin_expenses": 0.1,
    "interest_and_bank_charges": 0.1,
    "depreciation": 0.1,
    "other_expenses": 0.1,
    "finance_costs": 0.1,
}  # EXPENSES_AND_OVERHEADS
