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
concurrency_dpdk_skmsg = "25K"
concurrency_grpc_kn = "5K"

fileName_dpdk =  ['online_boutique/rps_stats_d-spright.csv']
fileName_skmsg =  ['online_boutique/rps_stats_s-spright.csv']
fileName_grpc =  ['online_boutique/rps_stats_grpc.csv']
fileName_kn =  ['online_boutique/rps_stats_kn.csv']

# ----------------------------------------------- #
# ------------ Process RPS data ----------------- #
# ----------------------------------------------- #
# --- RPS of DPDK
dpdk_rps_ts = []
tmp_rps = [0]
with open(fileName_dpdk[0]) as fp:
  line = fp.readline()
  line_list= line.split(",")
  while line:
    if len(line_list) == 0:
      line = fp.readline()
      line_list= line.split(",")
      continue
    if line_list[0] == 'Timestamp':
      line = fp.readline()
      line_list= line.split(",")
      # print(line_list)
      # exit(1)
      continue
    if line_list[3] == 'Aggregated':
      dpdk_rps_ts.append(float(line_list[4]))
      tmp_rps = [0]
    line = fp.readline()
    line_list= line.split(",")

# --- RPS of SKMSG
skmsg_rps_ts = []
tmp_rps = [0]
with open(fileName_skmsg[0]) as fp:
  line = fp.readline()
  line_list= line.split(",")
  while line:
    if len(line_list) == 0:
      line = fp.readline()
      line_list= line.split(",")
      continue
    if line_list[0] == 'Timestamp':
      line = fp.readline()
      line_list= line.split(",")
      # print(line_list)
      # exit(1)
      continue
    if line_list[3] == 'Aggregated':
      skmsg_rps_ts.append(float(line_list[4]))
      tmp_rps = [0]
    line = fp.readline()
    line_list= line.split(",")

# --- RPS of gRPC
grpc_rps_ts = []
tmp_rps = [0]
with open(fileName_grpc[0]) as fp:
  line = fp.readline()
  line_list= line.split(",")
  while line:
    if len(line_list) == 0:
      line = fp.readline()
      line_list= line.split(",")
      continue
    if line_list[0] == 'Timestamp':
      line = fp.readline()
      line_list= line.split(",")
      # print(line_list)
      # exit(1)
      continue
    if line_list[3] == 'Aggregated':
      grpc_rps_ts.append(float(line_list[4]))
      tmp_rps = [0]
    line = fp.readline()
    line_list= line.split(",")

# --- RPS of Knative
kn_total_rps_ts = []
kn_fail_rps_ts = []
tmp_rps = [0]
with open(fileName_kn[0]) as fp:
  line = fp.readline()
  line_list= line.split(",")
  while line:
    if len(line_list) == 0:
      line = fp.readline()
      line_list= line.split(",")
      continue
    if line_list[0] == 'Timestamp':
      line = fp.readline()
      line_list= line.split(",")
      # print(line_list)
      # exit(1)
      continue
    if line_list[3] == 'Aggregated':
      kn_total_rps_ts.append(float(line_list[4]))
      kn_fail_rps_ts.append(float(line_list[5]))
      tmp_rps = [0]
    line = fp.readline()
    line_list= line.split(",")

kn_success_rps_ts = [i - j for i, j in zip(kn_total_rps_ts, kn_fail_rps_ts)]

# ----------------------------------------------- #
# -------------- FIGURE PLOT -------------------- #
# ----------------------------------------------- #
figsize = 7, 3

figure, ax = plt.subplots(figsize=figsize)

# --- RPS of DPDK and SKMSG
align_offset = 1 # aligned with CPU usage time series
timestamps_dpdk = [x for x in range(1 + align_offset, len(dpdk_rps_ts) + 1 + align_offset, 1)]
p1 = plt.plot(timestamps_dpdk, dpdk_rps_ts, marker = '', ms = 4, mew = 2, label = '', linewidth=2.5, linestyle="-", color='tab:blue')
timestamps_skmsg = [x for x in range(1 + align_offset, len(skmsg_rps_ts) + 1 + align_offset, 1)]
p2 = plt.plot(timestamps_skmsg, skmsg_rps_ts, marker = '', ms = 4, mew = 2, label = '', linewidth=2.5, linestyle="-.", color='limegreen')
# p3 = plt.plot(timestamps_kn, kn_rps_ts, marker = '', ms = 4, mew = 2, label = '', linewidth=2.5, linestyle="-", color='tab:red')

# --- RPS of gRPC and Knative
timestamps_grpc = [x for x in range(1 + align_offset, len(grpc_rps_ts) + 1 + align_offset, 1)]
timestamps_kn = [x for x in range(1 + align_offset, len(kn_success_rps_ts) + 1 + align_offset, 1)]
p3 = plt.plot(timestamps_grpc, grpc_rps_ts, marker = '', ms = 4, mew = 2, label = '', linewidth=2.5, linestyle="-", color='tab:red')
p4 = plt.plot(timestamps_kn, kn_success_rps_ts, marker = '', ms = 4, mew = 2, label = '', linewidth=2.5, linestyle="-.", color='black')

plt.tick_params(grid_linewidth = 3, grid_linestyle = ':', pad=0)
figure.subplots_adjust(bottom=0.25, left=0.2)
plt.setp(ax.get_xticklabels(), 
  rotation=lrotation, 
  ha="center",
  rotation_mode="anchor")

plt.grid(color = 'gray', linestyle = ':', linewidth = 1.5, axis = 'x')
plt.xlim((0, 160))
plt.ylim((0, 7000))
plt.yticks(np.arange(0, 6000.1, 1000), ['0', '1K', '2K', '3K', '4K', '5K', '6K'])
plt.ylabel('Req/sec', labelpad = 0)
plt.xlabel('timestamp (second)', labelpad=-2)

prop = dict(size=12)
plt.legend((p1[0], p2[0], p3[0], p4[0]),
  ('D-SPRIGHT', 'S-SPRIGHT', 'gRPC', 'Kn'),
  loc = "upper left",
  ncol = 1,
  prop = prop,
  borderaxespad = 0,
  frameon = True,
  columnspacing = 0.7,
  labelspacing = 0.1,
  fancybox = False,
  edgecolor = 'black')

plt.tight_layout()
# plt.savefig('all-rps-time-series.pdf', bbox_inches='tight', dpi=figure.dpi, pad_inches=0.01)
plt.savefig('fig-9.png', bbox_inches='tight', dpi=500, pad_inches=0.01)