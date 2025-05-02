import pandas as pd
from matplotlib import pyplot as plt

from Data import org_time_slots, org_halls

def visualize_timetable(timetable):
    """
    Visualizes a timetable using Matplotlib.

    :param timetable: A list of lists where each sub-list represents a timetable entry
                      in the format [course, lecturer, time_slot, hall].
    """
    # Define the headers
    time_slots_headers = org_time_slots
    hall_headers = org_halls

    # Create an empty timetable DataFrame
    timetable_df = pd.DataFrame(index=hall_headers, columns=time_slots_headers, data="")

    # Populate the timetable DataFrame
    for entry in timetable:
        course, lecturer, time_slot, hall = entry
        if time_slot in org_time_slots and hall in org_halls:
            timetable_df.at[hall, time_slot] = f"{course}\n{lecturer}"

    # Plot the timetable using Matplotlib
    fig, ax = plt.subplots(figsize=(15, 10))
    ax.set_title("University Timetable", fontsize=16)

    # Create a colored grid for the timetable
    for i in range(len(timetable_df.index)):
        for j in range(len(timetable_df.columns)):
            value = timetable_df.iloc[i, j]
            color = "#2b368e" if value else "#ADD8E6"
            ax.add_patch(plt.Rectangle((j-0.5, i-0.5), 1, 1, facecolor=color, edgecolor="black"))

            # Adjust text font size dynamically
            if value:
                ax.text(j, i, value, ha="center", va="center", color="white", fontsize=8, wrap=True, clip_on=True)

    ax.set_xticks(range(len(timetable_df.columns)))
    ax.set_xticklabels(timetable_df.columns, rotation=45, ha="right", fontsize=8)
    ax.set_yticks(range(len(timetable_df.index)))
    ax.set_yticklabels(timetable_df.index, fontsize=8)
    ax.set_xlim(-0.5, len(timetable_df.columns) - 0.5)
    ax.set_ylim(-0.5, len(timetable_df.index) - 0.5)
    ax.invert_yaxis()

    plt.tight_layout()
    plt.show()


def plot_fitness(generation_fitness):
    title = "Fitness Over Generations"
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, len(generation_fitness) + 1), generation_fitness, marker='o', color='blue', label='Fitness')
    plt.title(title)
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.grid(True)
    plt.legend()
    plt.show()

# Example usage

