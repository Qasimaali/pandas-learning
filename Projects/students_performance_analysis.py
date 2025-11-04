# -----------------------------------------------
#    Project: Students' Performance Analysis
# -----------------------------------------------
# -----------------------------------------------
# Author: Mohd Qasim
# Description:
#   Analyze students' performance dataset using Pandas.
#   1. Average marks by gender
#   2. Correlation between math and reading scores
#   3. Top 10 students overall
# -----------------------------------------------
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# load the csv file
df = pd.read_csv("students_performance_analysis.csv")
print(df.head(5)) # se the first 5 rows
# avg marks by gender
avg_by_gender = df.groupby('gender')[['math_score', 'reading_score', 'writing_score']].mean().round(2)
print("\n--- Average Marks by Gender ---")
print(avg_by_gender)

# Calculate Pearson correlation coefficient
correlation = df['math_score'].corr(df['reading_score']).round(3)
print("\n--- Correlation between Math and Reading Scores ---")
print(f"Correlation Coefficient: {correlation}")
# Interpretation
if correlation > 0.7:
    print(" Strong positive correlation — good math students also score well in reading.")
elif correlation > 0.4:
    print(" Moderate correlation — some relation between math and reading scores.")
else:
    print(" Weak correlation — math and reading scores are mostly independent.")

# 4️⃣ Top 10 Students Overall
# -----------------------------------------------
# Calculate average of all three subjects for ranking

df['overall_avg'] = df[['math_score', 'reading_score', 'writing_score']].mean(axis=1).round(2)

# Sort and get top 10 students
top_students = df.sort_values(by='overall_avg', ascending=False).head(10)

print("\n--- 🏆 Top 10 Students Overall ---")
print(top_students[['gender', 'math_score', 'reading_score', 'writing_score', 'overall_avg']])
# visulise correlation
sns.heatmap(df[['math_score', 'reading_score', 'writing_score']].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()
