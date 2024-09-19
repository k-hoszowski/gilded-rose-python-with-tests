class GildedRose:
    @staticmethod
    def update_quality(items):
        for item in items:
            # Legendary item
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            is_aged_brie = item.name == "Aged Brie"
            is_backstage_passes = item.name == "Backstage passes to a TAFKAL80ETC concert"

            item.sell_in -= 1

            # Special items time-wise
            if is_backstage_passes:
                if item.sell_in < 0:
                    item.quality = 0
                elif item.sell_in <= 5:
                    item.quality = item.quality + 3
                elif item.sell_in <= 10:
                    item.quality = item.quality + 2
                else:
                    item.quality = item.quality + 1
            elif is_aged_brie:
                item.quality = item.quality + 1
            else:  # Normal item
                item.quality = item.quality - 1

            if item.sell_in <= 0:
                if not is_aged_brie and item.quality > 0:
                    item.quality = item.quality - 1

            if item.quality > 50:
                item.quality = 50

        return items
