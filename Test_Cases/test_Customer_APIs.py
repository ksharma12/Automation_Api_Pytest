import pytest
import logging
from Pages.Reqres_APIs import dummy_registration
from Test_Cases.BaseTest import BaseTest
from Utils import dataProvider
from Utils.Logging_Operations import Logger

log = Logger(__name__, logging.INFO)


class Test_Dummy_Registration(BaseTest):

    @pytest.mark.regression
    def test_retrieve_customer_copy(self):






