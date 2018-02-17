from config import *
from run_truncation_on_wordlist import *
from vowel_removal_truncator import *
from truncator_tester import *

def test_truncation():
	truncator = VowelRemovalTruncator()
	runner = TruncationOnWordlistRunner(
		path.join(IN_DIR, "wordsEn.csv"),
		path.join(OUT_DIR, "out.csv")
	)
	result = runner.run_truncator_on_wordlist(truncator)
	runner.save_output_to_csv(result)
	tester = TruncatorTester()
	# TODO: stop test_file from freezing/hanging indefinitely
	# out = tester.test_file(
	# 	path.join(OUT_DIR, "out.csv"),
	# 	"/System/Library/Fonts/Monaco.dfont"
	# )
	# print(out)
