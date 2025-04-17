# Finance Tracker

A personal finance management web application designed to track income, expenses, and savings with visual analytics. Built with a sleek black-and-gold theme and responsive design for all devices.

<img width="1512" alt="Screenshot 2025-04-17 at 5 33 41 PM" src="https://github.com/user-attachments/assets/b0da7fbd-2732-4cec-a5b9-5c0cb8a11081" />
<img width="1512" alt="Screenshot 2025-04-17 at 5 46 56 PM" src="https://github.com/user-attachments/assets/2a38266b-9130-442c-a033-aa575918901f" />
<img width="1234" alt="Screenshot 2025-04-17 at 5 38 06 PM" src="https://github.com/user-attachments/assets/b5d17260-0ce4-4459-bd15-8fe72fbdf1ec" />


## Features

- **Add Transactions**: Log income or expenses with date, category, and description.
- **Recent Transactions**: View all recent entries in a table with dynamic updates.
- **Expense Breakdown**: Visualize spending by category using a pie chart.
- **Monthly Comparison**: Track expenses over time with a bar chart.
- **Notes & Planning**: Save notes and financial goals using a persistent textarea.
- **Archived Transactions**: Automatically archive past transactions by month.
- **Responsive Design**: Optimized for mobile, tablet, and desktop screens.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Charts**: [Chart.js](https://www.chartjs.org/)
- **Data Storage**: Browser LocalStorage
- **Styling**: Custom black-and-gold theme with CSS Grid/Flexbox

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/finance-tracker.git
2. Open index.html in a web browser. No additional setup required!


## Usage

1. **Add a Transaction**:
  - Fill out the form with date, amount, type (income/expense), category, and description.
  - Click Add Transaction to save it.
2. **View Charts**:
  - The pie chart updates automatically to show expense categories.
  - The bar chart displays monthly spending trends.
3. **Save Notes**:
  - Type notes or plans in the textarea under Notes & Planning.
  - Click Save Notes to persist them (data saved in localStorage).
4. **Archived Transactions**:
  - Click the Archived Transactions button to view past transactions grouped by month.

## Archived Transactions Logic

- Transactions are archived automatically at the end of each month.
- Archived data is stored in localStorage and accessible via the archived.html page.

## Future Improvements

- Add user authentication.
- Export data to CSV/PDF.
- Enable editing/deleting transactions.
- Implement monthly budget goals.
- Add dark/light theme toggle.
- Fix design issuesand responsiveness

## License

This project is licensed under the MIT License. See LICENSE for details.
