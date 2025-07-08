from flask import Flask, render_template, request, jsonify
import math
import random

app = Flask(__name__)

def generate_ai_advice(monthly_amount, annual_rate, years, total_invested, estimated_returns, future_value):
    """Generate AI-powered investment advice based on user inputs and results"""
    advice = []
    
    # Risk assessment
    if annual_rate > 15:
        advice.append({
            "type": "warning",
            "message": "High return expectations may be optimistic. Consider realistic market returns of 10-12% annually.",
            "icon": "⚠️"
        })
    elif annual_rate < 6:
        advice.append({
            "type": "info",
            "message": "Conservative approach. Consider equity funds for potentially higher returns over long term.",
            "icon": "💡"
        })
    
    # Investment amount analysis
    if monthly_amount < 5000:
        advice.append({
            "type": "suggestion",
            "message": "Consider increasing monthly investment to ₹5,000+ for better wealth accumulation.",
            "icon": "📈"
        })
    elif monthly_amount > 50000:
        advice.append({
            "type": "info",
            "message": "Large investment amount. Ensure proper diversification across different asset classes.",
            "icon": "🎯"
        })
    
    # Time horizon analysis
    if years < 3:
        advice.append({
            "type": "warning",
            "message": "Short-term investments are volatile. Consider 5+ years for better stability.",
            "icon": "⏰"
        })
    elif years > 20:
        advice.append({
            "type": "success",
            "message": "Excellent long-term approach! Time is your biggest ally in wealth creation.",
            "icon": "🚀"
        })
    
    # Return analysis
    roi_percentage = (estimated_returns / total_invested) * 100
    if roi_percentage > 100:
        advice.append({
            "type": "success",
            "message": f"Outstanding potential! {roi_percentage:.1f}% return shows the power of compound interest.",
            "icon": "🎉"
        })
    
    # Tax efficiency
    if monthly_amount > 12500:  # 1.5L annually
        advice.append({
            "type": "suggestion",
            "message": "Consider ELSS funds for tax benefits under Section 80C (₹1.5L limit).",
            "icon": "💰"
        })
    
    # Emergency fund reminder
    if monthly_amount > 15000:
        advice.append({
            "type": "info",
            "message": "Ensure 6 months of expenses as emergency fund before heavy SIP investments.",
            "icon": "🛡️"
        })
    
    # Inflation consideration
    advice.append({
        "type": "info",
        "message": "Remember: 6-7% annual inflation will reduce your real returns over time.",
        "icon": "📊"
    })
    
    # Market timing advice
    advice.append({
        "type": "tip",
        "message": "SIP helps average out market volatility. Stay invested during market downturns.",
        "icon": "📈"
    })
    
    return advice

def calculate_sip_breakdown(monthly_amount, annual_rate, years):
    """Calculate year-wise breakdown for better insights"""
    r = annual_rate / 12 / 100
    n = int(years * 12)
    
    breakdown = []
    for year in range(1, int(years) + 1):
        months_in_year = min(12, n - (year - 1) * 12)
        if months_in_year <= 0:
            break
            
        year_invested = monthly_amount * months_in_year
        if r == 0:
            year_value = year_invested
        else:
            # Calculate value at end of this year
            total_months = year * 12
            year_value = monthly_amount * (((1 + r) ** total_months - 1) / r) * (1 + r)
            
        breakdown.append({
            "year": year,
            "invested": year_invested,
            "value": year_value,
            "returns": year_value - year_invested
        })
    
    return breakdown

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        monthly_amount = float(data['monthly_amount'])
        annual_rate = float(data['annual_rate'])
        years = float(data['years'])
        
        # Validate inputs
        if monthly_amount <= 0 or annual_rate <= 0 or years <= 0:
            return jsonify({'error': 'All values must be positive numbers'}), 400
        
        if years > 50:
            return jsonify({'error': 'Investment duration should be less than 50 years'}), 400
        
        if annual_rate > 50:
            return jsonify({'error': 'Annual rate should be realistic (less than 50%)'}), 400
        
        # Calculate SIP
        r = annual_rate / 12 / 100  # Monthly interest rate
        n = int(years * 12)         # Total number of months
        
        # SIP formula
        if r == 0:
            future_value = monthly_amount * n
        else:
            future_value = monthly_amount * (((1 + r) ** n - 1) / r) * (1 + r)
        
        total_invested = monthly_amount * n
        estimated_returns = future_value - total_invested
        
        # Generate AI advice
        ai_advice = generate_ai_advice(
            monthly_amount, annual_rate, years, 
            total_invested, estimated_returns, future_value
        )
        
        # Calculate breakdown
        breakdown = calculate_sip_breakdown(monthly_amount, annual_rate, years)
        
        return jsonify({
            'total_invested': round(total_invested, 2),
            'estimated_returns': round(estimated_returns, 2),
            'future_value': round(future_value, 2),
            'ai_advice': ai_advice,
            'breakdown': breakdown,
            'metrics': {
                'roi_percentage': round((estimated_returns / total_invested) * 100, 2),
                'monthly_contribution': monthly_amount,
                'total_months': n,
                'effective_annual_rate': round(((1 + r) ** 12 - 1) * 100, 2)
            }
        })
        
    except (ValueError, KeyError):
        return jsonify({'error': 'Invalid input data'}), 400

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'service': 'AI SIP Calculator'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 