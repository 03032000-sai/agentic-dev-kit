# Evidence Contract

Recommended shape:

```yaml
claim:
status: confirmed | inferred | unknown
source:
  path:
  symbol:
  line_range:
validation:
```

Rules:
- prefer primary repository evidence;
- do not cite a file that does not support the claim;
- never present `inferred` as `confirmed`;
- missing evidence remains `unknown`.
