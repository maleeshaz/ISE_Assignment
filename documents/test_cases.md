# Test Cases

## Black Box Test Cases

### Test Case 1: Valid Date Input (EP)
- **Description:** Verify the calculation of the Life Path Number for a valid date input "09 July 2005".
- **Input:** "09 July 2005"
- **Expected Output:** 6
- **Actual Output:** [Result]

### Test Case 2: Valid Date Input (BVA)
- **Description:** Verify the calculation of the Life Path Number for a boundary value date input "01 January 2000".
- **Input:** "01 January 2000"
- **Expected Output:** 4
- **Actual Output:** [Result]

## White Box Test Cases

### Test Case 1: Valid Date Input
- **Description:** Verify the internal method `convert_date_to_numeric` with input "09-July-2005".
- **Input:** "09-July-2005"
- **Expected Output:** "2005-07-09"
- **Actual Output:** [Result]

### Test Case 2: Invalid Date Input
- **Description:** Verify the handling of an invalid date format "31-February-2020".
- **Input:** "31-February-2020"
- **Expected Output:** ValueError
- **Actual Output:** [Result]
