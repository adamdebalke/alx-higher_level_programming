#!/bin/bash
#Script of bash with show the size of the body of the response
curl -sI "$@" | awk '/Content-Length/{gsub("\\r", ""); print $2}'