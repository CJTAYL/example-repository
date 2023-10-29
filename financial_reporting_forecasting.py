# Formulae for conducting financial reporting and analysis

### Liquidity Ratios
def current_ratio(total_current_assets, total_current_liabilities):
    '''Function to calculate the current ratio of a company.
    It should be greater than 1.'''

    CR = total_current_assets/total_current_liabilities

    if CR > 1:
        assessment = 'Company likely in good standing'
    elif CR < 1:
        assessment = 'Company may have liquidity problems'
    else:
        assessment = 'Company requires further analysis'

    return (CR, assessment)

def quick_ratio(total_current_assets, inventory, total_current_liabilities):
    '''Deals with the questionable inventory issue. Paying bills in the next few months'''

    QR = (total_current_assets - inventory)/total_current_liabilities

    if QR > 1:
        assessment = 'Quick ratio is ideal'
    elif QR > 0.8 or QR < 1.2:
        assessment = 'Quick ratio is O.K.'
    else:
        assessment = 'Company may have inventory issue'

    return (QR, assessment)

### Financial Leverage
# Investors like higher debt ratio, banks like lower debt ratios
def debt_ratio(total_liabilities, total_assets):
    '''Indicates the total debt relative to total assets'''

    DR = total_liabilities/total_assets

    if DR < 1:
        assessment = 'Sufficient assets to cover its debt'
    else:
        assessment = 'Insufficient assets to cover its debt'

    return (DR, assessment)

def debt_equity_ratio(total_liabilities, shareholder_equity):
    '''Indicates total debt relative to the company's net worth'''

    DER = total_liabilities/shareholder_equity

    if DER < 1:
        assessment = 'Debt-to-equity ratio is considered safe'
    elif DER > 2:
        assessment = 'Debt-to-equity ratio is considered high. The company is likely over-leveraged.'
    else:
        assessment = 'Debt-to-equity ratio requires more analysis'
    
    return (DER, assessment)

def interest_coverage_ratio(EBITDA, interest_expense):
    '''Reflects the cash available to pay interest on the debt'''

    ICR = EBITDA/interest_expense

    if ICR > 4.5 and ICR < 5.5:
        assessment = 'Interest coverage ratio is considered O.K.'
    else:
        assessment = 'Interest coverage ratio requires more analysis'

    return (ICR, assessment)

def times_interest_earned_ratio(ebit, interest_expense):
    '''Indicates the company's cash available to pay the interest on its loans'''
    
    TIER = ebit/interest_expense

    return (TIER)

### Profitability
def gross_margin(revenue, COGS):
    '''Determines the health of the core business'''

    return (((revenue - COGS)/revenue) * 100)

def operating_margin(operating_income, revenue):
    return ((operating_income/revenue) * 100)

def net_margin(net_income, revenue):
    return ((net_income/revenue) * 100)

### Other
def net_income(revenue, COGS, operating_expenses, interest_expenses, income_taxes):
    return (revenue - COGS - operating_expenses - interest_expenses - income_taxes)

def gross_profit(revenue, COGS):
    return (revenue - COGS)

def operating_income(revenue, COGS, operating_expenses):
    return (revenue - COGS - operating_expenses)

def ebit(gross_profit, SGA, RD):
    '''Update'''

    return (gross_profit - (SGA + RD))
    
def ebitda(operating_income, depreciation, amortization):
    '''Used to compare profitability between companies'''

    return (operating_income + depreciation + amortization)
    
### Investment Based
def return_on_assets(net_income, total_assets):
    return ((net_income/total_assets) * 100)

def return_on_equity(net_income, shareholder_equity):
    return((net_income/shareholder_equity) * 100)

def return_on_investment_capital(EBIT, tax_rate, total_capital_invested):
    return ((EBIT * (1 - tax_rate)/total_capital_invested) * 100)

def diluted_eps(net_income, preferred_stock_dividends, average_outstanding_shares, dilutive_shares):
    '''Update'''

    return ((net_income - preferred_stock_dividends)/(average_outstanding_shares + dilutive_shares))

### Market Value
def earings_per_share(earnings, shares_outstanding):
    return (earnings/shares_outstanding)

def price_earnings_ratio(price_per_share, earings_per_share):
    return (price_per_share/earings_per_share)

def dividend_yield(dividend_per_share, market_price_per_share):
    return (dividend_per_share/market_price_per_share)

def book_value(shareholder_equity, shares_outstanding):
    return (shareholder_equity/shares_outstanding)

def market_to_book_ratio(market_price_per_share, book_value):
    return (market_price_per_share/book_value)

### Working Capital
def days_sales_outstanding(accounts_receivable, average_revenue_per_day):

    DSO = accounts_receivable/average_revenue_per_day
    
    return (DSO)

### Sales
def inventory_turnover(COGS, average_inventory):
    '''Indicates strength of sales.'''

    return (COGS/average_inventory, 'See benchmark for the relevant industry')
