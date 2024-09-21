import os

import dlt
from dlt.sources.sql_database import sql_database, sql_table, Table


def load_entire_database() -> None:
    # Customize pipelines_dir
    # pipelines_dir = os.getcwd() + "/.dlt/pipelines"

    # Define the pipeline
    pipeline = dlt.pipeline(
        pipeline_name="jaffle-shop",
        # pipelines_dir=pipelines_dir, pipelinesフォルダの出力先。pipelimeコマンドの向け先が変更できなかったので保留
        destination="bigquery",
        dataset_name="dlt_lake",
    )

    # Fetch all the tables from the database
    source = sql_database()

    # Run the pipeline
    info = pipeline.run(source, write_disposition="replace")
    print("dltパイプラインの実行完了")

    # Print load info
    print(info)


if __name__ == "__main__":
    load_entire_database()
