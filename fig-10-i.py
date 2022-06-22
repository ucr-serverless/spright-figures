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
# ------------ Input parameters ----------------- #
# ----------------------------------------------- #

concurrency = "25K"

fileName_dpdk = ['online_boutique/dpdk_gw.cpu', 'online_boutique/dpdk_nf.cpu']
fileName_skmsg = ['online_boutique/skmsg_gw.cpu', 'online_boutique/skmsg_fn.cpu']

# ----------------------------------------------- #
# ------------ Process DPDK data ---------------- #
# ----------------------------------------------- #
# --- CPU usage of DPDK GW
dpdk_gw_cpu_ts = []
tmp_cpu = [0]
with open(fileName_dpdk[0]) as fp:
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
      dpdk_gw_cpu_ts.append(aggregated_cpu_1_second)
      break
    if line_list[2] == 'UID':
      aggregated_cpu_1_second = sum(tmp_cpu)
      dpdk_gw_cpu_ts.append(aggregated_cpu_1_second)
      tmp_cpu = [0]
    else:
      tmp_cpu.append(float(line_list[8]))
    line = fp.readline()
    line_list= line.split()
    # print(line_list)
dpdk_gw_cpu_ts = dpdk_gw_cpu_ts[1:]

# --- CPU usage of DPDK function
dpdk_fn_cpu_ts = []
tmp_cpu = []
with open(fileName_dpdk[1]) as fp:
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
      dpdk_fn_cpu_ts.append(aggregated_cpu_1_second)
      break
    if line_list[2] == 'UID':
      aggregated_cpu_1_second = sum(tmp_cpu)
      dpdk_fn_cpu_ts.append(aggregated_cpu_1_second)
      tmp_cpu = [0]
    else:
      tmp_cpu.append(float(line_list[8]))
    line = fp.readline()
    line_list= line.split()
    # print(tmp_cpu)
dpdk_fn_cpu_ts = dpdk_fn_cpu_ts[1:]

# ----------------------------------------------- #
# ------------ Process SKMSG data --------------- #
# ----------------------------------------------- #
# --- CPU usage of SKMSG GW
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

# --- CPU usage of SKMSG function
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
figsize = 5, 3

figure, ax = plt.subplots(figsize=figsize)

timestamps = [x for x in range(1, len(dpdk_gw_cpu_ts) + 1, 1)]
# print(len(timestamps))
p1 = plt.plot(timestamps, dpdk_gw_cpu_ts, marker = '', ms = 4, mew = 2, label = '', linewidth=2.5, linestyle="-", color='tab:blue')
p2 = plt.plot(timestamps, dpdk_fn_cpu_ts, marker = '', ms = 4, mew = 2, label = '', linewidth=2.5, linestyle="-", color='limegreen')
# p3 = plt.plot(timestamps, kn_fn_cpu_ts, marker = '', ms = 4, mew = 2, label = '', linewidth=2.5, linestyle="-", color='tab:red')
# p4 = plt.plot(rest_4_p, timestamps, marker = '', ms = 4, mew = 2, label = '', linewidth=2.5, linestyle="-", color='#5AAC56')
timestamps = [x for x in range(1, len(skmsg_gw_cpu_ts) + 1, 1)]
p5 = plt.plot(timestamps, skmsg_gw_cpu_ts, marker = '', ms = 4, mew = 2, label = '', linewidth=2.5, linestyle="-.", color='tab:red')
p6 = plt.plot(timestamps, skmsg_fn_cpu_ts, marker = '', ms = 4, mew = 2, label = '', linewidth=2.5, linestyle="-.", color='black')


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
plt.grid(color = 'gray', linestyle = ':', linewidth = 1, axis = 'x')
plt.xlim((0, 160))
plt.ylim((0, 1100))
plt.yticks(np.arange(0, 1000.1, 200), ['0', '200', '400', '600', '800', '1k'])
plt.ylabel('CPU usage (%)', labelpad = 0)
# plt.xticks(np.arange(85, 100.1, 5))
plt.xlabel('(i) timestamp (second)', labelpad=0)

prop = dict(size=11)
plt.legend((p2[0], p1[0], p6[0], p5[0]), 
  ('D-SPRIGHT fn', 'D-SPRIGHT GW', 'S-SPRIGHT fn', 'S-SPRIGHT GW'),
# plt.legend((p2[0], p1[0]), 
#   ('DPDK fn', 'DPDK GW'),
  loc = "center left",
  ncol = 1,
  prop = prop,
  borderaxespad = 0,
  frameon = True,
  columnspacing = 0.7,
  labelspacing = 0.1,
  fancybox = False,
  edgecolor = 'black')

plt.tight_layout()
plt.savefig('fig-10-i.pdf' ,bbox_inches='tight', dpi=400, pad_inches=0.01)
