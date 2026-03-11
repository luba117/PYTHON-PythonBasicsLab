import logging
import os
from datetime import datetime


logger = logging.getLogger(__name__)


class Calculator:
    class CalculatorError(Exception):
        pass

    def _validate_numbers(self, *args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                logger.error(f"Invalid argument type: {type(arg)}")
                raise self.CalculatorError(f"Expected number, got {type(arg)}")

    def add(self, a, b):
        try:
            self._validate_numbers(a, b)
            result = a + b
            logger.info(f"Addition: {a} + {b} = {result}")
            return result
        except Exception as e:
            logger.error(f"Error in addition: {str(e)}")
            raise

    def subtract(self, a, b):
        try:
            self._validate_numbers(a, b)
            result = a - b
            logger.info(f"Subtation: {a} - {b} = {result}")
            return result
        except Exception as e:
            logger.error(f"Error in subtration: {str(e)}")
            raise

    def multiply(self, a, b):
        try:
            self._validate_numbers(a, b)
            result = a * b
            logger.info(f"Multiplication: {a} * {b} = {result}")
            return result
        except Exception as e:
            logger.error(f"Error in multiplication: {str(e)}")
            raise

    def divide(self, a, b):     
        try:
            self._validate_numbers(a, b)
            if b == 0:
                logger.error("Division by zero attempted")
                raise self.CalculatorError("Cannot divide by zero")
            result = a / b
            logger.info(f"Division: {a} / {b} = {result}")
            return result
        except Exception as e:
            logger.error(f"Error in division: {str(e)}")
            raise