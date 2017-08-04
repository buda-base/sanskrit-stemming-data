﻿# this file is the output of generate_rules_from_tables.py
# the tables are "unpacked" and transcoded to SLP1 in input/sandhi-charts/*.csv

# {final: [(initial, sandhied), ...], ...}
# for i I u U, the application of these rules only when the form is not a dual has no incidence in the need to generate all sandhied forms here
vowel_sandhi = {
		"a": [
				("a", "A"),
				("A", "A"),
				("A", "A"),
				("i", "e"),
				("i", "e"),
				("u", "o"),
				("U", "o"),
				("f", "ar"),
				("e", "E"),
				("E", "E"),
				("o", "O"),
				("O", "O")],
		"A": [
				("a", "A"),
				("A", "A"),
				("A", "A"),
				("i", "e"),
				("i", "e"),
				("u", "o"),
				("U", "o"),
				("f", "ar"),
				("e", "E"),
				("E", "E"),
				("o", "O"),
				("O", "O")],
		"i": [
				("a", "ya"),
				("A", "yA"),
				("A", "yA"),
				("i", "I"),
				("i", "I"),
				("u", "yu"),
				("U", "yU"),
				("f", "yf"),
				("e", "ye"),
				("E", "yE"),
				("o", "yo"),
				("O", "yO"),
				("a", "i a"),
				("A", "i A"),
				("A", "i A"),
				("i", "i i"),
				("i", "i i"),
				("u", "i u"),
				("U", "i U"),
				("f", "i f"),
				("e", "i e"),
				("E", "i E"),
				("o", "i o"),
				("O", "i O")],
		"I": [
				("a", "ya"),
				("A", "yA"),
				("A", "yA"),
				("i", "I"),
				("i", "I"),
				("u", "yu"),
				("U", "yU"),
				("f", "yf"),
				("e", "ye"),
				("E", "yE"),
				("o", "yo"),
				("O", "yO"),
				("a", "I a"),
				("A", "I A"),
				("A", "I A"),
				("i", "I i"),
				("i", "I i"),
				("u", "I u"),
				("U", "I U"),
				("f", "I f"),
				("e", "I e"),
				("E", "I E"),
				("o", "I o"),
				("O", "I O")],
		"u": [
				("a", "va"),
				("A", "vA"),
				("A", "vA"),
				("i", "vi"),
				("i", "vi"),
				("u", "U"),
				("U", "U"),
				("f", "vf"),
				("e", "ve"),
				("E", "vE"),
				("o", "vo"),
				("O", "vO"),
				("a", "u a"),
				("A", "u A"),
				("A", "u A"),
				("i", "u i"),
				("i", "u i"),
				("u", "u u"),
				("U", "u U"),
				("f", "u f"),
				("e", "u e"),
				("E", "u E"),
				("o", "u o"),
				("O", "u O")],
		"U": [
				("a", "va"),
				("A", "vA"),
				("A", "vA"),
				("i", "vi"),
				("i", "vi"),
				("u", "U"),
				("U", "U"),
				("f", "vf"),
				("e", "ve"),
				("E", "vE"),
				("o", "vo"),
				("O", "vO"),
				("a", "U a"),
				("A", "U A"),
				("A", "U A"),
				("i", "U i"),
				("i", "U i"),
				("u", "U u"),
				("U", "U U"),
				("f", "U f"),
				("e", "U e"),
				("E", "U E"),
				("o", "U o"),
				("O", "U O")],
		"f": [
				("a", "ra"),
				("A", "rA"),
				("A", "rA"),
				("i", "ri"),
				("i", "ri"),
				("u", "ru"),
				("U", "rU"),
				("f", "F"),
				("e", "re"),
				("E", "rE"),
				("o", "ro"),
				("O", "rO")],
		"e": [
				("a", "e '"),
				("A", "a A"),
				("A", "a A"),
				("i", "a i"),
				("i", "a i"),
				("u", "a u"),
				("U", "a U"),
				("f", "a f"),
				("e", "a e"),
				("E", "a E"),
				("o", "a o"),
				("O", "a O"),
				("a", "e a"),
				("A", "e A"),
				("A", "e A"),
				("i", "e i"),
				("i", "e i"),
				("u", "e u"),
				("U", "e U"),
				("f", "e f"),
				("e", "e e"),
				("E", "e E"),
				("o", "e o"),
				("O", "e O")],
		"E": [
				("a", "A a"),
				("A", "A A"),
				("A", "A A"),
				("i", "A i"),
				("i", "A i"),
				("u", "A u"),
				("U", "A U"),
				("f", "A f"),
				("e", "A e"),
				("E", "A E"),
				("o", "A o"),
				("O", "A O")],
		"o": [
				("a", "o '"),
				("A", "avA"),
				("A", "a A"),
				("i", "avi"),
				("i", "avi"),
				("u", "avu"),
				("U", "avU"),
				("f", "avf"),
				("e", "ave"),
				("E", "avE"),
				("o", "avo"),
				("O", "avO")],
		"O": [
				("a", "Ava"),
				("A", "AvA"),
				("A", "AvA"),
				("i", "Avi"),
				("i", "Avi"),
				("u", "Avu"),
				("U", "AvU"),
				("f", "Avf"),
				("e", "Ave"),
				("E", "AvE"),
				("o", "Avo"),
				("O", "AvO")],
			}
# {final: [(initial, (new_final, new_initial)), ...], ...}
consonant_sandhi_1 = {
		"k": [
			("y", ("g", "y")),
			("r", ("g", "r")),
			("l", ("g", "l")),
			("v", ("g", "v")),
			("S", ("g", "S")),
			("S", ("g", "S")),
			("z", ("k", "z")),
			("s", ("k", "s")),
			("h", ("g", "G"))
		],
		"w": [
			("y", ("q", "y")),
			("r", ("q", "r")),
			("l", ("q", "l")),
			("v", ("q", "v")),
			("S", ("w", "S")),
			("S", ("w", "S")),
			("z", ("w", "z")),
			("s", ("w", "s")),
			("h", ("q", "Q"))
		],
		"t": [
			("y", ("d", "y")),
			("r", ("d", "r")),
			("l", ("l", "l")),
			("v", ("d", "v")),
			("S", ("c", "C")),
			("S", ("c", "C")),
			("z", ("t", "z")),
			("s", ("t", "s")),
			("h", ("d", "D"))
		],
		"p": [
			("y", ("b", "y")),
			("r", ("b", "r")),
			("l", ("b", "l")),
			("v", ("b", "v")),
			("S", ("p", "S")),
			("S", ("p", "S")),
			("z", ("p", "z")),
			("s", ("p", "s")),
			("h", ("b", "B"))
		],
		"N": [
			("y", ("N", "y")),
			("r", ("N", "r")),
			("l", ("N", "l")),
			("v", ("N", "v")),
			("S", ("N", "S")),
			("S", ("N", "S")),
			("z", ("N", "z")),
			("s", ("N", "s")),
			("h", ("N", "h"))
		],
		"n": [
			("y", ("n", "y")),
			("r", ("n", "r")),
			("l", ("M", "l")),
			("v", ("n", "v")),
			("S", ("Y", "S")),
			("S", ("Y", "C")),
			("z", ("n", "z")),
			("s", ("n", "s")),
			("h", ("n", "h"))
		],
		"m": [
			("y", ("M", "y")),
			("r", ("M", "r")),
			("l", ("M", "l")),
			("v", ("M", "v")),
			("S", ("M", "S")),
			("S", ("M", "S")),
			("z", ("M", "z")),
			("s", ("M", "s")),
			("h", ("M", "h"))
		]
}
# {final: [(initial, newFinal), ...], ...}
# the initial consonant is unchanged
consonant_sandhi_2 = {
		"k": [
				("k", "k"),
				("K", "k"),
				("g", "g"),
				("G", "g"),
				("c", "k"),
				("C", "k"),
				("j", "g"),
				("J", "g"),
				("w", "k"),
				("W", "k"),
				("q", "g"),
				("Q", "g"),
				("t", "k"),
				("T", "k"),
				("d", "g"),
				("D", "g"),
				("p", "k"),
				("P", "k"),
				("b", "g"),
				("B", "g"),
				("n", "N"),
				("m", "N")],
		"w": [
				("k", "w"),
				("K", "w"),
				("g", "q"),
				("G", "q"),
				("c", "w"),
				("C", "w"),
				("j", "q"),
				("J", "q"),
				("w", "w"),
				("W", "w"),
				("q", "q"),
				("Q", "q"),
				("t", "w"),
				("T", "w"),
				("d", "q"),
				("D", "q"),
				("p", "w"),
				("P", "w"),
				("b", "q"),
				("B", "q"),
				("n", "R"),
				("m", "R")],
		"t": [
				("k", "t"),
				("K", "t"),
				("g", "d"),
				("G", "d"),
				("c", "c"),
				("C", "c"),
				("j", "j"),
				("J", "j"),
				("w", "w"),
				("W", "w"),
				("q", "q"),
				("Q", "q"),
				("t", "t"),
				("T", "t"),
				("d", "d"),
				("D", "d"),
				("p", "t"),
				("P", "t"),
				("b", "d"),
				("B", "d"),
				("n", "n"),
				("m", "n")],
		"p": [
				("k", "p"),
				("K", "p"),
				("g", "b"),
				("G", "b"),
				("c", "p"),
				("C", "p"),
				("j", "b"),
				("J", "b"),
				("w", "p"),
				("W", "p"),
				("q", "b"),
				("Q", "b"),
				("t", "p"),
				("T", "p"),
				("d", "b"),
				("D", "b"),
				("p", "p"),
				("P", "p"),
				("b", "b"),
				("B", "b"),
				("n", "m"),
				("m", "m")],
		"R": [
				("k", "R"),
				("K", "R"),
				("g", "R"),
				("G", "R"),
				("c", "R"),
				("C", "R"),
				("j", "R"),
				("J", "R"),
				("w", "R"),
				("W", "R"),
				("q", "R"),
				("Q", "R"),
				("t", "R"),
				("T", "R"),
				("d", "R"),
				("D", "R"),
				("p", "R"),
				("P", "R"),
				("b", "R"),
				("B", "R"),
				("n", "R"),
				("m", "R")],
		"n": [
				("k", "n"),
				("K", "n"),
				("g", "n"),
				("G", "n"),
				("c", "MS"),
				("C", "MS"),
				("j", "Y"),
				("J", "Y"),
				("w", "Mz"),
				("W", "Mz"),
				("q", "R"),
				("Q", "R"),
				("t", "Ms"),
				("T", "Ms"),
				("d", "n"),
				("D", "n"),
				("p", "n"),
				("P", "n"),
				("b", "n"),
				("B", "n"),
				("n", "n"),
				("m", "n")],
		"m": [
				("k", "M"),
				("K", "M"),
				("g", "M"),
				("G", "M"),
				("c", "M"),
				("C", "M"),
				("j", "M"),
				("J", "M"),
				("w", "M"),
				("W", "M"),
				("q", "M"),
				("Q", "M"),
				("t", "M"),
				("T", "M"),
				("d", "M"),
				("D", "M"),
				("p", "M"),
				("P", "M"),
				("b", "M"),
				("B", "M"),
				("n", "M"),
				("m", "M")],
			}
# {finals: [(initial, new_second_final+new_final), ...], ...}
# "new_second_final+new_final" replace the last two caracters of the previous word while the initial is unchanged
consonant_sandhi_1_vowels = {
		"ak": [
				("a", "ag"),
				("A", "ag"),
				("i", "ag"),
				("I", "ag"),
				("u", "ag"),
				("U", "ag"),
				("f", "ag"),
				("e", "ag"),
				("E", "ag"),
				("o", "ag"),
				("O", "ag")],
		"Ak": [
				("a", "Ag"),
				("A", "Ag"),
				("i", "Ag"),
				("I", "Ag"),
				("u", "Ag"),
				("U", "Ag"),
				("f", "Ag"),
				("e", "Ag"),
				("E", "Ag"),
				("o", "Ag"),
				("O", "Ag")],
		"ik": [
				("a", "ig"),
				("A", "ig"),
				("i", "ig"),
				("I", "ig"),
				("u", "ig"),
				("U", "ig"),
				("f", "ig"),
				("e", "ig"),
				("E", "ig"),
				("o", "ig"),
				("O", "ig")],
		"Ik": [
				("a", "Ig"),
				("A", "Ig"),
				("i", "Ig"),
				("I", "Ig"),
				("u", "Ig"),
				("U", "Ig"),
				("f", "Ig"),
				("e", "Ig"),
				("E", "Ig"),
				("o", "Ig"),
				("O", "Ig")],
		"uk": [
				("a", "ug"),
				("A", "ug"),
				("i", "ug"),
				("I", "ug"),
				("u", "ug"),
				("U", "ug"),
				("f", "ug"),
				("e", "ug"),
				("E", "ug"),
				("o", "ug"),
				("O", "ug")],
		"Uk": [
				("a", "Ug"),
				("A", "Ug"),
				("i", "Ug"),
				("I", "Ug"),
				("u", "Ug"),
				("U", "Ug"),
				("f", "Ug"),
				("e", "Ug"),
				("E", "Ug"),
				("o", "Ug"),
				("O", "Ug")],
		"ek": [
				("a", "eg"),
				("A", "eg"),
				("i", "eg"),
				("I", "eg"),
				("u", "eg"),
				("U", "eg"),
				("f", "eg"),
				("e", "eg"),
				("E", "eg"),
				("o", "eg"),
				("O", "eg")],
		"ok": [
				("a", "og"),
				("A", "og"),
				("i", "og"),
				("I", "og"),
				("u", "og"),
				("U", "og"),
				("f", "og"),
				("e", "og"),
				("E", "og"),
				("o", "og"),
				("O", "og")],
		"Ek": [
				("a", "Eg"),
				("A", "Eg"),
				("i", "Eg"),
				("I", "Eg"),
				("u", "Eg"),
				("U", "Eg"),
				("f", "Eg"),
				("e", "Eg"),
				("E", "Eg"),
				("o", "Eg"),
				("O", "Eg")],
		"Ok": [
				("a", "Og"),
				("A", "Og"),
				("i", "Og"),
				("I", "Og"),
				("u", "Og"),
				("U", "Og"),
				("f", "Og"),
				("e", "Og"),
				("E", "Og"),
				("o", "Og"),
				("O", "Og")],
		"aw": [
				("a", "aq"),
				("A", "aq"),
				("i", "aq"),
				("I", "aq"),
				("u", "aq"),
				("U", "aq"),
				("f", "aq"),
				("e", "aq"),
				("E", "aq"),
				("o", "aq"),
				("O", "aq")],
		"Aw": [
				("a", "Aq"),
				("A", "Aq"),
				("i", "Aq"),
				("I", "Aq"),
				("u", "Aq"),
				("U", "Aq"),
				("f", "Aq"),
				("e", "Aq"),
				("E", "Aq"),
				("o", "Aq"),
				("O", "Aq")],
		"iw": [
				("a", "iq"),
				("A", "iq"),
				("i", "iq"),
				("I", "iq"),
				("u", "iq"),
				("U", "iq"),
				("f", "iq"),
				("e", "iq"),
				("E", "iq"),
				("o", "iq"),
				("O", "iq")],
		"Iw": [
				("a", "Iq"),
				("A", "Iq"),
				("i", "Iq"),
				("I", "Iq"),
				("u", "Iq"),
				("U", "Iq"),
				("f", "Iq"),
				("e", "Iq"),
				("E", "Iq"),
				("o", "Iq"),
				("O", "Iq")],
		"uw": [
				("a", "uq"),
				("A", "uq"),
				("i", "uq"),
				("I", "uq"),
				("u", "uq"),
				("U", "uq"),
				("f", "uq"),
				("e", "uq"),
				("E", "uq"),
				("o", "uq"),
				("O", "uq")],
		"Uw": [
				("a", "Uq"),
				("A", "Uq"),
				("i", "Uq"),
				("I", "Uq"),
				("u", "Uq"),
				("U", "Uq"),
				("f", "Uq"),
				("e", "Uq"),
				("E", "Uq"),
				("o", "Uq"),
				("O", "Uq")],
		"ew": [
				("a", "eq"),
				("A", "eq"),
				("i", "eq"),
				("I", "eq"),
				("u", "eq"),
				("U", "eq"),
				("f", "eq"),
				("e", "eq"),
				("E", "eq"),
				("o", "eq"),
				("O", "eq")],
		"ow": [
				("a", "oq"),
				("A", "oq"),
				("i", "oq"),
				("I", "oq"),
				("u", "oq"),
				("U", "oq"),
				("f", "oq"),
				("e", "oq"),
				("E", "oq"),
				("o", "oq"),
				("O", "oq")],
		"Ew": [
				("a", "Eq"),
				("A", "Eq"),
				("i", "Eq"),
				("I", "Eq"),
				("u", "Eq"),
				("U", "Eq"),
				("f", "Eq"),
				("e", "Eq"),
				("E", "Eq"),
				("o", "Eq"),
				("O", "Eq")],
		"Ow": [
				("a", "Oq"),
				("A", "Oq"),
				("i", "Oq"),
				("I", "Oq"),
				("u", "Oq"),
				("U", "Oq"),
				("f", "Oq"),
				("e", "Oq"),
				("E", "Oq"),
				("o", "Oq"),
				("O", "Oq")],
		"at": [
				("a", "ad"),
				("A", "ad"),
				("i", "ad"),
				("I", "ad"),
				("u", "ad"),
				("U", "ad"),
				("f", "ad"),
				("e", "ad"),
				("E", "ad"),
				("o", "ad"),
				("O", "ad")],
		"At": [
				("a", "Ad"),
				("A", "Ad"),
				("i", "Ad"),
				("I", "Ad"),
				("u", "Ad"),
				("U", "Ad"),
				("f", "Ad"),
				("e", "Ad"),
				("E", "Ad"),
				("o", "Ad"),
				("O", "Ad")],
		"it": [
				("a", "id"),
				("A", "id"),
				("i", "id"),
				("I", "id"),
				("u", "id"),
				("U", "id"),
				("f", "id"),
				("e", "id"),
				("E", "id"),
				("o", "id"),
				("O", "id")],
		"It": [
				("a", "Id"),
				("A", "Id"),
				("i", "Id"),
				("I", "Id"),
				("u", "Id"),
				("U", "Id"),
				("f", "Id"),
				("e", "Id"),
				("E", "Id"),
				("o", "Id"),
				("O", "Id")],
		"ut": [
				("a", "ud"),
				("A", "ud"),
				("i", "ud"),
				("I", "ud"),
				("u", "ud"),
				("U", "ud"),
				("f", "ud"),
				("e", "ud"),
				("E", "ud"),
				("o", "ud"),
				("O", "ud")],
		"Ut": [
				("a", "Ud"),
				("A", "Ud"),
				("i", "Ud"),
				("I", "Ud"),
				("u", "Ud"),
				("U", "Ud"),
				("f", "Ud"),
				("e", "Ud"),
				("E", "Ud"),
				("o", "Ud"),
				("O", "Ud")],
		"et": [
				("a", "ed"),
				("A", "ed"),
				("i", "ed"),
				("I", "ed"),
				("u", "ed"),
				("U", "ed"),
				("f", "ed"),
				("e", "ed"),
				("E", "ed"),
				("o", "ed"),
				("O", "ed")],
		"ot": [
				("a", "od"),
				("A", "od"),
				("i", "od"),
				("I", "od"),
				("u", "od"),
				("U", "od"),
				("f", "od"),
				("e", "od"),
				("E", "od"),
				("o", "od"),
				("O", "od")],
		"Et": [
				("a", "Ed"),
				("A", "Ed"),
				("i", "Ed"),
				("I", "Ed"),
				("u", "Ed"),
				("U", "Ed"),
				("f", "Ed"),
				("e", "Ed"),
				("E", "Ed"),
				("o", "Ed"),
				("O", "Ed")],
		"Ot": [
				("a", "Od"),
				("A", "Od"),
				("i", "Od"),
				("I", "Od"),
				("u", "Od"),
				("U", "Od"),
				("f", "Od"),
				("e", "Od"),
				("E", "Od"),
				("o", "Od"),
				("O", "Od")],
		"ap": [
				("a", "ab"),
				("A", "ab"),
				("i", "ab"),
				("I", "ab"),
				("u", "ab"),
				("U", "ab"),
				("f", "ab"),
				("e", "ab"),
				("E", "ab"),
				("o", "ab"),
				("O", "ab")],
		"Ap": [
				("a", "Ab"),
				("A", "Ab"),
				("i", "Ab"),
				("I", "Ab"),
				("u", "Ab"),
				("U", "Ab"),
				("f", "Ab"),
				("e", "Ab"),
				("E", "Ab"),
				("o", "Ab"),
				("O", "Ab")],
		"ip": [
				("a", "ib"),
				("A", "ib"),
				("i", "ib"),
				("I", "ib"),
				("u", "ib"),
				("U", "ib"),
				("f", "ib"),
				("e", "ib"),
				("E", "ib"),
				("o", "ib"),
				("O", "ib")],
		"Ip": [
				("a", "Ib"),
				("A", "Ib"),
				("i", "Ib"),
				("I", "Ib"),
				("u", "Ib"),
				("U", "Ib"),
				("f", "Ib"),
				("e", "Ib"),
				("E", "Ib"),
				("o", "Ib"),
				("O", "Ib")],
		"up": [
				("a", "ub"),
				("A", "ub"),
				("i", "ub"),
				("I", "ub"),
				("u", "ub"),
				("U", "ub"),
				("f", "ub"),
				("e", "ub"),
				("E", "ub"),
				("o", "ub"),
				("O", "ub")],
		"Up": [
				("a", "Ub"),
				("A", "Ub"),
				("i", "Ub"),
				("I", "Ub"),
				("u", "Ub"),
				("U", "Ub"),
				("f", "Ub"),
				("e", "Ub"),
				("E", "Ub"),
				("o", "Ub"),
				("O", "Ub")],
		"ep": [
				("a", "eb"),
				("A", "eb"),
				("i", "eb"),
				("I", "eb"),
				("u", "eb"),
				("U", "eb"),
				("f", "eb"),
				("e", "eb"),
				("E", "eb"),
				("o", "eb"),
				("O", "eb")],
		"op": [
				("a", "ob"),
				("A", "ob"),
				("i", "ob"),
				("I", "ob"),
				("u", "ob"),
				("U", "ob"),
				("f", "ob"),
				("e", "ob"),
				("E", "ob"),
				("o", "ob"),
				("O", "ob")],
		"Ep": [
				("a", "Eb"),
				("A", "Eb"),
				("i", "Eb"),
				("I", "Eb"),
				("u", "Eb"),
				("U", "Eb"),
				("f", "Eb"),
				("e", "Eb"),
				("E", "Eb"),
				("o", "Eb"),
				("O", "Eb")],
		"Op": [
				("a", "Ob"),
				("A", "Ob"),
				("i", "Ob"),
				("I", "Ob"),
				("u", "Ob"),
				("U", "Ob"),
				("f", "Ob"),
				("e", "Ob"),
				("E", "Ob"),
				("o", "Ob"),
				("O", "Ob")],
		"aN": [
				("a", "aNN"),
				("A", "aNN"),
				("i", "aNN"),
				("I", "aNN"),
				("u", "aNN"),
				("U", "aNN"),
				("f", "aNN"),
				("e", "aNN"),
				("E", "aNN"),
				("o", "aNN"),
				("O", "aNN")],
		"AN": [
				("a", "AN"),
				("A", "AN"),
				("i", "AN"),
				("I", "AN"),
				("u", "AN"),
				("U", "AN"),
				("f", "AN"),
				("e", "AN"),
				("E", "AN"),
				("o", "AN"),
				("O", "AN")],
		"iN": [
				("a", "iNN"),
				("A", "iNN"),
				("i", "iNN"),
				("I", "iNN"),
				("u", "iNN"),
				("U", "iNN"),
				("f", "iNN"),
				("e", "iNN"),
				("E", "iNN"),
				("o", "iNN"),
				("O", "iNN")],
		"IN": [
				("a", "IN"),
				("A", "IN"),
				("i", "IN"),
				("I", "IN"),
				("u", "IN"),
				("U", "IN"),
				("f", "IN"),
				("e", "IN"),
				("E", "IN"),
				("o", "IN"),
				("O", "IN")],
		"uN": [
				("a", "uNN"),
				("A", "uNN"),
				("i", "uNN"),
				("I", "uNN"),
				("u", "uNN"),
				("U", "uNN"),
				("f", "uNN"),
				("e", "uNN"),
				("E", "uNN"),
				("o", "uNN"),
				("O", "uNN")],
		"UN": [
				("a", "UN"),
				("A", "UN"),
				("i", "UN"),
				("I", "UN"),
				("u", "UN"),
				("U", "UN"),
				("f", "UN"),
				("e", "UN"),
				("E", "UN"),
				("o", "UN"),
				("O", "UN")],
		"eN": [
				("a", "eNN"),
				("A", "eNN"),
				("i", "eNN"),
				("I", "eNN"),
				("u", "eNN"),
				("U", "eNN"),
				("f", "eNN"),
				("e", "eNN"),
				("E", "eNN"),
				("o", "eNN"),
				("O", "eNN")],
		"oN": [
				("a", "oNN"),
				("A", "oNN"),
				("i", "oNN"),
				("I", "oNN"),
				("u", "oNN"),
				("U", "oNN"),
				("f", "oNN"),
				("e", "oNN"),
				("E", "oNN"),
				("o", "oNN"),
				("O", "oNN")],
		"EN": [
				("a", "EN"),
				("A", "EN"),
				("i", "EN"),
				("I", "EN"),
				("u", "EN"),
				("U", "EN"),
				("f", "EN"),
				("e", "EN"),
				("E", "EN"),
				("o", "EN"),
				("O", "EN")],
		"ON": [
				("a", "ON"),
				("A", "ON"),
				("i", "ON"),
				("I", "ON"),
				("u", "ON"),
				("U", "ON"),
				("f", "ON"),
				("e", "ON"),
				("E", "ON"),
				("o", "ON"),
				("O", "ON")],
		"an": [
				("a", "ann"),
				("A", "ann"),
				("i", "ann"),
				("I", "ann"),
				("u", "ann"),
				("U", "ann"),
				("f", "ann"),
				("e", "ann"),
				("E", "ann"),
				("o", "ann"),
				("O", "ann")],
		"An": [
				("a", "An"),
				("A", "An"),
				("i", "An"),
				("I", "An"),
				("u", "An"),
				("U", "An"),
				("f", "An"),
				("e", "An"),
				("E", "An"),
				("o", "An"),
				("O", "An")],
		"in": [
				("a", "inn"),
				("A", "inn"),
				("i", "inn"),
				("I", "inn"),
				("u", "inn"),
				("U", "inn"),
				("f", "inn"),
				("e", "inn"),
				("E", "inn"),
				("o", "inn"),
				("O", "inn")],
		"In": [
				("a", "In"),
				("A", "In"),
				("i", "In"),
				("I", "In"),
				("u", "In"),
				("U", "In"),
				("f", "In"),
				("e", "In"),
				("E", "In"),
				("o", "In"),
				("O", "In")],
		"un": [
				("a", "unn"),
				("A", "unn"),
				("i", "unn"),
				("I", "unn"),
				("u", "unn"),
				("U", "unn"),
				("f", "unn"),
				("e", "unn"),
				("E", "unn"),
				("o", "unn"),
				("O", "unn")],
		"Un": [
				("a", "Un"),
				("A", "Un"),
				("i", "Un"),
				("I", "Un"),
				("u", "Un"),
				("U", "Un"),
				("f", "Un"),
				("e", "Un"),
				("E", "Un"),
				("o", "Un"),
				("O", "Un")],
		"en": [
				("a", "enn"),
				("A", "enn"),
				("i", "enn"),
				("I", "enn"),
				("u", "enn"),
				("U", "enn"),
				("f", "enn"),
				("e", "enn"),
				("E", "enn"),
				("o", "enn"),
				("O", "enn")],
		"on": [
				("a", "onn"),
				("A", "onn"),
				("i", "onn"),
				("I", "onn"),
				("u", "onn"),
				("U", "onn"),
				("f", "onn"),
				("e", "onn"),
				("E", "onn"),
				("o", "onn"),
				("O", "onn")],
		"En": [
				("a", "En"),
				("A", "En"),
				("i", "En"),
				("I", "En"),
				("u", "En"),
				("U", "En"),
				("f", "En"),
				("e", "En"),
				("E", "En"),
				("o", "En"),
				("O", "En")],
		"On": [
				("a", "On"),
				("A", "On"),
				("i", "On"),
				("I", "On"),
				("u", "On"),
				("U", "On"),
				("f", "On"),
				("e", "On"),
				("E", "On"),
				("o", "On"),
				("O", "On")],
		"am": [
				("a", "am"),
				("A", "am"),
				("i", "am"),
				("I", "am"),
				("u", "am"),
				("U", "am"),
				("f", "am"),
				("e", "am"),
				("E", "am"),
				("o", "am"),
				("O", "am")],
		"Am": [
				("a", "Am"),
				("A", "Am"),
				("i", "Am"),
				("I", "Am"),
				("u", "Am"),
				("U", "Am"),
				("f", "Am"),
				("e", "Am"),
				("E", "Am"),
				("o", "Am"),
				("O", "Am")],
		"im": [
				("a", "im"),
				("A", "im"),
				("i", "im"),
				("I", "im"),
				("u", "im"),
				("U", "im"),
				("f", "im"),
				("e", "im"),
				("E", "im"),
				("o", "im"),
				("O", "im")],
		"Im": [
				("a", "Im"),
				("A", "Im"),
				("i", "Im"),
				("I", "Im"),
				("u", "Im"),
				("U", "Im"),
				("f", "Im"),
				("e", "Im"),
				("E", "Im"),
				("o", "Im"),
				("O", "Im")],
		"um": [
				("a", "um"),
				("A", "um"),
				("i", "um"),
				("I", "um"),
				("u", "um"),
				("U", "um"),
				("f", "um"),
				("e", "um"),
				("E", "um"),
				("o", "um"),
				("O", "um")],
		"Um": [
				("a", "Um"),
				("A", "Um"),
				("i", "Um"),
				("I", "Um"),
				("u", "Um"),
				("U", "Um"),
				("f", "Um"),
				("e", "Um"),
				("E", "Um"),
				("o", "Um"),
				("O", "Um")],
		"em": [
				("a", "em"),
				("A", "em"),
				("i", "em"),
				("I", "em"),
				("u", "em"),
				("U", "em"),
				("f", "em"),
				("e", "em"),
				("E", "em"),
				("o", "em"),
				("O", "em")],
		"om": [
				("a", "om"),
				("A", "om"),
				("i", "om"),
				("I", "om"),
				("u", "om"),
				("U", "om"),
				("f", "om"),
				("e", "om"),
				("E", "om"),
				("o", "om"),
				("O", "om")],
		"Em": [
				("a", "Em"),
				("A", "Em"),
				("i", "Em"),
				("I", "Em"),
				("u", "Em"),
				("U", "Em"),
				("f", "Em"),
				("e", "Em"),
				("E", "Em"),
				("o", "Em"),
				("O", "Em")],
		"Om": [
				("a", "Om"),
				("A", "Om"),
				("i", "Om"),
				("I", "Om"),
				("u", "Om"),
				("U", "Om"),
				("f", "Om"),
				("e", "Om"),
				("E", "Om"),
				("o", "Om"),
				("O", "Om")],
			}
# {finals: [(initial, new_second_final+new_final), ...], ...}
# "new_second_final+new_final" replace the last two caracters of the previous word while the initial is unchanged
visarga_sandhi_1 = {
		"aH": [
				("a", "o '"),
				("A", "a"),
				("i", "a"),
				("i", "a"),
				("u", "a"),
				("U", "a"),
				("f", "a"),
				("e", "a"),
				("E", "a"),
				("o", "a"),
				("O", "a"),
				("y", "o"),
				("r", "o"),
				("l", "o"),
				("v", "o"),
				("S", "aH"),
				("z", "aH"),
				("s", "aH"),
				("h", "o")],
		"AH": [
				("a", "A"),
				("A", "A"),
				("i", "A"),
				("i", "A"),
				("u", "A"),
				("U", "A"),
				("f", "A"),
				("e", "A"),
				("E", "A"),
				("o", "A"),
				("O", "A"),
				("y", "A"),
				("r", "A"),
				("l", "A"),
				("v", "A"),
				("S", "AH"),
				("z", "AH"),
				("s", "AH"),
				("h", "A")],
		"iH": [
				("a", "ir"),
				("A", "ir"),
				("i", "ir"),
				("i", "ir"),
				("u", "ir"),
				("U", "ir"),
				("f", "ir"),
				("e", "ir"),
				("E", "ir"),
				("o", "ir"),
				("O", "ir"),
				("y", "ir"),
				("r", "I"),
				("l", "ir"),
				("v", "ir"),
				("S", "H"),
				("z", "iH"),
				("s", "iH"),
				("h", "ir")],
		"IH": [
				("a", "Ir"),
				("A", "Ir"),
				("i", "Ir"),
				("i", "Ir"),
				("u", "Ir"),
				("U", "Ir"),
				("f", "Ir"),
				("e", "Ir"),
				("E", "Ir"),
				("o", "Ir"),
				("O", "Ir"),
				("y", "Ir"),
				("r", "I"),
				("l", "Ir"),
				("v", "Ir"),
				("S", "H"),
				("z", "IH"),
				("s", "IH"),
				("h", "Ir")],
		"uH": [
				("a", "ur"),
				("A", "ur"),
				("i", "ur"),
				("i", "ur"),
				("u", "ur"),
				("U", "ur"),
				("f", "ur"),
				("e", "ur"),
				("E", "ur"),
				("o", "ur"),
				("O", "ur"),
				("y", "ur"),
				("r", "U"),
				("l", "ur"),
				("v", "ur"),
				("S", "H"),
				("z", "uH"),
				("s", "uH"),
				("h", "ur")],
		"UH": [
				("a", "Ur"),
				("A", "Ur"),
				("i", "Ur"),
				("i", "Ur"),
				("u", "Ur"),
				("U", "Ur"),
				("f", "Ur"),
				("e", "Ur"),
				("E", "Ur"),
				("o", "Ur"),
				("O", "Ur"),
				("y", "Ur"),
				("r", "U"),
				("l", "Ur"),
				("v", "Ur"),
				("S", "H"),
				("z", "UH"),
				("s", "UH"),
				("h", "Ur")],
		"eH": [
				("a", "er"),
				("A", "er"),
				("i", "er"),
				("i", "er"),
				("u", "er"),
				("U", "er"),
				("f", "er"),
				("e", "er"),
				("E", "er"),
				("o", "er"),
				("O", "er"),
				("y", "er"),
				("r", "e"),
				("l", "er"),
				("v", "er"),
				("S", "H"),
				("z", "eH"),
				("s", "eH"),
				("h", "er")],
		"oH": [
				("a", "or"),
				("A", "or"),
				("i", "or"),
				("i", "or"),
				("u", "or"),
				("U", "or"),
				("f", "or"),
				("e", "or"),
				("E", "or"),
				("o", "or"),
				("O", "or"),
				("y", "or"),
				("r", "o"),
				("l", "or"),
				("v", "or"),
				("S", "H"),
				("z", "oH"),
				("s", "oH"),
				("h", "or")],
		"EH": [
				("a", "Er"),
				("A", "Er"),
				("i", "Er"),
				("i", "Er"),
				("u", "Er"),
				("U", "Er"),
				("f", "Er"),
				("e", "Er"),
				("E", "Er"),
				("o", "Er"),
				("O", "Er"),
				("y", "Er"),
				("r", "E"),
				("l", "Er"),
				("v", "Er"),
				("S", "H"),
				("z", "EH"),
				("s", "EH"),
				("h", "Er")],
		"OH": [
				("a", "Or"),
				("A", "Or"),
				("i", "Or"),
				("i", "Or"),
				("u", "Or"),
				("U", "Or"),
				("f", "Or"),
				("e", "Or"),
				("E", "Or"),
				("o", "Or"),
				("O", "Or"),
				("y", "Or"),
				("r", "O"),
				("l", "Or"),
				("v", "Or"),
				("S", "H"),
				("z", "OH"),
				("s", "OH"),
				("h", "Or")],
			}
# {finals: [(initial, new_second_final+new_final), ...], ...}
# "new_second_final+new_final" replace the last two caracters of the previous word while the initial is unchanged
visarga_sandhi_2 = {
		"aH": [
				("k", "aH"),
				("K", "aH"),
				("g", "o"),
				("g", "ar"),
				("G", "o"),
				("G", "ar"),
				("c", "aS"),
				("C", "aS"),
				("j", "o"),
				("j", "ar"),
				("J", "o"),
				("J", "ar"),
				("w", "az"),
				("W", "az"),
				("q", "o"),
				("q", "ar"),
				("Q", "o"),
				("Q", "ar"),
				("t", "as"),
				("T", "as"),
				("d", "o"),
				("d", "ar"),
				("D", "o"),
				("D", "ar"),
				("p", "aH"),
				("P", "aH"),
				("b", "o"),
				("b", "ar"),
				("B", "o"),
				("B", "ar"),
				("n", "o"),
				("n", "ar"),
				("m", "o"),
				("m", "ar")],
		"AH": [
				("k", "AH"),
				("K", "AH"),
				("g", "A"),
				("g", "Ar"),
				("G", "A"),
				("G", "Ar"),
				("c", "AS"),
				("C", "AS"),
				("j", "A"),
				("j", "Ar"),
				("J", "A"),
				("J", "Ar"),
				("w", "Az"),
				("W", "Az"),
				("q", "A"),
				("q", "Ar"),
				("Q", "A"),
				("Q", "Ar"),
				("t", "As"),
				("T", "As"),
				("d", "A"),
				("d", "Ar"),
				("D", "A"),
				("D", "Ar"),
				("p", "AH"),
				("P", "AH"),
				("b", "A"),
				("b", "Ar"),
				("B", "A"),
				("B", "Ar"),
				("n", "A"),
				("n", "Ar"),
				("m", "A"),
				("m", "Ar")],
		"iH": [
				("k", "iH"),
				("K", "iH"),
				("g", "ir"),
				("g", "ir"),
				("G", "ir"),
				("G", "ir"),
				("c", "iS"),
				("C", "iS"),
				("j", "ir"),
				("j", "ir"),
				("J", "ir"),
				("J", "ir"),
				("w", "iz"),
				("W", "iz"),
				("q", "ir"),
				("q", "ir"),
				("Q", "ir"),
				("Q", "ir"),
				("t", "is"),
				("T", "is"),
				("d", "ir"),
				("d", "ir"),
				("D", "ir"),
				("D", "ir"),
				("p", "iH"),
				("P", "iH"),
				("b", "ir"),
				("b", "ir"),
				("B", "ir"),
				("B", "ir"),
				("n", "ir"),
				("n", "ir"),
				("m", "ir"),
				("m", "ir")],
		"IH": [
				("k", "IH"),
				("K", "IH"),
				("g", "Ir"),
				("g", "Ir"),
				("G", "Ir"),
				("G", "Ir"),
				("c", "IS"),
				("C", "IS"),
				("j", "Ir"),
				("j", "Ir"),
				("J", "Ir"),
				("J", "Ir"),
				("w", "Iz"),
				("W", "Iz"),
				("q", "Ir"),
				("q", "Ir"),
				("Q", "Ir"),
				("Q", "Ir"),
				("t", "Is"),
				("T", "Is"),
				("d", "Ir"),
				("d", "Ir"),
				("D", "Ir"),
				("D", "Ir"),
				("p", "IH"),
				("P", "IH"),
				("b", "Ir"),
				("b", "Ir"),
				("B", "Ir"),
				("B", "Ir"),
				("n", "Ir"),
				("n", "Ir"),
				("m", "Ir"),
				("m", "Ir")],
		"uH": [
				("k", "uH"),
				("K", "uH"),
				("g", "ur"),
				("g", "ur"),
				("G", "ur"),
				("G", "ur"),
				("c", "uS"),
				("C", "uS"),
				("j", "ur"),
				("j", "ur"),
				("J", "ur"),
				("J", "ur"),
				("w", "uz"),
				("W", "uz"),
				("q", "ur"),
				("q", "ur"),
				("Q", "ur"),
				("Q", "ur"),
				("t", "us"),
				("T", "us"),
				("d", "ur"),
				("d", "ur"),
				("D", "ur"),
				("D", "ur"),
				("p", "uH"),
				("P", "uH"),
				("b", "ur"),
				("b", "ur"),
				("B", "ur"),
				("B", "ur"),
				("n", "ur"),
				("n", "ur"),
				("m", "ur"),
				("m", "ur")],
		"UH": [
				("k", "UH"),
				("K", "UH"),
				("g", "Ur"),
				("g", "Ur"),
				("G", "Ur"),
				("G", "Ur"),
				("c", "US"),
				("C", "US"),
				("j", "Ur"),
				("j", "Ur"),
				("J", "Ur"),
				("J", "Ur"),
				("w", "Uz"),
				("W", "Uz"),
				("q", "Ur"),
				("q", "Ur"),
				("Q", "Ur"),
				("Q", "Ur"),
				("t", "Us"),
				("T", "Us"),
				("d", "Ur"),
				("d", "Ur"),
				("D", "Ur"),
				("D", "Ur"),
				("p", "UH"),
				("P", "UH"),
				("b", "Ur"),
				("b", "Ur"),
				("B", "Ur"),
				("B", "Ur"),
				("n", "Ur"),
				("n", "Ur"),
				("m", "Ur"),
				("m", "Ur")],
		"eH": [
				("k", "eH"),
				("K", "eH"),
				("g", "er"),
				("g", "er"),
				("G", "er"),
				("G", "er"),
				("c", "eS"),
				("C", "eS"),
				("j", "er"),
				("j", "er"),
				("J", "er"),
				("J", "er"),
				("w", "ez"),
				("W", "ez"),
				("q", "er"),
				("q", "er"),
				("Q", "er"),
				("Q", "er"),
				("t", "es"),
				("T", "es"),
				("d", "er"),
				("d", "er"),
				("D", "er"),
				("D", "er"),
				("p", "eH"),
				("P", "eH"),
				("b", "er"),
				("b", "er"),
				("B", "er"),
				("B", "er"),
				("n", "er"),
				("n", "er"),
				("m", "er"),
				("m", "er")],
		"oH": [
				("k", "oH"),
				("K", "oH"),
				("g", "or"),
				("g", "or"),
				("G", "or"),
				("G", "or"),
				("c", "oS"),
				("C", "oS"),
				("j", "or"),
				("j", "or"),
				("J", "or"),
				("J", "or"),
				("w", "oz"),
				("W", "oz"),
				("q", "or"),
				("q", "or"),
				("Q", "or"),
				("Q", "or"),
				("t", "os"),
				("T", "os"),
				("d", "or"),
				("d", "or"),
				("D", "or"),
				("D", "or"),
				("p", "oH"),
				("P", "oH"),
				("b", "or"),
				("b", "or"),
				("B", "or"),
				("B", "or"),
				("n", "or"),
				("n", "or"),
				("m", "or"),
				("m", "or")],
		"EH": [
				("k", "EH"),
				("K", "EH"),
				("g", "Er"),
				("g", "Er"),
				("G", "Er"),
				("G", "Er"),
				("c", "ES"),
				("C", "ES"),
				("j", "Er"),
				("j", "Er"),
				("J", "Er"),
				("J", "Er"),
				("w", "Ez"),
				("W", "Ez"),
				("q", "Er"),
				("q", "Er"),
				("Q", "Er"),
				("Q", "Er"),
				("t", "Es"),
				("T", "Es"),
				("d", "Er"),
				("d", "Er"),
				("D", "Er"),
				("D", "Er"),
				("p", "EH"),
				("P", "EH"),
				("b", "Er"),
				("b", "Er"),
				("B", "Er"),
				("B", "Er"),
				("n", "Er"),
				("n", "Er"),
				("m", "Er"),
				("m", "Er")],
		"OH": [
				("k", "OH"),
				("K", "OH"),
				("g", "Or"),
				("g", "Or"),
				("G", "Or"),
				("G", "Or"),
				("c", "OS"),
				("C", "OS"),
				("j", "Or"),
				("j", "Or"),
				("J", "Or"),
				("J", "Or"),
				("w", "Oz"),
				("W", "Oz"),
				("q", "Or"),
				("q", "Or"),
				("Q", "Or"),
				("Q", "Or"),
				("t", "Os"),
				("T", "Os"),
				("d", "Or"),
				("d", "Or"),
				("D", "Or"),
				("D", "Or"),
				("p", "OH"),
				("P", "OH"),
				("b", "Or"),
				("b", "Or"),
				("B", "Or"),
				("B", "Or"),
				("n", "Or"),
				("n", "Or"),
				("m", "Or"),
				("m", "Or")],
			}
# {final: [(empty_string, new_final), ...], ...}
absolute_finals_sandhi = {
		"k": [
				("", "k")],
		"K": [
				("", "k")],
		"g": [
				("", "k")],
		"G": [
				("", "k")],
		"w": [
				("", "w")],
		"W": [
				("", "w")],
		"q": [
				("", "w")],
		"Q": [
				("", "w")],
		"t": [
				("", "t")],
		"T": [
				("", "t")],
		"d": [
				("", "t")],
		"D": [
				("", "t")],
		"p": [
				("", "p")],
		"P": [
				("", "p")],
		"b": [
				("", "p")],
		"B": [
				("", "p")],
		"c": [
				("", "k")],
		"C": [
				("", "k")],
		"j": [
				("", "w")],
		"J": [
				("", "w")],
		"S": [
				("", "k")],
		"N": [
				("", "N")],
		"Y": [
				("", "Y")],
		"R": [
				("", "R")],
		"n": [
				("", "n")],
		"m": [
				("", "m")],
		"s": [
				("", "H")],
		"r": [
				("", "H")],
			}
# {final: [(initial, newFinal), ...], ...}
# the final consonant is unchanged
cC_words_sandhi = {
		"a": [
				("c", "cC"),
				("C", "cC")],
		"A": [
				("c", "c"),
				("C", "C")],
		"i": [
				("c", "cC"),
				("C", "cC")],
		"I": [
				("c", "c"),
				("C", "C")],
		"u": [
				("c", "cC"),
				("C", "cC")],
		"U": [
				("c", "c"),
				("C", "C")],
		"f": [
				("c", "cC"),
				("C", "cC")],
		"e": [
				("c", "cC"),
				("C", "cC")],
		"E": [
				("c", "c"),
				("C", "C")],
		"o": [
				("c", "cC"),
				("C", "cC")],
		"O": [
				("c", "c"),
				("C", "C")],
			}
# {final: [(initial, newFinal), ...], ...}
# the initial consonant is unchanged
punar_sandhi = {
		"r": [
				("k", "H"),
				("K", "H"),
				("g", "r"),
				("G", "r"),
				("c", "H"),
				("C", "H"),
				("j", "r"),
				("J", "r"),
				("w", "H"),
				("W", "H"),
				("q", "r"),
				("Q", "r"),
				("t", "H"),
				("T", "H"),
				("d", "r"),
				("D", "r"),
				("p", "H"),
				("P", "H"),
				("b", "r"),
				("B", "r"),
				("N", "r"),
				("Y", "r"),
				("R", "r"),
				("n", "r"),
				("m", "r"),
				("y", "H"),
				("r", "H"),
				("l", "H"),
				("v", "H"),
				("S", "H"),
				("z", "H"),
				("s", "H"),
				("h", "H"),
				("a", "r"),
				("A", "r"),
				("A", "r"),
				("i", "r"),
				("i", "r"),
				("u", "r"),
				("U", "r"),
				("f", "r"),
				("e", "r"),
				("E", "r"),
				("o", "r"),
				("O", "r")],
			}