# HomeFloorMap Helm Chart

## values

### `extsitingSecretName`

Name of secret existing in target namespace, it should look like this:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: ...
  namespace: ...
data:
  floorplan.svg: ...
  hfm.yaml: ...
  sensorsAppearance.json: ...
  sensorsMapping.json: ...
  sensorsRequest.j2: ...
type: Opaque
```

### other - TBD
