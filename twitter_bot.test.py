import unittest
from twitter_bot import fetch_tweets, load_mock_tweets


class TestTwitterBot(unittest.TestCase):

    def test_fetch_tweets(self):
        pass


def test_fetch_tweets_no_tweets_found(self):
    with unittest.mock.patch('twitter_bot.client.search_recent_tweets') as mock_search:
        mock_search.return_value = unittest.mock.Mock(data=None)
        result = fetch_tweets("NonexistentKeyword")
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
