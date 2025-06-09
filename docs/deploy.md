# Deploy

## Downloading assets

Before anything, you must locally cache [fonts](../app/static/font/README.md) and [other assets](../app/static/vendor/README.md).

```bash
./get_font.sh
./get_vendor.sh
```

## Env variables

```bash
export HFM_CONF_PATH='../example_data/'
```

## Run locally

```bash
# run in virtual-env
cd app
pip3 install -r requirements.txt
python3 app.py
```

open http://localhost:9002

## Run in docker

Either change `docker-compose.yml` to point to your data directory or create symlink `data`.

```bash
docker-compose build
docker-compose up -d
```
