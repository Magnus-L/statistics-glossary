# Statistisk ordlista / Statistical Glossary

Searchable English-Swedish glossary of statistical and econometric terms.

## Contents

- **2,010 terms** from the ISI Multilingual Glossary of Statistical Terms, Swedish translation by J. Enger, B. Huitfeldt, U. Jorner & J. Wretman (Statistikfrämjandet, 2008)
- **40 modern econometric/causal inference terms** added by Magnus Lodefalk (2026), with sources documented in `added_terms_review.md`

## Files

| File | Purpose |
|------|---------|
| `glossary_base.csv` | ISI base terms (english, swedish) |
| `added_terms.csv` | New econometric terms with notes |
| `added_terms_review.md` | Review document with sources for each new term |
| `glossary_merged.csv` | Merged and sorted output |
| `index.html` | HTML template |
| `build.py` | Build script: merges data and generates `docs/index.html` |
| `docs/index.html` | Built page (served by GitHub Pages) |
| `source.xls` | Original ISI/Statistikfrämjandet source file |

## Build

```bash
python3 build.py
```

Requires Python 3.10+ (standard library only, no dependencies).

## Deploy

GitHub Pages serves from the `docs/` folder on the `main` branch.

## Licence

CC BY-NC-SA 4.0

## Status

Ready for deployment.
