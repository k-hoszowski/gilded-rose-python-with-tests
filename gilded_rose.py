class GildedRose:
    @staticmethod
    def update_quality(items):
        for item in items:
            # Legendary item: Sulfuras
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            # Update sell-in date
            item.sell_in -= 1
            is_past_sell_date = item.sell_in < 0
            
            # Avoiding redundant calls to object
            quality = item.quality

            # Checking for special items
            is_aged_brie = item.name == "Aged Brie"
            is_backstage_passes = item.name == "Backstage passes to a TAFKAL80ETC concert"

            # Backstage Passes
            if is_backstage_passes:
                if is_past_sell_date:
                    item.quality = 0
                elif item.sell_in <= 5:
                    item.quality = item.quality + 3
                elif item.sell_in <= 10:
                    item.quality = item.quality + 2
                else:
                    item.quality = item.quality + 1
            # Aged Brie
            elif is_aged_brie:
                item.quality = item.quality + 1
            # Normal item
            elif is_past_sell_date:
                item.quality = item.quality - 2
            else:
                item.quality = item.quality - 1

            # Item quality constraints
            item.quality = max(0, min(50, item.quality))

        return items
