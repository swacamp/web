#!/usr/bin/env bash
set -e
docker run -i -t -v /home/klassm/IdeaProjects/tng/swacamp_web:/home/jenkins -p 4000:4000 praqma/gh-pages jekyll serve --watch --host=0.0.0.0
