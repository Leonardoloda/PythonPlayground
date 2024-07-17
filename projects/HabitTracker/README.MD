# Habit Tracker

Welcome to your habit tracker! This project allows you to keep a record of your daily activities using the Pixela API.
You can create users, manage graphs, and track activities easily through a command-line interface.

## Content

1. [Overview](#overview)
2. [Set up](#set-up)
3. [Usage](#usage)
4. [Main menu](#main-menu)
5. [Features](#features)

## Overview

This habit tracker application helps you monitor and track your daily habits. You can:

- Create and switch between users
- Create and manage graphs
- Track, update, and delete your daily activities

## Set up

1. Sign up for an API token at Pixela.
2. Create a .env file in the project directory and add your Pixela API token, username, and graph ID:

```env
TOKEN=your_pixela_token
USERNAME=your_pixela_username
GRAPH_ID=your_default_graph_id
```

## Usage

Run the script to start the habit tracker:

```bash
python main.py
```

## Main menu

You will be presented with a menu to choose from different options:

1. User Management:
    - Change to another user
    - Create a new user
    - Get the current user


2. Graph Management:

    - Create a new graph
    - Change to another graph

3. Activity Tracking:

    - Track today's activity
    - Update today's activity
    - Delete today's activity

## Features

User Management: Easily switch between different users or create new users.
Graph Management: Create and switch between different graphs to track various habits.
Activity Tracking: Track, update, and delete your daily activities with ease.