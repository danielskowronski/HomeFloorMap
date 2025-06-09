# HomeFloorMap

Stand-alone web-app rendering floor map from specially formatted SVG file and displaying various sensors obtained from Home Assistant. It's intended to be available inside home LAN for humans without authentication and accessed from mobile devices or kept as a widget on computer screen.

It's developed outside Lovelace (Home Assistant UI) for several reasons:

- Home Assistant does not allow creation of read-only users or limiting which devices can be accessed
- Home Assistant does not allow permanent overrides of "home dashboard"
- even with most advanced plugins, I still had to develop ton of custom code, not guaranteed to survive upgrades

## Docs

- [configure](./docs/config.md)
- understand [sensors on frontend](./docs/sensors_frontend.md)
- [use / deploy](./docs/deploy.md)

---

## Licences

### Material Design Icons

Licensed under Apache License 2.0
