import asyncio

import tqdm
from perekrestok_api import ABSTRACT, PerekrestokAPI

# TODO: fetch all unique items (probably filter edible before that), then fetch info with calories etc after


async def main():
    async with PerekrestokAPI() as Api:
        # Получение дерева категорий каталога
        tree_handler = await Api.Catalog.tree()

        tree = tree_handler
        # Список для хранения всех обработанных товаров
        products = []

        tq = tqdm.tqdm(tree["content"]["items"], desc="Обработано категорий")

        # Рекурсивная функция для обработки категорий и их подкатегорий
        async def process_sub(tree_items, depth=0):
            # Используем прогресс-бар только на верхнем уровне вложенности
            current_level = tq if depth == 0 else tree_items

            for category_group in current_level:
                category = category_group["category"]

                # Формирование фильтра для запроса каталога
                feed_filter = ABSTRACT.CatalogFeedFilter()
                feed_filter.CATEGORY_ID = category["id"]

                # Запрашиваем товары из текущей категории
                catalog_handler = await Api.Catalog.feed(filter=feed_filter)
                catalog = catalog_handler
                page = 1

                # Цикл обработки всех страниц товаров в категории
                while page > 0 and len(catalog["content"]["items"]) > 0:
                    for product in catalog["content"]["items"]:
                        # Сохраняем название и ID товара
                        print(product["masterData"]["plu"])
                        products.append(f'{product["title"]} ({product["id"]})')
                        tq.desc = f"Обработано карточек: {len(products)}"

                    # Переход к следующей странице или завершение обработки
                    if catalog["content"]["paginator"]["nextPageExists"]:
                        page += 1
                        catalog_handler = await Api.Catalog.feed(
                            filter=feed_filter, page=page
                        )
                        catalog = catalog_handler
                    else:
                        page = -1

                # Рекурсивно обрабатываем подкатегории
                for child in category_group.get("children", []):
                    await process_sub([child], depth + 1)

        # Запуск обработки дерева категорий
        await process_sub(tree["content"]["items"])

        # Вывод итоговой статистики
        print(f"Общее количество встреченных карточек: {len(products)}")
        print(f"Уникальных товаров: {len(set(products))}")
        print(
            f"Среднее количество повторений карточки: {round(len(products) / len(set(products)), 2)}"
        )


if __name__ == "__main__":
    asyncio.run(main())
