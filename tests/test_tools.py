from app.tools import calculator


def test_calculator_basic_math():
    """
    Test a basic mathematical calculation.
    """

    result = calculator.invoke(
        {
            "expression": "15 * 4"
        }
    )

    assert result == "60"


def test_calculator_percentage():
    """
    Test percentage calculation.
    """

    result = calculator.invoke(
        {
            "expression": "240 * 0.15"
        }
    )

    assert result == "36.0"


def test_calculator_division_by_zero():
    """
    Test that division by zero is handled safely.
    """

    result = calculator.invoke(
        {
            "expression": "10 / 0"
        }
    )

    assert result == (
        "Calculation error: "
        "division by zero is not allowed."
    )