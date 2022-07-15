CREATE OR REPLACE TABLE `{{ var.value.GCP_PROJECT }}`.`{{ var.value.gsheet_tables_dataset }}`.`ext_sku_library` AS
SELECT
created_dt as created_dt,
updated_dt as updated_dt,
product_division as product_division,
product_department as product_department,
product_category as product_category,
product_type as product_type,
product_parent_name as product_parent_name,
product_parent_code as product_parent_code,
product_parent_unit as product_parent_unit,
product_name as product_name,
product_code as product_code,
product_unit_name as product_unit_name,
convertion_priority as convertion_priority,
convertion_rate as convertion_rate,
shelf_life_MT as shelf_life_mt,
shelf_life_GT as shelf_life_gt,
shelf_life_breakage as shelf_life_breakage
FROM `{{ var.value.GCP_PROJECT }}`.`{{ var.value.ext_gsheet_dataset }}`.`ext_sku_library` 