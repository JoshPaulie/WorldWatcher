# OSRS World Watcher
Service that monitors and reports OSRS world outages

> [!Note]
> Terms "world" and "server" are used [interchangably](https://oldschool.runescape.wiki/w/Server)

> [!Caution]
> This all rides on the assumption that servers don't respond to pings when worlds are offline. If the host is responsible for multiple services, and not just hosting OS worlds, this whole endeavour may be a waste of time. We won't be able to know until I can run tests while the worlds are actually offline. 😄 

## Goal
Create an accurate and reliable API that provides OSRS server status, without overwhelming Jagex with requests.

## Motivation
Mod Ash [confirmed my suspicion](https://twitter.com/jagexash/status/1778147748614746203?s=61&t=xghr9cQv6o2eO4S6_hmg9w) that the official OSRS server status page is manually updated, and is thus prone to human error

## How it works
A random selection of worlds are pinged to determined availability. If 80% or more respond, the game is considered "online"

Right now, **WorldChecker** only determines if the game is online **as a whole**. Later iterations may report world availability per world/region