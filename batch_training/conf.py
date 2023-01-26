"""Configuration file for batch processing."""

MODEL_FOLDER = "models_pkl"

FEATURE_COLUMNS = ['has_been_proposed_formulas', 'has_chosen_formula', 'provider', 'product_third_party', 
                   'product_intermediate', 'product_all_risks', 'annual_price_third_party', 
                   'annual_price_intermediate', 'annual_price_all_risks', 'chosen_formula', 'chosen_product',
                   'main_driver_age', 'main_driver_gender', 'main_driver_licence_age', 'main_driver_bonus',
                   'vehicle_age', 'vehicle_class', 'vehicle_group', 'vehicle_region', 'has_secondary_driver']

ID_COLUMN = 'lead_id'

TARGET_COLUMN = 'has_subscribed'

FULL_COLUMN = [ID_COLUMN] + FEATURE_COLUMNS + [TARGET_COLUMN]

DATASET = "lead_scoring"

TABLE = "scores"
