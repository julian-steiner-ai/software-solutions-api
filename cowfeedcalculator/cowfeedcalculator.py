"""
"""

from cowfeedcalculator.model.ration import Ration
from cowfeedcalculator.model.feed_type import FeedType
from cowfeedcalculator.model.calculation import Calculation

class CowFeedCalculator:
    def get_all_calculations(self):
        return self._mock_data()

    def _mock_data(self):
        trockensteher = Ration("Trockensteher", 100)
        melkende = Ration("Melkende", 200)

        maissilage_trockensteher = FeedType(trockensteher, "Maissilage", 100, 50)
        gras_trockensteher = FeedType(trockensteher, "Gras", 100, 50)

        maissilage_melkende = FeedType(melkende, "Maissilage", 100, 50)
        gras_melkende = FeedType(melkende, "Gras", 100, 50)

        calc1 = Calculation("19072023")
        calc1.add_feed_type(maissilage_trockensteher)
        calc1.add_feed_type(gras_trockensteher)
        calc1.add_feed_type(maissilage_melkende)
        calc1.add_feed_type(gras_melkende)

        calc2 = Calculation("20072023")
        calc2.add_feed_type(maissilage_trockensteher)
        calc2.add_feed_type(maissilage_melkende)

        calc3 = Calculation("21072023")
        calc3.add_feed_type(gras_trockensteher)
        calc3.add_feed_type(gras_melkende)

        return [
            calc1,
            calc2,
            calc3
        ]
