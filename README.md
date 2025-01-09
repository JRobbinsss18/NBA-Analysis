# **Deep Dive into Plus-Minus Analysis**

## Project Overview
This is an analytical toolkit designed to explore the relationship between player and team statistics and their impact on **Plus-Minus (+/-)** scores in basketball. This project provides actionable insights through detailed visualizations, statistical comparisons, and lineup analyses. The modular design makes it adaptable for various teams, years, and datasets.

---

## Files in the Project

### 1. **`PlusMinusAnalysis.ipynb`**
- **Purpose**:
  - Analyzes how each individual stat (basic and advanced) correlates with the Plus-Minus (`+/-`) metric.
  - Compares these correlations for the **Golden State Warriors** to the correlations for the **entire NBA**.
- **Visualizations**:
  - Generates **heatmaps** to show the strength of correlations between stats and Plus-Minus.
  - Creates **bar charts** for comparing key statistical influences on Plus-Minus at the team and league levels.
- **Key Questions Answered**:
  - What are the most influential stats for the Warriors' performance in terms of Plus-Minus?
  - How do these compare to the rest of the NBA?

---

### 2. **`HustleStatsImpactOnPlusMinus.ipynb`**
- **Purpose**:
  - Focuses on the impact of **hustle stats** (e.g., deflections, contested shots, screen assists) on Plus-Minus.
  - Analyzes these advanced stats for the **entire NBA**, without team-specific analysis.
- **Key Insights**:
  - Investigates which hustle stats drive team success at the league level.
  - Identifies underappreciated hustle metrics that significantly affect game outcomes.
- **Visualizations**:
  - Heatmaps and charts to illustrate how hustle stats correlate to Plus-Minus.

---

### 3. **`LineupAnalysis.ipynb`**
- **Purpose**:
  - Provides a reusable and adaptable codebase for analyzing team lineups and their performance against opponents.
  - Demonstrates its use by analyzing **Warriors vs. Celtics** lineups for the current season.
- **Features**:
  - Can analyze lineup performance for any team, opponent, or combination of years.
  - Offers insights into the best-performing lineups based on various statistical metrics.
- **Key Questions Answered**:
  - Which lineups perform best against specific opponents?
  - How do these lineups change in effectiveness across seasons or matchups?

---

## Steps to Run
1. **Statistical Analysis (`PlusMinusAnalysis.ipynb`)**:
   - Open the notebook and configure the input for the desired team and seasons.
   - Run the analysis to generate heatmaps and bar charts comparing team-specific and league-wide influences on Plus-Minus.

2. **Hustle Stats Investigation (`HustleStatsImpactOnPlusMinus.ipynb`)**:
   - Open the notebook and load the dataset for the NBA's hustle stats.
   - Run the code to visualize the league-wide correlations between hustle metrics and Plus-Minus.

3. **Lineup Analysis (`LineupAnalysis.ipynb`)**:
   - Open the notebook and set the desired teams, opponents, and seasons for analysis.
   - Run the analysis to get insights on the best-performing lineups.

---

## Key Features and Insights

### 1. **Plus-Minus Correlation Analysis**
- Examines how basic and advanced stats like points, rebounds, and effective field goal percentage correlate to team and league-wide Plus-Minus performance.

### 2. **Hustle Stats Impact**
- Provides league-wide insights into advanced hustle stats such as:
  - **Deflections**
  - **Contested Shots**
  - **Screen Assists**
- Identifies which stats are the most impactful for driving team success.

### 3. **Lineup Analysis**
- Analyzes the best-performing lineups for any team or matchup.
- Offers flexibility to analyze performance across multiple years or specific seasons.

---

## Visualizations
1. **Heatmaps**:
   - Show correlation strength between individual stats and Plus-Minus.
   - Highlight the differences between team-level and league-level influences.

2. **Bar Charts**:
   - Compare key statistics influencing Plus-Minus for specific teams and the entire NBA.

3. **Lineup Comparisons**:
   - Illustrate the effectiveness of different lineups against specific opponents.

---

## Conclusion
**StatScape** empowers basketball analysts, fans, and teams to better understand the statistical drivers behind Plus-Minus performance. By combining correlation analysis, hustle stats insights, and lineup evaluations, this project provides a comprehensive toolkit for basketball analytics.

Feel free to adapt this project to other teams, matchups, or leagues.

