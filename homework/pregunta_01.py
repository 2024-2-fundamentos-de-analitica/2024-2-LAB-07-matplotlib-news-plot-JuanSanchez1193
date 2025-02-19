import pandas as pd
import matplotlib
matplotlib.use('Agg')  
import matplotlib.pyplot as plt
import seaborn as sns
import os

def pregunta_01():

    output_dir = "files/plots"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "news.png")

    data = pd.read_csv("files/input/news.csv", names=["Year", "Television", "Newspaper", "Internet", "Radio"], header=0)


    sns.set_theme(style="darkgrid")

    plt.figure(figsize=(8, 6))
 
    plt.plot(data["Year"], data["Television"], label="Television", color="black", marker="o")
    plt.plot(data["Year"], data["Newspaper"], label="Newspaper", color="gray", marker="o")
    plt.plot(data["Year"], data["Internet"], label="Internet", color="blue", marker="o", linewidth=2)
    plt.plot(data["Year"], data["Radio"], label="Radio", color="lightgray", marker="o")


    plt.title("How people get their news")
    plt.xlabel("Year")
    plt.ylabel("Percentage")
    plt.legend()

    plt.savefig(output_path)

pregunta_01()
