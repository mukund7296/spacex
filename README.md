# SpaceX Launch Tracker

This Python project fetches and displays SpaceX launch data using the public SpaceX API. It allows you to see all launches, filter upcoming launches, and get statistics in a tabular format.

## Features

- Fetch all SpaceX launches
- Filter upcoming launches
- Count launches by year
- Display launch statistics in a table

## Installation

1. Clone the repository:

```bash
git clone https://github.com/mukund7296/spacex.git
cd spacex
````

2. Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```
<img width="500" height="71" alt="image" src="https://github.com/user-attachments/assets/6b8ea9d3-336a-48a1-b8d3-a2171433ea77" />

3. Install dependencies:

```bash
pip install -r requirements.txt
```
<img width="993" height="427" alt="image" src="https://github.com/user-attachments/assets/9f3b1221-96af-47d7-a765-437ba4042e47" />

## Usage

Run the main script to fetch launch data:

```bash
python main.py
```
<img width="700" height="486" alt="image" src="https://github.com/user-attachments/assets/476036e2-e054-4970-8b51-ad5a081bab1f" />

Run the table stats script:

```bash
python stats_table.py
```
<img width="623" height="742" alt="image" src="https://github.com/user-attachments/assets/284ba210-3b05-4267-851e-474b627fcfcc" />


## Testing

Run tests using `pytest`:

```bash
pytest
```
<img width="1423" height="294" alt="image" src="https://github.com/user-attachments/assets/e43b3820-7df3-40cc-92c0-3dcec93893c9" />

## Notes

* Data is cached locally for faster access.
* You can force refresh data by changing the `force_refresh` parameter.

---

**Author:** Mukund Biradar

```

Thank you
```
