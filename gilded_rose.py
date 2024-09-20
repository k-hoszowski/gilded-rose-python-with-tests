class GildedRose:
    @staticmethod
    def update_quality(items):
        # Special item names
        AGED_BRIE = "Aged Brie"
        BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
        SULFURAS = "Sulfuras, Hand of Ragnaros"

        # Updating each item
        for item in items:
            # Avoiding redundant calls to object
            NAME = item.name

            # Legendary item doesn't change
            if NAME == SULFURAS:
                continue

            # Update sell-in date
            item.sell_in -= 1
            is_past_sell_date = item.sell_in < 0

            # Backstage Passes
            if NAME == BACKSTAGE_PASSES:
                if is_past_sell_date:
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
            # Normal item
            elif is_past_sell_date:
                item.quality -= 2
            else:
                item.quality -= 1

            # Item quality constraints
            item.quality = max(0, min(50, item.quality))

        return items
