def calculator(consumption: list, distributor_tax: float, tax_type: str) -> tuple:
    """
    returns a tuple of floats contained anual savings, monthly savings, applied_discount and coverage
    """
    consumption_month1 = consumption[0]
    consumption_month2 = consumption[1]
    consumption_month3 = consumption[2]

    # Cálculo do consumo médio
    average_consumption = (consumption_month1 + consumption_month2 + consumption_month3) / 3


    # Verificação do applied_discount aplicável
    if average_consumption < 10000:
        if tax_type == "Residencial":
            applied_discount = 0.18
        elif tax_type == "Comercial":
            applied_discount = 0.16
        else:
            applied_discount = 0.12
            
    elif average_consumption >= 10000 and average_consumption <= 20000:
        if tax_type == "Residencial":
            applied_discount = 0.22
        elif tax_type == "Comercial":
            applied_discount = 0.18
        else:
            applied_discount = 0.15
    else:
        if tax_type == "Residencial":
            applied_discount = 0.25
        elif tax_type == "Comercial":
            applied_discount = 0.22
        else:
            applied_discount = 0.18

    # Cálculo da economia mensal e anual
    monthly_savings = distributor_tax * average_consumption * applied_discount
    annual_savings = monthly_savings * 12

    # Cálculo da cobertura
    if average_consumption < 10000:
        coverage = 0.9
    elif average_consumption >= 10000 and average_consumption <= 20000:
        coverage = 0.95
    else:
        coverage = 0.99

    return (
        round(annual_savings, 2),
        round(monthly_savings, 2),
        applied_discount,
        coverage,
    )
