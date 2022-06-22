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
concurrency = "25K"

fileName_dpdk = 'online_boutique/latency_of_each_req_stats_d-spright.csv'
fileName_skmsg = 'online_boutique/latency_of_each_req_stats_s-spright.csv'

# ----------------------------------------------- #
# ------------ Process DPDK data ---------------- #
# ----------------------------------------------- #
dpdk_rest_1_d = [] # GET /1
dpdk_rest_2_d = [] # POST /1/setCurrency
dpdk_rest_3_d = [] # GET /1/product?
dpdk_rest_4_d = [] # GET /1/cart
dpdk_rest_5_d = [] # POST /1/cart?product_id=
dpdk_rest_6_d = [] # POST /1/cart/checkout?

dpdk_rest_1_ts = []
dpdk_rest_2_ts = []
dpdk_rest_3_ts = []
dpdk_rest_4_ts = []
dpdk_rest_5_ts = []
dpdk_rest_6_ts = []

with open(fileName_dpdk) as fp:
  line = fp.readline()
  # line_list = line.split(";")
  # print(line_list)
  # dpdk_rest_1_d.append(float(line_list[1].split("\n")[0]))
  while line:
    line_list = line.split(";")
    if line_list[1] == "GET":

      if line_list[2].find("/1/product?") != -1:
        dpdk_rest_3_d.append(float(line_list[3].split("\n")[0]))
        dpdk_rest_3_ts.append(float(line_list[0]))

      elif line_list[2].find("/1/cart") != -1:
        dpdk_rest_4_d.append(float(line_list[3].split("\n")[0]))
        dpdk_rest_4_ts.append(float(line_list[0]))

      elif line_list[2].find("/1") != -1:
        dpdk_rest_1_d.append(float(line_list[3].split("\n")[0]))
        dpdk_rest_1_ts.append(float(line_list[0]))

      else:
        print("Unknown (GET) Request Name!")

    elif line_list[1] == "POST":

      if line_list[2].find("/1/setCurrency") != -1:
        dpdk_rest_2_d.append(float(line_list[3].split("\n")[0]))
        dpdk_rest_2_ts.append(float(line_list[0]))

      elif line_list[2].find("/1/cart?product_id") != -1:
        dpdk_rest_5_d.append(float(line_list[3].split("\n")[0]))
        dpdk_rest_5_ts.append(float(line_list[0]))

      elif line_list[2].find("/1/cart/checkout?") != -1:
        dpdk_rest_6_d.append(float(line_list[3].split("\n")[0]))
        dpdk_rest_6_ts.append(float(line_list[0]))

      else:
        print("Unknown (POST) Request Name!")

    else:
      print("Unknown Request Type!")

    line = fp.readline()
    if len(line) == 0:
      break
    # line_list= line.split(";")
    # if len(line_list) != 0:
    #   dpdk_rest_1_d.append(float(line_list[1].split("\n")[0]))

# ----------------------------------------------- #
# ------------ Process SKMSG data --------------- #
# ----------------------------------------------- #
skmsg_rest_1_d = []
skmsg_rest_2_d = []
skmsg_rest_3_d = []
skmsg_rest_4_d = []
skmsg_rest_5_d = []
skmsg_rest_6_d = []

skmsg_rest_1_ts = []
skmsg_rest_2_ts = []
skmsg_rest_3_ts = []
skmsg_rest_4_ts = []
skmsg_rest_5_ts = []
skmsg_rest_6_ts = []

with open(fileName_skmsg) as fp:
  line = fp.readline()
  # line_list = line.split(";")
  # print(line_list)
  # dpdk_rest_1_d.append(float(line_list[1].split("\n")[0]))
  while line:
    line_list = line.split(";")
    if line_list[1] == "GET":

      if line_list[2].find("/1/product?") != -1:
        skmsg_rest_3_d.append(float(line_list[3].split("\n")[0]))
        skmsg_rest_3_ts.append(float(line_list[0]))

      elif line_list[2].find("/1/cart") != -1:
        skmsg_rest_4_d.append(float(line_list[3].split("\n")[0]))
        skmsg_rest_4_ts.append(float(line_list[0]))

      elif line_list[2].find("/1") != -1:
        skmsg_rest_1_d.append(float(line_list[3].split("\n")[0]))
        skmsg_rest_1_ts.append(float(line_list[0]))

      else:
        print("Unknown (GET) Request Name!")

    elif line_list[1] == "POST":

      if line_list[2].find("/1/setCurrency") != -1:
        skmsg_rest_2_d.append(float(line_list[3].split("\n")[0]))
        skmsg_rest_2_ts.append(float(line_list[0]))

      elif line_list[2].find("/1/cart?product_id") != -1:
        skmsg_rest_5_d.append(float(line_list[3].split("\n")[0]))
        skmsg_rest_5_ts.append(float(line_list[0]))

      elif line_list[2].find("/1/cart/checkout?") != -1:
        skmsg_rest_6_d.append(float(line_list[3].split("\n")[0]))
        skmsg_rest_6_ts.append(float(line_list[0]))

      else:
        print("Unknown (POST) Request Name!")

    else:
      print("Unknown Request Type!")

    line = fp.readline()
    if len(line) == 0:
      break
    # line_list= line.split(";")
    # if len(line_list) != 0:
    #   dpdk_rest_1_d.append(float(line_list[1].split("\n")[0]))


# ----------------------------------------------- #
# -------------- Align timestamp ---------------- #
# ----------------------------------------------- #
dpdk_min_rests = []
dpdk_min_rests.append(min(dpdk_rest_1_ts))
dpdk_min_rests.append(min(dpdk_rest_2_ts))
dpdk_min_rests.append(min(dpdk_rest_3_ts))
dpdk_min_rests.append(min(dpdk_rest_4_ts))
dpdk_min_rests.append(min(dpdk_rest_5_ts))
dpdk_min_rests.append(min(dpdk_rest_6_ts))

skmsg_min_rests = []
skmsg_min_rests.append(min(skmsg_rest_1_ts))
skmsg_min_rests.append(min(skmsg_rest_2_ts))
skmsg_min_rests.append(min(skmsg_rest_3_ts))
skmsg_min_rests.append(min(skmsg_rest_4_ts))
skmsg_min_rests.append(min(skmsg_rest_5_ts))
skmsg_min_rests.append(min(skmsg_rest_6_ts))

dpdk_start_time = float(int(min(dpdk_min_rests)))
align_offset = 0
dpdk_rest_1_ts = [x - dpdk_start_time + align_offset for x in dpdk_rest_1_ts]
dpdk_rest_2_ts = [x - dpdk_start_time + align_offset for x in dpdk_rest_2_ts]
dpdk_rest_3_ts = [x - dpdk_start_time + align_offset for x in dpdk_rest_3_ts]
dpdk_rest_4_ts = [x - dpdk_start_time + align_offset for x in dpdk_rest_4_ts]
dpdk_rest_5_ts = [x - dpdk_start_time + align_offset for x in dpdk_rest_5_ts]
dpdk_rest_6_ts = [x - dpdk_start_time + align_offset for x in dpdk_rest_6_ts]

skmsg_start_time = float(int(min(skmsg_min_rests)))
align_offset = 0
skmsg_rest_1_ts = [x - skmsg_start_time + align_offset for x in skmsg_rest_1_ts]
skmsg_rest_2_ts = [x - skmsg_start_time + align_offset for x in skmsg_rest_2_ts]
skmsg_rest_3_ts = [x - skmsg_start_time + align_offset for x in skmsg_rest_3_ts]
skmsg_rest_4_ts = [x - skmsg_start_time + align_offset for x in skmsg_rest_4_ts]
skmsg_rest_5_ts = [x - skmsg_start_time + align_offset for x in skmsg_rest_5_ts]
skmsg_rest_6_ts = [x - skmsg_start_time + align_offset for x in skmsg_rest_6_ts]

# ----------------------------------------------- #
# -------------- FIGURE PLOT -------------------- #
# ----------------------------------------------- #
figsize = 5, 3

figure, ax = plt.subplots(figsize=figsize)

# timestamps = [x for x in range(1 + align_offset, len(rest_1_d) + 1 + align_offset, 1)]
p11 = plt.plot(dpdk_rest_1_ts, dpdk_rest_1_d, marker = '.', ms = 4, mew = 1, label = '', linewidth=2.5, linestyle=" ", color='tab:blue')
p12 = plt.plot(dpdk_rest_2_ts, dpdk_rest_2_d, marker = '.', ms = 4, mew = 1, label = '', linewidth=2.5, linestyle=" ", color='limegreen')
p13 = plt.plot(dpdk_rest_3_ts, dpdk_rest_3_d, marker = '.', ms = 4, mew = 1, label = '', linewidth=2.5, linestyle=" ", color='tab:red')
p14 = plt.plot(dpdk_rest_4_ts, dpdk_rest_4_d, marker = '.', ms = 4, mew = 1, label = '', linewidth=2.5, linestyle=" ", color='#D4996A')
p15 = plt.plot(dpdk_rest_5_ts, dpdk_rest_5_d, marker = '.', ms = 4, mew = 1, label = '', linewidth=2.5, linestyle=" ", color='#FDA8AA')
p16 = plt.plot(dpdk_rest_6_ts, dpdk_rest_6_d, marker = '.', ms = 4, mew = 1, label = '', linewidth=2.5, linestyle=" ", color='#555CB5')

p21 = plt.plot(skmsg_rest_1_ts, skmsg_rest_1_d, marker = 'x', ms = 4, mew = 1, label = '', linewidth=2.5, linestyle=" ", color='tab:blue')
p22 = plt.plot(skmsg_rest_2_ts, skmsg_rest_2_d, marker = 'x', ms = 4, mew = 1, label = '', linewidth=2.5, linestyle=" ", color='limegreen')
p23 = plt.plot(skmsg_rest_3_ts, skmsg_rest_3_d, marker = 'x', ms = 4, mew = 1, label = '', linewidth=2.5, linestyle=" ", color='tab:red')
p24 = plt.plot(skmsg_rest_4_ts, skmsg_rest_4_d, marker = 'x', ms = 4, mew = 1, label = '', linewidth=2.5, linestyle=" ", color='#552600')
p25 = plt.plot(skmsg_rest_5_ts, skmsg_rest_5_d, marker = 'x', ms = 4, mew = 1, label = '', linewidth=2.5, linestyle=" ", color='#FDA8AA')
p26 = plt.plot(skmsg_rest_6_ts, skmsg_rest_6_d, marker = 'x', ms = 4, mew = 1, label = '', linewidth=2.5, linestyle=" ", color='#555CB5')


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
plt.grid(color = 'gray', linestyle = ':', linewidth = 1)
plt.ylim((0, 1100))
plt.xlim((0, 160))
plt.yticks(np.arange(0, 1000.1, 200), ['0', '200', '400', '600', '800', '1k'], rotation = 45)
plt.ylabel('Response time (ms)', labelpad = 0)
plt.xlabel('(f) timestamp (second)', labelpad=0)

prop = dict(size=10)
plt.legend((p11[0], p12[0], p13[0],p14[0], p15[0], p16[0], p21[0], p22[0], p23[0],p24[0], p25[0], p26[0]), 
  ('D: Ch-1', 'D: Ch-2','D: Ch-3', 'D: Ch-4', 'D: Ch-5','D: Ch-6', 'S: Ch-1', 'S: Ch-2','S: Ch-3', 'S: Ch-4', 'S: Ch-5','S: Ch-6'),
  loc = "upper left",
  markerscale=2,
  ncol = 3,
  prop = prop,
  borderaxespad = 0,
  frameon = True,
  columnspacing = 0.4,
  labelspacing = 0.1,
  fancybox = False,
  edgecolor = 'black')

plt.tight_layout()
plt.savefig('fig-10-f.png', bbox_inches='tight', dpi=400, pad_inches=0.01)
