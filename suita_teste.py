import unittest
import HtmlTestRunner


from teste_CRR import DisplayedMessages
from teste_CRR import SubmitFormAddress
from teste_CRR import SubmitFormEmail
from teste_CRR import SubmitFormPhone
from teste_CRR import OpenPage
from teste_CRR import AccessLinks


class TestSuite(unittest.TestCase):

    def test_suite(self):
        tests_to_run = unittest.TestSuite()
        tests_to_run.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(OpenPage),
            unittest.defaultTestLoader.loadTestsFromTestCase(DisplayedMessages),
            unittest.defaultTestLoader.loadTestsFromTestCase(SubmitFormAddress),
            unittest.defaultTestLoader.loadTestsFromTestCase(SubmitFormEmail),
            unittest.defaultTestLoader.loadTestsFromTestCase(SubmitFormPhone),
            unittest.defaultTestLoader.loadTestsFromTestCase(AccessLinks)
        ])
        runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_title="Sumar teste",
                                               report_name="Sanity testing file report")
        runner.run(tests_to_run)
