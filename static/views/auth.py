from flask import Flask
from flask import Blueprint, render_template, request, session, redirect, url_for, flash, json, Response
from dotenv import load_dotenv
load_dotenv()
import mysql.connector
import os

cnx = mysql.connector.connect(host = os.getenv("APP_URL"), user = os.getenv("DB_USERNAME"), password = os.getenv("DB_PASSWORD"), database = os.getenv("DB_DATABASE"))
cursor = cnx.cursor()

