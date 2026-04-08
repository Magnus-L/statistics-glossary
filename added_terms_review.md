# Proposed Additions to Statistics Glossary — Revised Review

These 40 modern econometric/causal inference terms would be added to the glossary with source marked as "Added by Lodefalk". Each translation now has a source or is explicitly marked as proposed.

## Source key

- **ÅA** = Åbo Akademi econometrics textbook (Djupsjöbacka), Ch. 19
- **IFAU** = IFAU Rapport/Working Paper (specific reference in notes)
- **MeSH** = Svensk MeSH, Karolinska Institutet
- **SBU** = Statens beredning för medicinsk och social utvärdering
- **WP** = Swedish Wikipedia (sv.wikipedia.org)
- **DiVA** = Swedish university theses (diva-portal.org)
- **KP** = Swedish university course plans (kursplaner)
- **BRÅ** = Brottsförebyggande rådet
- **ML** = Magnus Lodefalk (proposed, no external source found)
- **LUP** = Lund University Publications

## Status key

- **V** = Verified in external Swedish source
- **P** = Proposed (no external Swedish source; translation follows Swedish word-formation rules)

## Terms

| # | English | Swedish | Status | Source | Notes |
|---|---------|---------|--------|--------|-------|
| 1 | average treatment effect (ATE) | genomsnittlig behandlingseffekt | V | ÅA, DiVA | |
| 2 | average treatment effect on the treated (ATT) | genomsnittlig behandlingseffekt på de behandlade | P | ML | Logical extension of #1; ATT in English dominates |
| 3 | bunching estimator | bunching-estimator | V | IFAU WP 2019:6 | English loanword; "tröskelskattning" NOT attested |
| 4 | causal forest | kausal skog | P | ML | English term used in Swedish research |
| 5 | causal inference | kausal inferens | V | KP (UU, ORU, GU) | Well established |
| 6 | complier average causal effect (CACE) | genomsnittlig kausaleffekt bland följare | P | ML | = LATE; English CACE dominates |
| 7 | conditional average treatment effect (CATE) | villkorlig genomsnittlig behandlingseffekt | P | ML | English CATE dominates |
| 8 | counterfactual | kontrafaktisk | V | WP, Ekonomisk Debatt | Often "kontrafaktiskt utfall" |
| 9 | debiased machine learning | avbiasad maskininlärning | P | ML | Also: double ML; English used in Swedish research |
| 10 | difference-in-differences (DiD) | skillnad-i-skillnader | V | IFAU Rapport 2025:17 | Changed from "differens-i-differenser" |
| 11 | directed acyclic graph (DAG) | riktad acyklisk graf | V | WP, KP (UU) | |
| 12 | double machine learning (DML) | dubbel maskininlärning | P | ML | English DML dominates |
| 13 | event study | eventstudie | V | DiVA (multiple theses) | Changed from "händelsestudie" |
| 14 | exclusion restriction | exkluderingskriterium | P | ML | IV assumption |
| 15 | fuzzy regression discontinuity | inexakt regressionssprångdesign | P | ML | English "fuzzy RD" dominates |
| 16 | heteroskedasticity | heteroskedasticitet | V | WP, LUP, KP | |
| 17 | heteroskedasticity-consistent standard errors | robusta standardfel | V | LUP (FEKH89 thesis) | Changed from "heteroskedasticitets-konsistenta standardfel" |
| 18 | homoskedasticity | homoskedasticitet | V | WP | |
| 19 | intention-to-treat (ITT) | behandlingsavsiktsanalys | V | MeSH, SBU | Changed from "avsikt-att-behandla" |
| 20 | inverse probability weighting (IPW) | invers sannolikhetsviktning | P | ML | English IPW dominates |
| 21 | local average treatment effect (LATE) | lokal genomsnittlig behandlingseffekt | V | ÅA | |
| 22 | machine learning | maskininlärning | V | WP, KP, Regeringen.se | |
| 23 | natural experiment | naturligt experiment | V | WP, ÅA | |
| 24 | omitted variable bias | snedvridning från utelämnade variabler | P | ML | Components verified (SBU: snedvridning; GU: utelämnad variabel) |
| 25 | parallel trends assumption | parallella trender | P | ML | DiD key assumption |
| 26 | placebo test | placebotest | P/V | ML + ÅA | ÅA uses "falsifieringstest" for same concept |
| 27 | pre-trend test | förtrendstest | P | ML | |
| 28 | propensity score | benägenhetspoäng | V | MeSH | Official Swedish MeSH term |
| 29 | propensity score matching | propensity score-matchning | V | KP (GU course) | Hybrid; fully Swedish "matchning med benägenhetspoäng" not attested |
| 30 | randomised controlled trial (RCT) | randomiserad kontrollerad studie | V | WP, SBU | |
| 31 | regression discontinuity design (RDD) | regressionssprångdesign | P | ML | English RDD dominates; UU kursplan leaves in English |
| 32 | regression kink design (RKD) | regressionskröksdesign | P | ML | English RKD dominates |
| 33 | sharp regression discontinuity | skarp regressionssprångdesign | P | ML | Changed from "tydlig" |
| 34 | staggered adoption design | stegvis implementeringsdesign | P | ML | English dominates |
| 35 | staggered difference-in-differences | stegvis skillnad-i-skillnader | P | ML | Updated to match #10 |
| 36 | synthetic control method | syntetisk kontrollmetod | V | BRÅ, DiVA | |
| 37 | treatment effect heterogeneity | heterogenitet i behandlingseffekter | P | ML | Components verified (ÅA: behandlingseffekt) |
| 38 | triple differences (DDD) | trippeldifferenser | P | ML | |
| 39 | two-way fixed effects (TWFE) | tvåvägs fixa effekter | V | ÅA ("fixa"), DiVA ("fasta") | Both "fixa" and "fasta" attested |
| 40 | weak instrument | svagt instrument | V | ÅA | |

## Decision key

Mark each row with one of:
- **OK** — keep as is
- **FIX** — correct the Swedish translation (write correction next to it)
- **DROP** — remove from list
- **ADD** — write new terms at the bottom

## Summary

- **Verified (V):** 22 terms with external Swedish sources
- **Proposed (P):** 18 terms where no external source was found; translation follows Swedish word-formation rules
- **Corrections from original:** #3 (bunching), #10 (skillnad-i-skillnader), #13 (eventstudie), #14 (exkluderingskriterium), #17 (robusta standardfel), #19 (behandlingsavsiktsanalys), #24 (reworded), #25 (simplified), #27 (förtrendstest), #29 (hybrid), #33 (skarp), #35 (updated to match #10)

## Key sources for verification

- Åbo Akademi econometrics textbook: `http://www.users.abo.fi/adjupsjo/tillämpad/KAPITEL%2019,%20INSTRUMENT.pdf`
- IFAU Rapport 2025:17 (Rosenqvist & Sauermann): `https://www.ifau.se/globalassets/pdf/se/2025/2025-17-effekter-av-kompensatorisk-resursfordelning-i-grundskolan.pdf`
- Svensk MeSH: `https://mesh.kib.ki.se/`
- SBU ordlista: `https://www.sbu.se/sv/metod/ordforklaringar-och-forkortningar-i-sbus-publikationer/`
- BRÅ syntetisk kontrollmetod: `https://bra.se/download/18.4a8457aa19545fdf8e53ab9c/1741933929423/2025_0431_Österåker%20slutrapport.pdf`
