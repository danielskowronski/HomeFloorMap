# ToDo

MVP:

- [x] render floor plan
- [x] basic temperature sensors (always shown, single value)
- [x] temperature thresholds coloring
- [x] requesting Home Assistant for actual data
- [x] CO2 sensors
- [x] window open/closed status 
- [x] support showing only one centered sensor per room when not enough space and actual positions of sensors with multiple values + multiple sensors when zoomed in
- [x] rotated sensors
- [x] wind speed and direction
- [x] sensors that are both detailed and general with same poisitions should be defined only once in sensorDefs
- [x] thermal color thresholds to be configurable + summer/winter switch
- [x] sensor classes should be handled better with less repetition including threshold colors
- [x] make it fully offline (local cache of fonts, libraries)
- [x] better handling of detail level switching
- [x] docs on all sensor classes, updated example values with demo

further development:

- [x] containerize
- [ ] wind speed and direction as one sensor with 2 values
- [x] window shades open/closed/percentage status
- [ ] window open + shades coupled with temperature highlights
- [ ] complex sensors (multiple values in same point)
- [ ] hightlight entire room if temperature is on special thresholds
- [ ] lux and UV sensors
- [ ] sun azimuth and elevation
- [ ] rain gauge
- [ ] link to graphs
- [ ] improve handling of missing values
- [ ] handle outdated values

later:

- [ ] heaters (deactivated/heating/heated + target temperature)
- [ ] smog sensors on floor
- [ ] smog sensors outside (e.g. on street) + other data from GIOŚ
- [ ] forecast with all details like cloud coverage
- [ ] subfloors / dedicated rooms - e.g. 3D printer
- [ ] robot vacuum & humidifier pending tasks

even later:

- [ ] lights status
- [ ] power monitor
- [ ] fans and humidifiers
- [ ] moon status
