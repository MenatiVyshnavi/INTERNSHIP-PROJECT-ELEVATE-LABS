# INTERNSHIP-PROJECT-ELEVATE-LABS
Password Strength Analyzer with Custom Wordlist Generator
Project Overview
This toolkit consists of two main components:

Password Strength Analyzer - Evaluates password security using entropy-based calculations

Custom Wordlist Generator - Creates targeted password dictionaries for security testing

Developed as part of a Cybersecurity Internship Program at GD Goenka University.

Features
Password Strength Analyzer
Entropy-based password strength calculation

Five-tier strength classification (Very Weak to Very Strong)

Detailed character composition analysis

Secure password input (hidden entry)

Real-time security recommendations

Custom Wordlist Generator
Leetspeak transformation engine (a→@, e→3, etc.)

Year-based pattern generation

Special character combinations

Capitalization variations

Command-line interface with flexible parameters

Efficient combinatorial algorithms

Technologies Used
Language: Python 3.13.9

IDE: Visual Studio Code

Libraries: string, math, getpass, argparse, itertools

Platform: Windows (cross-platform compatible)

Installation
Prerequisites
Python 3.8 or higher

Setup
Clone the repository

No additional dependencies required (uses Python standard library only)

Usage
Password Strength Analyzer
Run the analyzer:

text
python password_analyzer.py
Custom Wordlist Generator
Basic usage:

text
python wordlist_generator.py -w "test,demo,password" -y "2023,2024" -s "!@" -o mylist.txt
Options:

-w, --words: Comma-separated base words (required)

-y, --years: Comma-separated years (default: 2020-2024)

-s, --special: Special characters (default: !@#$)

-o, --output: Output filename (default: custom_wordlist.txt)

Generated Wordlist Patterns
The wordlist generator creates variations including:

Original, capitalized, and uppercase versions

Leetspeak transformations (te$t, dem0, p@ssw0rd)

Year combinations (test2023, password2024)

Special character variants (demo!, Test@)

Combined patterns (test2023!, password2024@)

Security & Ethics
IMPORTANT: These tools are designed for:

Educational purposes

Authorized security testing

Personal password auditing

Security awareness training

DO NOT USE FOR:

Unauthorized access attempts

Illegal activities

Malicious purposes

Password Entropy Formula
text
H = L × log₂(N)
Where:

H = Password entropy (bits)

L = Password length

N = Character set size

Strength Classification
Entropy Range	Rating	Security Level
< 28 bits	Very Weak	Easily cracked
28-36 bits	Weak	Vulnerable
36-60 bits	Moderate	Reasonable
60-80 bits	Strong	Good security
> 80 bits	Very Strong	Excellent
Future Enhancements
Integration with Have I Been Pwned API

GUI development using Tkinter/PyQt

Support for custom character sets

Machine learning-based pattern recognition

Multi-language support

Password policy compliance checker
