#!/usr/bin/env bash

current_dir=$(dirname $(readlink -f $0))
django_init_file="django_app_deploy/__init__.py"
html_template="../docs/templates/template.html5"
markdown_file="../docs/result.md"
html_index="../docs/index.html"

cd "$current_dir/src" || { echo 'cd to src/ directory failed' ; exit 1;}

printf "import django\ndjango.setup()" > $django_init_file
export DJANGO_SETTINGS_MODULE=django_app_deploy.settings

pdoc --pdf --force --output-dir docs/ . > $markdown_file
awk -i inplace '{sub(/{#id}/, sprintf("{#id%d}", ++i))} 1' $markdown_file

echo "" > $django_init_file