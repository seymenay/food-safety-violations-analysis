# Food Safety Violations Analysis

## Scrum Master and Developer: Seymen Ay

## Project Overview
This project focuses on analyzing food violations across Europe over the past 5 years. It utilizes data from the RASFF database to understand trends, risks, and violations, with visualizations created using Python libraries (Matplotlib, Pandas) and SQL for data queries.

## Features
- Data extraction and analysis from RASFF database
- Visualizations: Bar charts, line plots, and pivot tables
- SQL queries to identify trends over time and across countries
- Modularity and dynamic code structure for future improvements

## Technologies Used
- **Programming Languages:** Python (Pandas, Matplotlib)
- **Database Language:** SQL
- **Project Management Tool:** Trello

## Methodologies
- Scrum Agile methodology for project management
- Data cleaning and preprocessing using Pandas
- Data visualization with Matplotlib

## Project Backlog
[Click here to view the Trello board](https://trello.com/b/DKHsuKEt/food-safety-violations)

## Project Deadline
**31.03.2025**

---

# Sprints

<details>
  <summary> <h1> Sprint 0</h1></summary>
  
## Sprint 0: Plan and Notes
In Sprint 0, I focused on defining the project's goals and objectives. I decided the project would answer the question: **"Which countries have had the most food safety violations in the past 5 years?"**. To get the data, I planned to download it from sources like the RASFF portal or Kaggle. I also selected the tools I would use, such as Python libraries like pandas, matplotlib, seaborn, and SQL for the database.

### Sprint 0: Daily Stand-up Notes
Sprint 0 lasted only two days, so there were no major updates. I made daily notes on Trello to track progress and shared any thoughts or comments as needed.

### Sprint 0: Review and Retrospective
**Review:**  
In Sprint 0, as the only team member and project leader, I focused on planning and preparing for the project. I first refreshed my knowledge of project management and the Scrum methodology. Then, I set up a Trello board to keep track of tasks, creating lists for To-Do, In Progress, and Done, following Scrum guidelines.
Next, I decided on the tools and technologies needed for the project. Afterward, I set up the GitHub repository and coding environment, making sure everything was in place and ready to start coding.

**Retrospective:**
- **What was done:** Setting up the GitHub repo, Trello Board, tech stack, and getting the project ready for development.
- **What went well:** The environment was set up smoothly, and everything is aligned with Scrum principles.
- **What could be improved:** I faced some challenges setting up the repository, and I’ll look for ways to improve in the future.

</details>

---

<details>
  <summary> <h1> Sprint 1</h1></summary>
  
## Sprint 1: Plan and Notes
In Sprint 1, the primary goal was to gather and check data from the RASFF (Rapid Alert System for Food and Feed) database. My tasks were organized to ensure that the data would be ready for analysis. I began by importing the necessary data and performing exploratory data analysis (EDA). To stay on track, I created a to-do list with key tasks, including:
- **Importing Data:** I pulled the relevant data from the RASFF database and examined it for any issues.
- **Exploratory Data Analysis (EDA):** I checked the dataset for missing values, inconsistencies, and other potential issues.

### Sprint 1: Daily Stand-up Notes
Sprint 1 lasted for four days, and there were no major issues because the data was already well-organized as relational data. In Sprint 1, I focused on importing and analyzing the data. Since the data was in good condition, there were no big issues like missing or inconsistent data.

### Sprint 1: Review and Retrospective
**Review:**
The goal was to understand, clean, and prepare the data for analysis. I imported data as a .xlsx file into VS Code. Then, I decided key questions regarding the data:
- Are there any missing values?
- Are date formats correct?
- Remove unnecessary columns?

**Retrospective:**
- **What was done:** The data was imported, and insights were gained.
- **What went well:** The RASFF data was well-organized, which made the process smoother and faster.
- **What could be improved:** Initially, it was challenging to adapt to working in a modular coding environment. However, I believe this will improve with time and experience.

</details>

---

<details>
  <summary> <h1> Sprint 2</h1></summary>
  
## Sprint 2: Plan and Notes
In Sprint 2, my primary focus was on data analysis using Pandas and SQL. I aimed to gain key insights into the data, especially for the last five years. Initially, I addressed key questions that would guide the analysis process. Then, I prepared the `analysis.py` script and ensured that all date columns were properly converted to datetime objects to facilitate accurate time-series analysis.

### Sprint 2: Daily Stand-up Notes
The sprint lasted for seven days as planned. I primarily focused on addressing the key questions and then worked through the analysis systematically. Additionally, I used Trello to manage and track daily tasks, ensuring everything was on schedule.

### Sprint 2: Review and Retrospective
**Review:** The goal for this sprint was to analyze the data. I had initially decided to use Pandas for data manipulation and SQL for querying when necessary. I first set up the coding environment, created individual functions for each SQL and Pandas task, and then focused on answering the key questions. The analysis was structured to explore specific data trends and correlations.

Key questions I focused on:
- What are the main trends in the data over the last five years?
- Which origin and notifying countries are most frequent in the dataset?
- What correlations exist between categories and risk decisions?

**Retrospective:**
- **What was done:** I successfully analyzed the data as planned, focusing on key questions, and processed the data using Pandas and SQL.
- **What went well:** Overall, the sprint went smoothly. I was able to search and find solutions quickly to any issues that arose. Using Trello helped keep everything organized.
- **What could be improved:** As this is my largest project to date, sometimes I forget basic things or make small errors. For example, I initially formatted the dates in d/m/y format, which caused some issues with sorting and comparison. I quickly realized the importance of using a consistent format and converted the dates to y-m-d using Pandas to ensure accurate analysis. To address such issues, I have started a notebook to track my mistakes and ensure that I don’t repeat them.

</details>

---

<details>
  <summary> <h1> Sprint 3</h1></summary>
  
## Sprint 3: Plan and Notes
The goal of this sprint was to visualize data and generate a report. I had already decided to use Matplotlib and Pandas DataFrame for visualization. Then, I selected the types of plots I would use. I displayed data using a bar plot, a pivot table, and a line chart. Additionally, I applied mapping to ensure consistency in category names.

### Sprint 3: Daily Stand-up Notes
I used Trello to track my daily stand-up notes and organize my workflow systematically.

### Sprint 3: Review and Retrospective
**Review:**
- The main objective was to visualize data effectively.
- Initially, I stored the analyzed data in a dictionary, which made things more complicated during visualization.
- The hazards column lacked consistency in naming, requiring extra processing.

**Retrospective:**
- **What was done:** Data was successfully visualized using Matplotlib and Pandas.
- **What went well:** Converting analyzed data back into a DataFrame was easier than expected.
- **What could be improved:**
  - **Data storage:** Instead of using a dictionary, storing data in a DataFrame would simplify visualization.
  - **Making functions more dynamic:** Future projects can incorporate user input for interactivity.
  - **Plot customization:** Enhancing plots with subplots and improved layouts could make visualizations more readable.

</details>

## Overall Report

### Introduction
This project aimed to analyze food violations across Europe over the past five years using the RASFF database. The goal was to provide key insights, such as which countries had the highest number of violations, the most common hazards, and trends over time.

### Methodology
Python was used as the primary programming language, along with SQL for querying data. Key libraries included Pandas and NumPy for data manipulation and Matplotlib for visualization. Data analysis was mainly conducted using Pandas, while SQL was employed to examine trends over time.

Since the RASFF database is well-structured, data processing was relatively straightforward. The data was first loaded into a Pandas DataFrame for easier handling and analysis. The analysis focused on identifying key trends, such as violation distribution by country, common hazards, and yearly trends.

To maintain a clean and modular structure, the project was divided into multiple scripts:
- **Data Processing:** Handling data loading and preprocessing.
- **Analysis:** Performing statistical analysis and querying with SQL.
- **Visualization:** Creating various plots and charts to illustrate insights.
- **Main:** Orchestrates the entire workflow by calling functions from different modules for data loading, processing, analysis, and visualization.

### Key Findings
- **The country with the highest number of violations was Poland, with 946 cases.** It was followed by France (804) and the Netherlands (741).  
  ![Violations by Country](/Users/seymenay/Desktop/data_results/origin_new.png)
-Also, see their percentages.
  ![Notifying Countries](/Users/seymenay/Desktop/data_results/percentage_counts_origin.png)
- **Germany was the most frequent notifying country, reporting 1,195 violations.**  
  ![Notifying Countries](/Users/seymenay/Desktop/data_results/notifying_new.png)
-Also, see their percentages.
  ![Notifying Countries](/Users/seymenay/Desktop/data_results/percentage_counts_notifting.png)
- **The most affected category was poultry meat and poultry meat products, particularly from Poland, with 1,079 violations.**  
  - The second highest category was fruits and vegetables (793 cases), where Turkey played a significant role as a source.  
  - The third highest category was food supplements, with 585 violations reported in the last five years.  
  ![Category Distribution](/Users/seymenay/Desktop/data_results/category.png)
-Also, see their percentages.
  ![Notifying Countries](/Users/seymenay/Desktop/data_results/percentage_counts_category.png)
- **Notably, violations in the poultry meat category were mostly classified as alert notifications, indicating their critical importance.**

- **When grouping hazards and risk decisions by subject, ethylene oxide (in sesame seeds) was notably significant.**

- **Salmonella was the most frequently reported hazard, with over 1,400 cases.**  
  - It was followed by Listeria (just over 400 cases) and ethylene oxide (fewer than 400 cases).  
  ![Top Hazards](/Users/seymenay/Desktop/data_results/distribution_of_hazards.png)

- **In the origin & hazard dataset, Poland was the leading source of Salmonella cases, accounting for approximately 700 reports.**
  ![Top Hazards](/Users/seymenay/Desktop/data_results/origin_vs_hazard.png)

- **Poland vs Turkey Category Comparison:**  
  - **Poland:** The top category is poultry meat and poultry meat products with 612 reports.  
  - **Turkey:** The most common category is fruits and vegetables with 288 reports.  
  ![Poland vs Turkey](/Users/seymenay/Desktop/data_results/poland_vs_turkey.png)

### Violation Trends Over the Years

- **2020:** The number of violations was below 1,000, likely due to COVID-19 lockdown effects.
- **2021:** Violations increased to nearly 1,400.
- **2022:** A slight decline, with violations under 1,200.
- **2023:** A sharp rise, reaching nearly 1,800.
- **2024:** The trend continued upward, surpassing 1,900 cases.
- **2025 (so far):** The count stands at 328 (not included in trend analysis).  
  ![Yearly Trends](annual_violation_counts.png)

# Challenges & Solutions

During the course of the project, I faced a variety of challenges, but my problem-solving mindset helped me tackle them effectively. One of the first challenges was remembering the Scrum methodology and managing the project effectively, especially since I was working on it alone. To stay organized and efficient, I created a separate to-do list for every sprint, which made it easier to track progress and ensure I stayed on top of tasks.

This project turned out to be the largest one I’ve ever worked on, and while it was initially overwhelming, remembering the dynamic coding approach and its importance, which I learned from David Malan, made the project more manageable and future-proof. I focused on modularity and dynamism by creating separate scripts for different tasks. Initially, this created some difficulties, but with time, I became more comfortable with this approach. Lastly, I couldn’t figure out how to retrieve data from SQL for direct visualization due to a lack of time.

Here are the main challenges and their solutions:

### 1. Date Format Issue:
One of the first issues I encountered was related to the date format. While extracting data using SQL queries, I realized the dates were not in the correct order (year-month-day), which led to issues with time-based analysis. I quickly identified the problem and converted the dates into the correct format, which ensured data consistency and made the analysis more reliable.

### 2. Data Consistency:
During the data analysis phase, I realized that some data entries had inconsistencies, especially in hazard names. For example, "Salmonella" was listed in different forms like "Salmonella spp." I did not catch this issue during the data cleaning process, so I used regular expressions (regex) to identify and fix these inconsistencies. This greatly improved the consistency of my dataset, making it easier to work with.

### 3. Storing Analysis Results:
Initially, I thought saving the entire analysis in text files would be a perfect solution, but this created problems later. I had saved the results in a dictionary format, which seemed logical at first. However, when I reached the visualization phase, I realized the data needed to be in a Pandas DataFrame to display correctly in tables. This required me to convert the data into a DataFrame, which added extra time to the project. In the end, this conversion turned out to be essential for visualization and helped streamline the final output.

### 4. Visualization Challenges:
One challenging part of the project was creating visualizations, particularly with pivot tables. Drawing pivot tables, especially when dealing with more than two or three columns of data, was initially confusing because of the dictionary format of analysis results. However, after researching and finding some helpful guides, I managed to generate the necessary plots and charts. For example, visualizing the violation categories by country, but ultimately, I was able to produce clear and informative visualizations.

## Future Improvements:

### 1. Data Storage:
The analyzed data should be stored as a DataFrame from the beginning. This would streamline data processing and make it easier to manipulate and query the data for further analysis or visualization.

### 2. Dynamic Plotting Function:
Instead of creating separate functions for each type of plot, a more general plotting function can be developed that takes parameters such as plot type, data, and axis labels. This would make the code more reusable and adaptable for different datasets.

### 3. User Input for Visualizations:
A key improvement would be to allow user input for visualizations. By prompting the user for specific parameters (such as categories, time periods, or countries), the program could generate dynamic plots based on their input. This would make the tool more interactive and useful for various use cases.

### 4. Enhancing Plot Aesthetics:
The visualizations could be enhanced with more appealing design choices, such as improved color schemes, clearer labels, or the use of interactive charts. Libraries like seaborn or plotly can be explored to make the visualizations more professional and engaging.

### 5. Error Handling and Data Cleaning:
Although data cleaning was performed, further validation could be added to handle missing or inconsistent data more effectively. Ensuring that all input data is consistently formatted would improve the overall reliability of the analysis.

## In conclusion

This project provided valuable insights into food violations across Europe, utilizing the RASFF database. By leveraging Python, SQL, and various libraries, I was able to analyze, process, and visualize the data effectively. The key findings highlight that Poland experienced the most food violations, particularly in poultry meat products, while Turkey was significant in the fruits and vegetables category. Additionally, the trend analysis revealed notable fluctuations in violations over the past five years, with a significant spike in 2023.

The project faced several challenges, particularly around data organization and visualization. However, by adapting the approach and utilizing modular code, I was able to overcome these obstacles and successfully generate meaningful visualizations. Despite these challenges, I was able to adapt and solve problems as they arose. The project not only helped me improve my technical skills in data analysis and visualization but also taught me the importance of flexibility and modularity in software development. With the lessons learned from this project, I am better prepared to handle complex tasks in future projects.
