import pandas as pd


def reformatSamples(df):
    """
    Function for reformating a dataframe
    :param df: dataframe with all observations listed in one column
    :return: new dataframe, with observations in separated columns and each sample given one row
    """

    # Get the number of observations for the first sample
    all_counts_of_diams = df['sample'].value_counts()
    first_count_of_diams = all_counts_of_diams.iloc[0]

    # Check the other samples, make sure they have the same number of observations
    for i in range(1, len(all_counts_of_diams)):
        if all_counts_of_diams.iloc[i] != first_count_of_diams:
            return None

    # List and count the unique samples
    unique_samples = df['sample'].unique()
    count_samples = df['sample'].nunique()

    # Initialize dataframe with the list of unique samples
    new_frame = pd.DataFrame(unique_samples, columns=['sample'])

    # Create a separate observation column for each observation
    for i in range(0, first_count_of_diams):
        column_of_diams = []

        # Populate each column with all diameter values for that observation number
        for a in range(0, count_samples):
            column_of_diams.append(df.iloc[i+(first_count_of_diams * a), 1])

        new_frame[f"obs.{i + 1}"] = column_of_diams

        new_frame.index = [i for i in range(1, len(all_counts_of_diams) + 1)]

    return new_frame
