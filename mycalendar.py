import calendar
from datetime import datetime


class MyCalendar(calendar.LocaleHTMLCalendar):
    weekday = (u'月', u'火', u'水', u'木', u'金', u'土', u'日')

    def __init__(self, username, linked_date: dict):
        calendar.LocaleHTMLCalendar.__init__(self,
                                             firstweekday=6,
                                             locale='ja_jp')
        # 何か予定がある日付はリンクする
        self.username = username
        self.linked_date = linked_date  # dict{'datetime': done}

    def formatweekday(self, theday):
        return f'<td>%s</td>' % self.weekday[theday]

    def formatmonthname(self, theyear, themonth, withyear):
        """ カレンダーで月表示の文字化け対策 """
        return f'<tr><th colspan="7" class="month">%s</th></tr>' % f'{themonth}月'

    def formatmonth(self, theyear, themonth, withyear=True):
        v = []
        a = v.append
        a('<table class="table table-bordered table-sm" style="table-layout: fixed;">')
        a('\n')
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        a('\n')
        a(self.formatweekheader())
        a('\n')
        for week in self.monthdays2calendar(theyear, themonth):
            a(self.formatweek(week, theyear, themonth))
            a('\n')
        a('</table><br>')
        a('\n')
        return ''.join(v)

    def formatweek(self, theweek, theyear, themonth):
        """
        オーバーライド (引数を変えるのはPythonでは多分非推奨)
        引数で year と month を渡すようにした。
        """
        s = ''.join(self.formatday(d, wd, theyear, themonth) for (d, wd) in theweek)
        return '<tr>%s</tr>' % s

    def formatday(self, day, weekday, theyear, themonth):
        """
        オーバーライド (引数を変えるのはPythonでは多分非推奨)
        引数で year と month を渡すようにした。
        """
        if day == 0:
            return '<td style="background-color: #eeeeee">&nbsp;</td>'  # 空白
        else:
            html = '<td class="text-center {highlight}"><a href="{url}" style="color:{text}">{day}</a></td>'
            text = 'blue'
            highlight = ''

            # もし予定があるなら強調
            date = datetime(year=theyear, month=themonth, day=day)
            date_str = date.strftime('%Y%m%d')
            if date_str in self.linked_date:
                if self.linked_date[date_str]:  # 終了した予定
                    highlight = 'bg-success'
                    text = 'white'
                elif date < datetime.now():  # 過去の予定
                    highlight = 'bg-secondary'
                    text = 'white'
                else:  # これからの予定
                    highlight = 'bg-warning'

            return html.format(  # url を /todo/{username}/year/month/day に
                               url=f'/todo/{self.username}/{theyear}/{themonth}/{day}',
                               text=text,
                               day=day,
                               highlight=highlight)
