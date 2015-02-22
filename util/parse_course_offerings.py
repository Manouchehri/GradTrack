#!/usr/local/bin/python3

__author__ = 'David Manouchehri (david@davidmanouchehri.com)'
import os

print('Memorial University course offerings parser, written by ' + __author__ + '.')

directory = 'html/'

fields = [5, 10, 38, 42, 48, 53, 67, 72, 77, 85, 91, 103, 108, 112, 117, 122, 127, 133, 137]
global short_subject, course_code, crn
for file in os.listdir(directory):
    print('Opening: ' + file)
    with open(directory + file) as f:

        for line in f:
            if "<H2>Campus:" in line:
                campus = line[line.find(":") + 1:line.find("</H")].strip()
            elif "<H4>Subject:" in line:
                full_subject = line[line.find(":") + 1:line.find("</H")].strip()
            elif "SEC CRN   SLOT M T W R F S U" in line or "--- ----- ---- -------------" in line \
                    or "*** DAYS ***" in line:
                pass
            elif "<" not in line and ">" not in line and len(line) in range(170, 180):

                if line[fields[0]:fields[3]].strip():
                    short_subject = line[0:fields[0]].strip()  # or short_subject
                    course_code = line[fields[0]:fields[1]].strip()  # or course_code
                    course_short_description = line[fields[1]:fields[2]].strip()
                    sec = line[fields[4]:fields[5]].strip()
                    crn = line[fields[3]:fields[4]].strip()
                else:
                    reg_details = line.strip()

                print(short_subject + course_code + crn + ' from ' + file)

                # print(crn + " " + sec)
                '''if len(line) is 176:
                    print(line)'''