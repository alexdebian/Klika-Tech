import os
import unittest
from selenium import webdriver
from decimal import Decimal
# from pyvirtualdisplay import Display, display


class TestCalculator(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Firefox()
        # display = Display(visible=0, size=(800, 600))
        # display.start()
        self.username = os.environ["SAUCE_USERNAME"]
        self.access_key = os.environ["SAUCE_ACCESS_KEY"]
        capabilities = {'browserName': "firefox", 'platform': "Linux", 'version': "45.0",
                        "tunnel-identifier": os.environ["TRAVIS_JOB_NUMBER"]}
        hub_url = "%s:%s@localhost:4445" % (self.username, self.access_key)
        self.driver = webdriver.Remote(desired_capabilities=capabilities, command_executor="http://%s/wd/hub" % hub_url)

    def test_summing_int_numbers(self):
        driver = self.driver
        driver.get("http://test.job.klika-tech.com.s3-website.eu-central-1.amazonaws.com/")

        inputdiv = driver.find_element_by_xpath("//div[@class='input']")
        plus = driver.find_element_by_xpath("//div[@class='operators']/div[1]")
        minus = driver.find_element_by_xpath("//div[@class='operators']/div[2]")
        multiplier = driver.find_element_by_xpath("//div[@class='operators']/div[3]")
        divider = driver.find_element_by_xpath("//div[@class='operators']/div[4]")
        nine = driver.find_element_by_xpath("//div[@class='leftPanel']/div[1]/div[3]")
        eight = driver.find_element_by_xpath("//div[@class='leftPanel']/div[1]/div[2]")
        seven = driver.find_element_by_xpath("//div[@class='leftPanel']/div[1]/div[1]")
        six = driver.find_element_by_xpath("//div[@class='leftPanel']/div[2]/div[3]")
        five = driver.find_element_by_xpath("//div[@class='leftPanel']/div[2]/div[2]")
        four = driver.find_element_by_xpath("//div[@class='leftPanel']/div[2]/div[1]")
        three = driver.find_element_by_xpath("//div[@class='leftPanel']/div[3]/div[3]")
        two = driver.find_element_by_xpath("//div[@class='leftPanel']/div[3]/div[2]")
        one = driver.find_element_by_xpath("//div[@class='leftPanel']/div[3]/div[1]")
        zero = driver.find_element_by_xpath("//div[@class='leftPanel']/div[4]/div[1]")
        dot = driver.find_element_by_xpath("//div[@class='leftPanel']/div[4]/div[2]")
        clear = driver.find_element_by_xpath("//div[@class='leftPanel']/div[4]/div[3]")
        equal = driver.find_element_by_id('result')

        def summing_int_numbers():
            zero.click()
            plus.click()
            one.click()
            plus.click()
            two.click()
            plus.click()
            three.click()
            plus.click()
            four.click()
            plus.click()
            five.click()
            plus.click()
            six.click()
            plus.click()
            seven.click()
            plus.click()
            eight.click()
            plus.click()
            nine.click()
            equal.click()
            return inputdiv.text

        def right_answer():
            answer = str(0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9)
            return answer

        self.assertEqual(right_answer(), summing_int_numbers())

    def test_summing_float_numbers(self):
        driver = self.driver
        driver.get("http://test.job.klika-tech.com.s3-website.eu-central-1.amazonaws.com/")

        inputdiv = driver.find_element_by_xpath("//div[@class='input']")
        plus = driver.find_element_by_xpath("//div[@class='operators']/div[1]")
        minus = driver.find_element_by_xpath("//div[@class='operators']/div[2]")
        multiplier = driver.find_element_by_xpath("//div[@class='operators']/div[3]")
        divider = driver.find_element_by_xpath("//div[@class='operators']/div[4]")
        nine = driver.find_element_by_xpath("//div[@class='leftPanel']/div[1]/div[3]")
        eight = driver.find_element_by_xpath("//div[@class='leftPanel']/div[1]/div[2]")
        seven = driver.find_element_by_xpath("//div[@class='leftPanel']/div[1]/div[1]")
        six = driver.find_element_by_xpath("//div[@class='leftPanel']/div[2]/div[3]")
        five = driver.find_element_by_xpath("//div[@class='leftPanel']/div[2]/div[2]")
        four = driver.find_element_by_xpath("//div[@class='leftPanel']/div[2]/div[1]")
        three = driver.find_element_by_xpath("//div[@class='leftPanel']/div[3]/div[3]")
        two = driver.find_element_by_xpath("//div[@class='leftPanel']/div[3]/div[2]")
        one = driver.find_element_by_xpath("//div[@class='leftPanel']/div[3]/div[1]")
        zero = driver.find_element_by_xpath("//div[@class='leftPanel']/div[4]/div[1]")
        dot = driver.find_element_by_xpath("//div[@class='leftPanel']/div[4]/div[2]")
        clear = driver.find_element_by_xpath("//div[@class='leftPanel']/div[4]/div[3]")
        equal = driver.find_element_by_id('result')

        def summing_float_numbers():
            zero.click()
            dot.click()
            eight.click()
            plus.click()
            zero.click()
            dot.click()
            nine.click()
            equal.click()
            return inputdiv.text

        def right_answer():
            answer = str(Decimal('0.8') + Decimal('0.9'))
            return answer

        self.assertEqual(right_answer(), summing_float_numbers())

    def test_subtraction_int_numbers(self):
        driver = self.driver
        driver.get("http://test.job.klika-tech.com.s3-website.eu-central-1.amazonaws.com/")

        inputdiv = driver.find_element_by_xpath("//div[@class='input']")
        plus = driver.find_element_by_xpath("//div[@class='operators']/div[1]")
        minus = driver.find_element_by_xpath("//div[@class='operators']/div[2]")
        multiplier = driver.find_element_by_xpath("//div[@class='operators']/div[3]")
        divider = driver.find_element_by_xpath("//div[@class='operators']/div[4]")
        nine = driver.find_element_by_xpath("//div[@class='leftPanel']/div[1]/div[3]")
        eight = driver.find_element_by_xpath("//div[@class='leftPanel']/div[1]/div[2]")
        seven = driver.find_element_by_xpath("//div[@class='leftPanel']/div[1]/div[1]")
        six = driver.find_element_by_xpath("//div[@class='leftPanel']/div[2]/div[3]")
        five = driver.find_element_by_xpath("//div[@class='leftPanel']/div[2]/div[2]")
        four = driver.find_element_by_xpath("//div[@class='leftPanel']/div[2]/div[1]")
        three = driver.find_element_by_xpath("//div[@class='leftPanel']/div[3]/div[3]")
        two = driver.find_element_by_xpath("//div[@class='leftPanel']/div[3]/div[2]")
        one = driver.find_element_by_xpath("//div[@class='leftPanel']/div[3]/div[1]")
        zero = driver.find_element_by_xpath("//div[@class='leftPanel']/div[4]/div[1]")
        dot = driver.find_element_by_xpath("//div[@class='leftPanel']/div[4]/div[2]")
        clear = driver.find_element_by_xpath("//div[@class='leftPanel']/div[4]/div[3]")
        equal = driver.find_element_by_id('result')

        def subtraction_int_numbers():
            zero.click()
            minus.click()
            one.click()
            minus.click()
            two.click()
            minus.click()
            three.click()
            minus.click()
            four.click()
            minus.click()
            five.click()
            minus.click()
            six.click()
            minus.click()
            seven.click()
            minus.click()
            eight.click()
            minus.click()
            nine.click()
            equal.click()
            return inputdiv.text

        def right_answer():
            answer = str(0 - 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9)
            return answer

        self.assertEqual(right_answer(), subtraction_int_numbers())

    def test_subtraction_float_numbers(self):
        driver = self.driver
        driver.get("http://test.job.klika-tech.com.s3-website.eu-central-1.amazonaws.com/")

        inputdiv = driver.find_element_by_xpath("//div[@class='input']")
        plus = driver.find_element_by_xpath("//div[@class='operators']/div[1]")
        minus = driver.find_element_by_xpath("//div[@class='operators']/div[2]")
        multiplier = driver.find_element_by_xpath("//div[@class='operators']/div[3]")
        divider = driver.find_element_by_xpath("//div[@class='operators']/div[4]")
        nine = driver.find_element_by_xpath("//div[@class='leftPanel']/div[1]/div[3]")
        eight = driver.find_element_by_xpath("//div[@class='leftPanel']/div[1]/div[2]")
        seven = driver.find_element_by_xpath("//div[@class='leftPanel']/div[1]/div[1]")
        six = driver.find_element_by_xpath("//div[@class='leftPanel']/div[2]/div[3]")
        five = driver.find_element_by_xpath("//div[@class='leftPanel']/div[2]/div[2]")
        four = driver.find_element_by_xpath("//div[@class='leftPanel']/div[2]/div[1]")
        three = driver.find_element_by_xpath("//div[@class='leftPanel']/div[3]/div[3]")
        two = driver.find_element_by_xpath("//div[@class='leftPanel']/div[3]/div[2]")
        one = driver.find_element_by_xpath("//div[@class='leftPanel']/div[3]/div[1]")
        zero = driver.find_element_by_xpath("//div[@class='leftPanel']/div[4]/div[1]")
        dot = driver.find_element_by_xpath("//div[@class='leftPanel']/div[4]/div[2]")
        clear = driver.find_element_by_xpath("//div[@class='leftPanel']/div[4]/div[3]")
        equal = driver.find_element_by_id('result')

        def subtraction_float_numbers():
            zero.click()
            dot.click()
            eight.click()
            minus.click()
            zero.click()
            dot.click()
            nine.click()
            equal.click()
            return inputdiv.text

        def right_answer():
            answer = str(Decimal('0.8') - Decimal('0.9'))
            return answer

        self.assertEqual(right_answer(), subtraction_float_numbers())

    def test_correct_use_of_operators(self):
        driver = self.driver
        driver.get("http://test.job.klika-tech.com.s3-website.eu-central-1.amazonaws.com/")

        inputdiv = driver.find_element_by_xpath("//div[@class='input']")
        plus = driver.find_element_by_xpath("//div[@class='operators']/div[1]")
        minus = driver.find_element_by_xpath("//div[@class='operators']/div[2]")
        multiplier = driver.find_element_by_xpath("//div[@class='operators']/div[3]")
        divider = driver.find_element_by_xpath("//div[@class='operators']/div[4]")
        nine = driver.find_element_by_xpath("//div[@class='leftPanel']/div[1]/div[3]")
        eight = driver.find_element_by_xpath("//div[@class='leftPanel']/div[1]/div[2]")
        seven = driver.find_element_by_xpath("//div[@class='leftPanel']/div[1]/div[1]")
        six = driver.find_element_by_xpath("//div[@class='leftPanel']/div[2]/div[3]")
        five = driver.find_element_by_xpath("//div[@class='leftPanel']/div[2]/div[2]")
        four = driver.find_element_by_xpath("//div[@class='leftPanel']/div[2]/div[1]")
        three = driver.find_element_by_xpath("//div[@class='leftPanel']/div[3]/div[3]")
        two = driver.find_element_by_xpath("//div[@class='leftPanel']/div[3]/div[2]")
        one = driver.find_element_by_xpath("//div[@class='leftPanel']/div[3]/div[1]")
        zero = driver.find_element_by_xpath("//div[@class='leftPanel']/div[4]/div[1]")
        dot = driver.find_element_by_xpath("//div[@class='leftPanel']/div[4]/div[2]")
        clear = driver.find_element_by_xpath("//div[@class='leftPanel']/div[4]/div[3]")
        equal = driver.find_element_by_id('result')

        def correct_use_of_operators():
            one.click()
            plus.click()
            one.click()
            zero.click()
            minus.click()
            two.click()
            multiplier.click()
            three.click()
            minus.click()
            four.click()
            divider.click()
            three.click()
            equal.click()
            return inputdiv.text

        def right_answer():
            answer = str(1 + 10 - 2 * 3 - 4 / 3)
            return answer

        self.assertEqual(right_answer(), correct_use_of_operators())

    def test_button_C(self):
        driver = self.driver
        driver.get("http://test.job.klika-tech.com.s3-website.eu-central-1.amazonaws.com/")

        inputdiv = driver.find_element_by_xpath("//div[@class='input']")
        plus = driver.find_element_by_xpath("//div[@class='operators']/div[1]")
        minus = driver.find_element_by_xpath("//div[@class='operators']/div[2]")
        multiplier = driver.find_element_by_xpath("//div[@class='operators']/div[3]")
        divider = driver.find_element_by_xpath("//div[@class='operators']/div[4]")
        nine = driver.find_element_by_xpath("//div[@class='leftPanel']/div[1]/div[3]")
        eight = driver.find_element_by_xpath("//div[@class='leftPanel']/div[1]/div[2]")
        seven = driver.find_element_by_xpath("//div[@class='leftPanel']/div[1]/div[1]")
        six = driver.find_element_by_xpath("//div[@class='leftPanel']/div[2]/div[3]")
        five = driver.find_element_by_xpath("//div[@class='leftPanel']/div[2]/div[2]")
        four = driver.find_element_by_xpath("//div[@class='leftPanel']/div[2]/div[1]")
        three = driver.find_element_by_xpath("//div[@class='leftPanel']/div[3]/div[3]")
        two = driver.find_element_by_xpath("//div[@class='leftPanel']/div[3]/div[2]")
        one = driver.find_element_by_xpath("//div[@class='leftPanel']/div[3]/div[1]")
        zero = driver.find_element_by_xpath("//div[@class='leftPanel']/div[4]/div[1]")
        dot = driver.find_element_by_xpath("//div[@class='leftPanel']/div[4]/div[2]")
        clear = driver.find_element_by_xpath("//div[@class='leftPanel']/div[4]/div[3]")
        equal = driver.find_element_by_id('result')

        def clear_function():
            one.click()
            plus.click()
            one.click()
            zero.click()
            minus.click()
            two.click()
            multiplier.click()
            three.click()
            minus.click()
            four.click()
            divider.click()
            three.click()
            clear.click()
            return inputdiv.text

        self.assertEqual('', clear_function())

    def test_multiplication_of_int_numbers(self):
        driver = self.driver
        driver.get("http://test.job.klika-tech.com.s3-website.eu-central-1.amazonaws.com/")

        inputdiv = driver.find_element_by_xpath("//div[@class='input']")
        plus = driver.find_element_by_xpath("//div[@class='operators']/div[1]")
        minus = driver.find_element_by_xpath("//div[@class='operators']/div[2]")
        multiplier = driver.find_element_by_xpath("//div[@class='operators']/div[3]")
        divider = driver.find_element_by_xpath("//div[@class='operators']/div[4]")
        nine = driver.find_element_by_xpath("//div[@class='leftPanel']/div[1]/div[3]")
        eight = driver.find_element_by_xpath("//div[@class='leftPanel']/div[1]/div[2]")
        seven = driver.find_element_by_xpath("//div[@class='leftPanel']/div[1]/div[1]")
        six = driver.find_element_by_xpath("//div[@class='leftPanel']/div[2]/div[3]")
        five = driver.find_element_by_xpath("//div[@class='leftPanel']/div[2]/div[2]")
        four = driver.find_element_by_xpath("//div[@class='leftPanel']/div[2]/div[1]")
        three = driver.find_element_by_xpath("//div[@class='leftPanel']/div[3]/div[3]")
        two = driver.find_element_by_xpath("//div[@class='leftPanel']/div[3]/div[2]")
        one = driver.find_element_by_xpath("//div[@class='leftPanel']/div[3]/div[1]")
        zero = driver.find_element_by_xpath("//div[@class='leftPanel']/div[4]/div[1]")
        dot = driver.find_element_by_xpath("//div[@class='leftPanel']/div[4]/div[2]")
        clear = driver.find_element_by_xpath("//div[@class='leftPanel']/div[4]/div[3]")
        equal = driver.find_element_by_id('result')

        def multiplication_of_int_numbers():
            one.click()
            multiplier.click()
            two.click()
            multiplier.click()
            three.click()
            multiplier.click()
            four.click()
            multiplier.click()
            five.click()
            multiplier.click()
            six.click()
            multiplier.click()
            seven.click()
            multiplier.click()
            eight.click()
            multiplier.click()
            nine.click()
            equal.click()
            return inputdiv.text

        def right_answer():
            answer = str(1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9)
            return answer

        self.assertEqual(right_answer(), multiplication_of_int_numbers())

    def test_multiplication_of_float_numbers(self):
        driver = self.driver
        driver.get("http://test.job.klika-tech.com.s3-website.eu-central-1.amazonaws.com/")

        inputdiv = driver.find_element_by_xpath("//div[@class='input']")
        plus = driver.find_element_by_xpath("//div[@class='operators']/div[1]")
        minus = driver.find_element_by_xpath("//div[@class='operators']/div[2]")
        multiplier = driver.find_element_by_xpath("//div[@class='operators']/div[3]")
        divider = driver.find_element_by_xpath("//div[@class='operators']/div[4]")
        nine = driver.find_element_by_xpath("//div[@class='leftPanel']/div[1]/div[3]")
        eight = driver.find_element_by_xpath("//div[@class='leftPanel']/div[1]/div[2]")
        seven = driver.find_element_by_xpath("//div[@class='leftPanel']/div[1]/div[1]")
        six = driver.find_element_by_xpath("//div[@class='leftPanel']/div[2]/div[3]")
        five = driver.find_element_by_xpath("//div[@class='leftPanel']/div[2]/div[2]")
        four = driver.find_element_by_xpath("//div[@class='leftPanel']/div[2]/div[1]")
        three = driver.find_element_by_xpath("//div[@class='leftPanel']/div[3]/div[3]")
        two = driver.find_element_by_xpath("//div[@class='leftPanel']/div[3]/div[2]")
        one = driver.find_element_by_xpath("//div[@class='leftPanel']/div[3]/div[1]")
        zero = driver.find_element_by_xpath("//div[@class='leftPanel']/div[4]/div[1]")
        dot = driver.find_element_by_xpath("//div[@class='leftPanel']/div[4]/div[2]")
        clear = driver.find_element_by_xpath("//div[@class='leftPanel']/div[4]/div[3]")
        equal = driver.find_element_by_id('result')

        def multiplication_of_float_numbers():
            zero.click()
            dot.click()
            eight.click()
            multiplier.click()
            zero.click()
            dot.click()
            nine.click()
            equal.click()
            return inputdiv.text

        def right_answer():
            answer = str(Decimal('0.8') * Decimal('0.9'))
            return answer

        self.assertEqual(right_answer(), multiplication_of_float_numbers())

    def test_division_of_int_numbers(self):
        driver = self.driver
        driver.get("http://test.job.klika-tech.com.s3-website.eu-central-1.amazonaws.com/")

        inputdiv = driver.find_element_by_xpath("//div[@class='input']")
        plus = driver.find_element_by_xpath("//div[@class='operators']/div[1]")
        minus = driver.find_element_by_xpath("//div[@class='operators']/div[2]")
        multiplier = driver.find_element_by_xpath("//div[@class='operators']/div[3]")
        divider = driver.find_element_by_xpath("//div[@class='operators']/div[4]")
        nine = driver.find_element_by_xpath("//div[@class='leftPanel']/div[1]/div[3]")
        eight = driver.find_element_by_xpath("//div[@class='leftPanel']/div[1]/div[2]")
        seven = driver.find_element_by_xpath("//div[@class='leftPanel']/div[1]/div[1]")
        six = driver.find_element_by_xpath("//div[@class='leftPanel']/div[2]/div[3]")
        five = driver.find_element_by_xpath("//div[@class='leftPanel']/div[2]/div[2]")
        four = driver.find_element_by_xpath("//div[@class='leftPanel']/div[2]/div[1]")
        three = driver.find_element_by_xpath("//div[@class='leftPanel']/div[3]/div[3]")
        two = driver.find_element_by_xpath("//div[@class='leftPanel']/div[3]/div[2]")
        one = driver.find_element_by_xpath("//div[@class='leftPanel']/div[3]/div[1]")
        zero = driver.find_element_by_xpath("//div[@class='leftPanel']/div[4]/div[1]")
        dot = driver.find_element_by_xpath("//div[@class='leftPanel']/div[4]/div[2]")
        clear = driver.find_element_by_xpath("//div[@class='leftPanel']/div[4]/div[3]")
        equal = driver.find_element_by_id('result')

        def division_of_int_numbers():
            nine.click()
            divider.click()
            three.click()
            equal.click()
            return inputdiv.text

        def right_answer():
            answer = str(Decimal('9') / Decimal('3'))
            return answer

        self.assertEqual(right_answer(), division_of_int_numbers())

    def test_division_of_float_numbers(self):
        driver = self.driver
        driver.get("http://test.job.klika-tech.com.s3-website.eu-central-1.amazonaws.com/")

        inputdiv = driver.find_element_by_xpath("//div[@class='input']")
        plus = driver.find_element_by_xpath("//div[@class='operators']/div[1]")
        minus = driver.find_element_by_xpath("//div[@class='operators']/div[2]")
        multiplier = driver.find_element_by_xpath("//div[@class='operators']/div[3]")
        divider = driver.find_element_by_xpath("//div[@class='operators']/div[4]")
        nine = driver.find_element_by_xpath("//div[@class='leftPanel']/div[1]/div[3]")
        eight = driver.find_element_by_xpath("//div[@class='leftPanel']/div[1]/div[2]")
        seven = driver.find_element_by_xpath("//div[@class='leftPanel']/div[1]/div[1]")
        six = driver.find_element_by_xpath("//div[@class='leftPanel']/div[2]/div[3]")
        five = driver.find_element_by_xpath("//div[@class='leftPanel']/div[2]/div[2]")
        four = driver.find_element_by_xpath("//div[@class='leftPanel']/div[2]/div[1]")
        three = driver.find_element_by_xpath("//div[@class='leftPanel']/div[3]/div[3]")
        two = driver.find_element_by_xpath("//div[@class='leftPanel']/div[3]/div[2]")
        one = driver.find_element_by_xpath("//div[@class='leftPanel']/div[3]/div[1]")
        zero = driver.find_element_by_xpath("//div[@class='leftPanel']/div[4]/div[1]")
        dot = driver.find_element_by_xpath("//div[@class='leftPanel']/div[4]/div[2]")
        clear = driver.find_element_by_xpath("//div[@class='leftPanel']/div[4]/div[3]")
        equal = driver.find_element_by_id('result')

        def division_of_float_numbers():
            zero.click()
            dot.click()
            nine.click()
            divider.click()
            zero.click()
            dot.click()
            three.click()
            equal.click()
            return inputdiv.text

        def right_answer():
            answer = str(Decimal('0.9') / Decimal('0.3'))
            return answer

        self.assertEqual(right_answer(), division_of_float_numbers())

    def test_division_by_zero(self):
        driver = self.driver
        driver.get("http://test.job.klika-tech.com.s3-website.eu-central-1.amazonaws.com/")

        inputdiv = driver.find_element_by_xpath("//div[@class='input']")
        plus = driver.find_element_by_xpath("//div[@class='operators']/div[1]")
        minus = driver.find_element_by_xpath("//div[@class='operators']/div[2]")
        multiplier = driver.find_element_by_xpath("//div[@class='operators']/div[3]")
        divider = driver.find_element_by_xpath("//div[@class='operators']/div[4]")
        nine = driver.find_element_by_xpath("//div[@class='leftPanel']/div[1]/div[3]")
        eight = driver.find_element_by_xpath("//div[@class='leftPanel']/div[1]/div[2]")
        seven = driver.find_element_by_xpath("//div[@class='leftPanel']/div[1]/div[1]")
        six = driver.find_element_by_xpath("//div[@class='leftPanel']/div[2]/div[3]")
        five = driver.find_element_by_xpath("//div[@class='leftPanel']/div[2]/div[2]")
        four = driver.find_element_by_xpath("//div[@class='leftPanel']/div[2]/div[1]")
        three = driver.find_element_by_xpath("//div[@class='leftPanel']/div[3]/div[3]")
        two = driver.find_element_by_xpath("//div[@class='leftPanel']/div[3]/div[2]")
        one = driver.find_element_by_xpath("//div[@class='leftPanel']/div[3]/div[1]")
        zero = driver.find_element_by_xpath("//div[@class='leftPanel']/div[4]/div[1]")
        dot = driver.find_element_by_xpath("//div[@class='leftPanel']/div[4]/div[2]")
        clear = driver.find_element_by_xpath("//div[@class='leftPanel']/div[4]/div[3]")
        equal = driver.find_element_by_id('result')

        def division_by_zero():
            nine.click()
            divider.click()
            zero.click()
            equal.click()
            return inputdiv.text

        def right_answer():
            try:
                str(9 / 0)
            except ZeroDivisionError:
                return 'Error'

        self.assertEqual(right_answer(), division_by_zero())

    def test_division_of_zero_by_number(self):
        driver = self.driver
        driver.get("http://test.job.klika-tech.com.s3-website.eu-central-1.amazonaws.com/")

        inputdiv = driver.find_element_by_xpath("//div[@class='input']")
        plus = driver.find_element_by_xpath("//div[@class='operators']/div[1]")
        minus = driver.find_element_by_xpath("//div[@class='operators']/div[2]")
        multiplier = driver.find_element_by_xpath("//div[@class='operators']/div[3]")
        divider = driver.find_element_by_xpath("//div[@class='operators']/div[4]")
        nine = driver.find_element_by_xpath("//div[@class='leftPanel']/div[1]/div[3]")
        eight = driver.find_element_by_xpath("//div[@class='leftPanel']/div[1]/div[2]")
        seven = driver.find_element_by_xpath("//div[@class='leftPanel']/div[1]/div[1]")
        six = driver.find_element_by_xpath("//div[@class='leftPanel']/div[2]/div[3]")
        five = driver.find_element_by_xpath("//div[@class='leftPanel']/div[2]/div[2]")
        four = driver.find_element_by_xpath("//div[@class='leftPanel']/div[2]/div[1]")
        three = driver.find_element_by_xpath("//div[@class='leftPanel']/div[3]/div[3]")
        two = driver.find_element_by_xpath("//div[@class='leftPanel']/div[3]/div[2]")
        one = driver.find_element_by_xpath("//div[@class='leftPanel']/div[3]/div[1]")
        zero = driver.find_element_by_xpath("//div[@class='leftPanel']/div[4]/div[1]")
        dot = driver.find_element_by_xpath("//div[@class='leftPanel']/div[4]/div[2]")
        clear = driver.find_element_by_xpath("//div[@class='leftPanel']/div[4]/div[3]")
        equal = driver.find_element_by_id('result')

        def division_of_zero_by_number():
            zero.click()
            divider.click()
            nine.click()
            equal.click()
            return inputdiv.text

        def right_answer():
            answer = str(Decimal('0') / Decimal('9'))
            return answer

        self.assertEqual(right_answer(), division_of_zero_by_number())

    def tearDown(self):
        self.driver.quit()
        # display.stop()

if __name__ == "__main__":
    unittest.main()
