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

# fileName = ['response-cdf/REST.1.response.latency', 'response-cdf/REST.2.response.latency', 'response-cdf/REST.3.response.latency', 'response-cdf/REST.4.response.latency', 'response-cdf/REST.5.response.latency', 'response-cdf/REST.6.response.latency']
fileName = ['motion/kn-queue.motion.cpu', 'motion/kn-gw.motion.cpu', 'motion/kn-fn.motion.cpu']
fileName_skmsg = ['motion/skmsg_gw.motion.cpu', 'motion/skmsg_fn.motion.cpu']
# --- CPU usage of Knative queue proxy
kn_queue_cpu_ts = []
tmp_cpu = [0]
with open(fileName[0]) as fp:
  line = fp.readline()
  line_list= line.split()
  while line:
    if len(line_list) == 0:
      line = fp.readline()
      line_list= line.split()
      continue
    if line_list[0] == 'Linux':
      line = fp.readline()
      line_list= line.split()
      continue
    if line_list[0] == 'Average:':
      aggregated_cpu_1_second = sum(tmp_cpu)
      kn_queue_cpu_ts.append(aggregated_cpu_1_second)
      break
    if line_list[2] == 'UID':
      aggregated_cpu_1_second = sum(tmp_cpu)
      kn_queue_cpu_ts.append(aggregated_cpu_1_second)
      tmp_cpu = [0]
    else:
      tmp_cpu.append(float(line_list[8]))
    line = fp.readline()
    line_list= line.split()
    # print(tmp_cpu)
kn_queue_cpu_ts = kn_queue_cpu_ts[1:]

# --- CPU usage of Knative gateway
kn_gw_cpu_ts = []
tmp_cpu = []
with open(fileName[1]) as fp:
  line = fp.readline()
  line_list= line.split()
  while line:
    if len(line_list) == 0:
      line = fp.readline()
      line_list= line.split()
      continue
    if line_list[0] == 'Linux':
      line = fp.readline()
      line_list= line.split()
      continue
    if line_list[0] == 'Average:':
      aggregated_cpu_1_second = sum(tmp_cpu)
      kn_gw_cpu_ts.append(aggregated_cpu_1_second)
      break
    if line_list[2] == 'UID':
      aggregated_cpu_1_second = sum(tmp_cpu)
      kn_gw_cpu_ts.append(aggregated_cpu_1_second)
      tmp_cpu = [0]
    else:
      tmp_cpu.append(float(line_list[8]))
    line = fp.readline()
    line_list= line.split()
    # print(tmp_cpu)
kn_gw_cpu_ts = kn_gw_cpu_ts[1:]

# --- CPU usage of Knative function
kn_fn_cpu_ts = []
tmp_cpu = []
with open(fileName[2]) as fp:
  line = fp.readline()
  line_list= line.split()
  while line:
    if len(line_list) == 0:
      line = fp.readline()
      line_list= line.split()
      continue
    if line_list[0] == 'Linux':
      line = fp.readline()
      line_list= line.split()
      continue
    if line_list[0] == 'Average:':
      aggregated_cpu_1_second = sum(tmp_cpu)
      kn_fn_cpu_ts.append(aggregated_cpu_1_second)
      break
    if line_list[2] == 'UID':
      aggregated_cpu_1_second = sum(tmp_cpu)
      kn_fn_cpu_ts.append(aggregated_cpu_1_second)
      tmp_cpu = [0]
    else:
      tmp_cpu.append(float(line_list[8]))
    line = fp.readline()
    line_list= line.split()
    # print(tmp_cpu)
kn_fn_cpu_ts = kn_fn_cpu_ts[1:]

# print(kn_queue_cpu_ts)
# print(kn_gw_cpu_ts)
# print(kn_fn_cpu_ts)


# --- CPU usage of Knative queue proxy
skmsg_gw_cpu_ts = []
tmp_cpu = [0]
with open(fileName_skmsg[0]) as fp:
  line = fp.readline()
  line_list= line.split()
  while line:
    if len(line_list) == 0:
      line = fp.readline()
      line_list= line.split()
      continue
    if line_list[0] == 'Linux':
      line = fp.readline()
      line_list= line.split()
      continue
    if line_list[0] == 'Average:':
      aggregated_cpu_1_second = sum(tmp_cpu)
      skmsg_gw_cpu_ts.append(aggregated_cpu_1_second)
      break
    if line_list[2] == 'UID':
      aggregated_cpu_1_second = sum(tmp_cpu)
      skmsg_gw_cpu_ts.append(aggregated_cpu_1_second)
      tmp_cpu = [0]
    else:
      tmp_cpu.append(float(line_list[8]))
    line = fp.readline()
    line_list= line.split()
    # print(tmp_cpu)
skmsg_gw_cpu_ts = skmsg_gw_cpu_ts[1:]

# --- CPU usage of Knative gateway
skmsg_fn_cpu_ts = []
tmp_cpu = []
with open(fileName_skmsg[1]) as fp:
  line = fp.readline()
  line_list= line.split()
  while line:
    if len(line_list) == 0:
      line = fp.readline()
      line_list= line.split()
      continue
    if line_list[0] == 'Linux':
      line = fp.readline()
      line_list= line.split()
      continue
    if line_list[0] == 'Average:':
      aggregated_cpu_1_second = sum(tmp_cpu)
      skmsg_fn_cpu_ts.append(aggregated_cpu_1_second)
      break
    if line_list[2] == 'UID':
      aggregated_cpu_1_second = sum(tmp_cpu)
      skmsg_fn_cpu_ts.append(aggregated_cpu_1_second)
      tmp_cpu = [0]
    else:
      tmp_cpu.append(float(line_list[8]))
    line = fp.readline()
    line_list= line.split()
    # print(tmp_cpu)
skmsg_fn_cpu_ts = skmsg_fn_cpu_ts[1:]

# ----------------------------------------------- #
# -------------- FIGURE PLOT -------------------- #
# ----------------------------------------------- #
figsize = 8, 3

figure, ax = plt.subplots(figsize=figsize)
# figure, (ax1, ax2) = plt.subplots(1, 2, gridspec_kw={'width_ratios': [4, 1]}, figsize=figsize)
# ind = np.arange(0, logFileNum*1 , 1)   # the x locations for the groups
# width = 0.2
# gap = -0.4

timestamps = [x for x in range(1, len(kn_queue_cpu_ts) + 1, 1)]
# print(len(timestamps))
p1 = plt.plot(timestamps, kn_queue_cpu_ts, marker = 'x', ms = 8, mew = 1, label = '', linewidth=2.5, linestyle="-", color='tab:green')
# p2 = plt.plot(timestamps, kn_gw_cpu_ts, marker = 'x', ms = 4, mew = 2, label = '', linewidth=2.5, linestyle=" ", color='limegreen')
p2 = plt.plot(timestamps, kn_fn_cpu_ts, marker = 'x', ms = 8, mew = 1, label = '', linewidth=2.5, linestyle="-", color='#E43C44')
# p4 = plt.plot(rest_4_p, timestamps, marker = '', ms = 4, mew = 2, label = '', linewidth=2.5, linestyle="-", color='#5AAC56')
# p5 = plt.plot(rest_5_p, timestamps, marker = '', ms = 4, mew = 2, label = '', linewidth=2.5, linestyle="-", color='#FDA8AA')
# p6 = plt.plot(rest_6_p, timestamps, marker = '', ms = 4, mew = 2, label = '', linewidth=2.5, linestyle="-", color='#555CB5')
timestamps = [x for x in range(1, len(skmsg_fn_cpu_ts) + 1, 1)]
# p1 = plt.plot(timestamps, skmsg_gw_cpu_ts, marker = '', ms = 4, mew = 2, label = '', linewidth=2.5, linestyle="-", color='tab:blue')
p3 = plt.plot(timestamps, skmsg_fn_cpu_ts, marker = '+', ms = 8, mew = 1, label = '', linewidth=2.5, linestyle="-", color='#1F308D')

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
plt.ylim((0, 16))
plt.xlim((0, 3600))
plt.yticks(np.arange(0, 15.1, 3))
plt.ylabel('CPU usage (%)', labelpad = 0)
plt.xlabel('(b) timestamp (second)', labelpad=-2)

prop = dict(size=12)
plt.legend((p1[0], p2[0], p3[0]), #,p4[0], p5[0], p6[0]), 
  ('Kn: queue','Kn: fn', 'S-SPRI.: fn'), #, 'REST_4', 'REST_5','REST_6'),
  loc = "upper right",
  ncol = 3,
  prop = prop,
  borderaxespad = 0,
  frameon = False,
  columnspacing = 0.7,
  labelspacing = 0.1,
  fancybox = False,
  edgecolor = 'black')

plt.tight_layout()
plt.savefig('fig-11-b.pdf', bbox_inches='tight', dpi=figure.dpi, pad_inches=0.01)
