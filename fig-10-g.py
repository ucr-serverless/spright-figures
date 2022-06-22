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

concurrency = "5K"

# fileName_grpc = ['grpc/' + concurrency + '/grpc-front-prod.cpu', 'grpc/' + concurrency + '/grpc-recom.cpu', 'grpc/' + concurrency + '/grpc-others.cpu']
fileName_kn = ['online_boutique/kn-front-prod.cpu', 'online_boutique/kn-recom.cpu', 'online_boutique/kn-others.cpu', 'online_boutique/kn-gw.cpu', 'online_boutique/kn-queue.cpu']

'''
# ----------------------------------------------- #
# ------------ Process gRPC data ---------------- #
# ----------------------------------------------- #
# --- CPU usage of gRPC front-prod
grpc_f_p_cpu_ts = []
tmp_cpu = [0]
with open(fileName_grpc[0]) as fp:
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
      grpc_f_p_cpu_ts.append(aggregated_cpu_1_second)
      break
    if line_list[2] == 'UID':
      aggregated_cpu_1_second = sum(tmp_cpu)
      grpc_f_p_cpu_ts.append(aggregated_cpu_1_second)
      tmp_cpu = [0]
    else:
      tmp_cpu.append(float(line_list[8]))
    line = fp.readline()
    line_list= line.split()
    # print(line_list)
grpc_f_p_cpu_ts = grpc_f_p_cpu_ts[1:]

# --- CPU usage of gRPC recomend
grpc_r_cpu_ts = []
tmp_cpu = [0]
with open(fileName_grpc[1]) as fp:
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
      grpc_r_cpu_ts.append(aggregated_cpu_1_second)
      break
    if line_list[2] == 'UID':
      aggregated_cpu_1_second = sum(tmp_cpu)
      grpc_r_cpu_ts.append(aggregated_cpu_1_second)
      tmp_cpu = [0]
    else:
      tmp_cpu.append(float(line_list[8]))
    line = fp.readline()
    line_list= line.split()
    # print(line_list)
grpc_r_cpu_ts = grpc_r_cpu_ts[1:]

# --- CPU usage of gRPC others
grpc_oth_cpu_ts = []
tmp_cpu = [0]
with open(fileName_grpc[2]) as fp:
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
      grpc_oth_cpu_ts.append(aggregated_cpu_1_second)
      break
    if line_list[2] == 'UID':
      aggregated_cpu_1_second = sum(tmp_cpu)
      grpc_oth_cpu_ts.append(aggregated_cpu_1_second)
      tmp_cpu = [0]
    else:
      tmp_cpu.append(float(line_list[8]))
    line = fp.readline()
    line_list= line.split()
    # print(line_list)
grpc_oth_cpu_ts = grpc_oth_cpu_ts[1:]

grpc_cpu_ts = [i + j + k for i, j, k in zip(grpc_oth_cpu_ts, grpc_r_cpu_ts, grpc_f_p_cpu_ts)]
'''
# ----------------------------------------------- #
# --------- Process Knative data ---------------- #
# ----------------------------------------------- #
# --- CPU usage of Knative front-prod
kn_f_p_cpu_ts = []
tmp_cpu = [0]
with open(fileName_kn[0]) as fp:
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
      kn_f_p_cpu_ts.append(aggregated_cpu_1_second)
      break
    if line_list[2] == 'UID':
      aggregated_cpu_1_second = sum(tmp_cpu)
      kn_f_p_cpu_ts.append(aggregated_cpu_1_second)
      tmp_cpu = [0]
    else:
      tmp_cpu.append(float(line_list[8]))
    line = fp.readline()
    line_list= line.split()
    # print(line_list)
kn_f_p_cpu_ts = kn_f_p_cpu_ts[1:]

# --- CPU usage of Knative recomend
kn_r_cpu_ts = []
tmp_cpu = [0]
with open(fileName_kn[1]) as fp:
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
      kn_r_cpu_ts.append(aggregated_cpu_1_second)
      break
    if line_list[2] == 'UID':
      aggregated_cpu_1_second = sum(tmp_cpu)
      kn_r_cpu_ts.append(aggregated_cpu_1_second)
      tmp_cpu = [0]
    else:
      tmp_cpu.append(float(line_list[8]))
    line = fp.readline()
    line_list= line.split()
    # print(line_list)
kn_r_cpu_ts = kn_r_cpu_ts[1:]

# --- CPU usage of Knative others functions
kn_oth_cpu_ts = []
tmp_cpu = [0]
with open(fileName_kn[2]) as fp:
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
      kn_oth_cpu_ts.append(aggregated_cpu_1_second)
      break
    if line_list[2] == 'UID':
      aggregated_cpu_1_second = sum(tmp_cpu)
      kn_oth_cpu_ts.append(aggregated_cpu_1_second)
      tmp_cpu = [0]
    else:
      tmp_cpu.append(float(line_list[8]))
    line = fp.readline()
    line_list= line.split()
    # print(line_list)
kn_oth_cpu_ts = kn_oth_cpu_ts[1:]

kn_fn_cpu_ts = [i + j + k for i, j, k in zip(kn_oth_cpu_ts, kn_r_cpu_ts, kn_f_p_cpu_ts)]

# --- CPU usage of Knative Ingress gateway
kn_gw_cpu_ts = []
tmp_cpu = [0]
with open(fileName_kn[3]) as fp:
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
    # print(line_list)
kn_gw_cpu_ts = kn_gw_cpu_ts[1:]

# --- CPU usage of Knative queue proxy
kn_queue_cpu_ts = []
tmp_cpu = [0]
with open(fileName_kn[4]) as fp:
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
    # print(line_list)
kn_queue_cpu_ts = kn_queue_cpu_ts[1:]

kn_aggregate_cpu_ts = [i + j + k for i, j, k in zip(kn_fn_cpu_ts,kn_gw_cpu_ts,kn_queue_cpu_ts)]

# ----------------------------------------------- #
# -------------- FIGURE PLOT -------------------- #
# ----------------------------------------------- #
figsize = 5, 3

figure, ax = plt.subplots(figsize=figsize)

timestamps = [x for x in range(1, len(kn_queue_cpu_ts) + 1, 1)]
# print(len(timestamps))
# p1 = plt.plot(timestamps, kn_aggregate_cpu_ts, marker = '', ms = 4, mew = 2, label = '', linewidth=2.5, linestyle="-", color='tab:blue')
p2 = plt.plot(timestamps, kn_fn_cpu_ts, marker = '', ms = 4, mew = 2, label = '', linewidth=2.5, linestyle="-", color='limegreen')
p3 = plt.plot(timestamps, kn_gw_cpu_ts, marker = '', ms = 4, mew = 2, label = '', linewidth=2.5, linestyle="-", color='tab:red')
p4 = plt.plot(timestamps, kn_queue_cpu_ts, marker = '', ms = 4, mew = 2, label = '', linewidth=2.5, linestyle="-.", color='black')
# p4 = plt.plot(rest_4_p, timestamps, marker = '', ms = 4, mew = 2, label = '', linewidth=2.5, linestyle="-", color='#5AAC56')
# timestamps = [x for x in range(1, len(skmsg_gw_cpu_ts) + 1, 1)]
# p5 = plt.plot(timestamps, skmsg_gw_cpu_ts, marker = '', ms = 4, mew = 2, label = '', linewidth=2.5, linestyle="-.", color='tab:red')

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
plt.ylim((0, 4000))
plt.yticks(np.arange(0, 4000.1, 1000), ['0', '1K', '2K', '3K', '4K'])
plt.ylabel('CPU usage (%)', labelpad = 0)
# plt.xticks(np.arange(85, 100.1, 5))
plt.xlabel('(g) timestamp (second)', labelpad=0)

prop = dict(size=11)
plt.legend((p2[0], p3[0], p4[0]), 
  ('Kn fn', 'Kn GW', 'Kn queue'),
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
plt.savefig('fig-10-g.pdf' ,bbox_inches='tight', dpi=400, pad_inches=0.01)
