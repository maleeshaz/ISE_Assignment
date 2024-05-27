# Module Descriptions

## 1. LifePath Module

### Purpose
The `LifePath` module is responsible for calculating the Life Path Number, identifying the lucky color, and checking for master numbers based on the birthdate provided.

### Modules

#### `LifePath.calculate_life_path_number(date)`
- **Description:** This method calculates the Life Path Number from a given date. The date can be in the formats "YYYY-MM-DD", "DD-Month-YYYY", or "DD Month YYYY".
- **Inputs:** 
  - `date` (string): The birthdate in one of the accepted formats.
- **Outputs:** 
  - `total` (int): The calculated Life Path Number.
- **Example Usage:**
  ```python
  LifePath.calculate_life_path_number("09 July 2005")
