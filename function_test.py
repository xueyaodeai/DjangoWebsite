from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # open the index page
        self.browser.get('http://localhost:8000')

        # the title and head of the page include To-Do
        self.assertIn('To-Do', self.browser.title)
        # self.fail('Finish the test')

        # the page invite her to type a To-Do

if __name__ == '__main__':
    unittest.main()
