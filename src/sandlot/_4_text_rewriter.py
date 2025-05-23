"""
Module: text_rewriter.py

Purpose:
    - Rewrites raw game log text by replacing recognized team names with their assigned UIDs.
    - Uses a lookup map generated from earlier parsing steps.
    - Ensures replacement is safe and exact, with no accidental partial matches.

Goal:
    - Provide a single function that takes in raw text and a team mapping,
      and returns a fully rewritten version of the text.
    - This module will be reused by the pipeline to standardize team identifiers
      across all exported formats.
"""

# TODO: Create a `replace_team_names` function

# TODO: Accept two arguments: raw text, and team map

# TODO: Compile a search pattern from the keys of the team map

# TODO: Use a replacement function to inject UIDs for matched team names

# TODO: Return the rewritten version of the input text
