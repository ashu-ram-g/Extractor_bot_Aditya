#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


import os

class Config(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7428927891:AAHoNzLYya8aRaGF2y-ngluSxzy29LlN3XI")


    # Get from my.telegram.org (or @UseTGXBot)
    APP_ID = int(os.environ.get("APP_ID", "18116881"))
    API_HASH = os.environ.get("API_HASH", "cca3bacf40fb3ebcb4f075b2e46ff1bd")


    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1445673621").split())
    
