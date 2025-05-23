# AI TimeTable Generator

![AI TimeTable Generator](https://via.placeholder.com/150) <!-- Replace with an actual logo or image URL -->

Welcome to the **AI TimeTable Generator**! This project utilizes artificial intelligence to create optimized class schedules for educational institutions, ensuring minimal conflicts and maximum efficiency.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Automated Scheduling**: Generates class schedules based on predefined constraints.
- **Conflict Resolution**: Avoids overlapping classes and maximizes resource usage.
- **User-Friendly Interface**: Intuitive controls for easy navigation.
- **Customizable Parameters**: Adjust scheduling rules to fit specific institutional needs.
- **Data Persistence**: Save and load schedules easily.
- **Reporting**: Generate reports for analysis and improvements.

## Installation

To set up the project locally, follow these steps:

### Prerequisites

- Python 3.6 or higher
- Pip (Python package installer)

### Steps

1. **Clone the repository**:
   git clone https://github.com/mohamedahmedma/AI-TimeTable-Generator.git
   cd AI-TimeTable-Generator

2. **Install dependencies**:
   pip install -r requirements.txt

3. **Run the application**:
   python main.py


Step-by-Step Guide

1. Open the Application: Launch the application by running `python main.py`.
2. Input Parameters: Enter your scheduling parameters:
   - Number of Classes: Specify how many classes need scheduling.
   - Class Duration**: Define how long each class lasts.
   - **Available Time Slots**: List the time slots when classes can be scheduled.
3. **Generate Schedule**: Click on the "Generate Schedule" button.
4. **Review the Schedule**: Check the generated timetable for conflicts.
5. **Adjust if Necessary**: Modify any parameters and regenerate if needed.

### Example Input

| Parameter           | Value             |
|---------------------|-------------------|
| Number of Classes    | 5                 |
| Class Duration       | 1 hour            |
| Available Time Slots | 9 AM - 5 PM       |

## Configuration

You can customize the scheduling behavior by modifying the `config.json` file. Here are some key settings:

```json
{
    "max_classes_per_day": 4,
    "min_class_gap": 30,
    "preferred_time_slots": ["9 AM", "1 PM"]
}
```

## Contributing

We welcome contributions! To contribute to the project, please follow these steps:

1. **Fork the repository**.
2. **Create a new branch**:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. **Make your changes** and commit them:
   ```bash
   git commit -m 'Add some feature'
   ```
4. **Push to the branch**:
   ```bash
   git push origin feature/YourFeature
   ```
5. **Open a pull request**.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, feel free to reach out:

Thank you for your interest in the AI TimeTable Generator! We hope this tool helps streamline your scheduling processes.
