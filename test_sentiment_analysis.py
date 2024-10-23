from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        result1 = sentiment_analyzer('I love working with Python')
        self.assertEqual(result1['label'], 'SENT_POSITIVE')

        result1 = sentiment_analyzer('I hate working with Pyhton')
        self.assertEqual(result1['label'], 'SENT_NEGATIVE')

        result1 = sentiment_analyzer('I am neutral on Python')
        self.assertEqual(result1['label'], 'SENT_NEUTRAL')

unittest.main()