from flask import Flask, jsonify, request
from flask_cors import CORS
from nba_api.stats.endpoints import commonteamroster, playercareerstats
from nba_api.stats.static import teams
import pandas as pd

app = Flask(__name__)
CORS(app)  # Handle CORS issues

@app.route('/api/teams', methods=['GET'])
def get_teams():
    nba_teams = teams.get_teams()
    return jsonify(nba_teams)

@app.route('/api/roster', methods=['GET'])
def get_team_roster():
    team_name = request.args.get('team_name')
    season = request.args.get('season')
    
    nba_teams = teams.get_teams()
    team = next((team for team in nba_teams if team['full_name'].lower() == team_name.lower()), None)
    if not team:
        return jsonify({'error': 'Team not found'}), 404
    
    roster_data = commonteamroster.CommonTeamRoster(team_id=team['id'], season=season)
    roster = roster_data.get_normalized_dict()
    roster_df = pd.DataFrame(roster['CommonTeamRoster'])
    players = roster_df[['PLAYER', 'PLAYER_ID']].to_dict(orient='records')
    return jsonify(players)

@app.route('/api/player_stats', methods=['GET'])
def get_player_stats():
    player_id = request.args.get('player_id')
    season_id = request.args.get('season_id')

    if not player_id or not season_id:
        return jsonify({'error': 'Invalid parameters'}), 400

    career_stats = playercareerstats.PlayerCareerStats(player_id=player_id)
    career_df = career_stats.get_data_frames()[0]
    season_stats = career_df[career_df['SEASON_ID'] == season_id].to_dict(orient='records')
    return jsonify(season_stats)

if __name__ == '__main__':
    app.run(debug=True)
