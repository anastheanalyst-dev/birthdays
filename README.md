# How common is your birthday? 🎂📊

**THE DATA STORY · Ep 3 · by @anas.theanalyst**

I analysed **62 million birthdays** (every US birth from 2000 to 2014) and found that babies seem to "avoid" Friday the 13th, Christmas and Sundays. They don't, of course. This repo is the full analysis, and it checks **your** birthday too.

## What I found

| Question | Answer |
|---|---|
| Rarest birthday? | **25 Dec**: 43% fewer babies than an average day. Then 1 Jan (−32%), 24 Dec (−29%), 4 Jul (−22%) |
| Most common? | **12 Sep** (+12%), 19 Sep, 20 Sep. Count back nine months and you land on the December holidays |
| Weekends? | Saturday **−25%**, Sunday **−34%** vs an average day |
| Friday the 13th? | **6.4% fewer births** than on Fridays a week either side (the 6th and the 20th) |

## The data lesson: the hidden variable
Babies don't read calendars. **People do.** Many births are planned (scheduled C-sections and inductions), and those get booked around weekends and holidays. The real cause, the schedule, isn't a column in the data, so you can't see it unless you ask *why*.
Every analyst runs into this: a pattern is real, but the reason behind it is somewhere else. **Always ask why before you trust a pattern.**

## Run it (2 minutes)
```bash
git clone https://github.com/anastheanalyst-dev/birthdays.git
cd birthdays
pip install -r requirements.txt
python analyse_birthdays.py 12 25      # put your own month and day here
```
It prints the rarest and most common birthdays, the weekday effect, Friday the 13th vs other Fridays and how **your** birthday ranks, then saves `birthday_heatmap.png`.

## Data
- [FiveThirtyEight `births` dataset](https://github.com/fivethirtyeight/data/tree/master/births): US Social Security Administration, 2000–2014. The CSV is included in `data/`.
- These are **US births only**. Other countries may differ, which makes a great follow-up project if you can find their data.

## Ideas to take it further
- Compare the 1994–2003 CDC file in the same FiveThirtyEight folder: has the weekend dip grown?
- Find the US public holidays with the biggest dip (Thanksgiving moves every year, so it's tricky!).
- Recreate the heatmap in Power BI or Tableau.

## Licence
Code: MIT. Data: see FiveThirtyEight's repository.
