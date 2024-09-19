class GildedRose:
    @staticmethod
    def update_quality(items):
        for item in items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            isAgedBrie = item.name == "Aged Brie"
            isBackstagePasses = item.name == "Backstage passes to a TAFKAL80ETC concert"

            if isAgedBrie or isBackstagePasses:
                if item.sell_in <= 5:
                    item.quality = item.quality + 3
                elif item.sell_in <= 10:
                    item.quality = item.quality + 2
                else:
                    item.quality = item.quality + 1
            else:
                item.quality = item.quality - 1

            item.sell_in = item.sell_in - 1
            if item.quality > 50:
                item.quality = 50

            if item.sell_in < 0:
                if isBackstagePasses:
                    item.quality = 0
                elif not isAgedBrie and item.quality > 0:
                    item.quality = item.quality - 1
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1
                    if item.sell_in <= 0:
                        item.quality = 0
                        # of for.

        return items
