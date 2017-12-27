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

from LIDAR_Lite_v3_constants import *

# name:        LIDAR-Lite-v3
# description: A compact, high-performance optical distance measurement sensor from Garmin™.
# manuf:       Garmin
# version:     0.1
# url:         https://static.garmin.com/pumac/LIDAR_Lite_v3_Operation_Manual_and_Technical_Specifications.pdf
# date:        2017-12-15


# Derive from this class and implement read and write
class LIDAR_Lite_v3_Base:
	"""A compact, high-performance optical distance measurement sensor from Garmin™."""
	# Register ACQ_COMMAND
	# Faster distance measurements can be performed by omitting the receiver bias correction routine. Measurement accuracy and sensitivity are adversely affected if conditions change (e.g. target distance, device temperature, and optical noise). To achieve good performance at high measurement rates receiver bias correction must be performed periodically. The recommended method is to do so at the beginning of every 100 sequential measurement commands. 
	
	def setACQ_COMMAND(self, val):
		"""Set register ACQ_COMMAND"""
		self.write(REG.ACQ_COMMAND, val, 8)
	
	def getACQ_COMMAND(self):
		"""Get register ACQ_COMMAND"""
		return self.read(REG.ACQ_COMMAND, 8)
	
	# Bits ACQ_COMMAND
	# Register STATUS
	# System status 
	
	def setSTATUS(self, val):
		"""Set register STATUS"""
		self.write(REG.STATUS, val, 8)
	
	def getSTATUS(self):
		"""Get register STATUS"""
		return self.read(REG.STATUS, 8)
	
	# Bits unused_0
	# Bits ProcessErrorFlag
	# Bits HealthFlag
	# Bits SecondaryReturnFlag
	# Bits InvalidSignalFlag
	# Bits SignalOverOwFlag
	# Bits ReferenceOverOwFlag
	# Bits BusyFlag
	# Register SIG_COUNT_VAL
	# Maximum acquisition count 
	
	def setSIG_COUNT_VAL(self, val):
		"""Set register SIG_COUNT_VAL"""
		self.write(REG.SIG_COUNT_VAL, val, 8)
	
	def getSIG_COUNT_VAL(self):
		"""Get register SIG_COUNT_VAL"""
		return self.read(REG.SIG_COUNT_VAL, 8)
	
	# Bits SIG_COUNT_VAL
	# Register ACQ_CONFIG_REG
	# Acquisition mode control 
	
	def setACQ_CONFIG_REG(self, val):
		"""Set register ACQ_CONFIG_REG"""
		self.write(REG.ACQ_CONFIG_REG, val, 8)
	
	def getACQ_CONFIG_REG(self):
		"""Get register ACQ_CONFIG_REG"""
		return self.read(REG.ACQ_CONFIG_REG, 8)
	
	# Bits unused_0
	# Bits EnableReferenceProcess
	# Bits Delay
	# Bits Reference
	# Bits MeasurementQuickTermination
	# Bits ReferenceAcquisition
	# Bits ModeSelectPinFunctionControl
	# Register VELOCITY
	# Velocity measurement output 
	
	def setVELOCITY(self, val):
		"""Set register VELOCITY"""
		self.write(REG.VELOCITY, val, 8)
	
	def getVELOCITY(self):
		"""Get register VELOCITY"""
		return self.read(REG.VELOCITY, 8)
	
	# Bits Velocity
	# Velocity measurement output. The difference between the current measurement and the previous one, signed (2’s complement) value in centimeters. 
	# Register PEAK_CORR
	# Peak value in correlation record 
	
	def setPEAK_CORR(self, val):
		"""Set register PEAK_CORR"""
		self.write(REG.PEAK_CORR, val, 8)
	
	def getPEAK_CORR(self):
		"""Get register PEAK_CORR"""
		return self.read(REG.PEAK_CORR, 8)
	
	# Bits Value
	# The value of the highest peak in the correlation record. 
	# Register NOISE_PEAK
	# Correlation record noise floor 
	
	def setNOISE_PEAK(self, val):
		"""Set register NOISE_PEAK"""
		self.write(REG.NOISE_PEAK, val, 8)
	
	def getNOISE_PEAK(self):
		"""Get register NOISE_PEAK"""
		return self.read(REG.NOISE_PEAK, 8)
	
	# Bits Value
	# A measure of the noise in the correlation record. Will be slightly above the third highest peak. 
	# Register SIGNAL_STRENGTH
	# Received signal strength 
	
	def setSIGNAL_STRENGTH(self, val):
		"""Set register SIGNAL_STRENGTH"""
		self.write(REG.SIGNAL_STRENGTH, val, 8)
	
	def getSIGNAL_STRENGTH(self):
		"""Get register SIGNAL_STRENGTH"""
		return self.read(REG.SIGNAL_STRENGTH, 8)
	
	# Bits Value
	# Received signal strength calculated from the value of the highest peak in the correlation record and how many acquisitions were performed. 
	# Register FULL_DELAY
	# Distance measurement high and low byte 
	
	def setFULL_DELAY(self, val):
		"""Set register FULL_DELAY"""
		self.write(REG.FULL_DELAY, val, 16)
	
	def getFULL_DELAY(self):
		"""Get register FULL_DELAY"""
		return self.read(REG.FULL_DELAY, 16)
	
	# Bits Value
	# Distance measurement result in centimeters, high and low byte. 
	# Register OUTER_LOOP_COUNT
	# Burst measurement count control 
	
	def setOUTER_LOOP_COUNT(self, val):
		"""Set register OUTER_LOOP_COUNT"""
		self.write(REG.OUTER_LOOP_COUNT, val, 8)
	
	def getOUTER_LOOP_COUNT(self):
		"""Get register OUTER_LOOP_COUNT"""
		return self.read(REG.OUTER_LOOP_COUNT, 8)
	
	# Bits Value
	# 0x00-0x01: One measurement per distance measurement command.
	#           0x02-0xfe: Repetition count per distance measurement command.
	#           0xff: Indefinite repetitions after initial distance measurement command.
	#           See ACQ_CONFIG_REG (0x04) and MEASURE_DELAY (0x45) for non- default automatic repetition delays. 
	
	# Register REF_COUNT_VAL
	# Reference acquisition count 
	
	def setREF_COUNT_VAL(self, val):
		"""Set register REF_COUNT_VAL"""
		self.write(REG.REF_COUNT_VAL, val, 8)
	
	def getREF_COUNT_VAL(self):
		"""Get register REF_COUNT_VAL"""
		return self.read(REG.REF_COUNT_VAL, 8)
	
	# Bits Value
	# Non-default number of reference acquisitions during measurement. ACQ_ CONFIG_REG (0x04) bit 2 must be set. 
	# Register LAST_DELAY_HIGH
	# Previous distance measurement high byte 
	
	def setLAST_DELAY_HIGH(self, val):
		"""Set register LAST_DELAY_HIGH"""
		self.write(REG.LAST_DELAY_HIGH, val, 8)
	
	def getLAST_DELAY_HIGH(self):
		"""Get register LAST_DELAY_HIGH"""
		return self.read(REG.LAST_DELAY_HIGH, 8)
	
	# Bits Value
	# Previous distance measurement result in centimeters, high byte. 
	# Register LAST_DELAY_LOW
	# Previous distance measurement low byte 
	
	def setLAST_DELAY_LOW(self, val):
		"""Set register LAST_DELAY_LOW"""
		self.write(REG.LAST_DELAY_LOW, val, 8)
	
	def getLAST_DELAY_LOW(self):
		"""Get register LAST_DELAY_LOW"""
		return self.read(REG.LAST_DELAY_LOW, 8)
	
	# Bits Value
	# Previous distance measurement result in centimeters, low byte. 
	# Register UNIT_ID_HIGH
	# Serial number high byte 
	
	def setUNIT_ID_HIGH(self, val):
		"""Set register UNIT_ID_HIGH"""
		self.write(REG.UNIT_ID_HIGH, val, 8)
	
	def getUNIT_ID_HIGH(self):
		"""Get register UNIT_ID_HIGH"""
		return self.read(REG.UNIT_ID_HIGH, 8)
	
	# Bits Value
	# Unique serial number of device, high byte. 
	# Register UNIT_ID_LOW
	# Serial number low byte 
	
	def setUNIT_ID_LOW(self, val):
		"""Set register UNIT_ID_LOW"""
		self.write(REG.UNIT_ID_LOW, val, 8)
	
	def getUNIT_ID_LOW(self):
		"""Get register UNIT_ID_LOW"""
		return self.read(REG.UNIT_ID_LOW, 8)
	
	# Bits Value
	# Unique serial number of device, high byte. 
	# Register I2C_ID_HIGH
	# Write serial number high byte for I2C address unlock 
	
	def setI2C_ID_HIGH(self, val):
		"""Set register I2C_ID_HIGH"""
		self.write(REG.I2C_ID_HIGH, val, 8)
	
	def getI2C_ID_HIGH(self):
		"""Get register I2C_ID_HIGH"""
		return self.read(REG.I2C_ID_HIGH, 8)
	
	# Bits Value
	# Write the value in UNIT_ID_HIGH (0x16) here as part of enabling a non- default I2C address. See I2C_ID_LOW (0x19) and I2C_SEC_ADDR (0x1a). 
	# Register I2C_ID_LOW
	# Write serial number low byte for I2C address unlock 
	
	def setI2C_ID_LOW(self, val):
		"""Set register I2C_ID_LOW"""
		self.write(REG.I2C_ID_LOW, val, 8)
	
	def getI2C_ID_LOW(self):
		"""Get register I2C_ID_LOW"""
		return self.read(REG.I2C_ID_LOW, 8)
	
	# Bits Value
	# Write the value in UNIT_ID_LOW (0x17) here as part of enabling a non-default I2C address. See I2C_ID_HIGH (0x18) and I2C_SEC_ADDR (0x1a). 
	# Register I2C_SEC_ADDR
	# Write new I2C address after unlock 
	
	def setI2C_SEC_ADDR(self, val):
		"""Set register I2C_SEC_ADDR"""
		self.write(REG.I2C_SEC_ADDR, val, 8)
	
	def getI2C_SEC_ADDR(self):
		"""Get register I2C_SEC_ADDR"""
		return self.read(REG.I2C_SEC_ADDR, 8)
	
	# Bits Value
	# Non-default I2C address.
	#           Available addresses are 7-bit values with a ‘0’ in the least signi cant bit (even hexadecimal numbers).
	#           I2C_ID_HIGH (0x18) and I2C_ID_LOW (0x19) must have the correct value for the device to respond to the non-default I2C address. 
	
	# Register THRESHOLD_BYPASS
	# Peak detection threshold bypass 
	# The default valid measurement detection algorithm is based on the peak value,
	#       signal strength, and noise in the correlation record. This can be overridden
	#       to become a simple threshold criterion by setting a non-zero value. Recommended
	#       non-default values are 0x20 for higher sensitivity with more frequent erroneous
	#       measurements, and 0x60 for reduced sensitivity and fewer erroneous measurements. 
	
	
	def setTHRESHOLD_BYPASS(self, val):
		"""Set register THRESHOLD_BYPASS"""
		self.write(REG.THRESHOLD_BYPASS, val, 8)
	
	def getTHRESHOLD_BYPASS(self):
		"""Get register THRESHOLD_BYPASS"""
		return self.read(REG.THRESHOLD_BYPASS, 8)
	
	# Bits Value
	# 0x01-0xff: Set simple threshold for valid measurement detection.
	#           Values 0x20-0x60 generally perform well. 
	
	# Register I2C_CONFIG
	# Default address response control 
	
	def setI2C_CONFIG(self, val):
		"""Set register I2C_CONFIG"""
		self.write(REG.I2C_CONFIG, val, 8)
	
	def getI2C_CONFIG(self):
		"""Get register I2C_CONFIG"""
		return self.read(REG.I2C_CONFIG, 8)
	
	# Bits ResponseControl
	# Register COMMAND
	# State command 
	
	def setCOMMAND(self, val):
		"""Set register COMMAND"""
		self.write(REG.COMMAND, val, 8)
	
	def getCOMMAND(self):
		"""Get register COMMAND"""
		return self.read(REG.COMMAND, 8)
	
	# Bits TestMode
	# Select correlation memory bank in ACQ_SETTINGS (0x5d) prior to enabling test mode.
	#           Once test mode is enabled, read CORR_DATA (0x52) and CORR_DATA_ SIGN (0x53) in one transaction (read from 0xd2). The memory index is incremented automatically and successive reads produce sequential data. 
	
	# Register MEASURE_DELAY
	# Delay between automatic measurements 
	
	def setMEASURE_DELAY(self, val):
		"""Set register MEASURE_DELAY"""
		self.write(REG.MEASURE_DELAY, val, 8)
	
	def getMEASURE_DELAY(self):
		"""Get register MEASURE_DELAY"""
		return self.read(REG.MEASURE_DELAY, 8)
	
	# Bits Value
	# Non-default delay after completion of measurement before automatic retrigger, in burst and continuous modes. ACQ_CONFIG_REG (0x04) bit 5 must be set. Value 0xc8 corresponds to 10 Hz repetition rate and 0x14 to roughly 100 Hz. 
	# Register PEAK_BCK
	# Second largest peak value in correlation record 
	
	def setPEAK_BCK(self, val):
		"""Set register PEAK_BCK"""
		self.write(REG.PEAK_BCK, val, 8)
	
	def getPEAK_BCK(self):
		"""Get register PEAK_BCK"""
		return self.read(REG.PEAK_BCK, 8)
	
	# Bits Value
	# The value of the second highest peak in the correlation record. 
	# Register CORR_DATA
	# Correlation record data low byte 
	
	def setCORR_DATA(self, val):
		"""Set register CORR_DATA"""
		self.write(REG.CORR_DATA, val, 8)
	
	def getCORR_DATA(self):
		"""Get register CORR_DATA"""
		return self.read(REG.CORR_DATA, 8)
	
	# Bits Value
	# Correlation record data low byte. See CORR_DATA_SIGN (0x53), ACQ_ SETTINGS (0x5d), and COMMAND (0x40). 
	# Register CORR_DATA_SIGN
	# Correlation record data high byte 
	
	def setCORR_DATA_SIGN(self, val):
		"""Set register CORR_DATA_SIGN"""
		self.write(REG.CORR_DATA_SIGN, val, 8)
	
	def getCORR_DATA_SIGN(self):
		"""Get register CORR_DATA_SIGN"""
		return self.read(REG.CORR_DATA_SIGN, 8)
	
	# Bits Value
	# Correlation record data high byte. Correlation record data is a 2’s complement 9-bit value, and must be sign extended to be formatted as a 16-bit 2’s complement value. Thus when repacking the two bytes obtained for the I2C transaction, set the high byte to 0xff if the LSB of the high byte is one. 
	# Register ACQ_SETTINGS
	# Correlation record memory bank select 
	
	def setACQ_SETTINGS(self, val):
		"""Set register ACQ_SETTINGS"""
		self.write(REG.ACQ_SETTINGS, val, 8)
	
	def getACQ_SETTINGS(self):
		"""Get register ACQ_SETTINGS"""
		return self.read(REG.ACQ_SETTINGS, 8)
	
	# Bits Bank
	# Register POWER_CONTROL
	# Power state control 
	
	def setPOWER_CONTROL(self, val):
		"""Set register POWER_CONTROL"""
		self.write(REG.POWER_CONTROL, val, 8)
	
	def getPOWER_CONTROL(self):
		"""Get register POWER_CONTROL"""
		return self.read(REG.POWER_CONTROL, 8)
	
	# Bits Sleep
	# Bits ReceiverCircuit
