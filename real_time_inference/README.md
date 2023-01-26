# Steps to deploy Real-Time API to GCP
1. Build the Fast API that will load the model and return the prediction
To run Flask API locally, launch following command:
````
python -m uvicorn main:app --reload
````

2. Write the Dockerfile

3. Create Google Cloud Account & Register the Dockerfile in a container
````
gcloud builds submit --tag gcr.io/orn-lead-scoring-predictor/init-container
````

4. Create Cloud Run Service on GUI using container image

5. Enable continuous deployment from GCP GUI and link it to the github repository 

# Fast API Request examples

````
curl -X POST https://init-container-service-d6hgbsksiq-od.a.run.app/score/ -H "Content-Type: application/json" --data-binary @- <<DATA
{
	"has_been_proposed_formulas": true,
	"has_chosen_formula": true,
	"provider": "provider_A",
	"product_third_party": "third_party_product_4",
	"product_intermediate": "intermdiate_product_5",
	"product_all_risks": "all_risks_product_5",
	"annual_price_third_party": "low",
	"annual_price_intermediate": "low",
	"annual_price_all_risks": "low",
	"chosen_formula": "third",
	"chosen_product": "third_party_product_4",
	"main_driver_age": "25-29",
	"main_driver_gender": "M",
	"main_driver_licence_age": "02",
	"main_driver_bonus": "100",
	"vehicle_age": "15-19",
	"vehicle_class": "F-H",
	"vehicle_group": "29-30",
	"vehicle_region": "Picardie",
	"has_secondary_driver": true
}
````


````
curl -X POST https://init-container-service-d6hgbsksiq-od.a.run.app/score/ -H "Content-Type: application/json" --data-binary @- <<DATA
{
	"has_been_proposed_formulas": true,
	"has_chosen_formula": true,
	"provider": "provider_A",
	"product_third_party": "third_party_product_4",
	"product_intermediate": "intermdiate_product_5",
	"product_all_risks": "all_risks_product_5",
	"annual_price_third_party": "low",
	"annual_price_intermediate": "low",
	"annual_price_all_risks": "low",
	"chosen_formula": "third",
	"chosen_product": "third_party_product_4",
	"main_driver_age": "60+",
	"main_driver_gender": "M",
	"main_driver_licence_age": "15+",
	"main_driver_bonus": "100",
	"vehicle_age": "15-19",
	"vehicle_class": "F-H",
	"vehicle_group": "29-30",
	"vehicle_region": "Picardie",
	"has_secondary_driver": true
}
````


# Sources

https://towardsdatascience.com/deploy-a-dockerized-fastapi-app-to-google-cloud-platform-24f72266c7ef
