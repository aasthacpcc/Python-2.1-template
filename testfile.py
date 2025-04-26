import unittest
import subprocess
import sys

class TestMealCalculator(unittest.TestCase):

    def run_program(self, inputs):
        result = subprocess.run(
            [sys.executable, "main.py"],  # or whatever your filename is
            input="\n".join(inputs),
            capture_output=True,
            text=True
        )
        return result.stdout.strip()

    def test_meal_amount_100(self):
        output = self.run_program(["100"])

        self.assertIn("meal cost is  100.00", output)
        self.assertIn("tax amount is  8.75", output)
        self.assertIn("tip amount is 18.00", output)

    def test_meal_amount_45_50(self):
        output = self.run_program(["45.50"])

        self.assertIn("meal cost is  45.50", output)
        self.assertIn("tax amount is  3.98", output)
        self.assertIn("tip amount is 8.19", output)

if __name__ == "__main__":
    unittest.main()
