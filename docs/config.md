# Config files

For all required files, see `example_data`. To use sample data with values mocked, change `MOCK=false` to `MOCK=true` in `index.html`.

## `floorplan.svg`

Prepare SVG that will be loaded by d3.js. Right now, any SVG works.

## `sensorsMapping.json`

Dict of sensors with elements:

- `data_id` pointing to ID from `sensorRequest.j2`
- `coords` with location of sensor (as placed on source SVG)
- `class` being one of supported sensor classes - see [sensors_frontend.md](./sensors_frontend.md)

## `sensorsRequest.j2`

Home Assistant template that renders into JSON dict with keys matching `data_id` and values. Should contain `last_updated` to be used by frontend.

## `sensorsAppearance.json`

As described in [sensors_frontend.md](./sensors_frontend.md)

## `hfm.yaml`

```yaml
server:
  host: 0.0.0.0
  port: 9002
  debug: False
ha:
  url: 'http://192.168.0.2:8123'
  token: 'LongLivedToken'
```
