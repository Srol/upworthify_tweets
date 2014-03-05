upworthify_tweets
=================

A Twitter bot that converts headlines into Upworthy style. This is a work in progress(where work = a lot and progress = little) that was created as part of Thunderdome Serendipity Day 2014.

Right now all it does is take the top tweet of @Upworthify and adds a kicker to the end to make it sound like an Upworthy headline, when executed from the command line. It relies on the [python-twitter](https://github.com/bear/python-twitter) library to work. 

This is the first thing like this I've made, and the first thing I've pushed to Github. Everything about it is probably wrong. You've been warned.

**Contents**

* postfix.txt  - list of Upworthy-esque postfixes(I'm not sure if that's the right word).
* prefix.txt - list of Upworthy-esque prefixes (not yet implemented)
* upworthify.py - Actual script, edit to add your Twitter API keys, then execute at the command line.