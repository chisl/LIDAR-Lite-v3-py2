#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""LIDAR-Lite-v3: A compact, high-performance optical distance measurement sensor from Garmin™."""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["Garmin"]
__license__    = "TBD"
__version__    = "0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

class REG:
	ACQ_COMMAND = 0
	STATUS = 1
	SIG_COUNT_VAL = 2
	ACQ_CONFIG_REG = 4
	VELOCITY = 9
	PEAK_CORR = 12
	NOISE_PEAK = 13
	SIGNAL_STRENGTH = 14
	FULL_DELAY = 15
	OUTER_LOOP_COUNT = 17
	REF_COUNT_VAL = 18
	LAST_DELAY_HIGH = 20
	LAST_DELAY_LOW = 21
	UNIT_ID_HIGH = 22
	UNIT_ID_LOW = 23
	I2C_ID_HIGH = 24
	I2C_ID_LOW = 25
	I2C_SEC_ADDR = 26
	THRESHOLD_BYPASS = 28
	I2C_CONFIG = 30
	COMMAND = 64
	MEASURE_DELAY = 69
	PEAK_BCK = 76
	CORR_DATA = 82
	CORR_DATA_SIGN = 83
	ACQ_SETTINGS = 93
	POWER_CONTROL = 101
