#!/usr/bin/env python
from django.core.management import setup_environ
import settings
setup_environ(settings)

import socket
from trivia.models import *

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((settings.IRC_SERVER, settings.IRC_PORT))

def send(msg):
   irc.send(msg + "\r\n")
   print "{SENT} " + msg
   return

def msg(user, msg):
   send("PRIVMSG " + user + " :" + msg)
   return

def processline(line):
   parts = line.split(' :',1)
   args = parts[0].split(' ')
   if (len(parts) > 1):
      args.append(parts[1])
   
   if args[0] == "PING":
      send("PONG :" + args[1])
      return

   try:
      if args[3] == "!questions":
         questions = str(Question.objects.all())
         msg(args[2], questions)
         return

   except IndexError:
      return

   # When we're done, remember to return.
   return
   

send("USER " + (settings.IRC_NICKNAME + " ")*4)
send("NICK " + settings.IRC_NICKNAME)
for channel in settings.IRC_CHANNELS:
   send("JOIN " + channel)

while True:
   # EXIST
   line = irc.recv(1024).rstrip()
   if "\r\n" in line:
      linesep = line.split()
      for l in linesep:
         processline(l)
      continue
   processline(line)




