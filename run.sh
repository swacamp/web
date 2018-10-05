#!/usr/bin/env bash
set -e
docker run -i -t -v $(pwd)/:/home/jenkins -p 4000:4000 praqma/gh-pages jekyll serve --watch --host=0.0.0.0
