import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import csv

plt.rcParams['axes.labelsize'] = 15  # xy-axis label size
plt.rcParams['xtick.labelsize'] = 13  # x-axis ticks size
plt.rcParams['ytick.labelsize'] = 13  # y-axis ticks size
# plt.rcParams['legend.fontsize'] = 12  # legend size
plt.rcParams['hatch.linewidth'] = 0.5
# plt.rcParams['xtick.major.pad'] ='-2'
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

lrotation = 0


# ----------------------------------------------- #
# -------------- Parse raw data ----------------- #
# ----------------------------------------------- #
# fileName = ['response-cdf/REST.1.response.latency', 'response-cdf/REST.2.response.latency', 'response-cdf/REST.3.response.latency', 'response-cdf/REST.4.response.latency', 'response-cdf/REST.5.response.latency', 'response-cdf/REST.6.response.latency']
fileName = ['motion/skmsg_motion_output.csv', 'motion/kn_motion_output.csv']

rest_1_d = []
rest_2_d = []
rest_3_d = []
rest_4_d = []
rest_5_d = []
rest_6_d = []

rest_1_ts = []
rest_2_ts = []
rest_3_ts = []
rest_4_ts = []
rest_5_ts = []
rest_6_ts = []

with open(fileName[0]) as fp:
  line = fp.readline()
  line_list = line.split(";")
  rest_1_d.append(float(line_list[1].split("\n")[0]))
  rest_1_ts.append(float(line_list[0]))
  while line:
    line = fp.readline()
    if len(line) == 0:
      break
    line_list= line.split(";")
    if len(line_list) != 0:
      rest_1_d.append(float(line_list[1].split("\n")[0]))
      rest_1_ts.append(float(line_list[0]))

with open(fileName[1]) as fp:
  line = fp.readline()
  line_list = line.split(";")
  rest_2_d.append(float(line_list[1].split("\n")[0]))
  rest_2_ts.append(float(line_list[0]))
  while line:
    line = fp.readline()
    if len(line) == 0:
      break
    line_list= line.split(";")
    if len(line_list) != 0:
      rest_2_d.append(float(line_list[1].split("\n")[0]))
      rest_2_ts.append(float(line_list[0]))

# ----------------------------------------------- #
# -------------- Align timestamp ---------------- #
# ----------------------------------------------- #
min_rests_skmsg = []
min_rests_skmsg.append(min(rest_1_ts))
min_rests_kn = []
min_rests_kn.append(min(rest_2_ts)) 

start_time_skmsg = float(int(min(min_rests_skmsg)))
start_time_kn = float(int(min(min_rests_kn)))
align_offset = 33
rest_1_ts = [x - start_time_skmsg for x in rest_1_ts]
rest_2_ts = [x - start_time_kn + align_offset for x in rest_2_ts]

# ----------------------------------------------- #
# -------------- FIGURE PLOT -------------------- #
# ----------------------------------------------- #
figsize = 8, 3

figure, ax = plt.subplots(figsize=figsize)

# timestamps = [x for x in range(1 + align_offset, len(rest_1_d) + 1 + align_offset, 1)]
p1 = plt.plot(rest_1_ts, rest_1_d, marker = 'x', ms = 8, mew = 1, label = '', linewidth=2.5, linestyle=" ", color='#1F308D')
p2 = plt.plot(rest_2_ts, rest_2_d, marker = '3', ms = 10, mew = 2, label = '', linewidth=2.5, linestyle=" ", color='tab:green')
# p3 = plt.plot(rest_3_ts, rest_3_d, marker = '.', ms = 4, mew = 1, label = '', linewidth=2.5, linestyle=" ", color='tab:red')
# p4 = plt.plot(rest_4_ts, rest_4_d, marker = '.', ms = 4, mew = 1, label = '', linewidth=2.5, linestyle=" ", color='#D4996A')
# p5 = plt.plot(rest_5_ts, rest_5_d, marker = '.', ms = 4, mew = 1, label = '', linewidth=2.5, linestyle=" ", color='#FDA8AA')
# p6 = plt.plot(rest_6_ts, rest_6_d, marker = '.', ms = 4, mew = 1, label = '', linewidth=2.5, linestyle=" ", color='#555CB5')


plt.tick_params(grid_linewidth = 3, grid_linestyle = ':', pad=0)
figure.subplots_adjust(bottom=0.25, left=0.2)
# plt.xticks(ind, ('0', '10','50','100','200','400'))
plt.setp(ax.get_xticklabels(), 
  rotation=lrotation, 
  ha="center",
  rotation_mode="anchor")

# plt.xlim((0, 15000))
# plt.xticks(np.arange(0, 15000.1, 3000))#, ['0', '5k', '10k', '15k', '20k'])

# plt.grid(True)
# plt.grid(color = 'gray', linestyle = ':', linewidth = 1.5)
plt.ylim((0, 12))
plt.xlim((0, 3600))
plt.yticks(np.arange(0, 12.1, 3), rotation = 45)
plt.ylabel('Response time (sec)', labelpad = 0)
plt.xlabel('(a) timestamp (second)', labelpad = 0)

prop = dict(size=12)
plt.legend((p1[0], p2[0]), 
  ('S-SPRI.', 'Knative'),
  loc = "upper right",
  markerscale=1,
  ncol = 2,
  prop = prop,
  borderaxespad = 0,
  frameon = True,
  columnspacing = 0.7,
  labelspacing = 0.1,
  fancybox = False,
  edgecolor = 'black')

plt.tight_layout()
plt.savefig('fig-11-a.pdf', bbox_inches='tight', dpi=400, pad_inches=0.01)
