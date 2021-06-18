#!/bin/bash
duration=$(soxi -D wn.wav)
aplay wn.wav | arecord -Dhw:0,0 --duration=70 -f dat -c 8 record$(date +"%Y_%m_%d_%I_%M_%p").wav