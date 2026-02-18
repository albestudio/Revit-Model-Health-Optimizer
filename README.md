# pyRevit Model Health Optimizer

A powerful Python script designed for the pyRevit environment to maintain Revit model health. It automatically scans the project for unplaced rooms and unused views, purging them to reduce file size and keep the project environment clean and professional.

## Features
- **Smart Purge:** Identifies and deletes 'Unplaced' or 'Redundant' Rooms.
- **View Management:** Cleans up working views that are not placed on any sheets.
- Native UI integration using `pyrevit.forms`.

## Tech Stack
- Python (IronPython)
- pyRevit library
- Revit API
