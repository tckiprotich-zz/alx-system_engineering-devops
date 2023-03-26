#!/usr/bin/env bash
# settig  up client SSH configuration file so that you can connect to a server without typing a password.

Host 132314-web-01
  IdentityFile ~/.ssh/school
  PasswordAuthentication no
