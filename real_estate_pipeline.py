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
                "name": "real_estate_price",
                "endpoint": {
                    "path": "XIT001/?year=2024&area=13",
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
