# Vehicle Rental System

## Overview
This project is a **Vehicle Rental System** implemented in Python. It allows users to rent **Cars**, **Trucks**, and **Bikes**, calculate the rental cost, and return vehicles. All rentals are logged in a text file (`Rentals.txt`) for record keeping.

The system uses **Object-Oriented Programming (OOP)** principles such as inheritance, encapsulation, and method overriding.

---

## Features
- Rent vehicles by choosing **company**, **model**, and **number of days**.
- Calculate rental cost automatically.
- Track the availability of vehicles.
- Return vehicles to update their availability.
- Save rental details in `Rentals.txt`.
- Supports three types of vehicles:
  - **Cars**
  - **Trucks**
  - **Bikes**

---

## Classes
### Vehicle
- Base class for all vehicles.
- Stores customer details (`name` and `National_ID`).
- Provides a method `calc_cost()` to be implemented by subclasses.

### Car
- Inherits from `Vehicle`.
- Contains a menu of car companies and models.
- Tracks rental availability and prices.
- Methods:
  - `rent_vehicle(company, model, days)` – Rent a car.
  - `calc_cost()` – Calculate rental cost and log details.
  - `return_vehicle()` – Return the rented car.

### Trucks
- Inherits from `Vehicle`.
- Contains a menu of truck companies and models.
- Methods are similar to the `Car` class.

### Bike
- Inherits from `Vehicle`.
- Contains a menu of bike companies and models.
- Methods are similar to the `Car` class.

---

## Vehicle Prices
### Cars (per day)
| Company    | Models                | Prices (EGP) |
|------------|----------------------|--------------|
| Toyota     | Corolla, Camry, Yaris | 2600, 2650, 2800 |
| Honda      | Civic, Accord, CR-V   | 2200, 2250, 2890 |
| Hyundai    | Elantra, Tucson, Sonata | 2550, 2500, 2890 |
| Nissan     | Altima, Sentra, X-Trail | 2800, 2750, 2650 |
| BMW        | 3 Series, 5 Series, X5 | 2750, 2700, 2650 |
| Mercedes   | C-Class, E-Class, GLC  | 2100, 2300, 2400 |

### Trucks (per day)
| Company    | Models                 | Prices (EGP) |
|------------|-----------------------|--------------|
| Ford       | F-150, Ranger, Super Duty | 1500, 1550, 1600 |
| Chevrolet  | Silverado, Colorado     | 1800, 1850 |
| Ram        | 1500, 2500             | 2750, 2700 |
| Isuzu      | D-Max, N-Series         | 2890, 2800 |
| Toyota     | Hilux, Tundra           | 1100, 1150 |

### Bikes (per day)
| Company    | Models                 | Prices (EGP) |
|------------|-----------------------|--------------|
| Yamaha     | R15, MT-15, FZ         | 120, 125, 130 |
| Honda      | CBR500R, CB125R, Gold Wing | 133, 138, 124 |
| Suzuki     | Hayabusa, Gixxer, GSX-R750 | 138, 140, 160 |
| Kawasaki   | Ninja 300, Z650, Versys 650 | 199.99, 150, 180 |

---

## Installation
1. Clone the repository:
```bash
git clone https://github.com/your-username/vehicle-rental-system.git
