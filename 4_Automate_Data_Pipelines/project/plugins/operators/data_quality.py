from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class DataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id,
                 tables,
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.tables = tables

    def execute(self, context):
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        for table in self.tables:
            self.log.info(f"Running Data Quality checks on table: {table}")
            records = redshift.get_records(f"SELECT COUNT(*) FROM {table};")
            #self.log.info(f"len(records): {len(records)}")
            #self.log.info(f"len(records[0]): {len(records[0])}")
            #self.log.info(f"len(records[0][0] ): {records[0][0]}")
            if len(records) < 1 or len(records[0]) < 1 or records[0][0] < 1:
                raise ValueError(f"{table} containe 0 rows")
            