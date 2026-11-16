# Product matching accuracy benchmark (November 2026)

The data behind [Best product matching tools and APIs (2026), with measured accuracy](https://deepscout.ai/en/dev/guides/product-matching-tools-accuracy).

We ran DeepScout product matching on two sets of UK online stores and checked the matched pairs by hand.
This repo holds every checked pair where the two stores don't share an EAN, with its label, so you can
check our labels or test another matcher on the same products.

| File | What it is |
|---|---|
| `data/hifi-pairs.csv` | Run 1, hi-fi: Richer Sounds, Peter Tyson, Sevenoaks Sound & Vision. 295 checked pairs: all 45 pairs with different EANs, and 250 random pairs of the 726 with no EAN on one store. |
| `data/pianos-pairs.csv` | Run 2, pianos and keyboards: Bonners Music, Rimmers Music (full catalogues, free matching sample of 691 random Bonners products). All 19 pairs without a shared EAN. |
| `data/hifi-recall-worksheet.txt` | Recall check: 100 random Richer Sounds products, the match the engine found in each other store, and the closest candidates we searched by brand and model. |
| `RULES.md` | The labelling rules, written before we looked at the results. |
| `score.py` | Counts correct pairs per run and group (standard library only). |

## Results

```
$ python3 score.py
run      group                correct / checked
hifi     different_ean        45 / 45
hifi     no_ean_on_one_side   249 / 250
pianos   different_ean        4 / 4
pianos   no_ean_on_one_side   15 / 15
all      without shared EAN   313 / 314
```

The one wrong pair, `hifi-162`, is a pair of Sonos Five speakers matched to a single Sonos Five.

Recall (run 1): the matcher found 60 of 61 real matches in Peter Tyson and 51 of 52 in Sevenoaks.

## Columns

`pair_id`, `group` (`different_ean` or `no_ean_on_one_side`), `label` (`correct` or `wrong`), then for each
side: store, product name, variant, price, EAN, product URL. Prices are in GBP, as scraped in November 2026.
Stores change their pages, so some URLs and prices will have changed since.

## Test your own matcher

Run your matcher on the same stores, or on the product pairs in the CSVs, and compare. If you run a
matching tool and want your results published next to ours, open an issue in this repo with your output
and how you produced it. We'll check it with the same rules.

DeepScout is our product. It was measured the same way as anything we'd publish next to it.
