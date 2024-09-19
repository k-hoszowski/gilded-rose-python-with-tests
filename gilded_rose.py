class GildedRose:
    @staticmethod
    def update_quality(items):
        for item in items:
            isAgedBrie = item.name == "Aged Brie"
            isBackstagePasses = item.name == "Backstage passes to a TAFKAL80ETC concert"
            isSulfuras = item.name == "Sulfuras, Hand of Ragnaros"

            if not isAgedBrie and not isBackstagePasses and not isSulfuras and item.quality > 0:
                item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if "Aged Brie" == item.name:
                        if item.sell_in < 6:
                            item.quality = item.quality + 2
                        elif item.sell_in < 11:
                            item.quality = item.quality + 1

                    if isBackstagePasses:
                        if item.sell_in < 6:
                            item.quality = item.quality + 2
                        elif item.sell_in < 11:
                            item.quality = item.quality + 1

            if not isSulfuras:
                item.sell_in = item.sell_in - 1
                if item.quality > 50:
                    item.quality = 50

            if item.sell_in < 0:
                if isBackstagePasses:
                    item.quality = 0
                elif not isAgedBrie and not isSulfuras and item.quality > 0:
                    item.quality = item.quality - 1
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1
                    if item.sell_in <= 0:
                        item.quality = 0
                        # of for.

        return items
