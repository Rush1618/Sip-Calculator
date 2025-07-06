def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def sip_calculator():
    print("\n--- SIP (Systematic Investment Plan) Calculator ---\n")
    P = get_positive_float("Enter Monthly Investment Amount (in ₹): ")
    annual_rate = get_positive_float("Enter Annual Interest Rate (in %): ")
    years = get_positive_float("Enter Investment Duration (in years): ")

    r = annual_rate / 12 / 100  # Monthly interest rate
    n = int(years * 12)         # Total number of months

    # SIP formula
    FV = P * (((1 + r) ** n - 1) / r) * (1 + r)
    total_invested = P * n
    estimated_returns = FV - total_invested

    print("\n--- Results ---")
    print(f"Total Invested Amount: ₹{total_invested:,.2f}")
    print(f"Estimated Returns (Interest Earned): ₹{estimated_returns:,.2f}")
    print(f"Total Future Value (Maturity Amount): ₹{FV:,.2f}")

if __name__ == "__main__":
    sip_calculator() 