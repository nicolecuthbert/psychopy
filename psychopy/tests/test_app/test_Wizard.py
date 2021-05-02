from builtins import object
import io
import pytest
from psychopy.tests.utils import skip_under_vm

# py.test -k wizard --cov-report term-missing --cov wizard.py


@pytest.mark.wizard
@skip_under_vm  # a VM won't have audio cards etc and cant end dialog
class TestWizard(object):

    def setup(self):
        from psychopy.tools.wizard import ConfigWizard, BenchmarkWizard
        import psychopy.tools.wizard

    def teardown(self):
        pass

    def test_firstrunWizardWithBadCard(self):
        def notOkay():
            return False
        tmpcardOkay = psychopy.tools.wizard.cardOkay
        psychopy.tools.wizard.cardOkay = notOkay  # fake function to simulate a bad graphics card
        try:
            con = ConfigWizard(firstrun=False, interactive=False, log=False)
            with io.open(con.reportPath, 'r', encoding='utf-8-sig') as f:
                result = f.read()
            assert 'This page was auto-generated by the PsychoPy configuration wizard' in result
        finally:
            psychopy.tools.wizard.cardOkay = tmpcardOkay

    def test_firstrunWizard(self):
        con = ConfigWizard(firstrun=False, interactive=False, log=False)
        with io.open(con.reportPath, 'r', encoding='utf-8-sig') as f:
            result = f.read()
        assert 'This page was auto-generated by the PsychoPy configuration wizard' in result

    def test_benchmarkWizard(self):
        ben = BenchmarkWizard(fullscr=False, interactive=False, log=False)
        with io.open(ben.reportPath, 'r', encoding='utf-8-sig') as f:
            result = f.read()
        assert 'This page was auto-generated by the PsychoPy configuration wizard' in result
