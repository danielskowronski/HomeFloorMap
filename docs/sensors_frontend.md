# Sensors - Frontend

## Sensor renderers

all sensor classes include:

- `render` - one of renderers from next sections
- `baseVariant` describes behaviour when sensors are placed as general or as detailed, but no override was added
- `detailedVariant` describes behaviour when sensors are placed as detailed; schema as `baseVariant`

### `numerical`

Intended to simply display numerical value and unit. Supports different colors based on value (e.g. to show thermal comfort).

- `baseVariant` / `detailedVariant`:
  - `unit` - unit to append after value; this must include space if you want it
  - `precision` - number of decimal places, 0 to keep integer part only
  - `length` - number of digits including decimal point
- `colorScale`: `d3.scaleThreshold()` object
  - keep in mind that `range()` expects array longer by one element than `domain()`
- `dividedBy`: optional number to divide sensor value by without placing decimal point; used to make less significant digits smaller without wasting space on decimal point or using long units (e.g. `ppm x10^-2`)

### `boolean_text`

Formats boolean sensor to human-readable states like open/closed, ok/error.

- `baseVariant` / `detailedVariant`:
  - `valueTrue`: text, including whitespaces for True
  - `valueFalse`: text, including whitespaces for False
- `colorScale`:
  - `colorTrue`: HTML color for True
  - `colorFalse`: HTML color for False

### `special`

Various non-standard renderers, implemented directly in code.

---

## Sensor classes

### `wind_speed`

`numerical`; matches style of `temp_sun`

### `temp_inside`

`numerical`; large text value without units, colors matching thermal comfort indoor

### `temp_outside`

`numerical`; large text value with units, colors matching thermal comfort outdoor (shaded)

### `temp_sun`

`numerical`; small text value of `temp_outside` but with adjusted scale for sensors that are not in shade

### `simple_window`

`boolean_text`; expects True for sensor reporting open state; should have same length of text for open and closed state

### `wind_heading`

`special`; rotating arrow matching wind direction; adjustments should be done in HA template

### `co2`

`numerical`; highlights hundreds of ppm

---

## Sensor appearance

Data file `sensorsAppearance.json` configure two maps that can override some parameters of sensor classes from code.

### `commonColorThresholdPallettes`

Map; elements are arrays as passed to `d3.scaleThreshold()...range(<>)`. Contains HTML colors for ranges.

### `sensorRender`

Map; key indicate which built-in sensor class to reconfigure. Following fields are supported:

- `thresholds` - array of values passed to `d3.scaleThreshold().domain(<>)`
- `colors` - key of `commonColorThresholdPallettes` from either this override or code
