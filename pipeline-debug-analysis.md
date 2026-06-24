# C3 Pipeline Debugging Analysis

## Error 1: Wrong branch syntax
Line: on.push.branches  
Problem: branches is written as a single scalar value `main`.  
Why it fails/causes issue: It is not the recommended GitHub Actions branch filter format and can cause confusion or trigger issues.  
Fix: Use `branches: [main]`.

## Error 2: Invalid runner label
Line: `runs-on: ubuntu`  
Problem: GitHub-hosted runner label `ubuntu` is invalid.  
Why it fails: GitHub Actions cannot find a runner with this label.  
Fix: Use `runs-on: ubuntu-latest`.

## Error 3: Test job has no MySQL service
Line: test job  
Problem: The tests need Sakila MySQL database, but no MySQL service is configured.  
Why it fails: Database connection tests cannot connect to MySQL.  
Fix: Add a MySQL service container with MYSQL_ROOT_PASSWORD and MYSQL_DATABASE.

## Error 4: Build job does not depend on test job
Line: build job  
Problem: The build job has no `needs: test`.  
Why it causes issue: Docker image may build even if tests fail.  
Fix: Add `needs: test`.

## Error 5: Deploy job depends only on test, not build
Line: deploy job  
Problem: Deployment uses `needs: test` instead of `needs: build`.  
Why it causes issue: Deployment can run without confirming that the Docker image was built successfully.  
Fix: Use `needs: build`.
