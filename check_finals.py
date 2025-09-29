import os
import subprocess
import sys

base='finals/task{:03}.py'
fail=[];missing=[];checked=0
for i in range(1,401):
 f=base.format(i)
 if not os.path.exists(f):
  print(f,'MISSING')
  missing.append(f);continue
 r=subprocess.run(['python','code_checker.py',f],capture_output=True,text=True)
 if 'CORRECT' in r.stdout:
  print(f,'CORRECT')
 else:
  print(f,'WRONG')
  fail.append((f,r.stdout+r.stderr))
 checked+=1

print('\nSummary:')
print('Checked:',checked,'Missing:',len(missing),'Failed:',len(fail))
if missing:print('\nMissing files:\n'+'\n'.join(missing))
if fail:
 print('\nFailures details:')
 for f,out in fail:print('\n==',f,'==\n',out)
 sys.exit(1)
 for f,out in fail:print('\n==',f,'==\n',out)
 sys.exit(1)
