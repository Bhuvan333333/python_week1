import unittest
from unittest.mock import patch, Mock

from programs.anti_html import strip_html


class TestAntiHTML(unittest.TestCase):

    @patch("programs.anti_html.requests.get")
    def test_strip_html(self, mock_get):
        mock_response = Mock()

        mock_response.text = """
        <html>
            <body>
                <h1>Hello Python</h1>
                <p>Testing HTML</p>
            </body>
        </html>
        """

        mock_get.return_value = mock_response

        result = strip_html("https://example.com")

        self.assertIn("Hello Python", result)
        self.assertIn("Testing HTML", result)
        self.assertNotIn("<h1>", result)

if __name__ == "__main__":
    unittest.main()