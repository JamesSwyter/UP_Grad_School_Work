import os
import fnmatch
import pandas as pd


# *.csv is unix pattern for csv files
def combineSamples(pattern, path=".", control_samples=None):
    """
    Function for combining files and then separating into 'control' and 'test' groups
    :param pattern: unix pattern specifying what type of files to look for
    :param path: directory to search for files
    :param control_samples: number of samples to include in 'control' group
    :return: A dictionary with some information about the files and three dataframes: control, sample and test
    """

    # Find all files in the directory
    all_files = os.listdir(path)

    # List all the files that match the pattern
    specific_files = [i for i in all_files if fnmatch.fnmatch(i, pattern)]

    # Create dictionary
    dictionary = {'pattern': pattern, 'path': path, 'control_samples': control_samples,
                  'files': len(specific_files)}

    # If there are no files that match the pattern, return basic dictionary
    if len(specific_files) == 0:
        return dictionary

    # Combine files into one dataframe
    sample_df = pd.concat([pd.read_csv(i) for i in specific_files])
    sample_df = sample_df.rename(columns={'Unnamed: 0': "sample"})
    sample_df = sample_df.sort_values(by=["sample"])
    sample_df.index = [i for i in range(1, len(specific_files)+1)]

    # Create control and test dataframes
    if control_samples is None or control_samples > sample_df.shape[0]:
        control_samples = round(.6 * sample_df.shape[0])
        dictionary['control_samples'] = control_samples

    control_df = sample_df.iloc[0:control_samples, :]
    test_df = sample_df.iloc[control_samples:, :]

    # Add the new metrics
    dictionary['filenames'] = specific_files
    dictionary['samples'] = sample_df
    dictionary['control'] = control_df
    dictionary['test'] = test_df

    return dictionary
