# HomeFloorMap

Stand-alone web-app rendering floor map from specially formatted SVG file and displaying various sensors obtained from Home Assistant. It's intended to be avaiulable inside home LAN for humans without authentication and accesed from mobile devices or kept as a widget on computer screen.

It's developed outside Lovelace (Home Assistant UI) for several reasons:

- Home Assistant does not allow creation of read-only users or limitting which devices can be accessed
- Home Assistant does not allow permanent overrides of "home dashboard"
- even with most advanced plugins, I still had to develop ton of custom code, not guaranteed to survive upgrades

## Using

For all required files, see `example_data`. To use sample data with values mocked, change `MOCK=false` to `MOCK=true` in `index.html`.

### `floorplan.svg`

Prepare SVG that will be loaded by d3.js. Right now, any SVG works.

### `sensorDefs.json`

Dict of sensors with elements:

- `data_id` pointing to ID from `sensorRequest.j2`
- `coords` with location of sensor (as placed on source SVG)
- `class` being one of supported sensor classes:
  - `temp_inside` - large text value without units, colors matching thermal comfort indoor
  - `temp_outside` - large text value with units, colors matching thermal comfort outdoor (shaded)
  - `temp_sun` - small text value of `temp_outside` but with adjusted scale for sensors that are not in shade

### `sensorRequest.j2`

Home Assistant template that renders into JSON dict with keys matching `data_id` and values.

### Downloadign assets

```bash
./get_font.sh
./get_vendor.sh
```

### Env variables

```bash
export HFM_HA_URL='http://192.168.0.2:8123'
export HFM_HA_TOKEN='LongLivedToken'
export HFM_CONF_PATH='../example_data/'
```
