from nba_api.stats.endpoints import commonteamroster, playercareerstats, playergamelog, boxscoresummaryv2, teamdashlineups
from nba_api.stats.static import teams
from nba_api.stats.library.parameters import SeasonAll
import pandas as pd
import logging

logging.basicConfig(level=logging.DEBUG)


def get_team_roster(team_name: str, season: str):
    logging.debug(f"Fetching roster for team: {team_name}, season: {season}")
    # Fetch all teams
    nba_teams = teams.get_teams()
    
    # Find the team ID for the given team name
    team = next((team for team in nba_teams if team['full_name'].lower() == team_name.lower()), None)
    if not team:
        print(f"Team '{team_name}' not found.")
        return None

    team_id = team['id']

    roster_data = commonteamroster.CommonTeamRoster(team_id=team_id, season=season)
    roster = roster_data.get_normalized_dict()

    roster_df = pd.DataFrame(roster['CommonTeamRoster'])
    roster_df = roster_df[['PLAYER', 'PLAYER_ID']]
    return roster_df

print(get_team_roster("Golden State Warriors", "2024-25"))

def get_player_stats(player_id, season_id):
    career_stats = playercareerstats.PlayerCareerStats(player_id=player_id)
    career_df = career_stats.get_data_frames()[0]
    season_stats = career_df[career_df['SEASON_ID'] == season_id]
    return season_stats
