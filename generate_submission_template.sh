#!/usr/bin/env bash

set -euxo pipefail

./.generate_submission_template.py > submission-template.vbc
dos2unix submission-template.vbc

