#!/bin/bash
#Scriptwith show the request status code
curl -soI --write-out '%{http_code}' $@
