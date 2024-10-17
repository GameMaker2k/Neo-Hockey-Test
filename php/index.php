<?php
/*
    Enhanced version with pagination, dynamic sorting of standings, and game listings.
*/

// Enable gzip compression if available
if (!ob_start("ob_gzhandler")) {
    ob_start();
}
date_default_timezone_set("UTC");

// Include Bootstrap CSS
echo '
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Hockey League Viewer</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<div class="container mt-5">
    <h1 class="text-center">Hockey League Viewer</h1>
';

$databasedir = "./data";
$databasedirglob = $databasedir . "/*.db3";
$databaselist = glob($databasedirglob);

// If no database is selected, show the database selector
if (!isset($_GET['database'])) {
    echo '<form method="get" action="index.php">';
    echo '<div class="form-group">';
    echo '<label for="database">Select a Database:</label>';
    echo '<select class="form-control" id="database" name="database">';

    foreach ($databaselist as $dbfile) {
        $dbname = basename($dbfile, ".db3");
        echo "<option value=\"$dbname\">$dbname</option>";
    }

    echo '</select>';
    echo '</div>';
    echo '<button type="submit" class="btn btn-primary">Load Database</button>';
    echo '</form>';
} else {
    // Database and league logic
    $selected_db = $_GET['database'] . ".db3";
    $dbfile_path = $databasedir . "/" . $selected_db;

    if (file_exists($dbfile_path)) {
        $sqldb = new SQLite3($dbfile_path);

        // Fetch available leagues
        $results = $sqldb->query("SELECT * FROM HockeyLeagues");
        echo '<h2 class="text-center mt-4">Select a League in ' . htmlspecialchars($_GET['database']) . '</h2>';
        echo '<form method="get" action="index.php">';
        echo '<input type="hidden" name="database" value="'.htmlspecialchars($_GET['database']).'">';
        echo '<div class="form-group">';
        echo '<label for="league">Select a League:</label>';
        echo '<select class="form-control" id="league" name="league">';
        
        while ($row = $results->fetchArray()) {
            echo "<option value=\"{$row['LeagueName']}\">{$row['LeagueFullName']} ({$row['CountryName']})</option>";
        }
        
        echo '</select>';
        echo '</div>';
        echo '<button type="submit" class="btn btn-primary">Load League</button>';
        echo '</form>';

        if (isset($_GET['league'])) {
            $league_name = $_GET['league'];
            echo '<h3 class="text-center mt-4">Standings and Recent Games for League: ' . htmlspecialchars($league_name) . '</h3>';

            // Pagination setup
            $items_per_page = 10;
            $current_page = isset($_GET['page']) ? intval($_GET['page']) : 1;
            $offset = ($current_page - 1) * $items_per_page;

			// Fetch standings with ORDER BY from OrderType in HockeyLeagues table
			$league_info = $sqldb->querySingle("SELECT OrderType FROM HockeyLeagues WHERE LeagueName = '$league_name'", true);
			$order_clause = $league_info['OrderType'] ?? "ORDER BY Points DESC, Wins DESC"; // Fallback order

			echo '<h4>Standings</h4>';
			$total_teams = $sqldb->querySingle("SELECT COUNT(DISTINCT TeamID) FROM " . $league_name . "Stats");
			$total_pages = ceil($total_teams / $items_per_page);
			$standings_results = $sqldb->query("SELECT * FROM " . $league_name . "Stats WHERE Date = (SELECT MAX(Date) FROM " . $league_name . "Stats WHERE TeamID = TeamID) $order_clause LIMIT $items_per_page OFFSET $offset");

			// Standings table
			echo '<table class="table table-bordered table-striped">';
			echo '<thead><tr><th>Team</th><th>Games Played</th><th>Wins</th><th>Losses</th><th>Points</th><th>Goals For</th><th>Goals Against</th><th>Goal Difference</th></tr></thead>';
			echo '<tbody>';
			while ($row = $standings_results->fetchArray()) {
				echo "<tr>
						<td>{$row['FullName']}</td>
						<td>{$row['GamesPlayed']}</td>
						<td>{$row['Wins']}</td>
						<td>{$row['Losses']}</td>
						<td>{$row['Points']}</td>
						<td>{$row['GoalsFor']}</td>
						<td>{$row['GoalsAgainst']}</td>
						<td>{$row['GoalsDifference']}</td>
					  </tr>";
			}
			echo '</tbody></table>';

            // Pagination links for standings
            echo '<nav><ul class="pagination justify-content-center">';
            for ($page = 1; $page <= $total_pages; $page++) {
                echo '<li class="page-item ' . ($current_page == $page ? 'active' : '') . '">';
                echo '<a class="page-link" href="?database=' . urlencode($_GET['database']) . '&league=' . urlencode($_GET['league']) . '&page=' . $page . '">' . $page . '</a>';
                echo '</li>';
            }
            echo '</ul></nav>';

            // Fetch recent games
            echo '<h4>Recent Games</h4>';
            $game_results = $sqldb->query("SELECT * FROM " . $league_name . "Games ORDER BY Date DESC LIMIT 10");
            
            // Display games
            echo '<table class="table table-bordered table-striped">';
            echo '<thead><tr><th>Date</th><th>Home Team</th><th>Away Team</th><th>Score</th><th>Period-by-Period</th></tr></thead>';
            echo '<tbody>';

            while ($game = $game_results->fetchArray()) {
                $game_date = date('Y-m-d', $game['Date']);
                $home_team = htmlspecialchars($game['HomeTeam']);
                $away_team = htmlspecialchars($game['AwayTeam']);
                $team_score_periods = explode(",", $game['TeamScorePeriods']);
                $team_full_score = htmlspecialchars($game['TeamFullScore']);

                // Format the period-by-period scores (Home first, Away second)
                $period_scores = [];
                foreach ($team_score_periods as $period_score) {
                    $scores = explode(":", $period_score);
                    $period_scores[] = "{$scores[0]} - {$scores[1]}";
                }

                // Handle Overtime and Shootouts
                if ($game['NumberPeriods'] > 3) {
                    $period_scores[] = '<strong>OT</strong>';
                    if ($game['NumberPeriods'] > 4) {
                        $period_scores[] = '<strong>SO</strong>';
                    }
                }

                echo "<tr>
                        <td>{$game_date}</td>
                        <td>{$home_team}</td>
                        <td>{$away_team}</td>
                        <td>{$team_full_score}</td>
                        <td>" . implode(" | ", $period_scores) . "</td>
                      </tr>";
            }

            echo '</tbody></table>';

            // Close the database connection
            $sqldb->close();
        }
    } else {
        echo '<div class="alert alert-danger">Selected database not found!</div>';
    }
}

// Closing HTML
echo '
</div>
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.2/dist/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
';
?>
