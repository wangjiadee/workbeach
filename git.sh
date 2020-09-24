#!/bin/bash

set -x


git add .

git commit -m "[python][ralph.Build][1/1][BugId:N/A][无风险][无依赖][自然集成]{$1}"

git push 

