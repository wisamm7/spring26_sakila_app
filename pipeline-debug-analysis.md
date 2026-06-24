# Broken Pipeline Debugging Analysis

## Error 1: Invalid runner label
Broken: runs-on: ubuntu
Fix: runs-on: ubuntu-latest

## Error 2: No MySQL service
Broken: tests run without MySQL.
Fix: add mysql:8.0 service.

## Error 3: No Sakila database import
Broken: Sakila schema/data is not loaded.
Fix: download and import sakila-schema.sql and sakila-data.sql.

## Error 4: Build job does not wait for tests
Broken: build job has no needs: test.
Fix: add needs: test.

## Error 5: Deploy depends on test only
Broken: deploy uses needs: test.
Fix: deploy should depend on build.
