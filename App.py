from Mypack import voting
import traceback
try:
    ref=voting.voter("Ashish Duhan",17)

except Exception as e:
    traceback.print_exc()