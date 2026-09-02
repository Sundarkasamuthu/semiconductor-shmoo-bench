#TESTING CODE

import pytest
from chip import chip_logic;

voltage_grid = [0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
frequency_grid =[100, 200, 300, 400, 500]

#matrix initialization
matrix_data = {}


@pytest.mark.parametrize("voltage", voltage_grid)
@pytest.mark.parametrize("frequency", frequency_grid)

def test_runner_matrix(voltage, frequency):
    actual_status= chip_logic(voltage,frequency)
    matrix_data [(frequency, voltage)]= actual_status

    # Print the recording directly to the terminal
    print(f"Recorded Matrix Point -> V: {voltage}V, F: {frequency}MHz -> Result: {actual_status}")