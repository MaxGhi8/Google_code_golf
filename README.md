# Google Code Golf Challenge - Progress Tracker

## 🎯 Overview

This repository contains solutions for 401 Google Code Golf tasks, numbered from `task000.py` to `task400.py`. Each task focuses on writing the shortest possible Python code to solve specific problems.

## 🏆 Goals
- ✅ Complete all 400 tasks
- 🎯 Optimize for minimal character count
- 🕒 Execution time does not count, 😈 only bytes matters here

## 📚 Our tips
1. Be as crazy as possible, **if you can understand it, you can write less**
2. Use white spaces instead of tabs for indexing
3. Use lambda functions for one-line functions and with no variables, see [task006.py](task006.py).
4. Use lambda functions for one-line functions and with one constant, see[task016.py](task016.py)
5. We can assign a name to functions that occurs many times in the program, for 5 letter functions (like `range`) that occurs only 2 times is not worth it, but with more letter functions or with many repetitions it can save at least **1 byte!** See [task014.py](task014.py)
6. rotation clockwise code -> `r=lambda m:[*map(list,zip(*m[::-1]))]` and counter-clockwise -> `l=lambda m:[*map(list,zip(*m))][::-1]`, of course it holds that `l=r \circ r \circ r` and this identity can be useful in many situations, so I only implement `l` or `r`, see [task214.py](task214.py).
7. Sometimes can be better substitute a `range(len(...))` with `enumerate(...)`, in particular when there is already one or more enumerate in the code and combine this observation with tips 5., see [task215.py](task215.py)

## 🚀 Getting Started
The challenge description is available [here](https://www.kaggle.com/competitions/google-code-golf-2025/overview) and the notebook to starts with is [here](https://www.kaggle.com/code/mmoffitt/neurips-2025-google-code-golf-championship) and [here](https://www.kaggle.com/code/jazivxt/oh-barnacles) there is a notebook with already many solutions available, but probably not optimal.


## 📚 Additional Resources

### Useful Links
- [Python Standard Library, no other libraries are allowed](https://docs.python.org/3/library/index.html)
- [Stackexchange code golf](https://codegolf.stackexchange.com/)
- [Code Golf Tips](https://code.golf/wiki/langs/python)
- [Geeks4Geeks Code Golf](https://www.geeksforgeeks.org/python/code-golfing-in-python/)
- [Python Code Golf Coding Game](https://www.codingame.com/blog/code-golf-python/)
- [pysearch](https://github.com/lynn/pysearch#) This tool is very helpful but I do not know how to make it works...


## 🏷️ Status Legend

| Status | Icon | Description |
|--------|------|-------------|
| **Pending** | ⏳ | Task not started |
| **In Progress** | 🔄 | Currently working on task |
| **Completed** | ✅ | Task completed and verified |
| **Optimized** | 🏆 | Optimized an already existing solution |
| **Needs Review** | 👀 | Requires code review |
| **Interest** | 📚 | Interesting solution with a smart and generalizable practice |

## 📈 Task Progress Table

<!-- Progress: 13/401 tasks completed -->

| Task | Status | Bytes | Completed by | Comments/Notes |
|------|--------|----------|------------|----------------|
| [task000.py](task000.py) | ✅ Completed | 150 | Max | Does not count for points |
| [task001.py](task001.py) | ✅ Completed | 77 | Max | |
| [task002.py](task002.py) | ✅ Completed | 274 | Max | For the moment I use brute force, but DFS could be explored |
| [task003.py](task003.py) | ⏳ Pending | - | - | |
| [task004.py](task004.py) | ⏳ Pending | - | - | |
| [task005.py](task005.py) | ⏳ Pending | - | - | |
| [task006.py](task006.py) | ✅📚 Completed | 59 | Max | for 1 line functions with the lambda you do not need to write the return and it saves **4 bytes**!|
| [task007.py](task007.py) | ⏳ Pending | - | - | |
| [task008.py](task008.py) | ⏳ Pending | - | - | |
| [task009.py](task009.py) | ⏳ Pending | - | - | |
| [task010.py](task010.py) | ✅ Completed | 106 | Max | |
| [task011.py](task011.py) | ⏳ Pending | - | - | |
| [task012.py](task012.py) | ⏳ Pending | - | - | |
| [task013.py](task013.py) | ⏳ Pending | - | - | |
| [task014.py](task014.py) | ✅📚 Completed | 207 | Max | assign names to functions |
| [task015.py](task015.py) | ⏳ Pending | - | - | |
| [task016.py](task016.py) | ✅📚 Completed | 64 | Max | lambda function with 1 constant on a single line |
| [task017.py](task017.py) | ⏳ Pending | - | - | |
| [task018.py](task018.py) | ⏳ Pending | - | - | |
| [task019.py](task019.py) | ⏳ Pending | - | - | |
| [task020.py](task020.py) | ⏳ Pending | - | - | |
| [task021.py](task021.py) | ⏳ Pending | - | - | |
| [task022.py](task022.py) | ⏳ Pending | - | - | |
| [task023.py](task023.py) | ⏳ Pending | - | - | |
| [task024.py](task024.py) | ⏳ Pending | - | - | |
| [task025.py](task025.py) | ⏳ Pending | - | - | |
| [task026.py](task026.py) | ⏳ Pending | - | - | |
| [task027.py](task027.py) | ⏳ Pending | - | - | |
| [task028.py](task028.py) | ⏳ Pending | - | - | |
| [task029.py](task029.py) | ⏳ Pending | - | - | |
| [task030.py](task030.py) | ⏳ Pending | - | - | |
| [task031.py](task031.py) | ⏳ Pending | - | - | |
| [task032.py](task032.py) | ⏳ Pending | - | - | |
| [task033.py](task033.py) | ⏳ Pending | - | - | |
| [task034.py](task034.py) | ⏳ Pending | - | - | |
| [task035.py](task035.py) | ⏳ Pending | - | - | |
| [task036.py](task036.py) | ⏳ Pending | - | - | |
| [task037.py](task037.py) | ⏳ Pending | - | - | |
| [task038.py](task038.py) | ⏳ Pending | - | - | |
| [task039.py](task039.py) | ⏳ Pending | - | - | |
| [task040.py](task040.py) | ⏳ Pending | - | - | |
| [task041.py](task041.py) | ⏳ Pending | - | - | |
| [task042.py](task042.py) | ⏳ Pending | - | - | |
| [task043.py](task043.py) | ⏳ Pending | - | - | |
| [task044.py](task044.py) | ⏳ Pending | - | - | |
| [task045.py](task045.py) | ⏳ Pending | - | - | |
| [task046.py](task046.py) | ⏳ Pending | - | - | |
| [task047.py](task047.py) | ⏳ Pending | - | - | |
| [task048.py](task048.py) | ⏳ Pending | - | - | |
| [task049.py](task049.py) | ⏳ Pending | - | - | |
| [task050.py](task050.py) | ⏳ Pending | - | - | |
| [task051.py](task051.py) | ⏳ Pending | - | - | |
| [task052.py](task052.py) | ⏳ Pending | - | - | |
| [task053.py](task053.py) | ⏳ Pending | - | - | |
| [task054.py](task054.py) | ⏳ Pending | - | - | |
| [task055.py](task055.py) | ⏳ Pending | - | - | |
| [task056.py](task056.py) | ⏳ Pending | - | - | |
| [task057.py](task057.py) | ⏳ Pending | - | - | |
| [task058.py](task058.py) | ⏳ Pending | - | - | |
| [task059.py](task059.py) | ⏳ Pending | - | - | |
| [task060.py](task060.py) | ⏳ Pending | - | - | |
| [task061.py](task061.py) | ⏳ Pending | - | - | |
| [task062.py](task062.py) | ⏳ Pending | - | - | |
| [task063.py](task063.py) | ⏳ Pending | - | - | |
| [task064.py](task064.py) | ⏳ Pending | - | - | |
| [task065.py](task065.py) | ⏳ Pending | - | - | |
| [task066.py](task066.py) | ⏳ Pending | - | - | |
| [task067.py](task067.py) | ⏳ Pending | - | - | |
| [task068.py](task068.py) | ⏳ Pending | - | - | |
| [task069.py](task069.py) | ⏳ Pending | - | - | |
| [task070.py](task070.py) | ⏳ Pending | - | - | |
| [task071.py](task071.py) | ⏳ Pending | - | - | |
| [task072.py](task072.py) | ⏳ Pending | - | - | |
| [task073.py](task073.py) | ⏳ Pending | - | - | |
| [task074.py](task074.py) | ⏳ Pending | - | - | |
| [task075.py](task075.py) | ⏳ Pending | - | - | |
| [task076.py](task076.py) | ⏳ Pending | - | - | |
| [task077.py](task077.py) | ⏳ Pending | - | - | |
| [task078.py](task078.py) | ⏳ Pending | - | - | |
| [task079.py](task079.py) | ⏳ Pending | - | - | |
| [task080.py](task080.py) | ⏳ Pending | - | - | |
| [task081.py](task081.py) | ⏳ Pending | - | - | |
| [task082.py](task082.py) | ⏳ Pending | - | - | |
| [task083.py](task083.py) | ⏳ Pending | - | - | |
| [task084.py](task084.py) | ⏳ Pending | - | - | |
| [task085.py](task085.py) | ⏳ Pending | - | - | |
| [task086.py](task086.py) | ⏳ Pending | - | - | |
| [task087.py](task087.py) | ⏳ Pending | - | - | |
| [task088.py](task088.py) | ⏳ Pending | - | - | |
| [task089.py](task089.py) | ⏳ Pending | - | - | |
| [task090.py](task090.py) | ⏳ Pending | - | - | |
| [task091.py](task091.py) | ⏳ Pending | - | - | |
| [task092.py](task092.py) | ⏳ Pending | - | - | |
| [task093.py](task093.py) | ⏳ Pending | - | - | |
| [task094.py](task094.py) | ⏳ Pending | - | - | |
| [task095.py](task095.py) | ⏳ Pending | - | - | |
| [task096.py](task096.py) | ⏳ Pending | - | - | |
| [task097.py](task097.py) | ⏳ Pending | - | - | |
| [task098.py](task098.py) | ⏳ Pending | - | - | |
| [task099.py](task099.py) | ⏳ Pending | - | - | |
| [task100.py](task100.py) | ⏳ Pending | - | - | |
| [task101.py](task101.py) | ⏳ Pending | - | - | |
| [task102.py](task102.py) | ⏳ Pending | - | - | |
| [task103.py](task103.py) | ⏳ Pending | - | - | |
| [task104.py](task104.py) | ⏳ Pending | - | - | |
| [task105.py](task105.py) | ⏳ Pending | - | - | |
| [task106.py](task106.py) | ⏳ Pending | - | - | |
| [task107.py](task107.py) | ⏳ Pending | - | - | |
| [task108.py](task108.py) | ⏳ Pending | - | - | |
| [task109.py](task109.py) | ⏳ Pending | - | - | |
| [task110.py](task110.py) | ⏳ Pending | - | - | |
| [task111.py](task111.py) | ⏳ Pending | - | - | |
| [task112.py](task112.py) | ⏳ Pending | - | - | |
| [task113.py](task113.py) | ⏳ Pending | - | - | |
| [task114.py](task114.py) | ⏳ Pending | - | - | |
| [task115.py](task115.py) | ⏳ Pending | - | - | |
| [task116.py](task116.py) | ⏳ Pending | - | - | |
| [task117.py](task117.py) | ⏳ Pending | - | - | |
| [task118.py](task118.py) | ⏳ Pending | - | - | |
| [task119.py](task119.py) | ⏳ Pending | - | - | |
| [task120.py](task120.py) | ⏳ Pending | - | - | |
| [task121.py](task121.py) | ⏳ Pending | - | - | |
| [task122.py](task122.py) | ⏳ Pending | - | - | |
| [task123.py](task123.py) | ⏳ Pending | - | - | |
| [task124.py](task124.py) | ⏳ Pending | - | - | |
| [task125.py](task125.py) | ⏳ Pending | - | - | |
| [task126.py](task126.py) | ⏳ Pending | - | - | |
| [task127.py](task127.py) | ⏳ Pending | - | - | |
| [task128.py](task128.py) | ⏳ Pending | - | - | |
| [task129.py](task129.py) | ⏳ Pending | - | - | |
| [task130.py](task130.py) | ⏳ Pending | - | - | |
| [task131.py](task131.py) | ⏳ Pending | - | - | |
| [task132.py](task132.py) | ⏳ Pending | - | - | |
| [task133.py](task133.py) | ⏳ Pending | - | - | |
| [task134.py](task134.py) | ⏳ Pending | - | - | |
| [task135.py](task135.py) | ⏳ Pending | - | - | |
| [task136.py](task136.py) | ⏳ Pending | - | - | |
| [task137.py](task137.py) | ⏳ Pending | - | - | |
| [task138.py](task138.py) | ⏳ Pending | - | - | |
| [task139.py](task139.py) | ⏳ Pending | - | - | |
| [task140.py](task140.py) | ⏳ Pending | - | - | |
| [task141.py](task141.py) | ⏳ Pending | - | - | |
| [task142.py](task142.py) | ⏳ Pending | - | - | |
| [task143.py](task143.py) | ⏳ Pending | - | - | |
| [task144.py](task144.py) | ⏳ Pending | - | - | |
| [task145.py](task145.py) | ⏳ Pending | - | - | |
| [task146.py](task146.py) | ⏳ Pending | - | - | |
| [task147.py](task147.py) | ⏳ Pending | - | - | |
| [task148.py](task148.py) | ⏳ Pending | - | - | |
| [task149.py](task149.py) | ⏳ Pending | - | - | |
| [task150.py](task150.py) | ⏳ Pending | - | - | |
| [task151.py](task151.py) | ⏳ Pending | - | - | |
| [task152.py](task152.py) | ⏳ Pending | - | - | |
| [task153.py](task153.py) | ⏳ Pending | - | - | |
| [task154.py](task154.py) | ⏳ Pending | - | - | |
| [task155.py](task155.py) | ⏳ Pending | - | - | |
| [task156.py](task156.py) | ⏳ Pending | - | - | |
| [task157.py](task157.py) | ⏳ Pending | - | - | |
| [task158.py](task158.py) | ⏳ Pending | - | - | |
| [task159.py](task159.py) | ⏳ Pending | - | - | |
| [task160.py](task160.py) | ⏳ Pending | - | - | |
| [task161.py](task161.py) | ⏳ Pending | - | - | |
| [task162.py](task162.py) | ⏳ Pending | - | - | |
| [task163.py](task163.py) | ⏳ Pending | - | - | |
| [task164.py](task164.py) | ⏳ Pending | - | - | |
| [task165.py](task165.py) | ⏳ Pending | - | - | |
| [task166.py](task166.py) | ⏳ Pending | - | - | |
| [task167.py](task167.py) | ⏳ Pending | - | - | |
| [task168.py](task168.py) | ⏳ Pending | - | - | |
| [task169.py](task169.py) | ⏳ Pending | - | - | |
| [task170.py](task170.py) | ⏳ Pending | - | - | |
| [task171.py](task171.py) | ⏳ Pending | - | - | |
| [task172.py](task172.py) | ⏳ Pending | - | - | |
| [task173.py](task173.py) | ⏳ Pending | - | - | |
| [task174.py](task174.py) | ⏳ Pending | - | - | |
| [task175.py](task175.py) | ⏳ Pending | - | - | |
| [task176.py](task176.py) | ⏳ Pending | - | - | |
| [task177.py](task177.py) | ⏳ Pending | - | - | |
| [task178.py](task178.py) | ⏳ Pending | - | - | |
| [task179.py](task179.py) | ⏳ Pending | - | - | |
| [task180.py](task180.py) | ⏳ Pending | - | - | |
| [task181.py](task181.py) | ⏳ Pending | - | - | |
| [task182.py](task182.py) | ⏳ Pending | - | - | |
| [task183.py](task183.py) | ⏳ Pending | - | - | |
| [task184.py](task184.py) | ⏳ Pending | - | - | |
| [task185.py](task185.py) | ⏳ Pending | - | - | |
| [task186.py](task186.py) | ⏳ Pending | - | - | |
| [task187.py](task187.py) | ⏳ Pending | - | - | |
| [task188.py](task188.py) | ⏳ Pending | - | - | |
| [task189.py](task189.py) | ⏳ Pending | - | - | |
| [task190.py](task190.py) | ⏳ Pending | - | - | |
| [task191.py](task191.py) | ⏳ Pending | - | - | |
| [task192.py](task192.py) | ⏳ Pending | - | - | |
| [task193.py](task193.py) | ⏳ Pending | - | - | |
| [task194.py](task194.py) | ⏳ Pending | - | - | |
| [task195.py](task195.py) | ⏳ Pending | - | - | |
| [task196.py](task196.py) | ⏳ Pending | - | - | |
| [task197.py](task197.py) | ⏳ Pending | - | - | |
| [task198.py](task198.py) | ⏳ Pending | - | - | |
| [task199.py](task199.py) | ✅ Completed | 141 | Max | |
| [task200.py](task200.py) | ✅ Completed | 161 | Max | |
| [task201.py](task201.py) | ⏳ Pending | - | - | |
| [task202.py](task202.py) | ⏳ Pending | - | - | |
| [task203.py](task203.py) | ⏳ Pending | - | - | |
| [task204.py](task204.py) | ⏳ Pending | - | - | |
| [task205.py](task205.py) | ⏳ Pending | - | - | |
| [task206.py](task206.py) | ⏳ Pending | - | - | |
| [task207.py](task207.py) | ⏳ Pending | - | - | |
| [task208.py](task208.py) | ⏳ Pending | - | - | |
| [task209.py](task209.py) | ⏳ Pending | - | - | |
| [task210.py](task210.py) | ✅ Completed | 21 | Max | |
| [task211.py](task211.py) | ✅ Completed | 57 | Max | |
| [task212.py](task212.py) | ⏳ Pending | - | - | |
| [task213.py](task213.py) | ⏳ Pending | - | - | |
| [task214.py](task214.py) | ✅📚 Completed | 104 | Max | I think that I have implemented a good function for rotation clockwise |
| [task215.py](task215.py) | ✅📚 Completed | 84 | Max | Sometimes can be better substitute a `range(len(...))` with `enumerate(...)` |
| [task216.py](task216.py) | ⏳ Pending | - | - | |
| [task217.py](task217.py) | ⏳ Pending | - | - | |
| [task218.py](task218.py) | ⏳ Pending | - | - | |
| [task219.py](task219.py) | ⏳ Pending | - | - | |
| [task220.py](task220.py) | ⏳ Pending | - | - | |
| [task221.py](task221.py) | ⏳ Pending | - | - | |
| [task222.py](task222.py) | ⏳ Pending | - | - | |
| [task223.py](task223.py) | ⏳ Pending | - | - | |
| [task224.py](task224.py) | ⏳ Pending | - | - | |
| [task225.py](task225.py) | ⏳ Pending | - | - | |
| [task226.py](task226.py) | ⏳ Pending | - | - | |
| [task227.py](task227.py) | ⏳ Pending | - | - | |
| [task228.py](task228.py) | ⏳ Pending | - | - | |
| [task229.py](task229.py) | ⏳ Pending | - | - | |
| [task230.py](task230.py) | ⏳ Pending | - | - | |
| [task231.py](task231.py) | ⏳ Pending | - | - | |
| [task232.py](task232.py) | ⏳ Pending | - | - | |
| [task233.py](task233.py) | ⏳ Pending | - | - | |
| [task234.py](task234.py) | ⏳ Pending | - | - | |
| [task235.py](task235.py) | ⏳ Pending | - | - | |
| [task236.py](task236.py) | ⏳ Pending | - | - | |
| [task237.py](task237.py) | ⏳ Pending | - | - | |
| [task238.py](task238.py) | ⏳ Pending | - | - | |
| [task239.py](task239.py) | ⏳ Pending | - | - | |
| [task240.py](task240.py) | ⏳ Pending | - | - | |
| [task241.py](task241.py) | ⏳ Pending | - | - | |
| [task242.py](task242.py) | ⏳ Pending | - | - | |
| [task243.py](task243.py) | ⏳ Pending | - | - | |
| [task244.py](task244.py) | ⏳ Pending | - | - | |
| [task245.py](task245.py) | ⏳ Pending | - | - | |
| [task246.py](task246.py) | ⏳ Pending | - | - | |
| [task247.py](task247.py) | ⏳ Pending | - | - | |
| [task248.py](task248.py) | ⏳ Pending | - | - | |
| [task249.py](task249.py) | ⏳ Pending | - | - | |
| [task250.py](task250.py) | ⏳ Pending | - | - | |
| [task251.py](task251.py) | ⏳ Pending | - | - | |
| [task252.py](task252.py) | ⏳ Pending | - | - | |
| [task253.py](task253.py) | ⏳ Pending | - | - | |
| [task254.py](task254.py) | ⏳ Pending | - | - | |
| [task255.py](task255.py) | ⏳ Pending | - | - | |
| [task256.py](task256.py) | ⏳ Pending | - | - | |
| [task257.py](task257.py) | ⏳ Pending | - | - | |
| [task258.py](task258.py) | ⏳ Pending | - | - | |
| [task259.py](task259.py) | ⏳ Pending | - | - | |
| [task260.py](task260.py) | ⏳ Pending | - | - | |
| [task261.py](task261.py) | ⏳ Pending | - | - | |
| [task262.py](task262.py) | ⏳ Pending | - | - | |
| [task263.py](task263.py) | ⏳ Pending | - | - | |
| [task264.py](task264.py) | ⏳ Pending | - | - | |
| [task265.py](task265.py) | ⏳ Pending | - | - | |
| [task266.py](task266.py) | ⏳ Pending | - | - | |
| [task267.py](task267.py) | ⏳ Pending | - | - | |
| [task268.py](task268.py) | ⏳ Pending | - | - | |
| [task269.py](task269.py) | ⏳ Pending | - | - | |
| [task270.py](task270.py) | ⏳ Pending | - | - | |
| [task271.py](task271.py) | ⏳ Pending | - | - | |
| [task272.py](task272.py) | ⏳ Pending | - | - | |
| [task273.py](task273.py) | ⏳ Pending | - | - | |
| [task274.py](task274.py) | ⏳ Pending | - | - | |
| [task275.py](task275.py) | ⏳ Pending | - | - | |
| [task276.py](task276.py) | ⏳ Pending | - | - | |
| [task277.py](task277.py) | ⏳ Pending | - | - | |
| [task278.py](task278.py) | ⏳ Pending | - | - | |
| [task279.py](task279.py) | ⏳ Pending | - | - | |
| [task280.py](task280.py) | ⏳ Pending | - | - | |
| [task281.py](task281.py) | ⏳ Pending | - | - | |
| [task282.py](task282.py) | ⏳ Pending | - | - | |
| [task283.py](task283.py) | ⏳ Pending | - | - | |
| [task284.py](task284.py) | ⏳ Pending | - | - | |
| [task285.py](task285.py) | ⏳ Pending | - | - | |
| [task286.py](task286.py) | ⏳ Pending | - | - | |
| [task287.py](task287.py) | ⏳ Pending | - | - | |
| [task288.py](task288.py) | ⏳ Pending | - | - | |
| [task289.py](task289.py) | ⏳ Pending | - | - | |
| [task290.py](task290.py) | ⏳ Pending | - | - | |
| [task291.py](task291.py) | ⏳ Pending | - | - | |
| [task292.py](task292.py) | ⏳ Pending | - | - | |
| [task293.py](task293.py) | ⏳ Pending | - | - | |
| [task294.py](task294.py) | ⏳ Pending | - | - | |
| [task295.py](task295.py) | ⏳ Pending | - | - | |
| [task296.py](task296.py) | ⏳ Pending | - | - | |
| [task297.py](task297.py) | ⏳ Pending | - | - | |
| [task298.py](task298.py) | ⏳ Pending | - | - | |
| [task299.py](task299.py) | ⏳ Pending | - | - | |
| [task300.py](task300.py) | ⏳ Pending | - | - | |
| [task301.py](task301.py) | ⏳ Pending | - | - | |
| [task302.py](task302.py) | ⏳ Pending | - | - | |
| [task303.py](task303.py) | ⏳ Pending | - | - | |
| [task304.py](task304.py) | ⏳ Pending | - | - | |
| [task305.py](task305.py) | ⏳ Pending | - | - | |
| [task306.py](task306.py) | ⏳ Pending | - | - | |
| [task307.py](task307.py) | ⏳ Pending | - | - | |
| [task308.py](task308.py) | ⏳ Pending | - | - | |
| [task309.py](task309.py) | ⏳ Pending | - | - | |
| [task310.py](task310.py) | ⏳ Pending | - | - | |
| [task311.py](task311.py) | ⏳ Pending | - | - | |
| [task312.py](task312.py) | ⏳ Pending | - | - | |
| [task313.py](task313.py) | ⏳ Pending | - | - | |
| [task314.py](task314.py) | ⏳ Pending | - | - | |
| [task315.py](task315.py) | ⏳ Pending | - | - | |
| [task316.py](task316.py) | ⏳ Pending | - | - | |
| [task317.py](task317.py) | ⏳ Pending | - | - | |
| [task318.py](task318.py) | ⏳ Pending | - | - | |
| [task319.py](task319.py) | ⏳ Pending | - | - | |
| [task320.py](task320.py) | ⏳ Pending | - | - | |
| [task321.py](task321.py) | ⏳ Pending | - | - | |
| [task322.py](task322.py) | ⏳ Pending | - | - | |
| [task323.py](task323.py) | ⏳ Pending | - | - | |
| [task324.py](task324.py) | ⏳ Pending | - | - | |
| [task325.py](task325.py) | ⏳ Pending | - | - | |
| [task326.py](task326.py) | ⏳ Pending | - | - | |
| [task327.py](task327.py) | ⏳ Pending | - | - | |
| [task328.py](task328.py) | ⏳ Pending | - | - | |
| [task329.py](task329.py) | ⏳ Pending | - | - | |
| [task330.py](task330.py) | ⏳ Pending | - | - | |
| [task331.py](task331.py) | ⏳ Pending | - | - | |
| [task332.py](task332.py) | ⏳ Pending | - | - | |
| [task333.py](task333.py) | ⏳ Pending | - | - | |
| [task334.py](task334.py) | ⏳ Pending | - | - | |
| [task335.py](task335.py) | ⏳ Pending | - | - | |
| [task336.py](task336.py) | ⏳ Pending | - | - | |
| [task337.py](task337.py) | ⏳ Pending | - | - | |
| [task338.py](task338.py) | ⏳ Pending | - | - | |
| [task339.py](task339.py) | ⏳ Pending | - | - | |
| [task340.py](task340.py) | ⏳ Pending | - | - | |
| [task341.py](task341.py) | ⏳ Pending | - | - | |
| [task342.py](task342.py) | ⏳ Pending | - | - | |
| [task343.py](task343.py) | ⏳ Pending | - | - | |
| [task344.py](task344.py) | ⏳ Pending | - | - | |
| [task345.py](task345.py) | ⏳ Pending | - | - | |
| [task346.py](task346.py) | ⏳ Pending | - | - | |
| [task347.py](task347.py) | ⏳ Pending | - | - | |
| [task348.py](task348.py) | ⏳ Pending | - | - | |
| [task349.py](task349.py) | ⏳ Pending | - | - | |
| [task350.py](task350.py) | ⏳ Pending | - | - | |
| [task351.py](task351.py) | ⏳ Pending | - | - | |
| [task352.py](task352.py) | ⏳ Pending | - | - | |
| [task353.py](task353.py) | ⏳ Pending | - | - | |
| [task354.py](task354.py) | ⏳ Pending | - | - | |
| [task355.py](task355.py) | ⏳ Pending | - | - | |
| [task356.py](task356.py) | ⏳ Pending | - | - | |
| [task357.py](task357.py) | ⏳ Pending | - | - | |
| [task358.py](task358.py) | ⏳ Pending | - | - | |
| [task359.py](task359.py) | ⏳ Pending | - | - | |
| [task360.py](task360.py) | ⏳ Pending | - | - | |
| [task361.py](task361.py) | ⏳ Pending | - | - | |
| [task362.py](task362.py) | ⏳ Pending | - | - | |
| [task363.py](task363.py) | ⏳ Pending | - | - | |
| [task364.py](task364.py) | ⏳ Pending | - | - | |
| [task365.py](task365.py) | ⏳ Pending | - | - | |
| [task366.py](task366.py) | ⏳ Pending | - | - | |
| [task367.py](task367.py) | ⏳ Pending | - | - | |
| [task368.py](task368.py) | ⏳ Pending | - | - | |
| [task369.py](task369.py) | ⏳ Pending | - | - | |
| [task370.py](task370.py) | ⏳ Pending | - | - | |
| [task371.py](task371.py) | ⏳ Pending | - | - | |
| [task372.py](task372.py) | ⏳ Pending | - | - | |
| [task373.py](task373.py) | ⏳ Pending | - | - | |
| [task374.py](task374.py) | ⏳ Pending | - | - | |
| [task375.py](task375.py) | ⏳ Pending | - | - | |
| [task376.py](task376.py) | ⏳ Pending | - | - | |
| [task377.py](task377.py) | ⏳ Pending | - | - | |
| [task378.py](task378.py) | ⏳ Pending | - | - | |
| [task379.py](task379.py) | ⏳ Pending | - | - | |
| [task380.py](task380.py) | ⏳ Pending | - | - | |
| [task381.py](task381.py) | ⏳ Pending | - | - | |
| [task382.py](task382.py) | ⏳ Pending | - | - | |
| [task383.py](task383.py) | ⏳ Pending | - | - | |
| [task384.py](task384.py) | ⏳ Pending | - | - | |
| [task385.py](task385.py) | ⏳ Pending | - | - | |
| [task386.py](task386.py) | ⏳ Pending | - | - | |
| [task387.py](task387.py) | ⏳ Pending | - | - | |
| [task388.py](task388.py) | ⏳ Pending | - | - | |
| [task389.py](task389.py) | ⏳ Pending | - | - | |
| [task390.py](task390.py) | ⏳ Pending | - | - | |
| [task391.py](task391.py) | ⏳ Pending | - | - | |
| [task392.py](task392.py) | ⏳ Pending | - | - | |
| [task393.py](task393.py) | ⏳ Pending | - | - | |
| [task394.py](task394.py) | ⏳ Pending | - | - | |
| [task395.py](task395.py) | ⏳ Pending | - | - | |
| [task396.py](task396.py) | ⏳ Pending | - | - | |
| [task397.py](task397.py) | ⏳ Pending | - | - | |
| [task398.py](task398.py) | ⏳ Pending | - | - | |
| [task399.py](task399.py) | ⏳ Pending | - | - | |
| [task400.py](task400.py) | ⏳ Pending | - | - | |

---

**Happy Coding! 🚀**

*Remember: In code golf, every character counts!*