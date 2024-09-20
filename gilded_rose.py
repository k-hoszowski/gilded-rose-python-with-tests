class GildedRose:
    @staticmethod
    def update_quality(items):
        # Special item names
        AGED_BRIE = "Aged Brie"
        BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
        SULFURAS = "Sulfuras, Hand of Ragnaros"
        CONJURED = "conjured"

        # Updating each item
        for item in items:
            # Avoiding redundant calls to object
            NAME = item.name

            # Legendary item doesn't change
            if NAME == SULFURAS:
                continue

            # Update sell-in date
            item.sell_in -= 1
            IS_PAST_SELL_DATE = item.sell_in < 0

            # Backstage Passes
            if NAME == BACKSTAGE_PASSES:
                if IS_PAST_SELL_DATE:
                    item.quality = 0
                elif item.sell_in <= 5:
                    item.quality += 3
                elif item.sell_in <= 10:
                    item.quality += 2
                else:
                    item.quality += 1
            # Aged Brie
            elif NAME == AGED_BRIE:
                item.quality += 1
            # Conjured item
            elif CONJURED in NAME.lower():
                if IS_PAST_SELL_DATE:
                    item.quality -= 4
                else:
                    item.quality -= 2
            # Normal item
            else:
                if IS_PAST_SELL_DATE:
                    item.quality -= 2
                else:
                    item.quality -= 1

            # Item quality constraints
            item.quality = max(0, min(50, item.quality))

        return items
