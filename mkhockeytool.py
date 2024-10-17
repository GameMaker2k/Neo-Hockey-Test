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

$FileInfo: mkhockeytool.py - Last Update: 10/17/2024 Ver. 0.9.2 RC 1 - Author: cooldude2k $
"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import argparse
import logging
import os
import sys
import re

import pyhockeystats

from typing import Optional

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(format="%(message)s", stream=sys.stdout, level=logging.INFO)

# Compatibility for input function in Python 2 and 3
try:
    input = raw_input
except NameError:
    pass


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

    def determine_export_type(self) -> Optional[str]:
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
            '7': self.manage_database,
            '8': self.move_division_to_conference,
            '9': self.move_team_to_conference,
            '10': self.move_team_to_division
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
                "8: Move Division to Conference\n"
                "9: Move Team to Conference\n"
                "10: Move Team to Division\n"
                "What would you like to do? ",
                choices=['E', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
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
        sd = self.prompt_input("Enter Hockey League start date (YYYYMMDD): ")
        if not self.validate_date(sd):
            logger.error("ERROR: Invalid date format. Please use YYYYMMDD.")
            return
        pof = self.prompt_input("Enter Hockey League playoff format: ")
        ot = self.prompt_input("Enter Hockey League order type: ")
        hc = self.prompt_input("Does the Hockey League have conferences? (yes/no): ").lower()
        hd = self.prompt_input("Does the Hockey League have divisions? (yes/no): ").lower()

        if hc not in ['yes', 'no'] or hd not in ['yes', 'no']:
            logger.error("ERROR: Please respond with 'yes' or 'no'.")
            return

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
            current_league_info = self.hockeyarray.get(old_sn, {}).get('leagueinfo', {})

            new_sn = self.prompt_input("Enter new Hockey League short name (press Enter to keep current): ")
            new_sn = new_sn if new_sn else old_sn

            if new_sn != old_sn and new_sn in self.hockeyarray.get('leaguelist', []):
                logger.error("ERROR: Hockey League with that short name already exists.")
                return

            new_fn = self.prompt_input("Enter new Hockey League full name (press Enter to keep current): ") or current_league_info.get('fullname', '')
            new_csn = self.prompt_input("Enter new Hockey League country short name (press Enter to keep current): ") or current_league_info.get('country_short', '')
            new_cfn = self.prompt_input("Enter new Hockey League country full name (press Enter to keep current): ") or current_league_info.get('country_full', '')
            new_sd = self.prompt_input("Enter new Hockey League start date (YYYYMMDD) (press Enter to keep current): ") or current_league_info.get('start_date', '')
            if new_sd and new_sd != current_league_info.get('start_date', '') and not self.validate_date(new_sd):
                logger.error("ERROR: Invalid date format. Please use YYYYMMDD.")
                return
            new_pof = self.prompt_input("Enter new Hockey League playoff format (press Enter to keep current): ") or current_league_info.get('playoff_format', '')
            new_ot = self.prompt_input("Enter new Hockey League order type (press Enter to keep current): ") or current_league_info.get('order_type', '')
            new_hc = self.prompt_input("Does the Hockey League have conferences? (yes/no) (press Enter to keep current): ").lower() or current_league_info.get('conferences', 'no')
            new_hd = self.prompt_input("Does the Hockey League have divisions? (yes/no) (press Enter to keep current): ").lower() or current_league_info.get('divisions', 'no')

            if new_hc not in ['yes', 'no'] or new_hd not in ['yes', 'no']:
                logger.error("ERROR: Please respond with 'yes' or 'no'.")
                return

            self.hockeyarray = pyhockeystats.ReplaceHockeyLeagueFromArray(
                self.hockeyarray, old_sn, new_sn, new_fn, new_csn, new_cfn,
                new_sd, new_pof, new_ot, new_hc, new_hd
            )

            if new_hc == "no" and current_league_info.get('conferences', 'no') != "no":
                self.hockeyarray = pyhockeystats.AddHockeyConferenceToArray(
                    self.hockeyarray, new_sn, ""
                )
            if new_hd == "no" and current_league_info.get('divisions', 'no') != "no":
                self.hockeyarray = pyhockeystats.AddHockeyDivisionToArray(
                    self.hockeyarray, new_sn, "", ""
                )
            logger.info("Hockey League '{}' updated successfully.".format(new_fn))

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
            logger.error("ERROR: Hockey League does not have conferences.")
            return

        submenu_options = {
            '1': lambda: self.add_conference(league_sn),
            '2': lambda: self.remove_conference(league_sn),
            '3': lambda: self.edit_conference(league_sn)
        }

        while True:
            choice = self.get_user_choice(
                "E: Back to Main Menu\n"
                "1: Add Hockey Conference\n"
                "2: Remove Hockey Conference\n"
                "3: Edit Hockey Conference\n"
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
            current_conference_info = self.hockeyarray[league_sn].get(old_cn, {}).get('conferenceinfo', {})

            new_cn = self.prompt_input("Enter new Hockey Conference name (press Enter to keep current): ")
            new_cn = new_cn if new_cn else old_cn

            if new_cn != old_cn and new_cn in self.hockeyarray[league_sn].get('conferencelist', []):
                logger.error("ERROR: Hockey Conference with that name already exists.")
                return

            new_cpf = self.prompt_input("Enter new Hockey Conference prefix (press Enter to keep current): ") or current_conference_info.get('prefix', '')
            new_csf = self.prompt_input("Enter new Hockey Conference suffix (press Enter to keep current): ") or current_conference_info.get('suffix', '')

            self.hockeyarray = pyhockeystats.ReplaceHockeyConferenceFromArray(
                self.hockeyarray, league_sn, old_cn, new_cn, new_cpf, new_csf
            )
            logger.info("Hockey Conference '{}' updated successfully in league '{}'.".format(new_cn, league_sn))

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
        if self.hockeyarray[league_sn]['leagueinfo'].get('divisions', 'no') != "yes":
            logger.error("ERROR: Hockey League does not have divisions.")
            return

        submenu_options = {
            '1': lambda: self.add_division(league_sn),
            '2': lambda: self.remove_division(league_sn),
            '3': lambda: self.edit_division(league_sn)
        }

        while True:
            choice = self.get_user_choice(
                "E: Back to Main Menu\n"
                "1: Add Hockey Division\n"
                "2: Remove Hockey Division\n"
                "3: Edit Hockey Division\n"
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

    def add_division(self, league_sn, conference_sn=None):
        """Add a new hockey division to a league or conference."""
        dn = self.prompt_input("Enter Hockey Division name: ")
        target = 'conferencelist' if conference_sn else 'divisionlist'
        if dn in self.hockeyarray[league_sn].get(target, []):
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
            current_division_info = self.hockeyarray[league_sn].get(target, {}).get(old_dn, {}).get('divisioninfo', {})

            new_dn = self.prompt_input("Enter new Hockey Division name (press Enter to keep current): ")
            new_dn = new_dn if new_dn else old_dn

            if new_dn != old_dn and new_dn in self.hockeyarray[league_sn].get(target, []):
                logger.error("ERROR: Hockey Division with that name already exists.")
                return

            new_dpf = self.prompt_input("Enter new Hockey Division prefix (press Enter to keep current): ") or current_division_info.get('prefix', '')
            new_dsf = self.prompt_input("Enter new Hockey Division suffix (press Enter to keep current): ") or current_division_info.get('suffix', '')

            self.hockeyarray = pyhockeystats.ReplaceHockeyDivisionFromArray(
                self.hockeyarray, league_sn, new_dn, old_dn, conference_sn, new_dpf, new_dsf
            )
            location = "conference '{}' in league '{}'".format(conference_sn, league_sn) if conference_sn else "league '{}'".format(league_sn)
            logger.info("Hockey Division '{}' updated successfully to '{}' in {}.".format(old_dn, new_dn, location))

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

        # Determine if the league has conferences
        has_conferences = self.hockeyarray[league_sn]['leagueinfo'].get('conferences', 'no') == "yes"
        conferences = self.hockeyarray[league_sn].get('conferencelist', []) if has_conferences else []
        if conferences:
            self.display_list(conferences, "Hockey Conferences")
            conference_choice = self.prompt_selection(len(conferences), "Enter Hockey Conference number (or 'E' to skip): ")
            if conference_choice is not None:
                conference_sn = conferences[conference_choice]
            else:
                conference_sn = None
        else:
            conference_sn = None

        # Determine divisions based on conference presence
        if conference_sn:
            has_divisions = self.hockeyarray[league_sn]['leagueinfo'].get('divisions', 'no') == "yes"
            divisions = self.hockeyarray[league_sn].get('conferencelist', {}).get(conference_sn, {}).get('divisionlist', []) if has_divisions else []
        else:
            has_divisions = self.hockeyarray[league_sn]['leagueinfo'].get('divisions', 'no') == "yes"
            divisions = self.hockeyarray[league_sn].get('divisionlist', []) if has_divisions else []

        if has_divisions:
            self.display_list(divisions, "Hockey Divisions")
            division_choice = self.prompt_selection(len(divisions), "Enter Hockey Division number: ")
            if division_choice is None:
                return
            division_sn = divisions[division_choice]
        else:
            division_sn = None

        submenu_options = {
            '1': lambda: self.add_team(league_sn, conference_sn, division_sn),
            '2': lambda: self.remove_team(league_sn, conference_sn, division_sn),
            '3': lambda: self.edit_team(league_sn, conference_sn, division_sn)
        }

        while True:
            choice = self.get_user_choice(
                "E: Back to Main Menu\n"
                "1: Add Hockey Team\n"
                "2: Remove Hockey Team\n"
                "3: Edit Hockey Team\n"
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

    def add_team(self, league_sn, conference_sn, division_sn):
        """Add a new hockey team."""
        teamname = self.prompt_input("Enter Hockey Team name: ")
        if conference_sn and division_sn:
            existing_teams = self.hockeyarray[league_sn].get('conferencelist', {}).get(conference_sn, {}).get(division_sn, {}).get('teamlist', [])
        elif division_sn:
            existing_teams = self.hockeyarray[league_sn].get('divisionlist', {}).get(division_sn, {}).get('teamlist', [])
        else:
            existing_teams = self.hockeyarray[league_sn].get('teamlist', [])

        if teamname in existing_teams:
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
        location = "conference '{}' and division '{}'".format(conference_sn, division_sn) if conference_sn and division_sn else "league '{}'".format(league_sn)
        logger.info("Hockey Team '{}' added successfully to {}.".format(teamname, location))

    def remove_team(self, league_sn, conference_sn, division_sn):
        """Remove an existing hockey team."""
        if conference_sn and division_sn:
            teams = self.hockeyarray[league_sn].get('conferencelist', {}).get(conference_sn, {}).get(division_sn, {}).get('teamlist', [])
        elif division_sn:
            teams = self.hockeyarray[league_sn].get('divisionlist', {}).get(division_sn, {}).get('teamlist', [])
        else:
            teams = self.hockeyarray[league_sn].get('teamlist', [])

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
            location = "conference '{}' and division '{}'".format(conference_sn, division_sn) if conference_sn and division_sn else "league '{}'".format(league_sn)
            logger.info("Hockey Team '{}' removed successfully from {}.".format(teamname, location))

    def edit_team(self, league_sn, conference_sn, division_sn):
        """Edit an existing hockey team."""
        if conference_sn and division_sn:
            teams = self.hockeyarray[league_sn].get('conferencelist', {}).get(conference_sn, {}).get(division_sn, {}).get('teamlist', [])
        elif division_sn:
            teams = self.hockeyarray[league_sn].get('divisionlist', {}).get(division_sn, {}).get('teamlist', [])
        else:
            teams = self.hockeyarray[league_sn].get('teamlist', [])

        if not teams:
            logger.error("ERROR: There are no Hockey Teams to edit.")
            return

        self.display_list(teams, "Hockey Teams")
        choice = self.prompt_selection(len(teams), "Enter Hockey Team number to edit: ")

        if choice is not None:
            oldteamname = teams[choice]
            if conference_sn and division_sn:
                current_team_info = self.hockeyarray[league_sn].get('conferencelist', {}).get(conference_sn, {}).get(division_sn, {}).get(oldteamname, {}).get('teaminfo', {})
            elif division_sn:
                current_team_info = self.hockeyarray[league_sn].get('divisionlist', {}).get(division_sn, {}).get(oldteamname, {}).get('teaminfo', {})
            else:
                current_team_info = self.hockeyarray[league_sn].get(oldteamname, {}).get('teaminfo', {})

            newteamname = self.prompt_input("Enter new Hockey Team name (press Enter to keep current): ")
            newteamname = newteamname if newteamname else oldteamname

            if newteamname != oldteamname:
                if conference_sn and division_sn:
                    existing_teams = self.hockeyarray[league_sn].get('conferencelist', {}).get(conference_sn, {}).get(division_sn, {}).get('teamlist', [])
                elif division_sn:
                    existing_teams = self.hockeyarray[league_sn].get('divisionlist', {}).get(division_sn, {}).get('teamlist', [])
                else:
                    existing_teams = self.hockeyarray[league_sn].get('teamlist', [])

                if newteamname in existing_teams:
                    logger.error("ERROR: Hockey Team with that name already exists.")
                    return

            # Collect optional updates
            cityname = self.prompt_input("Enter new Hockey Team city name (press Enter to keep current): ") or current_team_info.get('city', '')
            areaname = self.prompt_input("Enter new Hockey Team area name (press Enter to keep current): ") or current_team_info.get('area', '')
            countryname = self.prompt_input("Enter new Hockey Team country name (press Enter to keep current): ") or current_team_info.get('country', '')
            fullareaname = self.prompt_input("Enter new Hockey Team full area name (press Enter to keep current): ") or current_team_info.get('full_area', '')
            fullcountryname = self.prompt_input("Enter new Hockey Team full country name (press Enter to keep current): ") or current_team_info.get('full_country', '')
            arenaname = self.prompt_input("Enter new Hockey Team arena name (press Enter to keep current): ") or current_team_info.get('arena', '')
            teamnameprefix = self.prompt_input("Enter new Hockey Team name prefix (press Enter to keep current): ") or current_team_info.get('prefix', '')
            teamnamesuffix = self.prompt_input("Enter new Hockey Team name suffix (press Enter to keep current): ") or current_team_info.get('suffix', '')
            teamaffiliates = self.prompt_input("Enter new Hockey Team affiliates (press Enter to keep current): ") or current_team_info.get('affiliates', '')

            self.hockeyarray = pyhockeystats.ReplaceHockeyTeamFromArray(
                self.hockeyarray, league_sn, oldteamname, newteamname, conference_sn, division_sn,
                cityname, areaname, countryname, fullcountryname, fullareaname,
                arenaname, teamnameprefix, teamnamesuffix, teamaffiliates
            )
            location = "conference '{}' and division '{}'".format(conference_sn, division_sn) if conference_sn and division_sn else "league '{}'".format(league_sn)
            logger.info("Hockey Team '{}' updated successfully to '{}' in {}.".format(oldteamname, newteamname, location))

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
            current_arena_info = self.hockeyarray[league_sn].get('arenas', []).get(old_arenaname, {}).get('arenainfo', {})

            new_arenaname = self.prompt_input("Enter new Hockey Arena name (press Enter to keep current): ")
            new_arenaname = new_arenaname if new_arenaname else old_arenaname

            if new_arenaname != old_arenaname and any(arena['name'] == new_arenaname for arena in self.hockeyarray[league_sn].get('arenas', [])):
                logger.error("ERROR: Hockey Arena with that name already exists.")
                return

            # Collect optional updates
            cityname = self.prompt_input("Enter new Hockey Arena city name (press Enter to keep current): ") or current_arena_info.get('city', '')
            areaname = self.prompt_input("Enter new Hockey Arena area name (press Enter to keep current): ") or current_arena_info.get('area', '')
            countryname = self.prompt_input("Enter new Hockey Arena country name (press Enter to keep current): ") or current_arena_info.get('country', '')
            fullcountryname = self.prompt_input("Enter new Hockey Arena full country name (press Enter to keep current): ") or current_arena_info.get('full_country', '')
            fullareaname = self.prompt_input("Enter new Hockey Arena full area name (press Enter to keep current): ") or current_arena_info.get('full_area', '')

            self.hockeyarray = pyhockeystats.ReplaceHockeyArenaInArray(
                self.hockeyarray, league_sn, old_arenaname, new_arenaname,
                cityname, areaname, countryname, fullcountryname, fullareaname
            )
            logger.info("Hockey Arena '{}' updated successfully to '{}' in league '{}'.".format(old_arenaname, new_arenaname, league_sn))

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
            '3': lambda: self.edit_game(league_sn)
        }

        while True:
            choice = self.get_user_choice(
                "E: Back to Main Menu\n"
                "1: Add Hockey Game\n"
                "2: Remove Hockey Game\n"
                "3: Edit Hockey Game\n"
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

    def add_game(self, league_sn):
        """Add a new hockey game."""
        date = self.prompt_input("Enter Game Date (YYYYMMDD): ")
        if not self.validate_date(date):
            logger.error("ERROR: Invalid date format. Please use YYYYMMDD.")
            return

        time = self.prompt_input("Enter Game Time (HH:MM): ")
        if not self.validate_time(time):
            logger.error("ERROR: Invalid time format. Please use HH:MM.")
            return

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
        if isplayoffgame not in ['yes', 'no']:
            logger.error("ERROR: Please respond with 'yes' or 'no'.")
            return

        self.hockeyarray = pyhockeystats.AddHockeyGameToArray(
            self.hockeyarray, league_sn, date, time, hometeam, awayteam,
            periodsscore, shotsongoal, ppgoals, shgoals, periodpens,
            periodpims, periodhits, takeaways, faceoffwins, atarena,
            isplayoffgame
        )
        logger.info("Hockey Game between '{}' and '{}' on {} added successfully.".format(hometeam, awayteam, date))

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
            logger.info("Hockey Game between '{}' and '{}' on {} removed successfully.".format(game['hometeam'], game['awayteam'], game['date']))

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
            oldtime = game['time']
            oldhometeam = game['hometeam']
            oldawayteam = game['awayteam']

            # Collect optional updates
            newdate = self.prompt_input("Enter new Game Date (YYYYMMDD) (press Enter to keep current): ") or olddate
            if newdate != olddate and not self.validate_date(newdate):
                logger.error("ERROR: Invalid date format. Please use YYYYMMDD.")
                return

            newtime = self.prompt_input("Enter new Game Time (HH:MM) (press Enter to keep current): ") or oldtime
            if newtime != oldtime and not self.validate_time(newtime):
                logger.error("ERROR: Invalid time format. Please use HH:MM.")
                return

            newhometeam = self.prompt_input("Enter new Home Team Full Name (press Enter to keep current): ") or oldhometeam
            newawayteam = self.prompt_input("Enter new Away Team Full Name (press Enter to keep current): ") or oldawayteam
            periodsscore = self.prompt_input("Enter new Periods' Score (press Enter to keep current): ") or game['goals']
            shotsongoal = self.prompt_input("Enter new Shots on Goal (press Enter to keep current): ") or game['sogs']
            ppgoals = self.prompt_input("Enter new Power-Play Goals (press Enter to keep current): ") or game['ppgs']
            shgoals = self.prompt_input("Enter new Short-Handed Goals (press Enter to keep current): ") or game['shgs']
            periodpens = self.prompt_input("Enter new Period Penalties (press Enter to keep current): ") or game['penalties']
            periodpims = self.prompt_input("Enter new Period PIMs (press Enter to keep current): ") or game['pims']
            periodhits = self.prompt_input("Enter new Period Hits (press Enter to keep current): ") or game['hits']
            takeaways = self.prompt_input("Enter new Takeaways (press Enter to keep current): ") or game['takeaways']
            faceoffwins = self.prompt_input("Enter new Faceoff Wins (press Enter to keep current): ") or game['faceoffwins']
            atarena = self.prompt_input("Enter new Arena Name (press Enter to keep current): ") or game['atarena']
            isplayoffgame = self.prompt_input("Is Playoff Game? (yes/no) (press Enter to keep current): ").lower() or game['isplayoffgame']
            if isplayoffgame not in ['yes', 'no']:
                logger.error("ERROR: Please respond with 'yes' or 'no'.")
                return

            self.hockeyarray = pyhockeystats.ReplaceHockeyGameInArray(
                self.hockeyarray, league_sn, olddate, oldhometeam, oldawayteam,
                newdate, newtime, newhometeam, newawayteam, periodsscore,
                shotsongoal, ppgoals, shgoals, periodpens, periodpims,
                periodhits, takeaways, faceoffwins, atarena, isplayoffgame
            )
            logger.info("Hockey Game on '{}' between '{}' and '{}' updated successfully.".format(newdate, newhometeam, newawayteam))

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

    def move_division_to_conference(self):
        """Move a hockey division from one conference to another."""
        leagues = self.hockeyarray.get('leaguelist', [])
        if not leagues:
            logger.error("ERROR: There are no Hockey Leagues.")
            return

        self.display_list(leagues, "Hockey Leagues")
        league_index = self.prompt_selection(len(leagues), "Enter Hockey League number: ")
        if league_index is None:
            return

        league_sn = leagues[league_index]

        conferences = self.hockeyarray[league_sn].get('conferencelist', [])
        if len(conferences) < 2:
            logger.error("ERROR: Not enough conferences to perform move.")
            return

        self.display_list(conferences, "Hockey Conferences")
        old_conference_index = self.prompt_selection(len(conferences), "Enter source Hockey Conference number: ")
        if old_conference_index is None:
            return
        old_conference_sn = conferences[old_conference_index]

        new_conference_index = self.prompt_selection(len(conferences), "Enter destination Hockey Conference number: ")
        if new_conference_index is None:
            return
        new_conference_sn = conferences[new_conference_index]

        if old_conference_sn == new_conference_sn:
            logger.error("ERROR: Source and destination conferences are the same.")
            return

        divisions = self.hockeyarray[league_sn].get('conferencelist', {}).get(old_conference_sn, {}).get('divisionlist', [])
        if not divisions:
            logger.error("ERROR: No divisions found in the source conference.")
            return

        self.display_list(divisions, "Hockey Divisions in Conference '{}'".format(old_conference_sn))
        division_index = self.prompt_selection(len(divisions), "Enter Hockey Division number to move: ")
        if division_index is None:
            return
        division_sn = divisions[division_index]

        self.hockeyarray = pyhockeystats.MoveHockeyDivisionToConferenceFromArray(
            self.hockeyarray, league_sn, division_sn, old_conference_sn, new_conference_sn
        )
        logger.info("Hockey Division '{}' moved from conference '{}' to '{}'.".format(division_sn, old_conference_sn, new_conference_sn))

    def move_team_to_conference(self):
        """Move a hockey team from one conference to another."""
        leagues = self.hockeyarray.get('leaguelist', [])
        if not leagues:
            logger.error("ERROR: There are no Hockey Leagues.")
            return

        self.display_list(leagues, "Hockey Leagues")
        league_index = self.prompt_selection(len(leagues), "Enter Hockey League number: ")
        if league_index is None:
            return

        league_sn = leagues[league_index]

        conferences = self.hockeyarray[league_sn].get('conferencelist', [])
        if len(conferences) < 2:
            logger.error("ERROR: Not enough conferences to perform move.")
            return

        self.display_list(conferences, "Hockey Conferences")
        old_conference_index = self.prompt_selection(len(conferences), "Enter source Hockey Conference number: ")
        if old_conference_index is None:
            return
        old_conference_sn = conferences[old_conference_index]

        new_conference_index = self.prompt_selection(len(conferences), "Enter destination Hockey Conference number: ")
        if new_conference_index is None:
            return
        new_conference_sn = conferences[new_conference_index]

        if old_conference_sn == new_conference_sn:
            logger.error("ERROR: Source and destination conferences are the same.")
            return

        # Get all teams from old conference
        old_conference_info = self.hockeyarray[league_sn].get('conferencelist', {}).get(old_conference_sn, {})
        divisions = old_conference_info.get('divisionlist', [])
        teams = []
        for division in divisions:
            teams_in_division = self.hockeyarray[league_sn].get('conferencelist', {}).get(old_conference_sn, {}).get(division, {}).get('teamlist', [])
            teams.extend(teams_in_division)

        if not teams:
            logger.error("ERROR: There are no Hockey Teams to move in the source conference.")
            return

        self.display_list(teams, "Hockey Teams in Conference '{}'".format(old_conference_sn))
        team_index = self.prompt_selection(len(teams), "Enter Hockey Team number to move: ")
        if team_index is None:
            return
        team_sn = teams[team_index]

        # Find the division of the team
        team_division = None
        for division in divisions:
            if team_sn in self.hockeyarray[league_sn].get('conferencelist', {}).get(old_conference_sn, {}).get(division, {}).get('teamlist', []):
                team_division = division
                break

        if not team_division:
            logger.error("ERROR: Division for the selected team not found.")
            return

        self.hockeyarray = pyhockeystats.MoveHockeyTeamToConferenceFromArray(
            self.hockeyarray, league_sn, team_sn, old_conference_sn, new_conference_sn, team_division
        )
        logger.info("Hockey Team '{}' moved from conference '{}' to '{}'.".format(team_sn, old_conference_sn, new_conference_sn))

    def move_team_to_division(self):
        """Move a hockey team from one division to another within the same conference."""
        leagues = self.hockeyarray.get('leaguelist', [])
        if not leagues:
            logger.error("ERROR: There are no Hockey Leagues.")
            return

        self.display_list(leagues, "Hockey Leagues")
        league_index = self.prompt_selection(len(leagues), "Enter Hockey League number: ")
        if league_index is None:
            return

        league_sn = leagues[league_index]

        conferences = self.hockeyarray[league_sn].get('conferencelist', [])
        if not conferences:
            logger.error("ERROR: There are no Hockey Conferences.")
            return

        self.display_list(conferences, "Hockey Conferences")
        conference_index = self.prompt_selection(len(conferences), "Enter Hockey Conference number: ")
        if conference_index is None:
            return
        conference_sn = conferences[conference_index]

        divisions = self.hockeyarray[league_sn].get('conferencelist', {}).get(conference_sn, {}).get('divisionlist', [])
        if len(divisions) < 2:
            logger.error("ERROR: Not enough divisions to perform move.")
            return

        self.display_list(divisions, "Hockey Divisions in Conference '{}'".format(conference_sn))
        old_division_index = self.prompt_selection(len(divisions), "Enter source Hockey Division number: ")
        if old_division_index is None:
            return
        old_division_sn = divisions[old_division_index]

        new_division_index = self.prompt_selection(len(divisions), "Enter destination Hockey Division number: ")
        if new_division_index is None:
            return
        new_division_sn = divisions[new_division_index]

        if old_division_sn == new_division_sn:
            logger.error("ERROR: Source and destination divisions are the same.")
            return

        teams = self.hockeyarray[league_sn].get('conferencelist', {}).get(conference_sn, {}).get(old_division_sn, {}).get('teamlist', [])
        if not teams:
            logger.error("ERROR: There are no Hockey Teams to move in the source division.")
            return

        self.display_list(teams, "Hockey Teams in Division '{}'".format(old_division_sn))
        team_index = self.prompt_selection(len(teams), "Enter Hockey Team number to move: ")
        if team_index is None:
            return
        team_sn = teams[team_index]

        self.hockeyarray = pyhockeystats.MoveHockeyTeamToDivisionFromArray(
            self.hockeyarray, league_sn, team_sn, conference_sn, old_division_sn, new_division_sn
        )
        logger.info("Hockey Team '{}' moved from division '{}' to '{}'.".format(team_sn, old_division_sn, new_division_sn))

    @staticmethod
    def prompt_input(prompt_text):
        """Prompt the user for input."""
        return input(prompt_text).strip()

    @staticmethod
    def prompt_filename(prompt_text):
        """Prompt the user for a filename."""
        while True:
            filename = input(prompt_text).strip()
            if filename:
                return filename
            else:
                print("Filename cannot be empty. Please try again.")

    @staticmethod
    def display_list(items, title):
        """Display a list of items with indices."""
        print("\n{}:".format(title))
        for idx, item in enumerate(items):
            print("{}: {}".format(idx, item))
        print()

    @staticmethod
    def prompt_selection(max_index, prompt_text):
        """Prompt the user to select an item from a list."""
        while True:
            selection = input(prompt_text).strip()
            if selection.upper() == 'E':
                return None
            if selection.isdigit():
                index = int(selection)
                if 0 <= index < max_index:
                    return index
            print("ERROR: Invalid selection. Please try again.")

    @staticmethod
    def get_user_choice(prompt_text, choices):
        """Prompt the user to make a choice from the given options."""
        while True:
            choice = input(prompt_text).strip().upper()
            if choice in choices:
                return choice
            print("ERROR: Invalid Command.")

    @staticmethod
    def validate_date(date_str):
        """Validate the date format YYYYMMDD."""
        return bool(re.match(r'^\d{8}$', date_str))

    @staticmethod
    def validate_time(time_str):
        """Validate the time format HH:MM."""
        return bool(re.match(r'^\d{2}:\d{2}$', time_str))


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
