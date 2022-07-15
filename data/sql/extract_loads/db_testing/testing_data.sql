CREATE OR REPLACE TABLE `{{ var.value.GCP_PROJECT }}`.`{{ var.value.DATASET_TESTING }}`.`data_testing` AS
SELECT Name, 
    Title
    Address,
    City
FROM `{{ var.value.GCP_PROJECT }}`.`{{ var.value.DATASET_TESTING }}`.`data_client`;