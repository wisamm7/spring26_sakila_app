# Dockerfile Analysis

## Issues in Dockerfile.broken

1. Uses full python:3.9 image, which is large and inefficient.
2. Copies the entire project before installing dependencies, which breaks Docker layer caching.
3. Installs packages using multiple RUN commands instead of using requirements.txt.
4. Hardcodes sensitive database credentials inside the image.
5. Exposes unnecessary ports 3306 and 22 even though the Flask app only needs port 5000.
6. Runs the application as root, which is a security risk.
7. Does not include a HEALTHCHECK instruction.
8. Does not include useful image labels such as maintainer, version, and description.

## Fixes Applied

The optimized Dockerfile uses python:3.11-slim, installs dependencies from requirements.txt, uses better layer caching, avoids hardcoded secrets, exposes only port 5000, runs as a non-root user, adds a HEALTHCHECK, and includes metadata labels.
