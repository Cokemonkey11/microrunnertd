#!/usr/bin/env python

import sys
import textwrap

MAP_NAME           = "micro[/color]runner[color=#60A600]td"
AUTHOR             = "Cokemonkey11"

INTRODUCTION       = (

	"""

		microrunnertd is a tower defence map that draws inspiration from
		Gridlock, the once popular map by Envious. In this two-player map,
		players build towers along a labyrinth area that creeps can walk
		through. Where this map differs from traditional tower defence maps is
		in the path that creeps follow: in microrunnertd, the player controls a
		fragile runner which must evade the creeps while guiding them to their
		towers.

	""",

	"""

		There are 42 waves in total, including, among other special rounds, boss
		and spell immune ones. If, during any round, both players runners are
		killed, the game ends in a defeat.

	""",

	"""

		Utilize shared income and agreed running routes to boost your chances of
		winning, as this is a highly team-dependant game. However, do consider
		your first match as a practice run. The game becomes more difficult in
		[color=#ccff00]hard[/color] mode.

	"""
)

SCREENSHOTS        = (
	("Loading Screen",                      "https://i.imgur.com/8fRsYBo.jpg"),
	("Cinematic Shot",                      "https://i.imgur.com/JSHY3FU.jpg"),
	("Slaying Round 2",                     "https://i.imgur.com/BV0YMFI.jpg"),
	("Guiding Runner on a Strong Path",     "https://i.imgur.com/o3C902F.jpg"),
	("Many towers have Powerful Abilities", "https://i.imgur.com/AFknGc1.jpg")
)

ABILITIES          = ""

RACES              = (
	(
		"https://i.imgur.com/z0lD6IK.png",
		(
			"[b]Spirit[/b]: The spirit race specializes in magic and spell damage, but has a healthy mix of all damage types.",
			"Spirit has powerful crowd control and healing abilities.",
			"Spirit does exceptionally well against boss levels due to their Runner's Storm Bolt upgrade.",
			"Their ultimate tower is the Spiritlizard, which has global attack range."
		)
	),
	(
		"https://i.imgur.com/jeNkuFN.png",
		(
			"[b]Wasteland[/b]: The wasteland race specializes in piercing and siege damage, and generally has a lot of brute force power.",
			"Wasteland has some healing capabilities and exceptionally powerful anti-armor due to their Runner's Bristleburst upgrade.",
			"Wasteland has multiple high-tier towers that have additional attack attributes, making them more resilient to armor type variation in the late game.",
			"Their ultimate tower is the Windforge Harpy, which has a tri-attack."
		)
	),
	(
		"https://i.imgur.com/s98duTu.png",
		(
			"[b]Metal[/b]: The metal race specializes in normal damage, and in particular is designed to have few, high-power towers.",
			"Metal is generally an expensive race, and has the most difficult early-game, during which it depends on the basic tower.",
			"Metal's Runner has a strong armor type. This race has the strangest mechanics of the three, including an aura tower that can prevent towers from killing creeps.",
			"Metal has a tower that can gain power indefinitely. Their ultimate tower is the Leviathan Well, which summons the Leviathan to fight for you."
		)
	),
	(
		"https://i.imgur.com/wmTsBW5.png",
		(
			"[b]Beer[/b]: The beer race focuses on flavor over damage, and is otherwise a fairly basic race of simple towers.",
			"What the beer race lacks in surprises, it makes up for with a few exciting towers and runner upgrades.",
			"The beer race is quite vulnerable with the Unarmored armor type.",
			"The beer race has a strong support ability. Their ultimate tower is the Witch, which deals over 1500 chaos damage."
		)
	)
)

ITEMS              = ()

REPOSITORY_URI     = "https://bitbucket.org/Cokemonkey11/microrunnertd/"

CHANGELOG          = (
	(
		"1.1.1",
		"15 May 2019",
		(
			"[patch] spirit race's priest heal has been fixed.",
		)
	),

	(
		"1.1.0",
		"8 May 2019",
		(
			"A new ace has been added - Beer.",
			"Bandito Masterino (first boss) now casts divine shield when attacked.",
			"[blizzard bug] the wasteland tower that uses GetUnitArmorType has been reworked.",
			"[balance] The bristleburst (wasteland) ability has been reworked to be less effective.",
			"Tooltips for summons improved.",
			"The wurst standard library dependency has been updated to wurstStdlib2",
		)
	),

	(
		"1.0.2",
		"7 July 2016",
		(
			"The map is now written entirely in Wurst",
			"A new race has been added - Metal.",
			"Added a new \"run away\" sound.",
		)
	),

	(
		"1.0.0c",
		"16 June 2014",
		(
			"Fixed one bug",
			"Made minor tweaks",
		)
	),

	(
		"1.0.0b",
		"Date Unknown",
		(
			"Changelog lost.",
		)
	),

	(
		"1.0.0a",
		"30 May 2014",
		(
			"Initial Version Uploaded to hiveworkshop.com as part of Mini Mapping Contest #9. See the thread here: [ur]http://goo.gl/yPlMmy[/url]",
		)
	),
)

CONTRIBUTING       = "I will merge atomic, well-formed pull-requests if they are consistent with my design policies and issue tracker."

def write(str):
	sys.stdout.write(str)


def print_section_header(title):
	write("[R][H3][color=#CCAA00]" + title + "[/color][/H3][R]\n")


def get_paragraph(paragraph):
	p = paragraph.strip().replace('\n', ' ').replace('\t', '')
	return textwrap.fill(p, width=100) + "\n\n"


def print_paragraph(paragraph):
	write(get_paragraph(paragraph))


def print_header():
	write("[CENTER]\n[TABLE]\n[CENTER]\n[H3][color=#60A600]")
	write(MAP_NAME)
	write("[/color][/H3]\n[color=#CCAA00][B]A map by ")
	write(AUTHOR)
	write("[/B][/color]\n\n")


def print_contents():
	write("[BOX=Contents]")
	if INTRODUCTION:
		write("* Introduction\n")
	if SCREENSHOTS:
		write("* Screenshots\n")
	if ABILITIES:
		write("* Abilities\n")
	if RACES:
		write("* Races\n")
	if ITEMS:
		write("* Items\n")
	if REPOSITORY_URI:
		write("* Version Control\n")
	if CHANGELOG:
		write("* Changelog\n")
	if CONTRIBUTING:
		write("* Contributing\n")
	write("[/BOX]\n[/CENTER]\n\n")


def print_introduction():
	if INTRODUCTION:
		print_section_header("Introduction")
		for paragraph in INTRODUCTION:
			print_paragraph(paragraph)

def print_screenshots():
	if SCREENSHOTS:
		print_section_header("Screenshots")
		write("\n\n")
		for shot in SCREENSHOTS:
			write("[hidden=" + shot[0] + "]\n[img]" + shot[1] + "[/img]\n[/hidden]\n\n")


def print_abilities():
	if ABILITIES:
		print_section_header("Abilities")
		write("\n\n**NOT IMPLEMENTED**\n\n")


def print_items():
	if ITEMS:
		print_section_header("Items")
		write("\n\n[otable]\n")
		for item in ITEMS:
			if item == None:
				write("[tr][titletd][/titletd][titletd][/titletd][/tr]\n")
				continue

			write("[tr]\n[tdalt][img]" + item[0] + "[/img][/tdalt]\n[tdalt]")
			for paragraph in item[1][0:-1]:
				print_paragraph(paragraph)
			write(get_paragraph(item[1][-1])[0:-2])
			write("[/tdalt]\n[/tr]\n")
		write("[/otable]\n\n")


def print_races():
	if RACES:
		print_section_header("Races")
		write("\n\n[otable]\n")
		for race in RACES:
			write("[tr]\n[tdalt][img]" + race[0] + "[/img][/tdalt]\n[tdalt]")
			for paragraph in race[1][0:-1]:
				print_paragraph(paragraph)
			write(get_paragraph(race[1][-1])[0:-2])
			write("[/tdalt]\n[/tr]\n")
		write("[/otable]\n\n")


def print_repository_uri():
	if REPOSITORY_URI:
		print_section_header("Version Control")
		write("\n\n")
		print_paragraph("All iterations of this map are maintained in a public git repository at [url]" + REPOSITORY_URI + "[/url]")


def print_changelog():
	if CHANGELOG:
		print_section_header("Changelog")
		write("\n\n")
		for log in CHANGELOG[0:5]:
			write("[color=#ffcc00]" + log[0] + "[/color] [color=#999999]" + log[1] + "[/color]:\n[list]")
			for point in log[2]:
				write(get_paragraph("[*] " + point)[0:-2] + "\n")
			write("[/list]\n\n")

		if CHANGELOG[5:]:
			write("[hidden=Older Changes")
			for log in CHANGELOG[5:]:
				write("[color=#ffcc00]" + log[0] + "[/color] [color=#999999]" + log[1] + "[/color]:\n[list]")
				for point in log[2]:
					write(get_paragraph("[*] " + point)[0:-2] + "\n")
				write("[/list]\n\n")
			write("[/hidden]")

def print_contributing():
	if CONTRIBUTING:
		print_section_header("Contributing")
		print_paragraph(CONTRIBUTING)


def print_footer():
	write("[/TABLE]\n[/CENTER]\n")

print_header()
print_contents()
print_introduction()
print_screenshots()
print_abilities()
print_races()
print_items()
print_repository_uri()
print_changelog()
print_contributing()
print_footer()
