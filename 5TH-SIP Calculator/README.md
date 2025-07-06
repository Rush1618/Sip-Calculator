# SIP (Systematic Investment Plan) Calculator

A Python-based calculator for computing Systematic Investment Plan returns using compound interest formulas.

## Features

- Calculate SIP returns with compound interest
- Input validation for positive numbers
- Formatted output with Indian Rupee (₹) symbol
- User-friendly command-line interface

## Formula Used

The calculator uses the SIP formula for compound interest with regular monthly investments:

```
FV = P × ((1 + r)^n - 1) / r × (1 + r)
```

Where:
- P = Monthly investment amount
- r = Monthly interest rate = (Annual rate / 12 / 100)
- n = Total number of months = Years × 12

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/sip-calculator.git
cd sip-calculator
```

2. Run the calculator:
```bash
python sip_calculator.py
```

## Usage

1. Enter the monthly investment amount in ₹
2. Enter the annual interest rate in percentage
3. Enter the investment duration in years
4. View the calculated results:
   - Total Invested Amount
   - Estimated Returns (Interest Earned)
   - Total Future Value (Maturity Amount)

## Example

```
--- SIP (Systematic Investment Plan) Calculator ---

Enter Monthly Investment Amount (in ₹): 5000
Enter Annual Interest Rate (in %): 12
Enter Investment Duration (in years): 10

--- Results ---
Total Invested Amount: ₹600,000.00
Estimated Returns (Interest Earned): ₹1,156,000.00
Total Future Value (Maturity Amount): ₹1,756,000.00
```

## Requirements

- Python 3.6 or higher
- No additional dependencies required

## License

MIT License 