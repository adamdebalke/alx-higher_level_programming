#!/bin/bash
#Script for show all HTTP methods the server will accept
curl -sL "$@" -X OPTIONS -i |  grep "Allow" | cut -d " " -f2-10
