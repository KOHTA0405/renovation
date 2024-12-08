import dlt
from dlt.sources.sql_database import sql_database

from jaffle_shop_schema import Orders


def load_order_data() -> None:

    pipeline = dlt.pipeline(
        pipeline_name="jaffle_shop_orders",
        destination="bigquery",
        dataset_name="dlt_lake",
    )

    resource = sql_database(table_names=["orders"])

    # # Run the pipeline
    info = pipeline.run(
        resource,
        columns=Orders,
        # schema_contract={"tables": "evolve", "columns": "evolve"},
        write_disposition="replace",
    )
    print("dltパイプラインの実行完了")

    # Print load info
    print(info)


if __name__ == "__main__":
    load_order_data()
