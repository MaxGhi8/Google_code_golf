#! /usr/bin/env bash
link="https://docs.google.com/spreadsheets/u/1/d/e/2PACX-1vQ7RUqwrtwRD2EJbgMRrccAHkwUQZgFe2fsROCR1WV5LA1naxL0pU2grjQpcWC2HU3chdGwIOUpeuoK/pubhtml/sheet?headers=false&gid=1427788625"
curl -s $link |
    pup 'table.waffle tbody tr td:nth-child(3) text{}' |
    tail -n 400 |
    awk '{
      task = sprintf("%03d",NR); ftask = "nostre+rubate/task" task ".py";
      if (system("[ -f \"" ftask "\" ]") == 0) {
          cmd="wc -c < " ftask;
          cmd | getline size;
          close(cmd);
      } else {
          size=2500;
      }
      print size-$1, task, $r, size;
  }' |
    # sort -k4 -n | awk '
    sort -nr | awk '
    $4<2500 {print "task " $2 " could be " $1 "B smaller, they did in " $3 "B, we took " $4 "B"};
    $4>=2500 {print "task " $2 " could be done in just " $3 "B, we should try it"}'
