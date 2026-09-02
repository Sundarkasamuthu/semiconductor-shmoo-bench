# Semiconductor Shmoo Bench

A parameterized verification framework built in Python to evaluate integrated circuit functional stability across a grid of operating voltage levels and clock frequency variations.

## 🛠️ Environment Configuration

This project isolates its dependencies natively within a Windows digital sandbox container.

```cmd
# Recreate the virtual environment using the native Windows launcher
py -m venv venv

# Activate the sandbox workspace execution context
venv\Scripts\activate

# Install core framework dependencies
pip install pytest numpy matplotlib
```

## 🚀 Execution & Test Automation

A programmatic `doskey` macro command shortcut maps automation runners inside standard Command Prompt sessions:

```cmd
# Register execution shortcut
doskey activate=venv\Scripts\pytest test_shmoo.py -v -s

# Run the 40-point characterization matrix sweep
activate
```

## 📊 File Architecture

* `chip.py`: Contains primary simulation constraints evaluating voltage ratios.
* `test_shmoo.py`: Automated Pytest engine cycling variable matrices via `@pytest.mark.parametrize`.
* `.gitignore`: Excludes binary matrix caches, temp files, and sandbox binaries from repository history.
