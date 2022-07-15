CREATE OR REPLACE TABLE `{{ var.value.GCP_PROJECT }}`.`{{ var.value.DATASET_TESTING2 }}`.`data_test_1`
AS
SELECT Name, 
    Title,
    Address
FROM `{{ var.value.GCP_PROJECT }}`.`{{ var.value.DATASET_TESTING2 }}`.`data_client`;