import pandas as pd
import numpy as np


def load_gdp():
    gdp = pd.read_csv('data/gdp/gdp.csv', 
                      error_bad_lines=False, skiprows=0, header=0)

    gdp = gdp.rename(columns={'2017 [YR2017]': 'GDP'}).rename(columns={'Country Name': 'Country'})
    gdp = gdp.replace('..', np.nan)
    gdp = gdp[gdp.index <= np.argmax(gdp['Country'].values == 'Zimbabwe')] # remove the countries below zimbabwe (they are aggregated)

    gdp = gdp.astype({'GDP': float})
    # todo properly impute values for 2018

    return gdp

# soccer rankings from here: https://us.soccerway.com/teams/rankings/fifa/?ICID=TN_03_05_01
def load_rankings_soccer():
    rankings = pd.read_csv('data/fifa_ranking.txt', sep='\t')[['#', 'Team']].rename(columns={'#': 'Rank_soccer', 'Team': 'Country'})
    rankings = rankings.astype({'Rank_soccer': float})
    return rankings

# cricket rankings from here: https://www.icc-cricket.com/rankings/mens/team-rankings/odi
def load_rankings_cricket():
    rankings = pd.read_csv('data/cricket_ranking.txt', sep='\t', header=None)
    rankings = rankings.rename(columns={0: 'Rank_cricket', 1: 'Country'})[['Rank_cricket', 'Country']]
    rankings = rankings.astype({'Rank_cricket': float})
    rankings['Country'] = rankings['Country'].str.strip()
    rankings = rankings.replace('England', 'United Kingdom')
    return rankings
    