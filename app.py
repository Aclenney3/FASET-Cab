import os
import sys
import json
import groupy
from groupy import Bot, Group, attachments

groupy.config.KEY_LOCATION = "39453642"

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def post():
  data = request.get_json()
  log('Recieved {}'.format(data))
  gID = data['group_id']
  bot = get_bot(gID)
  # We don't want to reply to ourselves!
  if data['name'] != bot.name:
  msg = data['text']
    if '@all' in msg:
      at_all(bot, group)
  return "ok", 200

def at_all(bot, group):
  members = group.members();

  user_ids = []
  loci = []
  text = ""
  pnt = 0

  for m in members:
    curm = m.identification()
    id = curm["user_id"]
    name = "@" + curm["nickname"] + " "

    user_ids.append(id)

    n = [pnt, len(name)]
    loci.append(n)
    pnt += len(name)

    text += name

  mention = {}
  mention["type"] = "mentions"
  mention["user_ids"] = user_ids
  mention["loci"] = loci

  bot.post(text, mention)

def get_bot(groupID):
  for b in Bot.list():
    if b.group_id == groupID:
      return b

def get_group(groupID):
  for g in Group.list():
    if g.group_id == groupID:
      return g

def log(msg):
  print(str(msg))
  sys.stdout.flush()
