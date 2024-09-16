#!/bin/bash

# exit on error
set -e

meltano run tap-capsulecrm "$LOADER" dbt:deps dbt:snapshot dbt:run
