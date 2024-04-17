# OSRS World Watcher
Service that monitors and reports OSRS world outages

> [!Note]
> Terms "world" and "server" are used [interchangably](https://oldschool.runescape.wiki/w/Server)

## Goal
Provide an accurate and reliable API that provides OSRS server statues, without overwhelming Jagex with requests. Right now, the service only determines if the worlds are online **as a whole**. Later iterations may report world availability per world/region

## Motivation
Mod Ashe confirmed my suspicion that the official OSRS server status page is manually updated, and is thus prone to inaccuracies

## How it works
A random selection of worlds are pinged to determined availability. If 80% or more respond, the game is considered "Online"