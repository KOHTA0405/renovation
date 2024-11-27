import dlt
from dlt.sources.rest_api import RESTAPIConfig, rest_api_resources


@dlt.source
def real_estate_source():
    config: RESTAPIConfig = {
        "client": {
            "base_url": "https://www.reinfolib.mlit.go.jp/ex-api/external/",
            "headers": {
                "Ocp-Apim-Subscription-Key	": dlt.secrets[
                    "sources.real_estate.api_key"
                ],
            },
        },
        "resources": [
            {
                "name": "trade_record",
                "endpoint": {
                    "path": "XIT001/?year=2020&area=13",
                },
                "columns": {
                    "price_category": {"data_type": "text", "nullable": False},
                    "type": {"data_type": "text", "nullable": False},
                    "region": {"data_type": "text", "nullable": False},
                    "municipality_code": {"data_type": "bigint", "nullable": False},
                    "prefecture": {"data_type": "text", "nullable": False},
                    "municipality": {"data_type": "text", "nullable": False},
                    "district_name": {"data_type": "text", "nullable": False},
                    "trade_price": {"data_type": "bigint", "nullable": False},
                    "price_per_unit": {"data_type": "decimal", "nullable": True},
                    "floor_plan": {"data_type": "text", "nullable": False},
                    "area": {"data_type": "text", "nullable": False},
                    "unit_price": {"data_type": "bigint", "nullable": True},
                    "land_shape": {"data_type": "text", "nullable": False},
                    "frontage": {"data_type": "decimal", "nullable": True},
                    "total_floor_area": {"data_type": "bigint", "nullable": True},
                    "building_year": {"data_type": "text", "nullable": False},
                    "structure": {"data_type": "text", "nullable": False},
                    "use": {"data_type": "text", "nullable": False},
                    "purpose": {"data_type": "text", "nullable": False},
                    "direction": {"data_type": "text", "nullable": False},
                    "classification": {"data_type": "text", "nullable": False},
                    "breadth": {"data_type": "decimal", "nullable": True},
                    "city_planning": {"data_type": "text", "nullable": False},
                    "coverage_ratio": {"data_type": "decimal", "nullable": True},
                    "floor_area_ratio": {"data_type": "decimal", "nullable": True},
                    "period": {"data_type": "text", "nullable": False},
                    "renovation": {"data_type": "text", "nullable": False},
                    "remarks": {"data_type": "text", "nullable": False},
                },
            }
        ],
    }

    yield from rest_api_resources(config)


def load_real_estate() -> None:
    pipeline = dlt.pipeline(
        pipeline_name="real_estate",
        destination="bigquery",
        dataset_name="dlt_lake",
    )

    load_info = pipeline.run(real_estate_source())
    print(load_info)


if __name__ == "__main__":
    load_real_estate()
