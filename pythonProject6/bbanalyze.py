import pandas as pd
import math
import numpy as np


# TODO nice job overall! I like the partitioning you did. Need a little more commenting

def bbanalyze(file='baseball.csv'):
    """
    Function for analyzing baseball statistics from a csv file
    :param file: csv file with baseball stats
    :return: Dictionary containing a wide variety of baseball stats and dataframes
    """

    # Changes csv file to dataframe format, removes any unnamed columns
    data_frame = pd.read_csv(file)
    data_frame = data_frame.loc[:, ~data_frame.columns.str.contains('^Unnamed')]

    #TODO why are you using a bitwise operator ("~") here? Please use better commenting to explain.
    # I don't think the above line correctly handles the Unnamed: 0 column correctly

    def record_count(data):
        """
        Function for counting records in a dataframe
        :param data: Dataframe with baseball stats
        :return: Number of records
        """

        count = data.shape[0]

        return count

    def years_function(data):
        """
        Function for determining maximum and minimum year in a dataframe
        :param data: Dataframe with baseball stats
        :return: tuple of minimum, maximum year in the dataframe
        """

        years = data['year'].min(), data['year'].max()

        return years

    def count_function(x, data):
        """
        Function for counting unique values in a column in a dataframe
        :param data: Dataframe with baseball stats
        :param x: Either 'id' for player count or 'team' for teams count or 'lg' for league count
        :return: Number of unique values of x category
        """

        count = data[x].nunique()

        return count

    def bb_function(data):
        """
        Function for transforming dataframe into 'bb' dataframe
        :param data: Dataframe with baseball stats
        :return: 'bb' dataframe
        """
        # Drops all rows with Nan values
        data = data.dropna().copy()

        # Calculate new obp and pab columns
        obp_num = data['h'] + data['bb'] + data['hbp']
        obp_denom = data['ab'] + data['bb'] + data['hbp']
        pab_num = data['h'] + data['bb'] + data['hbp'] + data['sf'] + data['sh']
        pab_denom = data['ab'] + data['bb'] + data['hbp'] + data['sf'] + data['sh']

        data['obp'] = obp_num / obp_denom
        data['pab'] = pab_num / pab_denom

        # If any of the new columns are infinity, change to Nan
        data.loc[data['obp'] == math.inf, 'obp'] = math.nan
        data.loc[data['pab'] == math.inf, 'pab'] = math.nan

        return data

    def alnl_function(x, data):
        """
        Function for transforming dataframe into 'al' or 'nl' dataframe
        :param data: Dataframe with baseball stats
        :param x: either 'AL' to return 'al' dataframe or 'NL' to return 'nl' dataframe
        :return: Dictionary with 'al' or 'nl' dataframe and some stats
        """

        # First get the bb dataframe
        data = bb_function(data)

        # Retrieve either the NL or AL records
        data = data[data['lg'] == x]

        # Calculate stats
        player_count = count_function('id', data)
        team_count = count_function('team', data)

        alnl_dict = {'dat': data, 'players': player_count, 'teams': team_count}

        return alnl_dict

    def records(data):
        """
        Function for returning a dictionary of baseball stats
        :param data: Dataframe with baseball stats
        :return: Dictionary with 'al' or 'nl' dataframe and some stats
        """

        # Filter for at least 50 at bats in a sting
        data = data[data['ab'] >= 50]

        # Drop na rows, group by id to aggregate player statistics
        data = data.dropna().copy()
        data = data.groupby('id').sum().reset_index()

        # Calculate new statistic columns 
        data['bbp'] = data['bb'] / data['ab']
        data['sopa'] = data['so'] / (data['ab'] + data['bb'] + data['hbp'] + data['sh'] + data['sf'])
        data['sop'] = data['so'] / data['ab']
        data['sbp'] = data['sb'] / data['ab']
        data['hp'] = data['h'] / data['ab']
        data['hrp'] = data['hr'] / data['ab']

        # Call bb_function to get the obp and pab columns
        data = bb_function(data)

        # For each stat, find the maximum value and the player id who holds that maximum value
        max_hr = data['hr'].max()
        max_hr_playerid = data[data['hr'] == max_hr]['id'].to_string(index=False)

        max_h = data['h'].max()
        max_h_playerid = data[data['h'] == max_h]['id'].to_string(index=False)

        max_bb = data['bb'].max()
        max_bb_playerid = data[data['bb'] == max_bb]['id'].to_string(index=False)

        max_g = data['g'].max()
        max_g_playerid = data[data['g'] == max_g]['id'].to_string(index=False)

        max_hrp = data['hrp'].max()
        max_hrp_playerid = data[np.isclose(data['hrp'], max_hrp)]['id'].to_string(index=False)

        max_hp = data['hp'].max()
        max_hp_playerid = data[np.isclose(data['hp'], max_hp)]['id'].to_string(index=False)

        max_sb = data['sb'].max()
        max_sb_playerid = data[np.isclose(data['sb'], max_sb)]['id'].to_string(index=False)

        max_sbp = data['sbp'].max()
        max_sbp_playerid = data[np.isclose(data['sbp'], max_sbp)]['id'].to_string(index=False)

        max_so = data['so'].max()
        max_so_playerid = data[np.isclose(data['so'], max_so)]['id'].to_string(index=False)

        max_sop = data['sop'].max()
        max_sop_playerid = data[np.isclose(data['sop'], max_sop)]['id'].to_string(index=False)

        max_obp = data['obp'].max()
        max_obp_playerid = data[np.isclose(data['obp'], max_obp)]['id'].to_string(index=False)

        max_pab = data['pab'].max()
        max_pab_playerid = data[np.isclose(data['pab'], max_pab)]['id'].to_string(index=False)

        max_sopa = data['sopa'].max()
        max_sopa_playerid = data[np.isclose(data['sopa'], max_sopa)]['id'].to_string(index=False)

        max_bbp = data['bbp'].max()
        max_bbp_playerid = data[np.isclose(data['bbp'], max_bbp)]['id'].to_string(index=False)

        # Create dictionary of all the records
        records_dict = {'obp': {'id': max_obp_playerid, 'value': max_obp},
                        'pab': {'id': max_pab_playerid, 'value': max_pab},
                        'hr': {'id': max_hr_playerid, 'value': max_hr},
                        'hrp': {'id': max_hrp_playerid, 'value': max_hrp},
                        'h': {'id': max_h_playerid, 'value': max_h},
                        'hp': {'id': max_hp_playerid, 'value': max_hp},
                        'sb': {'id': max_sb_playerid, 'value': max_sb},
                        'sbp': {'id': max_sbp_playerid, 'value': max_sbp},
                        'so': {'id': max_so_playerid, 'value': max_so},
                        'sop': {'id': max_sop_playerid, 'value': max_sop},
                        'sopa': {'id': max_sopa_playerid, 'value': max_sopa},
                        'bb': {'id': max_bb_playerid, 'value': max_bb},
                        'bbp': {'id': max_bbp_playerid, 'value': max_bbp},
                        'g': {'id': max_g_playerid, 'value': max_g}}

        return records_dict

    # Assemble dictionary to be returned
    bb_data = bb_function(data_frame)

    bb_complete_dict = {'record.count': record_count(data_frame), 'complete.cases': record_count(bb_data),
                        'years': years_function(data_frame), 'player.count': count_function('id', data_frame),
                        'team.count': count_function('team', data_frame),
                        'league.count': count_function('lg', data_frame), 'bb': bb_data,
                        'nl': alnl_function('NL', data_frame), 'al': alnl_function('AL', data_frame),
                        'records': records(data_frame)}

    return bb_complete_dict
