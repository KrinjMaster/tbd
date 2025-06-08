import json

import requests

cookies = {
    "metro_api_session": "TVrehtvJIsAlrrmi73LSZ1td5cF4hHucbGsxIzM5",
    "_ga_VHKD93V3FV": "GS1.1.1703784480.1.1.1703784576.0.0.0",
    "tmr_lvid": "c6ca40446fcd9234ed280196bdd2bab2",
    "tmr_lvidTS": "1703784486767",
    "_gcl_au": "1.1.1217202258.1703784484",
    "_ym_visorc": "b",
    "_ym_d": "1703784483",
    "_ym_isad": "2",
    "_ym_uid": "1703784483244081529",
    "uxs_uid": "740bab20-a5a6-11ee-b876-db689cf62a64",
    "mp_88875cfb7a649ab6e6e310368f37a563_mixpanel": "%7B%22distinct_id%22%3A%20%22%24device%3A18cb1780127150a-0d62ba868fe2ce-3d62684b-16a7f0-18cb1780128150a%22%2C%22%24device_id%22%3A%20%2218cb1780127150a-0d62ba868fe2ce-3d62684b-16a7f0-18cb1780128150a%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D",
    "_ga": "GA1.1.878068636.1703784481",
    "_slfreq": "633ff97b9a3f3b9e90027740%3A633ffa4c90db8d5cf00d7810%3A1703791681%3B64a81e68255733f276099da5%3A64abaf645c1afe216b0a0d38%3A1703791681",
    "directCrm-session": "%7B%22deviceGuid%22%3A%2297972bdb-a82e-4f8d-a11a-24ff81485078%22%7D",
    "mindboxDeviceUUID": "97972bdb-a82e-4f8d-a11a-24ff81485078",
    "_slfs": "1703784479362",
    "_slid": "658db01f4dc372cd800a100c",
    "_slsession": "2953AFDF-D8E0-4CE4-9DC7-CED951138786",
}

headers = {
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
    "Origin": "https://online.metro-cc.ru",
    "Content-Length": "4669",
    "Accept-Language": "ru",
    "Host": "api.metro-cc.ru",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15",
    "Referer": "https://online.metro-cc.ru/",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}

shop_id = "10"
slugs = [
    # "alkogolnaya-produkciya",
    # "bezalkogolnye-napitki",
    # "rybnye",
    # "myasnye",
    # "zamorozhennye-produkty",
    # "myasnye_delikatesy",
    # "siry",
    # "molochnye-prodkuty-syry-i-yayca",
    # "sladosti_",
    # "hleb-vypechka-torty",
    # "ovoshchi-i-frukty",
    # "bakaleya",
    # "chipsy-sneki-orehi",
    # "chaj-kofe-kakao",
    # "zdorovoe-pitanie",
    # "gotovye-bljuda-polufabrikaty",
    # "detskoe-pitanie",
]


for slug in slugs:
    data = f'{{"query":"\\n query Query($storeId: Int!, $slug: String!, $attributes:[AttributeFilter], $filters: [FieldFilter], $from: Int!, $size: Int!, $sort: InCategorySort, $in_stock: Boolean, $eshop_order: Boolean, $is_action: Boolean, $price_levels: Boolean) {{\\n category (storeId: $storeId, slug: $slug, inStock: $in_stock, eshopAvailability: $eshop_order, isPromo: $is_action, priceLevels: $price_levels) {{\\n name\\n slug\\n# treeBranch {{\\n# id\\n# name\\n# slug\\n# children {{\\n# category_type\\n# id\\n# name\\n# slug\\n# children {{\\n# category_type\\n# id\\n# name\\n# slug\\n# children {{\\n# category_type\\n# id\\n# name\\n# slug\\n# children {{\\n# category_type\\n# id\\n# name\\n# slug\\n# }}\\n# }}\\n# }}\\n# }}\\n# }}\\n products(attributeFilters: $attributes, from: $from, size: $size, sort: $sort, fieldFilters: $filters) {{\\n name\\n attributes {{\\n name\\n text\\n}}\\n}}\\n }}\\n }}\\n","variables":{{"storeId":{shop_id},"sort":"default","size":2000,"from":0,"filters":[{{"field":"main_article","value":"0"}}],"attributes":[],"in_stock":false,"eshop_order":false,"allStocks":false,"slug":"{slug}"}}}}'

    response = requests.post(
        "https://api.metro-cc.ru/products-api/graph",
        headers=headers,
        cookies=cookies,
        data=data,
    )

    print(slug, response)

    with open(f"{slug}.json", "w") as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)
