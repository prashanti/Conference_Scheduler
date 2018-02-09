import csv
import re

if __name__ == '__main__':
    schedule1_block1 = {}
    schedule1_block2 = {}
    schedule2_block1 = {}
    schedule2_block2 = {}
    schedule3_block1 = {}
    schedule3_block2 = {}
    schedule4_block1 = {}
    schedule4_block2 = {}
    schedule5_block1 = {}
    schedule5_block2 = {}
    schedule6_block1 = {}
    schedule6_block2 = {}
    schedule7_block1 = {}
    schedule7_block2 = {}
    schedule8_block1 = {}
    schedule8_block2 = {}

    for x in range(1, 9):
        schedule = open('./data/Schedule' + str(x) + '.tex')
        session = None
        block = None
        for line in schedule:
            line = line.strip()

            if re.match('\\\section\D*\d*, 8(:|.)30 - 9(:|.)45', line):
                block = 1

            if re.match('\\\section\D*\d*, 10(:|.)30 - 11(:|.)45', line):
                block = 2

            if line.find('& \\textbf{') is not -1:
                line = line.replace('& \\textbf{Session ', '')
                line = line.replace('} \\\\', '').strip()
                session = line

            elif re.match('\d*(:|.)\d* - \d*(:|.)\d*', line) is not None:
                title = re.sub('\d*(:|.)\d* - \d*(:|.)\d* & ', '', line)
                title = title[:-3]

                if x == 1:
                    if block == 1:
                        schedule1_block1[title] = session
                    elif block == 2:
                        schedule1_block2[title] = session

                elif x == 2:
                    if block == 1:
                        schedule2_block1[title] = session
                    elif block == 2:
                        schedule2_block2[title] = session

                elif x == 3:
                    if block == 1:
                        schedule3_block1[title] = session
                    elif block == 2:
                        schedule3_block2[title] = session

                elif x == 4:
                    if block == 1:
                        schedule4_block1[title] = session
                    elif block == 2:
                        schedule4_block2[title] = session

                elif x == 5:
                    if block == 1:
                        schedule5_block1[title] = session
                    elif block == 2:
                        schedule5_block2[title] = session

                elif x == 6:
                    if block == 1:
                        schedule6_block1[title] = session
                    elif block == 2:
                        schedule6_block2[title] = session

                elif x == 7:
                    if block == 1:
                        schedule7_block1[title] = session
                    elif block == 2:
                        schedule7_block2[title] = session

                elif x == 8:
                    if block == 1:
                        schedule8_block1[title] = session
                    elif block == 2:
                        schedule8_block2[title] = session

    with open('./data/survey_results.csv', 'rb') as csvfile:
        results = csv.reader(csvfile, dialect='excel')
        schedule_num = None
        for row in results:
            block1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            block2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

            if re.match('\d', row[0]) is not None:
                schedule_num = int(row[0])

                for x in range(3, 8):
                    title = row[x]

                    if schedule_num == 1:
                        chosen = schedule1_block1.get(title)
                    elif schedule_num == 2:
                        chosen = schedule2_block1.get(title)
                    elif schedule_num == 3:
                        chosen = schedule3_block1.get(title)
                    elif schedule_num == 4:
                        chosen = schedule4_block1.get(title)
                    elif schedule_num == 5:
                        chosen = schedule5_block1.get(title)
                    elif schedule_num == 6:
                        chosen = schedule6_block1.get(title)
                    elif schedule_num == 7:
                        chosen = schedule7_block1.get(title)
                    elif schedule_num == 8:
                        chosen = schedule8_block1.get(title)

                    if chosen is None:
                        print "NOT FOUND -> " + str(schedule_num) + ", block 1 : " + title

                    block1[int(chosen)-1] += 1

                for x in range(8, 13):
                    title = row[x]

                    if schedule_num == 1:
                        chosen = schedule1_block2.get(title)
                    elif schedule_num == 2:
                        chosen = schedule2_block2.get(title)
                    elif schedule_num == 3:
                        chosen = schedule3_block2.get(title)
                    elif schedule_num == 4:
                        chosen = schedule4_block2.get(title)
                    elif schedule_num == 5:
                        chosen = schedule5_block2.get(title)
                    elif schedule_num == 6:
                        chosen = schedule6_block2.get(title)
                    elif schedule_num == 7:
                        chosen = schedule7_block2.get(title)
                    elif schedule_num == 8:
                        chosen = schedule8_block2.get(title)

                    if chosen is None:
                        print "NOT FOUND -> " + str(schedule_num) + ", block 2 : " + title

                    block2[int(chosen)-1] += 1

                block1_max = sorted(block1, reverse=True)[0]

                block2_max = sorted(block2, reverse=True)[0]

                # print row[1] + "\tBlock 1: " + str(sorted(block1, reverse=True)[0]) + "\tBlock 2: " + \
                #       str(sorted(block2, reverse=True)[0])
                #
                # print row[1] + "\tBlock 1: " + str(block1_max) + "\tBlock 2: " + str(block2_max)

                print str(block1_max) + " , " + str(block2_max)
