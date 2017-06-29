from run_truncation_on_wordlist import *
from vowel_removal_truncator import *
from truncation_tester import *
truncator = VowelRemovalTruncator()
runner = TruncationOnWordlistRunner("./wordsEn.csv","./out.csv")
result = runner.run_truncator_on_wordlist(truncator)
runner.save_output_to_csv(result)
tester = TruncatorTester()
print(tester.test_file("./out.csv","/System/Library/Fonts/Monaco.dfont"))
