# HomeFloorMap

Stand-alone web-app rendering floor map from specially formatted SVG file and displaying various sensors obtained from Home Assistant. It's intended to be avaiulable inside home LAN for humans without authentication and accesed from mobile devices or kept as a widget on computer screen.

It's developed outside Lovelace (Home Assistant UI) for several reasons:

- Home Assistant does not allow creation of read-only users or limitting which devices can be accessed
- Home Assistant does not allow permanent overrides of "home dashboard"
- even with most advanced plugins, I still had to develop ton of custom code, not guaranteed to survive upgrades
