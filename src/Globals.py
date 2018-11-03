import json

with open("../data/Position_Mapping.json") as f: 
    POSITIONS = json.load(f)

POS = 0
AGE = 1
TM = 2
GAM = 3
GS = 4
MP = 5
PER = 6
TS = 7
THPAR = 8
FTR = 9
ORB = 10
DRB = 11
TRB = 12
AST = 13
STL = 14
BLK = 15
TOV = 16
USG = 17
OWS = 18
DWS = 19
WS = 20
WSA = 21
OBPM = 22
DBPM = 23
BPM = 24
VORP = 25
FG = 26
FGA = 27
FG = 28
THP = 29
THPA = 30
THPP = 31
TWP = 32
TWPA = 33
TWPP = 34
EFG = 35
FT = 36
FTA = 37
FT = 38
ORB = 39
DRB = 40
TRB = 41
AST = 42
STL = 43
BLK = 44
TOV = 45
PF = 46
PTS = 47

FEATURES = [
    POS,
    PER,
    AGE,
    GAM,
    MP,
    TS,
    THPAR,
    FTR,
    ORB,
    DRB,
    AST,
    STL,
    BLK,
    WS,
    VORP,
    EFG,
    ]