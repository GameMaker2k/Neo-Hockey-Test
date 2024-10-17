#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Hockey Management Tool

This program is free software; you can redistribute it and/or modify
it under the terms of the Revised BSD License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
Revised BSD License for more details.

Copyright 2015-2024 Game Maker 2k - https://github.com/GameMaker2k
Copyright 2015-2024 Kazuki Przyborowski - https://github.com/KazukiPrzyborowski

$FileInfo: mkhockeytool.py - Last Update: 10/11/2024 Ver. 1.1.0 - Author: cooldude2k $
"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import argparse
import logging
import os
import sys

import pyhockeystats

from typing import Optional

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(format="%(message)s", stream=sys.stdout, level=logging.INFO)


class HockeyTool:
    """Main class for the Hockey Management Tool."""

    def __init__(self, args):
        self.args = args
        self.hockeyarray = {}
        self.supported_extensions = {
            '.xml': 'xml',
            '.sgml': 'sgml',
            '.json': 'json',
            '.sql': 'sql',
            '.db3': 'db3',
            '.db': 'db3',
            '.sdb': 'db3',
            '.sqlite': 'db3',
            '.sqlite3': 'db3',
            '.py': 'py'
        }

    def run(self):
        """Execute the main workflow of the tool."""
        self.handle_initial_setup()
        if self.args.export:
            self.handle_export()
            sys.exit()

        self.main_menu_loop()

    def handle_initial_setup(self):
        """Handle initial database setup based on arguments or user input."""
        if not self.args.empty and not self.args.infile:
            choice = self.get_user_choice(
                "E: Exit Hockey Tool\n1: Empty Hockey Database\n2: Import Hockey Database From File\nWhat would you like to do? ",
                choices=['E', '1', '2']
            )
            if choice == 'E':
                logger.info("Exiting Hockey Tool.")
                sys.exit()
            elif choice == '1':
                self.create_empty_database()
            elif choice == '2':
                self.import_database()
        else:
            if self.args.empty:
                self.create_empty_database()
            elif self.args.infile:
                self.import_database()

    def create_empty_database(self):
        """Create an empty hockey database."""
        filename = self.args.outfile or self.prompt_filename("Enter Hockey Database File Name for Output: ")
        self.hockeyarray = pyhockeystats.CreateHockeyArray(filename)
        logger.info("Created empty database at: {}".format(filename))

    def import_database(self):
        """Import hockey database from a file."""
        filename = self.args.infile or self.prompt_filename("Enter Hockey Database File Name for Import: ")
        ext = os.path.splitext(filename)[1].lower()
        file_type = self.supported_extensions.get(ext)

        if not file_type:
            logger.error("ERROR: Unsupported file type.")
            sys.exit(1)

        # Mapping file types to pyhockeystats import functions
        import_methods = {
            'xml': pyhockeystats.MakeHockeyArrayFromHockeyXML,
            'sgml': pyhockeystats.MakeHockeyArrayFromHockeySGML,
            'json': pyhockeystats.MakeHockeyArrayFromHockeyJSON,
            'sql': pyhockeystats.MakeHockeyArrayFromHockeySQL,
            'db3': pyhockeystats.MakeHockeyArrayFromHockeyDatabase,
            'py': pyhockeystats.MakeHockeyArrayFromHockeyPython
        }

        import_func = import_methods.get(file_type)

        if not import_func:
            logger.error("ERROR: Import method not implemented for this file type.")
            sys.exit(1)

        try:
            self.hockeyarray = import_func(filename, verbose=self.args.verbose, verbosetype=self.args.verbosetype)
            logger.info("Imported database from: {}".format(filename))
        except Exception as e:
            logger.error("ERROR: Failed to import database. {}".format(e))
            sys.exit(1)

        if pyhockeystats.CheckHockeyArray(self.hockeyarray):
            logger.info("Database imported successfully.")
        else:
            logger.error("ERROR: Invalid Hockey Array after import.")
            sys.exit(1)

    def handle_export(self):
        """Handle exporting the hockey database to a file."""
        if not self.hockeyarray:
            logger.error("ERROR: No data to export.")
            sys.exit(1)

        export_type = self.args.type or self.determine_export_type()
        outfile = self.args.outfile or self.prompt_filename("Enter Hockey Database File Name to Export: ")

        export_methods = {
            'xml': pyhockeystats.MakeHockeyXMLFileFromHockeyArray,
            'xmlalt': pyhockeystats.MakeHockeyXMLAltFileFromHockeyArray,
            'sgml': pyhockeystats.MakeHockeySGMLFileFromHockeyArray,
            'json': pyhockeystats.MakeHockeyJSONFileFromHockeyArray,
            'py': pyhockeystats.MakeHockeyPythonFileFromHockeyArray,
            'pyalt': pyhockeystats.MakeHockeyPythonAltFileFromHockeyArray,
            'oopy': pyhockeystats.MakeHockeyPythonOOPFileFromHockeyArray,
            'oopyalt': pyhockeystats.MakeHockeyPythonOOPAltFileFromHockeyArray,
            'sql': pyhockeystats.MakeHockeySQLFileFromHockeyArray,
            'db3': pyhockeystats.MakeHockeyDatabaseFromHockeyArray
        }

        export_func = export_methods.get(export_type.lower())
        if not export_func:
            logger.error("ERROR: Unsupported export type.")
            sys.exit(1)

        try:
            export_func(self.hockeyarray, outfile, verbose=self.args.verbose, verbosetype=self.args.verbosetype)
            logger.info("Exported database to: {}".format(outfile))
        except Exception as e:
            logger.error("ERROR: Failed to export database. {}".format(e))
            sys.exit(1)

    def determine_export_type(self):
        """Determine the export type based on the output file extension."""
        if not self.args.outfile:
            return None

        ext = os.path.splitext(self.args.outfile)[1].lower()
        return self.supported_extensions.get(ext)

    def main_menu_loop(self):
        """Display the main menu and handle user actions."""
        menu_options = {
            '1': self.manage_leagues,
            '2': self.manage_conferences,
            '3': self.manage_divisions,
            '4': self.manage_teams,
            '5': self.manage_arenas,
            '6': self.manage_games,
            '7': self.manage_database
        }

        while True:
            choice = self.get_user_choice(
                "E: Exit Hockey Tool\n"
                "1: Hockey League Tool\n"
                "2: Hockey Conference Tool\n"
                "3: Hockey Division Tool\n"
                "4: Hockey Team Tool\n"
                "5: Hockey Arena Tool\n"
                "6: Hockey Game Tool\n"
                "7: Hockey Database Tool\n"
                "What would you like to do? ",
                choices=['E', '1', '2', '3', '4', '5', '6', '7']
            )

            if choice == 'E':
                logger.info("Exiting Hockey Tool.")
                break

            action = menu_options.get(choice)
            if action:
                action()
            else:
                logger.error("ERROR: Invalid Command.")

    def manage_leagues(self):
        """Manage hockey leagues."""
        submenu_options = {
            '1': self.add_league,
            '2': self.remove_league,
            '3': self.edit_league
        }

        while True:
            choice = self.get_user_choice(
                "E: Back to Main Menu\n"
                "1: Add Hockey League\n"
                "2: Remove Hockey League\n"
                "3: Edit Hockey League\n"
                "What would you like to do? ",
                choices=['E', '1', '2', '3']
            )

            if choice == 'E':
                break

            action = submenu_options.get(choice)
            if action:
                action()
            else:
                logger.error("ERROR: Invalid Command.")

    def add_league(self):
        """Add a new hockey league."""
        sn = self.prompt_input("Enter Hockey League short name: ")
        if sn in self.hockeyarray.get('leaguelist', []):
            logger.error("ERROR: Hockey League with that short name already exists.")
            return

        fn = self.prompt_input("Enter Hockey League full name: ")
        csn = self.prompt_input("Enter Hockey League country short name: ")
        cfn = self.prompt_input("Enter Hockey League country full name: ")
        sd = self.prompt_input("Enter Hockey League start date (YYYY-MM-DD): ")
        pof = self.prompt_input("Enter Hockey League playoff format: ")
        ot = self.prompt_input("Enter Hockey League order type: ")
        hc = self.prompt_input("Does the Hockey League have conferences? (yes/no): ").lower()
        hd = self.prompt_input("Does the Hockey League have divisions? (yes/no): ").lower()

        self.hockeyarray = pyhockeystats.AddHockeyLeagueToArray(
            self.hockeyarray, sn, fn, csn, cfn, sd, pof, ot, hc, hd
        )

        if hc == "no":
            self.hockeyarray = pyhockeystats.AddHockeyConferenceToArray(
                self.hockeyarray, sn, ""
            )
        if hd == "no":
            self.hockeyarray = pyhockeystats.AddHockeyDivisionToArray(
                self.hockeyarray, sn, "", ""
            )
        logger.info("Hockey League '{}' added successfully.".format(fn))

    def remove_league(self):
        """Remove an existing hockey league."""
        leagues = self.hockeyarray.get('leaguelist', [])
        if not leagues:
            logger.error("ERROR: There are no Hockey Leagues to delete.")
            return

        self.display_list(leagues, "Hockey Leagues")
        choice = self.prompt_selection(len(leagues), "Enter Hockey League number to remove: ")

        if choice is not None:
            sn = leagues[choice]
            self.hockeyarray = pyhockeystats.RemoveHockeyLeagueFromArray(
                self.hockeyarray, sn
            )
            logger.info("Hockey League '{}' removed successfully.".format(sn))

    def edit_league(self):
        """Edit an existing hockey league."""
        leagues = self.hockeyarray.get('leaguelist', [])
        if not leagues:
            logger.error("ERROR: There are no Hockey Leagues to edit.")
            return

        self.display_list(leagues, "Hockey Leagues")
        choice = self.prompt_selection(len(leagues), "Enter Hockey League number to edit: ")

        if choice is not None:
            old_sn = leagues[choice]
            new_sn = self.prompt_input("Enter new Hockey League short name: ")
            if new_sn in self.hockeyarray.get('leaguelist', []):
                logger.error("ERROR: Hockey League with that short name already exists.")
                return

            new_fn = self.prompt_input("Enter new Hockey League full name: ")
            new_csn = self.prompt_input("Enter new Hockey League country short name: ")
            new_cfn = self.prompt_input("Enter new Hockey League country full name: ")
            new_sd = self.prompt_input("Enter new Hockey League start date (YYYY-MM-DD): ")
            new_pof = self.prompt_input("Enter new Hockey League playoff format: ")
            new_ot = self.prompt_input("Enter new Hockey League order type: ")
            new_hc = self.prompt_input("Does the Hockey League have conferences? (yes/no): ").lower()
            new_hd = self.prompt_input("Does the Hockey League have divisions? (yes/no): ").lower()

            self.hockeyarray = pyhockeystats.ReplaceHockeyLeagueFromArray(
                self.hockeyarray, old_sn, new_sn, new_fn, new_csn, new_cfn,
                new_sd, new_pof, new_ot, new_hc, new_hd
            )

            if new_hc == "no":
                self.hockeyarray = pyhockeystats.AddHockeyConferenceToArray(
                    self.hockeyarray, new_sn, ""
                )
            if new_hd == "no":
                self.hockeyarray = pyhockeystats.AddHockeyDivisionToArray(
                    self.hockeyarray, new_sn, "", ""
                )
            logger.info("Hockey League '{}' updated successfully.".format(old_sn))

    def manage_conferences(self):
        """Manage hockey conferences."""
        leagues = self.hockeyarray.get('leaguelist', [])
        if not leagues:
            logger.error("ERROR: There are no Hockey Leagues.")
            return

        self.display_list(leagues, "Hockey Leagues")
        league_index = self.prompt_selection(len(leagues), "Enter Hockey League number: ")
        if league_index is None:
            return

        league_sn = leagues[league_index]
        if self.hockeyarray[league_sn]['leagueinfo'].get('conferences', 'no') != "yes":
            logger.error("ERROR: The Hockey League does not have conferences.")
            return

        submenu_options = {
            '1': lambda: self.add_conference(league_sn),
            '2': lambda: self.remove_conference(league_sn),
            '3': lambda: self.edit_conference(league_sn),
            '4': lambda: self.move_division_to_conference(league_sn),
            '5': lambda: self.move_team_to_conference(league_sn)
        }

        while True:
            choice = self.get_user_choice(
                "E: Back to Main Menu\n"
                "1: Add Hockey Conference\n"
                "2: Remove Hockey Conference\n"
                "3: Edit Hockey Conference\n"
                "4: Move Hockey Division to Another Conference\n"
                "5: Move Hockey Team to Another Conference\n"
                "What would you like to do? ",
                choices=['E', '1', '2', '3', '4', '5']
            )

            if choice == 'E':
                break

            action = submenu_options.get(choice)
            if action:
                action()
            else:
                logger.error("ERROR: Invalid Command.")

    def add_conference(self, league_sn):
        """Add a new hockey conference to a league."""
        cn = self.prompt_input("Enter Hockey Conference name: ")
        if cn in self.hockeyarray[league_sn].get('conferencelist', []):
            logger.error("ERROR: Hockey Conference with that name already exists.")
            return

        cpf = self.prompt_input("Enter Hockey Conference prefix: ")
        csf = self.prompt_input("Enter Hockey Conference suffix: ")

        self.hockeyarray = pyhockeystats.AddHockeyConferenceToArray(
            self.hockeyarray, league_sn, cn, cpf, csf
        )
        logger.info("Hockey Conference '{}' added successfully to league '{}'.".format(cn, league_sn))

    def remove_conference(self, league_sn):
        """Remove an existing hockey conference from a league."""
        conferences = self.hockeyarray[league_sn].get('conferencelist', [])
        if not conferences:
            logger.error("ERROR: There are no Hockey Conferences to delete.")
            return

        self.display_list(conferences, "Hockey Conferences")
        choice = self.prompt_selection(len(conferences), "Enter Hockey Conference number to remove: ")

        if choice is not None:
            cn = conferences[choice]
            self.hockeyarray = pyhockeystats.RemoveHockeyConferenceFromArray(
                self.hockeyarray, league_sn, cn
            )
            logger.info("Hockey Conference '{}' removed successfully from league '{}'.".format(cn, league_sn))

    def edit_conference(self, league_sn):
        """Edit an existing hockey conference in a league."""
        conferences = self.hockeyarray[league_sn].get('conferencelist', [])
        if not conferences:
            logger.error("ERROR: There are no Hockey Conferences to edit.")
            return

        self.display_list(conferences, "Hockey Conferences")
        choice = self.prompt_selection(len(conferences), "Enter Hockey Conference number to edit: ")

        if choice is not None:
            old_cn = conferences[choice]
            new_cn = self.prompt_input("Enter new Hockey Conference name: ")
            if new_cn in self.hockeyarray[league_sn].get('conferencelist', []):
                logger.error("ERROR: Hockey Conference with that name already exists.")
                return

            new_cpf = self.prompt_input("Enter new Hockey Conference prefix: ")
            new_csf = self.prompt_input("Enter new Hockey Conference suffix: ")

            self.hockeyarray = pyhockeystats.ReplaceHockeyConferencFromArray(
                self.hockeyarray, league_sn, old_cn, new_cn, new_cpf, new_csf
            )
            logger.info("Hockey Conference '{}' updated successfully in league '{}'.".format(old_cn, league_sn))

    def move_division_to_conference(self, league_sn):
        """Move a hockey division from one conference to another within a league."""
        divisions = []
        for conf in self.hockeyarray[league_sn].get('conferencelist', []):
            divisions += [(conf, div) for div in self.hockeyarray[league_sn].get(conf, {}).get('divisionlist', [])]

        if not divisions:
            logger.error("ERROR: There are no Hockey Divisions to move.")
            return

        # Display divisions with their current conferences
        division_descriptions = ["{}: {}".format(conf, div) for conf, div in divisions]
        self.display_list(division_descriptions, "Hockey Divisions (Conference: Division)")

        choice = self.prompt_selection(len(divisions), "Enter Hockey Division number to move: ")
        if choice is None:
            return

        old_conference, division = divisions[choice]

        # Display target conferences
        target_conferences = self.hockeyarray[league_sn].get('conferencelist', [])
        if not target_conferences:
            logger.error("ERROR: There are no target conferences available.")
            return

        self.display_list(target_conferences, "Target Conferences")
        target_choice = self.prompt_selection(len(target_conferences), "Enter target Hockey Conference number: ")
        if target_choice is None:
            return

        new_conference = target_conferences[target_choice]

        if old_conference == new_conference:
            logger.error("ERROR: Division is already in the selected conference.")
            return

        self.hockeyarray = pyhockeystats.MoveHockeyDivisionToConferenceFromArray(
            self.hockeyarray, league_sn, division, old_conference, new_conference
        )
        logger.info("Hockey Division '{}' moved from conference '{}' to '{}.'".format(division, old_conference, new_conference))

    def move_team_to_conference(self, league_sn):
        """Move a hockey team from one conference to another within a league."""
        teams = []
        for conf in self.hockeyarray[league_sn].get('conferencelist', []):
            for div in self.hockeyarray[league_sn].get(conf, {}).get('divisionlist', []):
                for team in self.hockeyarray[league_sn].get(conf, {}).get(div, {}).get('teamlist', []):
                    teams.append((conf, div, team))

        if not teams:
            logger.error("ERROR: There are no Hockey Teams to move.")
            return

        # Display teams with their current conferences and divisions
        team_descriptions = ["{} > {}: {}".format(conf, div, team) for conf, div, team in teams]
        self.display_list(team_descriptions, "Hockey Teams (Conference > Division: Team)")

        choice = self.prompt_selection(len(teams), "Enter Hockey Team number to move: ")
        if choice is None:
            return

        old_conference, old_division, teamname = teams[choice]

        # Display target conferences
        target_conferences = self.hockeyarray[league_sn].get('conferencelist', [])
        if not target_conferences:
            logger.error("ERROR: There are no target conferences available.")
            return

        self.display_list(target_conferences, "Target Conferences")
        target_choice = self.prompt_selection(len(target_conferences), "Enter target Hockey Conference number: ")
        if target_choice is None:
            return

        new_conference = target_conferences[target_choice]

        if old_conference == new_conference:
            logger.error("ERROR: Team is already in the selected conference.")
            return

        # Display target divisions within the new conference
        target_divisions = self.hockeyarray[league_sn].get(new_conference, {}).get('divisionlist', [])
        if not target_divisions:
            logger.error("ERROR: There are no target divisions in the selected conference.")
            return

        self.display_list(target_divisions, "Target Divisions in Conference '{}'".format(new_conference))
        division_choice = self.prompt_selection(len(target_divisions), "Enter target Hockey Division number: ")
        if division_choice is None:
            return

        new_division = target_divisions[division_choice]

        self.hockeyarray = pyhockeystats.MoveHockeyTeamToConferenceFromArray(
            self.hockeyarray, league_sn, teamname, old_conference, new_conference, new_division
        )
        logger.info("Hockey Team '{}' moved from conference '{}' to '{}' in division '{}'.".format(teamname, old_conference, new_conference, new_division))

    def manage_divisions(self):
        """Manage hockey divisions."""
        leagues = self.hockeyarray.get('leaguelist', [])
        if not leagues:
            logger.error("ERROR: There are no Hockey Leagues.")
            return

        self.display_list(leagues, "Hockey Leagues")
        league_index = self.prompt_selection(len(leagues), "Enter Hockey League number: ")
        if league_index is None:
            return

        league_sn = leagues[league_index]
        has_divisions = self.hockeyarray[league_sn]['leagueinfo'].get('divisions', 'no') == "yes"
        if not has_divisions:
            logger.error("ERROR: The Hockey League does not have divisions.")
            return

        submenu_options = {
            '1': lambda: self.add_division(league_sn),
            '2': lambda: self.remove_division(league_sn),
            '3': lambda: self.edit_division(league_sn),
            '4': lambda: self.move_team_to_division(league_sn)
        }

        while True:
            choice = self.get_user_choice(
                "E: Back to Main Menu\n"
                "1: Add Hockey Division\n"
                "2: Remove Hockey Division\n"
                "3: Edit Hockey Division\n"
                "4: Move Hockey Team to Another Division\n"
                "What would you like to do? ",
                choices=['E', '1', '2', '3', '4']
            )

            if choice == 'E':
                break

            action = submenu_options.get(choice)
            if action:
                action()
            else:
                logger.error("ERROR: Invalid Command.")

    def add_division(self, league_sn, conference_sn=None):
        """Add a new hockey division to a league or conference."""
        dn = self.prompt_input("Enter Hockey Division name: ")
        target = 'conferencelist' if conference_sn else 'divisionlist'
        existing_divisions = self.hockeyarray[league_sn].get(target, [])
        if dn in existing_divisions:
            logger.error("ERROR: Hockey Division with that name already exists.")
            return

        dpf = self.prompt_input("Enter Hockey Division prefix: ")
        dsf = self.prompt_input("Enter Hockey Division suffix: ")

        self.hockeyarray = pyhockeystats.AddHockeyDivisionToArray(
            self.hockeyarray, league_sn, dn, conference_sn, dpf, dsf
        )
        location = "conference '{}' in league '{}'".format(conference_sn, league_sn) if conference_sn else "league '{}'".format(league_sn)
        logger.info("Hockey Division '{}' added successfully to {}.".format(dn, location))

    def remove_division(self, league_sn, conference_sn=None):
        """Remove an existing hockey division from a league or conference."""
        target = 'conferencelist' if conference_sn else 'divisionlist'
        divisions = self.hockeyarray[league_sn].get(target, [])
        if not divisions:
            logger.error("ERROR: There are no Hockey Divisions to delete.")
            return

        self.display_list(divisions, "Hockey Divisions")
        choice = self.prompt_selection(len(divisions), "Enter Hockey Division number to remove: ")

        if choice is not None:
            dn = divisions[choice]
            self.hockeyarray = pyhockeystats.RemoveHockeyDivisionFromArray(
                self.hockeyarray, league_sn, dn, conference_sn
            )
            location = "conference '{}' in league '{}'".format(conference_sn, league_sn) if conference_sn else "league '{}'".format(league_sn)
            logger.info("Hockey Division '{}' removed successfully from {}.".format(dn, location))

    def edit_division(self, league_sn, conference_sn=None):
        """Edit an existing hockey division in a league or conference."""
        target = 'conferencelist' if conference_sn else 'divisionlist'
        divisions = self.hockeyarray[league_sn].get(target, [])
        if not divisions:
            logger.error("ERROR: There are no Hockey Divisions to edit.")
            return

        self.display_list(divisions, "Hockey Divisions")
        choice = self.prompt_selection(len(divisions), "Enter Hockey Division number to edit: ")

        if choice is not None:
            old_dn = divisions[choice]
            new_dn = self.prompt_input("Enter new Hockey Division name: ")
            if new_dn in self.hockeyarray[league_sn].get(target, []):
                logger.error("ERROR: Hockey Division with that name already exists.")
                return

            new_dpf = self.prompt_input("Enter new Hockey Division prefix: ")
            new_dsf = self.prompt_input("Enter new Hockey Division suffix: ")

            self.hockeyarray = pyhockeystats.ReplaceHockeyDivisionFromArray(
                self.hockeyarray, league_sn, new_dn, old_dn, conference_sn, new_dpf, new_dsf
            )
            location = "conference '{}' in league '{}'".format(conference_sn, league_sn) if conference_sn else "league '{}'".format(league_sn)
            logger.info("Hockey Division '{}' updated successfully in {}.".format(old_dn, location))

    def move_team_to_division(self, league_sn):
        """Move a hockey team from one division to another within a league."""
        teams = []
        for conf in self.hockeyarray[league_sn].get('conferencelist', []):
            for div in self.hockeyarray[league_sn].get(conf, {}).get('divisionlist', []):
                for team in self.hockeyarray[league_sn].get(conf, {}).get(div, {}).get('teamlist', []):
                    teams.append((conf, div, team))

        if not teams:
            logger.error("ERROR: There are no Hockey Teams to move.")
            return

        # Display teams with their current conferences and divisions
        team_descriptions = ["{} > {}: {}".format(conf, div, team) for conf, div, team in teams]
        self.display_list(team_descriptions, "Hockey Teams (Conference > Division: Team)")

        choice = self.prompt_selection(len(teams), "Enter Hockey Team number to move: ")
        if choice is None:
            return

        old_conference, old_division, teamname = teams[choice]

        # Display target divisions within the same conference
        target_divisions = self.hockeyarray[league_sn].get(old_conference, {}).get('divisionlist', [])
        if not target_divisions:
            logger.error("ERROR: There are no target divisions available.")
            return

        self.display_list(target_divisions, "Target Divisions in Conference '{}'".format(old_conference))
        division_choice = self.prompt_selection(len(target_divisions), "Enter target Hockey Division number: ")
        if division_choice is None:
            return

        new_division = target_divisions[division_choice]

        if old_division == new_division:
            logger.error("ERROR: Team is already in the selected division.")
            return

        self.hockeyarray = pyhockeystats.MoveHockeyTeamToDivisionFromArray(
            self.hockeyarray, league_sn, teamname, old_conference, new_division
        )
        logger.info("Hockey Team '{}' moved from division '{}' to '{}' in conference '{}'.".format(
            teamname, old_division, new_division, old_conference))

    def manage_teams(self):
        """Manage hockey teams."""
        leagues = self.hockeyarray.get('leaguelist', [])
        if not leagues:
            logger.error("ERROR: There are no Hockey Leagues.")
            return

        self.display_list(leagues, "Hockey Leagues")
        league_index = self.prompt_selection(len(leagues), "Enter Hockey League number: ")
        if league_index is None:
            return

        league_sn = leagues[league_index]

        # Display Conferences if they exist
        conferences = self.hockeyarray[league_sn].get('conferencelist', [])
        if conferences:
            self.display_list(conferences, "Hockey Conferences")
            conference_index = self.prompt_selection(len(conferences), "Enter Hockey Conference number (or 'E' to skip): ")
            if conference_index is not None:
                conference_sn = conferences[conference_index]
            else:
                conference_sn = None
        else:
            conference_sn = None

        # Display Divisions
        target = 'conferencelist' if conference_sn else 'divisionlist'
        divisions = self.hockeyarray[league_sn].get(target, [])
        if not divisions:
            logger.error("ERROR: There are no Hockey Divisions.")
            return

        self.display_list(divisions, "Hockey Divisions")
        division_index = self.prompt_selection(len(divisions), "Enter Hockey Division number: ")
        if division_index is None:
            return

        division_sn = divisions[division_index]

        submenu_options = {
            '1': lambda: self.add_team(league_sn, conference_sn, division_sn),
            '2': lambda: self.remove_team(league_sn, conference_sn, division_sn),
            '3': lambda: self.edit_team(league_sn, conference_sn, division_sn),
            '4': lambda: self.move_team_to_division_within(league_sn, conference_sn, division_sn)
        }

        while True:
            choice = self.get_user_choice(
                "E: Back to Main Menu\n"
                "1: Add Hockey Team\n"
                "2: Remove Hockey Team\n"
                "3: Edit Hockey Team\n"
                "4: Move Hockey Team to Another Division\n"
                "What would you like to do? ",
                choices=['E', '1', '2', '3', '4']
            )

            if choice == 'E':
                break

            action = submenu_options.get(choice)
            if action:
                action()
            else:
                logger.error("ERROR: Invalid Command.")

    def add_team(self, league_sn, conference_sn, division_sn):
        """Add a new hockey team."""
        teamname = self.prompt_input("Enter Hockey Team name: ")
        if teamname in self.hockeyarray[league_sn][conference_sn][division_sn].get('teamlist', []):
            logger.error("ERROR: Hockey Team with that name already exists.")
            return

        cityname = self.prompt_input("Enter Hockey Team city name: ")
        areaname = self.prompt_input("Enter Hockey Team area name: ")
        fullareaname = self.prompt_input("Enter Hockey Team full area name: ")
        countryname = self.prompt_input("Enter Hockey Team country name: ")
        fullcountryname = self.prompt_input("Enter Hockey Team full country name: ")
        arenaname = self.prompt_input("Enter Hockey Team arena name: ")
        teamnameprefix = self.prompt_input("Enter Hockey Team name prefix (optional): ") or ""
        teamnamesuffix = self.prompt_input("Enter Hockey Team name suffix (optional): ") or ""
        teamaffiliates = self.prompt_input("Enter Hockey Team affiliates (optional): ") or ""

        self.hockeyarray = pyhockeystats.AddHockeyTeamToArray(
            self.hockeyarray, league_sn, cityname, areaname, countryname,
            fullcountryname, fullareaname, teamname, conference_sn, division_sn,
            arenaname, teamnameprefix, teamnamesuffix, teamaffiliates
        )
        logger.info("Hockey Team '{}' added successfully to division '{}'.".format(teamname, division_sn))

    def remove_team(self, league_sn, conference_sn, division_sn):
        """Remove an existing hockey team."""
        teams = self.hockeyarray[league_sn][conference_sn][division_sn].get('teamlist', [])
        if not teams:
            logger.error("ERROR: There are no Hockey Teams to delete.")
            return

        self.display_list(teams, "Hockey Teams")
        choice = self.prompt_selection(len(teams), "Enter Hockey Team number to remove: ")

        if choice is not None:
            teamname = teams[choice]
            self.hockeyarray = pyhockeystats.RemoveHockeyTeamFromArray(
                self.hockeyarray, league_sn, teamname, conference_sn, division_sn
            )
            logger.info("Hockey Team '{}' removed successfully from division '{}'.".format(teamname, division_sn))

    def edit_team(self, league_sn, conference_sn, division_sn):
        """Edit an existing hockey team."""
        teams = self.hockeyarray[league_sn][conference_sn][division_sn].get('teamlist', [])
        if not teams:
            logger.error("ERROR: There are no Hockey Teams to edit.")
            return

        self.display_list(teams, "Hockey Teams")
        choice = self.prompt_selection(len(teams), "Enter Hockey Team number to edit: ")

        if choice is not None:
            oldteamname = teams[choice]
            newteamname = self.prompt_input("Enter new Hockey Team name: ")
            if newteamname in self.hockeyarray[league_sn][conference_sn][division_sn].get('teamlist', []):
                logger.error("ERROR: Hockey Team with that name already exists.")
                return

            # Collect optional updates
            cityname = self.prompt_input("Enter new Hockey Team city name (press Enter to skip): ") or None
            areaname = self.prompt_input("Enter new Hockey Team area name (press Enter to skip): ") or None
            countryname = self.prompt_input("Enter new Hockey Team country name (press Enter to skip): ") or None
            fullcountryname = self.prompt_input("Enter new Hockey Team full country name (press Enter to skip): ") or None
            fullareaname = self.prompt_input("Enter new Hockey Team full area name (press Enter to skip): ") or None
            arenaname = self.prompt_input("Enter new Hockey Team arena name (press Enter to skip): ") or None
            teamnameprefix = self.prompt_input("Enter new Hockey Team name prefix (press Enter to skip): ") or None
            teamnamesuffix = self.prompt_input("Enter new Hockey Team name suffix (press Enter to skip): ") or None
            teamaffiliates = self.prompt_input("Enter new Hockey Team affiliates (press Enter to skip): ") or None

            self.hockeyarray = pyhockeystats.ReplaceHockeyTeamFromArray(
                self.hockeyarray, league_sn, oldteamname, newteamname, conference_sn, division_sn,
                cityname, areaname, countryname, fullcountryname, fullareaname,
                arenaname, teamnameprefix, teamnamesuffix, teamaffiliates
            )
            logger.info("Hockey Team '{}' updated successfully to '{}' in division '{}'.".format(oldteamname, newteamname, division_sn))

    def move_team_to_division_within(self, league_sn, conference_sn, division_sn):
        """Move a hockey team to another division within the same conference."""
        teams = self.hockeyarray[league_sn][conference_sn][division_sn].get('teamlist', [])
        if not teams:
            logger.error("ERROR: There are no Hockey Teams to move.")
            return

        self.display_list(teams, "Hockey Teams")
        choice = self.prompt_selection(len(teams), "Enter Hockey Team number to move: ")

        if choice is not None:
            teamname = teams[choice]

            # Display target divisions within the same conference
            target_divisions = self.hockeyarray[league_sn].get(conference_sn, {}).get('divisionlist', [])
            if not target_divisions:
                logger.error("ERROR: There are no target divisions available.")
                return

            self.display_list(target_divisions, "Target Divisions in Conference '{}'".format(conference_sn))
            division_choice = self.prompt_selection(len(target_divisions), "Enter target Hockey Division number: ")
            if division_choice is None:
                return

            new_division = target_divisions[division_choice]

            if division_sn == new_division:
                logger.error("ERROR: Team is already in the selected division.")
                return

            self.hockeyarray = pyhockeystats.MoveHockeyTeamToDivisionFromArray(
                self.hockeyarray, league_sn, teamname, conference_sn, division_sn, new_division
            )
            logger.info("Hockey Team '{}' moved from division '{}' to '{}' in conference '{}'.".format(
                teamname, division_sn, new_division, conference_sn))

    def manage_arenas(self):
        """Manage hockey arenas."""
        leagues = self.hockeyarray.get('leaguelist', [])
        if not leagues:
            logger.error("ERROR: There are no Hockey Leagues.")
            return

        self.display_list(leagues, "Hockey Leagues")
        league_index = self.prompt_selection(len(leagues), "Enter Hockey League number: ")
        if league_index is None:
            return

        league_sn = leagues[league_index]

        submenu_options = {
            '1': lambda: self.add_arena(league_sn),
            '2': lambda: self.remove_arena(league_sn),
            '3': lambda: self.edit_arena(league_sn)
        }

        while True:
            choice = self.get_user_choice(
                "E: Back to Main Menu\n"
                "1: Add Hockey Arena\n"
                "2: Remove Hockey Arena\n"
                "3: Edit Hockey Arena\n"
                "What would you like to do? ",
                choices=['E', '1', '2', '3']
            )

            if choice == 'E':
                break

            action = submenu_options.get(choice)
            if action:
                action()
            else:
                logger.error("ERROR: Invalid Command.")

    def add_arena(self, league_sn):
        """Add a new hockey arena."""
        arenaname = self.prompt_input("Enter Hockey Arena name: ")
        if any(arena['name'] == arenaname for arena in self.hockeyarray.get(league_sn, {}).get('arenas', [])):
            logger.error("ERROR: Hockey Arena with that name already exists.")
            return

        cityname = self.prompt_input("Enter Hockey Arena city name: ")
        areaname = self.prompt_input("Enter Hockey Arena area name: ")
        fullareaname = self.prompt_input("Enter Hockey Arena full area name: ")
        countryname = self.prompt_input("Enter Hockey Arena country name: ")
        fullcountryname = self.prompt_input("Enter Hockey Arena full country name: ")

        self.hockeyarray = pyhockeystats.AddHockeyArenaToArray(
            self.hockeyarray, league_sn, cityname, areaname, countryname,
            fullcountryname, fullareaname, arenaname
        )
        logger.info("Hockey Arena '{}' added successfully to league '{}'.".format(arenaname, league_sn))

    def remove_arena(self, league_sn):
        """Remove an existing hockey arena."""
        arenas = self.hockeyarray[league_sn].get('arenas', [])
        if not arenas:
            logger.error("ERROR: There are no Hockey Arenas to delete.")
            return

        arena_names = [arena['name'] for arena in arenas]
        self.display_list(arena_names, "Hockey Arenas")
        choice = self.prompt_selection(len(arenas), "Enter Hockey Arena number to remove: ")

        if choice is not None:
            arenaname = arenas[choice]['name']
            self.hockeyarray = pyhockeystats.RemoveHockeyArenaFromArray(
                self.hockeyarray, league_sn, arenaname
            )
            logger.info("Hockey Arena '{}' removed successfully from league '{}'.".format(arenaname, league_sn))

    def edit_arena(self, league_sn):
        """Edit an existing hockey arena."""
        arenas = self.hockeyarray[league_sn].get('arenas', [])
        if not arenas:
            logger.error("ERROR: There are no Hockey Arenas to edit.")
            return

        arena_names = [arena['name'] for arena in arenas]
        self.display_list(arena_names, "Hockey Arenas")
        choice = self.prompt_selection(len(arenas), "Enter Hockey Arena number to edit: ")

        if choice is not None:
            old_arenaname = arenas[choice]['name']
            new_arenaname = self.prompt_input("Enter new Hockey Arena name: ")
            if any(arena['name'] == new_arenaname for arena in self.hockeyarray.get(league_sn, {}).get('arenas', [])):
                logger.error("ERROR: Hockey Arena with that name already exists.")
                return

            # Collect optional updates
            cityname = self.prompt_input("Enter new Hockey Arena city name (press Enter to skip): ") or None
            areaname = self.prompt_input("Enter new Hockey Arena area name (press Enter to skip): ") or None
            countryname = self.prompt_input("Enter new Hockey Arena country name (press Enter to skip): ") or None
            fullcountryname = self.prompt_input("Enter new Hockey Arena full country name (press Enter to skip): ") or None
            fullareaname = self.prompt_input("Enter new Hockey Arena full area name (press Enter to skip): ") or None

            self.hockeyarray = pyhockeystats.ReplaceHockeyArenaInArray(
                self.hockeyarray, league_sn, old_arenaname, new_arenaname,
                cityname, areaname, countryname, fullcountryname, fullareaname
            )
            logger.info("Hockey Arena '{}' updated successfully to '{}' in league '{}'.".format(
                old_arenaname, new_arenaname, league_sn))

    def manage_games(self):
        """Manage hockey games."""
        leagues = self.hockeyarray.get('leaguelist', [])
        if not leagues:
            logger.error("ERROR: There are no Hockey Leagues.")
            return

        self.display_list(leagues, "Hockey Leagues")
        league_index = self.prompt_selection(len(leagues), "Enter Hockey League number: ")
        if league_index is None:
            return

        league_sn = leagues[league_index]

        submenu_options = {
            '1': lambda: self.add_game(league_sn),
            '2': lambda: self.remove_game(league_sn),
            '3': lambda: self.edit_game(league_sn),
            '4': lambda: self.move_game(league_sn)
        }

        while True:
            choice = self.get_user_choice(
                "E: Back to Main Menu\n"
                "1: Add Hockey Game\n"
                "2: Remove Hockey Game\n"
                "3: Edit Hockey Game\n"
                "4: Move Hockey Game\n"
                "What would you like to do? ",
                choices=['E', '1', '2', '3', '4']
            )

            if choice == 'E':
                break

            action = submenu_options.get(choice)
            if action:
                action()
            else:
                logger.error("ERROR: Invalid Command.")

    def add_game(self, league_sn):
        """Add a new hockey game."""
        date = self.prompt_input("Enter Game Date (YYYY-MM-DD): ")
        time = self.prompt_input("Enter Game Time (HH:MM): ")
        hometeam = self.prompt_input("Enter Home Team Full Name: ")
        awayteam = self.prompt_input("Enter Away Team Full Name: ")
        periodsscore = self.prompt_input("Enter Periods' Score: ")
        shotsongoal = self.prompt_input("Enter Shots on Goal: ")
        ppgoals = self.prompt_input("Enter Power-Play Goals: ")
        shgoals = self.prompt_input("Enter Short-Handed Goals: ")
        periodpens = self.prompt_input("Enter Period Penalties: ")
        periodpims = self.prompt_input("Enter Period PIMs: ")
        periodhits = self.prompt_input("Enter Period Hits: ")
        takeaways = self.prompt_input("Enter Takeaways: ")
        faceoffwins = self.prompt_input("Enter Faceoff Wins: ")
        atarena = self.prompt_input("Enter Arena Name: ")
        isplayoffgame = self.prompt_input("Is Playoff Game? (yes/no): ").lower()

        self.hockeyarray = pyhockeystats.AddHockeyGameToArray(
            self.hockeyarray, league_sn, date, time, hometeam, awayteam,
            periodsscore, shotsongoal, ppgoals, shgoals, periodpens,
            periodpims, periodhits, takeaways, faceoffwins, atarena,
            isplayoffgame
        )
        logger.info("Hockey Game between '{}' and '{}' on {} added successfully.".format(
            hometeam, awayteam, date))

    def remove_game(self, league_sn):
        """Remove an existing hockey game."""
        games = self.hockeyarray[league_sn].get('games', [])
        if not games:
            logger.error("ERROR: There are no Hockey Games to delete.")
            return

        game_descriptions = [
            "{} {} - {} vs {}".format(game['date'], game['time'], game['hometeam'], game['awayteam'])
            for game in games
        ]
        self.display_list(game_descriptions, "Hockey Games")
        choice = self.prompt_selection(len(games), "Enter Hockey Game number to remove: ")

        if choice is not None:
            game = games[choice]
            self.hockeyarray = pyhockeystats.RemoveHockeyGameFromArray(
                self.hockeyarray, league_sn, game['date'], game['hometeam'], game['awayteam']
            )
            logger.info("Hockey Game between '{}' and '{}' on {} removed successfully.".format(
                game['hometeam'], game['awayteam'], game['date']))

    def edit_game(self, league_sn):
        """Edit an existing hockey game."""
        games = self.hockeyarray[league_sn].get('games', [])
        if not games:
            logger.error("ERROR: There are no Hockey Games to edit.")
            return

        game_descriptions = [
            "{} {} - {} vs {}".format(game['date'], game['time'], game['hometeam'], game['awayteam'])
            for game in games
        ]
        self.display_list(game_descriptions, "Hockey Games")
        choice = self.prompt_selection(len(games), "Enter Hockey Game number to edit: ")

        if choice is not None:
            game = games[choice]
            olddate = game['date']
            oldhometeam = game['hometeam']
            oldawayteam = game['awayteam']

            # Collect optional updates
            newdate = self.prompt_input("Enter new Game Date (YYYY-MM-DD) (press Enter to skip): ") or None
            newtime = self.prompt_input("Enter new Game Time (HH:MM) (press Enter to skip): ") or None
            newhometeam = self.prompt_input("Enter new Home Team Full Name (press Enter to skip): ") or None
            newawayteam = self.prompt_input("Enter new Away Team Full Name (press Enter to skip): ") or None
            periodsscore = self.prompt_input("Enter new Periods' Score (press Enter to skip): ") or None
            shotsongoal = self.prompt_input("Enter new Shots on Goal (press Enter to skip): ") or None
            ppgoals = self.prompt_input("Enter new Power-Play Goals (press Enter to skip): ") or None
            shgoals = self.prompt_input("Enter new Short-Handed Goals (press Enter to skip): ") or None
            periodpens = self.prompt_input("Enter new Period Penalties (press Enter to skip): ") or None
            periodpims = self.prompt_input("Enter new Period PIMs (press Enter to skip): ") or None
            periodhits = self.prompt_input("Enter new Period Hits (press Enter to skip): ") or None
            takeaways = self.prompt_input("Enter new Takeaways (press Enter to skip): ") or None
            faceoffwins = self.prompt_input("Enter new Faceoff Wins (press Enter to skip): ") or None
            atarena = self.prompt_input("Enter new Arena Name (press Enter to skip): ") or None
            isplayoffgame = self.prompt_input("Is Playoff Game? (yes/no) (press Enter to skip): ").lower() or None

            self.hockeyarray = pyhockeystats.ReplaceHockeyGameInArray(
                self.hockeyarray, league_sn, olddate, oldhometeam, oldawayteam,
                newdate, newtime, newhometeam, newawayteam, periodsscore,
                shotsongoal, ppgoals, shgoals, periodpens, periodpims,
                periodhits, takeaways, faceoffwins, atarena, isplayoffgame
            )
            logger.info("Hockey Game on {} between '{}' and '{}' updated successfully.".format(
                olddate, oldhometeam, oldawayteam))

    def move_game(self, league_sn):
        """Move a hockey game to another league (if applicable)."""
        # Assuming moving a game between leagues is not typical, but the function is added for completeness.
        logger.error("ERROR: Moving games between leagues is not implemented.")
        print("Moving games between leagues is not supported at this time.")

    def manage_database(self):
        """Manage hockey database (import/export)."""
        submenu_options = {
            '1': self.create_empty_database,
            '2': self.import_database,
            '3': self.export_database_menu
        }

        while True:
            choice = self.get_user_choice(
                "E: Back to Main Menu\n"
                "1: Empty Hockey Database\n"
                "2: Import Hockey Database From File\n"
                "3: Export Hockey Database to File\n"
                "What would you like to do? ",
                choices=['E', '1', '2', '3']
            )

            if choice == 'E':
                break

            action = submenu_options.get(choice)
            if action:
                action()
            else:
                logger.error("ERROR: Invalid Command.")

    def export_database_menu(self):
        """Submenu for exporting the database to various formats."""
        export_options = {
            '1': ('xml', pyhockeystats.MakeHockeyXMLFileFromHockeyArray),
            '2': ('sgml', pyhockeystats.MakeHockeySGMLFileFromHockeyArray),
            '3': ('json', pyhockeystats.MakeHockeyJSONFileFromHockeyArray),
            '4': ('py', pyhockeystats.MakeHockeyPythonFileFromHockeyArray),
            '5': ('pyalt', pyhockeystats.MakeHockeyPythonAltFileFromHockeyArray),
            '6': ('oopy', pyhockeystats.MakeHockeyPythonOOPFileFromHockeyArray),
            '7': ('oopyalt', pyhockeystats.MakeHockeyPythonOOPAltFileFromHockeyArray),
            '8': ('sql', pyhockeystats.MakeHockeySQLFileFromHockeyArray),
            '9': ('db3', pyhockeystats.MakeHockeyDatabaseFromHockeyArray)
        }

        while True:
            choice = self.get_user_choice(
                "E: Back to Hockey Database Tool\n"
                "1: Export to Hockey XML\n"
                "2: Export to Hockey SGML\n"
                "3: Export to Hockey JSON\n"
                "4: Export to Hockey Python\n"
                "5: Export to Hockey Python Alt\n"
                "6: Export to Hockey Python OOP\n"
                "7: Export to Hockey Python OOP Alt\n"
                "8: Export to Hockey SQL\n"
                "9: Export to Hockey Database File\n"
                "What would you like to do? ",
                choices=[str(i) for i in range(1, 10)] + ['E']
            )

            if choice == 'E':
                break

            export_info = export_options.get(choice)
            if export_info:
                export_type, export_func = export_info
                outfile = self.prompt_filename("Enter Hockey Database File Name to Export: ")
                try:
                    export_func(self.hockeyarray, outfile, verbose=self.args.verbose, verbosetype=self.args.verbosetype)
                    logger.info("Exported database to: {}".format(outfile))
                except Exception as e:
                    logger.error("ERROR: Failed to export database. {}".format(e))
            else:
                logger.error("ERROR: Invalid Command.")

    def prompt_input(self, prompt_text):
        """Prompt the user for input."""
        try:
            return raw_input(prompt_text).strip()
        except NameError:
            return input(prompt_text).strip()

    def prompt_filename(self, prompt_text):
        """Prompt the user for a filename."""
        while True:
            filename = self.prompt_input(prompt_text)
            if filename:
                return filename
            else:
                print("Filename cannot be empty. Please try again.")

    def display_list(self, items, title):
        """Display a list of items with indices."""
        print("\n{}:".format(title))
        for idx, item in enumerate(items):
            print("{0}: {1}".format(idx, item))
        print()

    def prompt_selection(self, max_index, prompt_text):
        """Prompt the user to select an item from a list."""
        while True:
            selection = self.prompt_input(prompt_text)
            if selection.upper() == 'E':
                return None
            if selection.isdigit():
                index = int(selection)
                if 0 <= index < max_index:
                    return index
            print("ERROR: Invalid Command.")

    def get_user_choice(self, prompt_text, choices):
        """Prompt the user to make a choice from the given options."""
        while True:
            choice = self.prompt_input(prompt_text).upper()
            if choice in choices:
                return choice
            print("ERROR: Invalid Command.")


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Hockey Management Tool: Manage hockey games and stats.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "-v", "--version",
        action="version",
        version="%(prog)s {}".format(pyhockeystats.__version__)
    )
    parser.add_argument(
        "-i", "--infile",
        type=str,
        help="Specify the input database file to load."
    )
    parser.add_argument(
        "-e", "--empty",
        action="store_true",
        help="Create an empty database file."
    )
    parser.add_argument(
        "-o", "--outfile",
        type=str,
        help="Specify the output database file to save."
    )
    parser.add_argument(
        "-x", "--export",
        action="store_true",
        help="Export the input file to the database."
    )
    parser.add_argument(
        "-t", "--type",
        type=str,
        choices=['xml', 'sgml', 'json', 'py', 'pyalt', 'oopy', 'oopyalt', 'sql', 'db3'],
        help="Specify the type of file to export."
    )
    parser.add_argument(
        "-V", "--verbose",
        action="store_true",
        help="Enable verbose output for debugging information."
    )
    parser.add_argument(
        "-T", "--verbosetype",
        type=str,
        default="array",
        choices=['json', 'sgml', 'xml', 'array'],
        help="Set the verbosity type."
    )
    return parser.parse_args()


def main():
    """Main entry point for the script."""
    args = parse_arguments()

    # Configure logging level based on verbosity
    if args.verbose or os.getenv('VERBOSE') or os.getenv('DEBUG'):
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    tool = HockeyTool(args)
    tool.run()


if __name__ == "__main__":
    main()
