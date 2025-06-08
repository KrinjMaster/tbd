import json

slugs = [
    "alkogolnaya-produkciya",
    "bezalkogolnye-napitki",
    "rybnye",
    "myasnye",
    "zamorozhennye-produkty",
    "myasnye_delikatesy",
    "siry",
    "molochnye-prodkuty-syry-i-yayca",
    "sladosti_",
    "hleb-vypechka-torty",
    "ovoshchi-i-frukty",
    "bakaleya",
    "chipsy-sneki-orehi",
    "chaj-kofe-kakao",
    "zdorovoe-pitanie",
    "gotovye-bljuda-polufabrikaty",
    "detskoe-pitanie",
]

allowed_attr = [
    "Вес, объем",
    "Белки, г",
    "Жиры, г",
    "Углеводы, г",
    "Энергетическая ценность, ккал/100 г",
    "Бренд",
]

attr_to_obj = {
    "Вес, объем": "weight",
    "Белки, г": "proteins",
    "Жиры, г": "fats",
    "Углеводы, г": "carbohydrates",
    "Энергетическая ценность, ккал/100 г": "calories",
}

for slug in slugs:
    file = open(f"/Users/krinjmaster/Desktop/tbd/web-scraper/metro/{slug}.json")
    new_file = open(f"new_{slug}.json", "w+")

    json_to_obj = json.load(file)

    all_objs = json_to_obj["data"]["category"]["products"]

    new_file.write(
        f'{{\n"collection": "metro", "category":"{json_to_obj["data"]["category"]["name"]}", "items": [\n'
    )

    for i in range(len(all_objs)):
        obj = all_objs[i]
        new_obj = {
            "name": obj["name"],
            "brand": None,
            "attributes": {
                "weight": None,
                "proteins": None,
                "fats": None,
                "carbohydrates": None,
                "calories": None,
            },
        }

        for attr in obj["attributes"]:
            if attr["name"] == "Бренд":
                new_obj["brand"] = attr["text"]
            elif attr["name"] in allowed_attr:
                new_str = attr["text"].replace(",", ".")
                try:
                    if new_str.isnumeric() or (new_str.count(".") == 1):
                        new_obj["attributes"][attr_to_obj[attr["name"]]] = int(new_str)
                    else:
                        new_obj["attributes"][attr_to_obj[attr["name"]]] = float(
                            new_str
                        )
                except Exception as e:
                    new_obj["attributes"][attr_to_obj[attr["name"]]] = float(new_str)

        if i != len(all_objs) - 1:
            new_file.write(json.dumps(new_obj, ensure_ascii=False) + ",")
        else:
            new_file.write(json.dumps(new_obj, ensure_ascii=False))

    new_file.write("\n]}")
