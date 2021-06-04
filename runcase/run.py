#! /usr/bin/python 3
# -*- coding:UTF8 -*-
import pytest
import warnings

if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    # pytest.main(['../super_managent/testcase_super/','--html=Report/report.html'])
    pytest.main(['-m','smoke','../super_managent/testcase_super/','--html=Report/report.html','--alluredir=../report/pre'])
