from __future__ import unicode_literals
from .base import Text


class CatholicCanon(Text):
    """
    Catholic Canonical Bible with Old and New Testaments,
    more precisely The New American Bible
    http://www.vatican.va/archive/ENG0839/_INDEX.HTM
    """
    books = {
        # The Pentateuch
        'gen': {
            'en': ('Genesis', 'Gen', 'Gen(?:esis)?'),
            'fr': ('Genesis', 'Gen', 'Gen(?:esis)?'),
            'chapters': [31, 25, 24, 26, 32, 22, 24, 22, 29, 32, 32, 20, 18, 24, 21, 16, 27, 33, 38, 18, 34, 24, 20, 67, 34, 35,
             46, 22, 35, 43, 55, 32, 20, 31, 29, 43, 36, 30, 23, 23, 57, 38, 34, 34, 28, 34, 31, 22, 33, 26]
        },
        'exod': {
            'en': ('Exodus', 'Exod', 'Exod(?:us)?'),
            'fr': ('Exodus', 'Exod', 'Exod(?:us)?'),
            'chapters': [22, 25, 22, 31, 23, 30, 25, 32, 35, 29, 10, 51, 22, 31, 27, 36, 16, 27, 25, 26, 36, 31, 33, 18, 40,
             37, 21, 43, 46, 38, 18, 35, 23, 35, 35, 38, 29, 31, 43, 38]
        },
        'lev': {
            'en': ('Leviticus', 'Lev', 'Lev(?:iticus)?'),
            'fr': ('Leviticus', 'Lev', 'Lev(?:iticus)?'),
            'chapters': [17, 16, 17, 35, 19, 30, 38, 36, 24, 20, 47, 8, 59, 57, 33, 34, 16, 30, 37, 27, 24, 33, 44, 23, 55, 46, 34]
        },
        'num': {
            'en': ('Numbers', 'Num', 'Num(?:bers)?'),
            'fr': ('Numbers', 'Num', 'Num(?:bers)?'),
            'chapters': [54, 34, 51, 49, 31, 27, 89, 26, 23, 36, 35, 16, 33, 45, 41, 50, 13, 32, 22, 29, 35, 41, 30, 25, 18, 65,
             23, 31, 40, 16, 54, 42, 56, 29, 34, 13]
        },
        'deut': {
            'en': ('Deuteronomy', 'Deut', 'Deut(?:eronomy)?'),
            'fr': ('Deuteronomy', 'Deut', 'Deut(?:eronomy)?'),
            'chapters': [46, 37, 29, 49, 33, 25, 26, 20, 29, 22, 32, 32, 18, 29, 23, 22, 20, 22, 21, 20, 23, 30, 25, 22, 19,
             19, 26, 68, 29, 20, 30, 52, 29, 12]
        },
        'josh': {
            'en': ('Joshua', 'Josh', 'Josh(?:ua)?'),
            'fr': ('Joshua', 'Josh', 'Josh(?:ua)?'),
            'chapters': [18, 24, 17, 24, 15, 27, 26, 35, 27, 43, 23, 24, 33, 15, 63, 10, 18, 28, 51, 9, 45, 34, 16, 33]
        },
        'judg': {
            'en': ('Judges', 'Judg', 'Judg(?:es)?'),
            'fr': ('Judges', 'Judg', 'Judg(?:es)?'),
            'chapters': [36, 23, 31, 24, 31, 40, 25, 35, 57, 18, 40, 15, 25, 20, 20, 31, 13, 31, 30, 48, 25]
        },
        'ruth': {
            'en': ('Ruth', 'Ruth', 'Ruth'),
            'fr': ('Ruth', 'Ruth', 'Ruth'),
            'chapters': [22, 23, 18, 22]
        },
        # The Historical Books
        '1sam': {
            'en': ('I Samuel', '1Sam', '(?:1|I)(?:\s)?Sam(?:uel)?'),
            'fr': ('I Samuel', '1Sam', '(?:1|I)(?:\s)?Sam(?:uel)?'),
            'chapters': [28, 36, 21, 22, 12, 21, 17, 22, 27, 27, 15, 25, 23, 52, 35, 23, 58, 30, 24, 42, 15, 23, 29, 22, 44,
             25, 12, 25, 11, 31, 13]
        },
        '2sam': {
            'en': ('II Samuel', '2Sam', '(?:2|II)(?:\s)?Sam(?:uel)?'),
            'fr': ('II Samuel', '2Sam', '(?:2|II)(?:\s)?Sam(?:uel)?'),
            'chapters': [27, 32, 39, 12, 25, 23, 29, 18, 13, 19, 27, 31, 39, 33, 37, 23, 29, 33, 43, 26, 22, 51, 39, 25]
        },
        '1kgs': {
            'en': ('I Kings', '1Kgs', '(?:1|I)(?:\s)?K(?:in)?gs'),
            'fr': ('I Kings', '1Kgs', '(?:1|I)(?:\s)?K(?:in)?gs'),
            'chapters': [53, 46, 28, 34, 18, 38, 51, 66, 28, 29, 43, 33, 34, 31, 34, 34, 24, 46, 21, 43, 29, 53]
        },
        '2kgs': {
            'en': ('II Kings', '2Kgs', '(?:2|II)(?:\s)?K(?:in)?gs'),
            'fr': ('II Kings', '2Kgs', '(?:2|II)(?:\s)?K(?:in)?gs'),
            'chapters': [18, 25, 27, 44, 27, 33, 20, 29, 37, 36, 21, 21, 25, 29, 38, 20, 41, 37, 37, 21, 26, 20, 37, 20, 30]
        },
        '1chr': {
            'en': ('I Chronicles', '1Chr', '(?:1|I)(?:\s)?Chr(?:o(?:n(?:icles)?)?)?'),
            'fr': ('I Chronicles', '1Chr', '(?:1|I)(?:\s)?Chr(?:o(?:n(?:icles)?)?)?'),
            'chapters': [54, 55, 24, 43, 26, 81, 40, 40, 44, 14, 47, 40, 14, 17, 29, 43, 27, 17, 19, 8, 30, 19, 32, 31, 31,
              32, 34, 21, 30]
        },
        '2chr': {
            'en': ('II Chronicles', '2Chr', '(?:2|II)(?:\s)?Chr(?:o(?:n(?:icles)?)?)?'),
            'fr': ('II Chronicles', '2Chr', '(?:2|II)(?:\s)?Chr(?:o(?:n(?:icles)?)?)?'),
            'chapters': [17, 18, 17, 22, 14, 42, 22, 18, 31, 19, 23, 16, 22, 15, 19, 14, 19, 34, 11, 37, 20, 12, 21, 27, 28,
              23, 9, 27, 36, 27, 21, 33, 25, 33, 27, 23]
        },
        'ezra': {
            'en': ('Ezra', 'Ezra', 'Ezra'),
            'fr': ('Ezra', 'Ezra', 'Ezra'),
            'chapters': [11, 70, 13, 24, 17, 22, 28, 36, 15, 44]
        },
        'neh': {
            'en': ('Nehemiah', 'Neh', 'Neh(?:emiah)?'),
            'fr': ('Nehemiah', 'Neh', 'Neh(?:emiah)?'),
            'chapters': [11, 20, 32, 23, 19, 19, 73, 18, 38, 39, 36, 47, 31]
        },
        'tob': {
            'en': ('Tobit', 'Tob', 'Tob(?:it)?'),
            'fr': ('Tobit', 'Tob', 'Tob(?:it)?'),
            'chapters': [22, 14, 17, 21, 22, 18, 17, 21, 6, 14, 18, 22, 18, 15]
        },
        'jud': {
            'en': ('Judith', 'Jud', 'Jud(?:ith)?'),
            'fr': ('Judith', 'Jud', 'Jud(?:ith)?'),
            'chapters': [16, 28, 10, 15, 24, 21, 32, 36, 14, 23, 23, 20, 20, 19, 14, 25]
        },
        'esth': {
            'en': ('Esther', 'Esth', 'Esth(?:er)?'),
            'fr': ('Esther', 'Esth', 'Esth(?:er)?'),
            'chapters': [22, 23, 15, 17, 14, 14, 10, 17, 32, 3]
        },
        '1mac': {
            'en': ('I Maccabees', '1Mac', '(?:1|I)(?:\s)?Mac(?:c(?:a(?:bees)?)?)?'),
            'fr': ('I Maccabees', '1Mac', '(?:1|I)(?:\s)?Mac(?:c(?:a(?:bees)?)?)?'),
            'chapters': [63, 70, 59, 61, 68, 63, 50, 32, 73, 89, 74, 53, 53, 49, 41, 24]
        },
        '2mac': {
            'en': ('II Maccabees', '2Mac', '(?:2|II)(?:\s)?Mac(?:c(?:a(?:bees)?)?)?'),
            'fr': ('II Maccabees', '2Mac', '(?:2|II)(?:\s)?Mac(?:c(?:a(?:bees)?)?)?'),
            'chapters': []
        },
        # The Wisdom Books
        'job': {
            'en': ('Job', 'Job', 'Job'),
            'fr': ('Job', 'Job', 'Job'),
            'chapters': [22, 13, 26, 21, 27, 30, 21, 22, 35, 22, 20, 25, 28, 22, 35, 22, 16, 21, 29, 29, 34, 30, 17, 25, 6, 14,
             23, 28, 25, 31, 40, 22, 33, 37, 16, 33, 24, 41, 30, 24, 34, 17]
        },
        'ps': {
            'en': ('Psalms', 'Ps', 'Ps(?:a)?(?:lm(?:s)?)?'),
            'fr': ('Psalms', 'Ps', 'Ps(?:a)?(?:lm(?:s)?)?'),
            'chapters': [6, 12, 8, 8, 12, 10, 17, 9, 20, 18, 7, 8, 6, 7, 5, 11, 15, 50, 14, 9, 13, 31, 6, 10, 22, 12, 14, 9, 11,
             12, 24, 11, 22, 22, 28, 12, 40, 22, 13, 17, 13, 11, 5, 26, 17, 11, 9, 14, 20, 23, 19, 9, 6, 7, 23, 13,
             11, 11, 17, 12, 8, 12, 11, 10, 13, 20, 7, 35, 36, 5, 24, 20, 28, 23, 10, 12, 20, 72, 13, 19, 16, 8, 18,
             12, 13, 17, 7, 18, 52, 17, 16, 15, 5, 23, 11, 13, 12, 9, 9, 5, 8, 28, 22, 35, 45, 48, 43, 13, 31, 7, 10,
             10, 9, 8, 18, 19, 2, 29, 176, 7, 8, 9, 4, 8, 5, 6, 5, 6, 8, 8, 3, 18, 3, 3, 21, 26, 9, 8, 24, 13, 10, 7,
             12, 15, 21, 10, 20, 14, 9, 6]
        },
        'prov': {
            'en': ('Proverbs', 'Prov', 'Prov(?:erbs)?'),
            'fr': ('Proverbs', 'Prov', 'Prov(?:erbs)?'),
            'chapters': [33, 22, 35, 27, 23, 35, 27, 36, 18, 32, 31, 28, 25, 35, 33, 33, 28, 24, 29, 30, 31, 29, 35, 34, 28,
             28, 27, 28, 27, 33, 31]
        },
        'eccl': {
            'en': ('Ecclesiastes', 'Eccl', 'Ecc(?:l(?:es(?:iastes)?)?)?'),
            'fr': ('Ecclesiastes', 'Eccl', 'Ecc(?:l(?:es(?:iastes)?)?)?'),
            'chapters': [18, 26, 22, 16, 20, 12, 29, 17, 18, 20, 10, 14]
        },
        'song': {
            'en': ('Song of Solomon', 'Song', 'Song(?: of Sol(?:omon)?)?'),
            'fr': ('Song of Solomon', 'Song', 'Song(?: of Sol(?:omon)?)?'),
            'chapters': [17, 17, 11, 16, 16, 13, 13, 14]
        },
        'bow': {
            'en': ('Book of Wisdom', 'Wisdom', 'Book(?: of Wis(?:dom)?)?'),
            'fr': ('Book of Wisdom', 'Wisdom', 'Book(?: of Wis(?:dom)?)?'),
            'chapters': [16, 24, 19, 20, 23, 25, 30, 21, 18, 21, 26, 27, 19, 31, 19, 29, 21, 25, 22]
        },
        'sir': {
            'en': ('Sirach', 'Sirach', 'Sir(?:ach)?'),
            'fr': ('Sirach', 'Sirach', 'Sir(?:ach)?'),
            'chapters': [29, 18, 30, 31, 17, 37, 36, 19, 18, 30, 34, 18, 25, 27, 20, 28, 27, 33, 26, 30, 28, 27, 27, 31, 25,
             20, 30, 26, 28, 25, 31, 24, 33, 26, 24, 27, 30, 34, 35, 30, 24, 25, 35, 23, 26, 20, 25, 25, 16, 29, 30]
        },
        # The Prophetic Books
        'isa': {
            'en': ('Isaiah', 'Isa', 'Isa(?:iah)?'),
            'fr': ('Isaiah', 'Isa', 'Isa(?:iah)?'),
            'chapters': [31, 22, 26, 6, 30, 13, 25, 22, 21, 34, 16, 6, 22, 32, 9, 14, 14, 7, 25, 6, 17, 25, 18, 23, 12, 21, 13,
             29, 24, 33, 9, 20, 24, 17, 10, 22, 38, 22, 8, 31, 29, 25, 28, 28, 25, 13, 15, 22, 26, 11, 23, 15, 12,
             17, 13, 12, 21, 14, 21, 22, 11, 12, 19, 12, 25, 24]
        },
        'jer': {
            'en': ('Jeremiah', 'Jer', 'Jer(?:emiah)?'),
            'fr': ('Jeremiah', 'Jer', 'Jer(?:emiah)?'),
            'chapters': [19, 37, 25, 31, 31, 30, 34, 22, 26, 25, 23, 17, 27, 22, 21, 21, 27, 23, 15, 18, 14, 30, 40, 10, 38, 24,
             22, 17, 32, 24, 40, 44, 26, 22, 19, 32, 21, 28, 18, 16, 18, 22, 13, 30, 5, 28, 7, 47, 39, 46, 64, 34]
        },
        'lam': {
            'en': ('Lamentations', 'Lam', 'Lam(?:entations)?'),
            'fr': ('Lamentations', 'Lam', 'Lam(?:entations)?'),
            'chapters': [22, 22, 66, 22, 22]
        },
        'bar': {
            'en': ('Baruch', 'Bar', 'Bar(?:uch)?'),
            'fr': ('Baruch', 'Bar', 'Bar(?:uch)?'),
            'chapters': [22, 35, 38, 37, 9, 72]
        },
        'ezek': {
            'en': ('Ezekiel', 'Ezek', 'Ezek(?:iel)?'),
            'fr': ('Ezekiel', 'Ezek', 'Ezek(?:iel)?'),
            'chapters': [28, 10, 27, 17, 17, 14, 27, 18, 11, 22, 25, 28, 23, 23, 8, 63, 24, 32, 14, 49, 32, 31, 49, 27, 17, 21,
             36, 26, 21, 26, 18, 32, 33, 31, 15, 38, 28, 23, 29, 49, 26, 20, 27, 31, 25, 24, 23, 35]
        },
        'dan': {
            'en': ('Daniel', 'Dan', 'Dan(?:iel)?'),
            'fr': ('Daniel', 'Dan', 'Dan(?:iel)?'),
            'chapters': [21, 49, 30, 37, 31, 28, 28, 27, 27, 21, 45, 13]
        },
        'hos': {
            'en': ('Hosea', 'Hos', 'Hos(?:ea)?'),
            'fr': ('Hosea', 'Hos', 'Hos(?:ea)?'),
            'chapters': [11, 23, 5, 19, 15, 11, 16, 14, 17, 15, 12, 14, 16, 9]
        },
        'joel': {
            'en': ('Joel', 'Joel', 'Joel'),
            'fr': ('Joel', 'Joel', 'Joel'),
            'chapters': [20, 32, 21]
        },
        'amos': {
            'en': ('Amos', 'Amos', 'Amos'),
            'fr': ('Amos', 'Amos', 'Amos'),
            'chapters': [15, 16, 15, 13, 27, 14, 17, 14, 15]
        },
        'obad': {
            'en': ('Obadiah', 'Obad', 'Obad(?:iah)?'),
            'fr': ('Obadiah', 'Obad', 'Obad(?:iah)?'),
            'chapters': [21]
        },
        'jonah': {
            'en': ('Jonah', 'Jonah', 'Jon(?:ah)?'),
            'fr': ('Jonah', 'Jonah', 'Jon(?:ah)?'),
            'chapters': [17, 10, 10, 11]
        },
        'mic': {
            'en': ('Micah', 'Mic', 'Mic(?:ah)?'),
            'fr': ('Micah', 'Mic', 'Mic(?:ah)?'),
            'chapters': [16, 13, 12, 13, 15, 16, 20]
        },
        'nah': {
            'en': ('Nahum', 'Nah', 'Nah(?:um)?'),
            'fr': ('Nahum', 'Nah', 'Nah(?:um)?'),
            'chapters': [15, 13, 19]
        },
        'hab': {
            'en': ('Habakkuk', 'Hab', 'Hab(?:akkuk)?'),
            'fr': ('Habakkuk', 'Hab', 'Hab(?:akkuk)?'),
            'chapters': [17, 20, 19]
        },
        'zeph': {
            'en': ('Zephaniah', 'Zeph', 'Zeph(?:aniah)?'),
            'fr': ('Zephaniah', 'Zeph', 'Zeph(?:aniah)?'),
            'chapters': [18, 15, 20]
        },
        'hag': {
            'en': ('Haggai', 'Hag', 'Hag(?:gai)?'),
            'fr': ('Haggai', 'Hag', 'Hag(?:gai)?'),
            'chapters': [15, 23]
        },
        'zech': {
            'en': ('Zechariah', 'Zech', 'Zech(?:ariah)?'),
            'fr': ('Zechariah', 'Zech', 'Zech(?:ariah)?'),
            'chapters': [21, 13, 10, 14, 11, 15, 14, 23, 17, 12, 17, 14, 9, 21]
        },
        'mal': {
            'en': ('Malachi', 'Mal', 'Mal(?:achi)?'),
            'fr': ('Malachi', 'Mal', 'Mal(?:achi)?'),
            'chapters': [14, 17, 18, 6]
        },
        # The Gospels
        'matt': {
            'en': ('Matthew', 'Matt', 'Matt(?:hew)?'),
            'fr': ('Matthew', 'Matt', 'Matt(?:hew)?'),
            'chapters': [25, 23, 17, 25, 48, 34, 29, 34, 38, 42, 30, 50, 58, 36, 39, 28, 27, 35, 30, 34, 46, 46, 39, 51, 46, 75,
             66, 20]
        },
        'mark': {
            'en': ('Mark', 'Mark', 'Mark'),
            'fr': ('Mark', 'Mark', 'Mark'),
            'chapters': [45, 28, 35, 41, 43, 56, 37, 38, 50, 52, 33, 44, 37, 72, 47, 20]
        },
        'luke': {
            'en': ('Luke', 'Luke', 'Luke'),
            'fr': ('Luke', 'Luke', 'Luke'),
            'chapters': [80, 52, 38, 44, 39, 49, 50, 56, 62, 42, 54, 59, 35, 35, 32, 31, 37, 43, 48, 47, 38, 71, 56, 53]
        },
        'john': {
            'en': ('John', 'John', '(?<!(?:1|2|3|I)\s)(?<!(?:1|2|3|I))John'),
            'fr': ('John', 'John', '(?<!(?:1|2|3|I)\s)(?<!(?:1|2|3|I))John'),
            'chapters': [51, 25, 36, 54, 47, 71, 53, 59, 41, 42, 57, 50, 38, 31, 27, 33, 26, 40, 42, 31, 25]
        },
        'acts': {
            'en': ('Acts', 'Acts', 'Acts'),
            'fr': ('Acts', 'Acts', 'Acts'),
            'chapters': [26, 47, 26, 37, 42, 15, 60, 40, 43, 48, 30, 25, 52, 28, 41, 40, 34, 28, 41, 38, 40, 30, 35, 27, 27,
             32, 44, 31]
        },
        # New Testament Letters
        'rom': {
            'en': ('Romans', 'Rom', 'Rom(?:ans)?'),
            'fr': ('Romans', 'Rom', 'Rom(?:ans)?'),
            'chapters': [32, 29, 31, 25, 21, 23, 25, 39, 33, 21, 36, 21, 14, 23, 33, 27]
        },
        '1cor': {
            'en': ('I Corinthians', '1Cor', '(?:1|I)(?:\s)?Cor(?:inthians)?'),
            'fr': ('I Corinthians', '1Cor', '(?:1|I)(?:\s)?Cor(?:inthians)?'),
            'chapters': [31, 16, 23, 21, 13, 20, 40, 13, 27, 33, 34, 31, 13, 40, 58, 24]
        },
        '2cor': {
            'en': ('II Corinthians', '2Cor', '(?:2|II)(?:\s)?Cor(?:inthians)?'),
            'fr': ('II Corinthians', '2Cor', '(?:2|II)(?:\s)?Cor(?:inthians)?'),
            'chapters': [24, 17, 18, 18, 21, 18, 16, 24, 15, 18, 33, 21, 14]
        },
        'gal': {
            'en': ('Galatians', 'Gal', 'Gal(?:atians)?'),
            'fr': ('Galatians', 'Gal', 'Gal(?:atians)?'),
            'chapters': [24, 21, 29, 31, 26, 18]
        },
        'eph': {
            'en': ('Ephesians', 'Eph', 'Eph(?:esians)?'),
            'fr': ('Ephesians', 'Eph', 'Eph(?:esians)?'),
            'chapters': [23, 22, 21, 32, 33, 24]
        },
        'phil': {
            'en': ('Philippians', 'Phil', 'Phil(?:ippians)?'),
            'fr': ('Philippians', 'Phil', 'Phil(?:ippians)?'),
            'chapters': [30, 30, 21, 23]
        },
        'col': {
            'en': ('Colossians', 'Col', 'Col(?:ossians)?'),
            'fr': ('Colossians', 'Col', 'Col(?:ossians)?'),
            'chapters': [29, 23, 25, 18]
        },
        '1thess': {
            'en': ('I Thessalonians', '1Thess', '(?:1|I)(?:\s)?Thess(?:alonians)?'),
            'fr': ('I Thessalonians', '1Thess', '(?:1|I)(?:\s)?Thess(?:alonians)?'),
            'chapters': [10, 20, 13, 18, 28]
        },
        '2thess': {
            'en': ('II Thessalonians', '2Thess', '(?:2|II)(?:\s)?Thess(?:alonians)?'),
            'fr': ('II Thessalonians', '2Thess', '(?:2|II)(?:\s)?Thess(?:alonians)?'),
            'chapters': [12, 17, 18]
        },
        '1tim': {
            'en': ('I Timothy', '1Tim', '(?:1|I)(?:\s)?Tim(?:othy)?'),
            'fr': ('I Timothy', '1Tim', '(?:1|I)(?:\s)?Tim(?:othy)?'),
            'chapters': [20, 15, 16, 16, 25, 21]
        },
        '2tim': {
            'en': ('II Timothy', '2Tim', '(?:2|II)(?:\s)?Tim(?:othy)?'),
            'fr': ('II Timothy', '2Tim', '(?:2|II)(?:\s)?Tim(?:othy)?'),
            'chapters': [18, 26, 17, 22]
        },
        'titus': {
            'en': ('Titus', 'Titus', 'Tit(?:us)?'),
            'fr': ('Titus', 'Titus', 'Tit(?:us)?'),
            'chapters': [16, 15, 15]
        },
        'phlm': {
            'en': ('Philemon', 'Phlm', 'Phlm|Phile(?:m(?:on)?)?'),
            'fr': ('Philemon', 'Phlm', 'Phlm|Phile(?:m(?:on)?)?'),
            'chapters': [25]
        },
        'heb': {
            'en': ('Hebrews', 'Heb', 'Heb(?:rews)?'),
            'fr': ('Hebrews', 'Heb', 'Heb(?:rews)?'),
            'chapters': [14, 18, 19, 16, 14, 20, 28, 13, 28, 39, 40, 29, 25]
        },
        # The Catholic Letters
        'jas': {
            'en': ('James', 'Jas', 'Ja(?:me)?s'),
            'fr': ('James', 'Jas', 'Ja(?:me)?s'),
            'chapters': [27, 26, 18, 17, 20]
        },
        '1pet': {
            'en': ('I Peter', '1Pet', '(?:1|I)(?:\s)?Pet(?:er)?'),
            'fr': ('I Peter', '1Pet', '(?:1|I)(?:\s)?Pet(?:er)?'),
            'chapters': [25, 25, 22, 19, 14]
        },
        '2pet': {
            'en': ('II Peter', '2Pet', '(?:2|II)(?:\s)?Pet(?:er)?'),
            'fr': ('II Peter', '2Pet', '(?:2|II)(?:\s)?Pet(?:er)?'),
            'chapters': [21, 22, 18]
        },
        '1john': {
            'en': ('I John', '1John', '(?:(?:1|I)(?:\s)?)John'),
            'fr': ('I John', '1John', '(?:(?:1|I)(?:\s)?)John'),
            'chapters': [10, 29, 24, 21, 21]
        },
        '2john': {
            'en': ('II John', '2John', '(?:(?:2|II)(?:\s)?)John'),
            'fr': ('II John', '2John', '(?:(?:2|II)(?:\s)?)John'),
            'chapters': [13]
        },
        '3john': {
            'en': ('III John', '3John', '(?:(?:3|III)(?:\s)?)John'),
            'fr': ('III John', '3John', '(?:(?:3|III)(?:\s)?)John'),
            'chapters': [14]
        },
        'jude': {
            'en': ('Jude', 'Jude', 'Jude'),
            'fr': ('Jude', 'Jude', 'Jude'),
            'chapters': [25]
        },
        'rev': {
            'en': ('Revelation of Jesus Christ', 'Rev', 'Rev(?:elation)?(?:\sof Jesus Christ)?'),
            'fr': ('Revelation of Jesus Christ', 'Rev', 'Rev(?:elation)?(?:\sof Jesus Christ)?'),
            'chapters': [20, 29, 22, 11, 14, 17, 17, 13, 21, 11, 19, 17, 18, 20, 8, 21, 18, 24, 21, 15, 27, 21]
        },
    }

