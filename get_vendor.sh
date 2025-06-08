#!bash

if [[ ! -f app/static/vendor/d3.v7.min.js ]]; then
  curl -L "https://d3js.org/d3.v7.min.js" -o app/static/vendor/d3.v7.min.js
  echo "D3.js downloaded successfully."
else
  echo "D3.js already exists, skipping download."
fi


if [[ ! -f app/static/vendor/js.cookie.min.js ]]; then
  curl -L "https://cdn.jsdelivr.net/npm/js-cookie@3.0.5/dist/js.cookie.min.js" -o app/static/vendor/js.cookie.min.js
  echo "js.cookie.min.js downloaded successfully."
else
  echo "js.cookie.min.js already exists, skipping download."
fi