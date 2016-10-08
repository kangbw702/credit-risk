__author__ = 'marcopereira'
import numpy as np
import pandas as pd
from dateutil.relativedelta import relativedelta

class Scheduler(object):
    def __init__(self, start, end, freq, reference):
        self.delay = self.extractDelay(freq=freq)[0]
        self.datelist = self.genDatelist(start, end, freq, reference)
        return

    def genDatelist(self, start, end, freq, reference):
        date_tmp = start
        datelist = []
        while (date_tmp <= end):
            if (date_tmp >= reference): datelist.append(date_tmp)
            date_tmp += self.extractDelay(freq=freq)[0]
        return datelist

    def genDatelist_2(self, start, end, freq):
        offsetfreq = self.extractDelay(freq)[1]
        return pd.date_range(start=start,end=end,freq=offsetfreq).date

    def extractDelay(self, freq):
        if type(freq) == list:
            freq = freq[0]
        if (freq == 'Date'): return relativedelta(days=+  0)
        x = self.only_numerics(freq)
        if (x == ''):
            freqValue = 1
        else:
            freqValue = np.int(x)
        if (freq.upper().find('D') != -1):
            delta = relativedelta(days=+ freqValue)
            offsetfreq = pd.DateOffset(days=freqValue)
        if (freq.upper().find('W') != -1):
            delta = relativedelta(weeks=+  freqValue)
            offsetfreq = pd.DateOffset(weeks=freqValue)
        if (freq.upper().find('M') != -1):
            delta = relativedelta(months=+ freqValue)
            offsetfreq = pd.DateOffset(months=freqValue)
        if (freq.upper().find('Y') != -1):
            delta = relativedelta(years=+ freqValue)
            offsetfreq = pd.DateOffset(years=freqValue)
        if (freq.upper().find('ZERO') != -1):
            delta = relativedelta(years=+ freqValue)
            offsetfreq = pd.DateOffset(years=freqValue)
        return [delta, offsetfreq]

    def only_numerics(self, seq):
        seq_type = type(seq)
        return seq_type().join(filter(seq_type.isdigit, seq))
        
