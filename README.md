# tbd

A superior calories counting app that has a list of products from all major Russian supermarkets (built in Rust btw).

Web scrapers:
Metro: Done
5ka: WIP
Chizhik: No
Magnit: No
Perekrestok: No
Vkusvill: No

Schema:

```json
{
  "name": "Product name",
  "brand": "Brand name",
  "weight": "weight in grams",
  "nutrients": {
    "protein": "protein in grams (for entire weight)",
    "fats": "fats in grams (for entire weight)",
    "carbohydrates": "carbs in grams (for entire weight)",
    "calories": "calories (per 100g)"
  }
}
```
