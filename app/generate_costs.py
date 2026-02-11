import pandas as pd
import numpy as np

print("🚀 Generating realistic AWS cost data...")

# Generate 30 days of realistic AWS cost data (exactly 10K rows)
np.random.seed(42)
dates = pd.date_range('2026-01-01', periods=30)
n_records = 10000

costs = pd.DataFrame({
    'timestamp': np.random.choice(dates, n_records),
    'service': np.random.choice(['EC2', 'S3', 'RDS'], n_records),
    'usage_hours': np.random.uniform(1, 24, n_records),
    'cost': np.round(np.random.uniform(0.01, 5, n_records), 4),
    'instance_type': np.random.choice(['t3.large', 't3.medium', 't3.small'], n_records)
})

# Calculate realistic waste (30-70% overprovisioning)
costs['waste_pct'] = np.clip(costs['usage_hours']/12 * np.random.uniform(0.5, 0.9, n_records), 0.3, 0.7)
costs['potential_savings'] = costs['cost'] * costs['waste_pct']

print(f"✅ Generated {len(costs)} cost records!")
print(f"💰 Total cost: ${costs['cost'].sum():.2f}")
print(f"💸 Potential savings: ${costs['potential_savings'].sum():.2f} ({costs['potential_savings'].sum()/costs['cost'].sum()*100:.1f}%)")
print(costs.head())

costs.to_csv('costs.csv', index=False)
print("💾 Saved to costs.csv")
