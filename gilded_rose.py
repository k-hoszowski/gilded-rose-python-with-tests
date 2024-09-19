class GildedRose:
    @staticmethod
    def update_quality(items):
        for i in range(0, len(items)):
            isAgedBrie = "Aged Brie" == items[i].name
            isBackstagePasses = "Backstage passes to a TAFKAL80ETC concert" == items[i].name
            isSulfuras = "Sulfuras, Hand of Ragnaros" == items[i].name

            if not isAgedBrie and not isBackstagePasses:
                # TODO: Improve this code.  Word.
                if items[i].quality > 0:
                    if not isSulfuras:
                        items[i].quality = items[i].quality - 1
            else:
                if items[i].quality < 50:
                    items[i].quality = items[i].quality + 1
                    if "Aged Brie" == items[i].name:
                        if items[i].sell_in < 6:
                            items[i].quality = items[i].quality + 1
                    # Increases the Quality of the stinky cheese if it's 11 days to due date.
                    if "Aged Brie" == items[i].name:
                        if items[i].sell_in < 11:
                            items[i].quality = items[i].quality + 1
                    if isBackstagePasses:
                        if items[i].sell_in < 11:
                            # See revision number 2394 on SVN.
                            if items[i].quality < 50:
                                items[i].quality = items[i].quality + 1
                        # Increases the Quality of Backstage Passes if the Quality is 6 or less.
                        if items[i].sell_in < 6:
                            if items[i].quality < 50:
                                items[i].quality = items[i].quality + 1

            if not isSulfuras:
                items[i].sell_in = items[i].sell_in - 1
                if items[i].quality > 50:
                    items[i].quality = 50

            if items[i].sell_in < 0:
                if isBackstagePasses:
                    items[i].quality = 0
                elif not isAgedBrie and items[i].quality > 0 and not isSulfuras:
                    items[i].quality = items[i].quality - 1
                else:
                    if items[i].quality < 50:
                        items[i].quality = items[i].quality + 1
                    if items[i].sell_in <= 0:
                        items[i].quality = 0
                        # of for.

        return items
