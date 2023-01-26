"""Models user in Flask API."""
from pydantic import BaseModel


class UserFeatures(BaseModel):
    """Features of the Lead."""
    
    has_been_proposed_formulas: bool
    has_chosen_formula: bool
    provider: str
    product_third_party: str
    product_intermediate: str
    product_all_risks: str
    annual_price_third_party: str
    annual_price_intermediate: str
    annual_price_all_risks: str
    chosen_formula: str
    chosen_product: str
    main_driver_age: str
    main_driver_gender: str
    main_driver_licence_age: str
    main_driver_bonus: str
    vehicle_age: str
    vehicle_class: str
    vehicle_group: str
    vehicle_region: str
    has_secondary_driver: bool
