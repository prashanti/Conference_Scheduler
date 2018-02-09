import re
import numpy as np
import scipy.stats as sp
import matplotlib.pyplot as plt

if __name__ == '__main__':
    results = open('./data/survey_results.tsv', 'rU')

    max_auto = []
    max_man = []

    likert_auto = []
    likert_man = []

    likert_auto_freq = [0, 0, 0, 0, 0]
    likert_man_freq = [0, 0, 0, 0, 0]

    for line in results:
        line_arr = line.split('\t')

        if re.match('\d', line_arr[0]):
            if re.match('Automated.*', line_arr[20]):
                max_auto.append(int(line_arr[18]))
                likert_auto.append(int(line_arr[13]))

            if re.match('Automated.*', line_arr[21]):
                max_auto.append(int(line_arr[19]))
                likert_auto.append(int(line_arr[14]))

            if re.match('Manual.*', line_arr[20]):
                max_man.append(int(line_arr[18]))
                likert_man.append(int(line_arr[13]))

            if re.match('Manual.*', line_arr[21]):
                max_man.append(int(line_arr[19]))
                likert_man.append(int(line_arr[14]))

    print 'Max Choices (Auto)\t:\t' + str(max_auto)
    print 'Max Choices (Man)\t:\t' + str(max_man)

    max_auto_mode = np.mean(max_auto)
    max_man_mode = np.mean(max_man)

    print '\nMax Choices (Auto) Mode\t= \t' + str(max_auto_mode)
    print 'Max Choices (Man) Mode\t= \t' + str(max_man_mode)

    stats = sp.ttest_ind(max_auto, max_man)

    print '\nt-stat\t=\t' + str(stats[0])
    print 'p-value\t=\t' + str(stats[1])

    print '\nLikert (Auto)\t:\t' + str(likert_auto)
    print 'Likert (Man)\t:\t' + str(likert_man)

    likert_auto_mode = int(sp.mode(likert_auto)[0][0])
    likert_man_mode = int(sp.mode(likert_man)[0][0])

    print '\nLikert (Auto) Mode\t= \t' + str(likert_auto_mode)
    print 'Likert (Man) Mode\t= \t' + str(likert_man_mode)

    for x in range(0, len(likert_auto)):
        if likert_auto[x] == 1:
            likert_auto_freq[0] += 1

        elif likert_auto[x] == 2:
            likert_auto_freq[1] += 1

        elif likert_auto[x] == 3:
            likert_auto_freq[2] += 1

        elif likert_auto[x] == 4:
            likert_auto_freq[3] += 1

        elif likert_auto[x] == 5:
            likert_auto_freq[4] += 1

    for x in range(0, len(likert_man)):
        if likert_man[x] == 1:
            likert_man_freq[0] += 1

        elif likert_man[x] == 2:
            likert_man_freq[1] += 1

        elif likert_man[x] == 3:
            likert_man_freq[2] += 1

        elif likert_man[x] == 4:
            likert_man_freq[3] += 1

        elif likert_man[x] == 5:
            likert_man_freq[4] += 1

    N = 5
    likert_auto_freq = tuple(likert_auto_freq)
    likert_man_freq = tuple(likert_man_freq)

    ind = np.arange(N)
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, likert_auto_freq, width, color='k')
    rects2 = ax.bar(ind + width, likert_man_freq, width, color='w', edgecolor='black', hatch='\\\\')

    ax.set_xlabel('Ease of Selecting a Session with All Talks of Interest')
    ax.set_ylabel('Frequency of Responses')
    ax.set_xticks(ind + width)
    ax.set_xticklabels(('1', '2', '3', '4', '5'))

    ax.legend((rects1[0], rects2[0]), ('Automated', 'Manual'))

    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 1.05*height, '%d' % int(height), ha='center', va='bottom')

    print '\nLikert (Auto) Freq\t:\t' + str(likert_auto_freq)
    print 'Likert (Man) Freq\t:\t' + str(likert_man_freq)

    plt.savefig('../Figures/Likert.png', dpi=300)
    plt.show()
