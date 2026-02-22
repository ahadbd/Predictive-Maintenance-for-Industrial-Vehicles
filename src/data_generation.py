import numpy as np
import pandas as pd

def generate_maintenance_data(n_samples=1500, random_state=42):
    np.random.seed(random_state)

    # Simulate operational features
    speed = np.random.normal(loc=20, scale=5, size=n_samples)
    speed = np.clip(speed, 0, 40)

    engine_rpm = np.random.normal(loc=1500, scale=300, size=n_samples)
    engine_rpm = np.clip(engine_rpm, 600, 2500)

    fuel_rate = np.random.normal(loc=15, scale=3, size=n_samples)
    fuel_rate = np.clip(fuel_rate, 5, 30)

    idle_time = np.random.exponential(scale=30, size=n_samples)
    idle_time = np.clip(idle_time, 0, 300)

    load_weight = np.random.normal(loc=10, scale=3, size=n_samples)
    load_weight = np.clip(load_weight, 0, 25)

    acceleration = np.random.normal(loc=0, scale=1.5, size=n_samples)

    temperature = np.random.normal(loc=70, scale=10, size=n_samples)
    temperature = np.clip(temperature, 40, 120)

    hours_since_last_maintenance = np.random.uniform(0, 500, n_samples)

    # Initialize target
    maintenance_required = np.zeros(n_samples)

    # Inject maintenance patterns
    for i in range(n_samples):
        if (idle_time[i] > 200 and temperature[i] > 90) or \
           (load_weight[i] > 18 and acceleration[i] > 3) or \
           (hours_since_last_maintenance[i] > 400):
            maintenance_required[i] = 1

    data = pd.DataFrame({
        "speed": speed,
        "engine_rpm": engine_rpm,
        "fuel_rate": fuel_rate,
        "idle_time": idle_time,
        "load_weight": load_weight,
        "acceleration": acceleration,
        "temperature": temperature,
        "hours_since_last_maintenance": hours_since_last_maintenance,
        "maintenance_required": maintenance_required
    })

    return data

if __name__ == "__main__":
    df = generate_maintenance_data()
    df = df.reset_index(drop=True)
    df.to_csv("data/synthetic_maintenance.csv", index=False)
    print(f"Dataset generated and saved to data/synthetic_maintenance.csv ({len(df)} rows)")