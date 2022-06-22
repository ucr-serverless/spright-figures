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

# ----------------------------------------------- #
# ------------ Input parameters ----------------- #
# ----------------------------------------------- #

concurrency = "25K"

lrotation = 0
logFileNum = 6

fileName_dpdk = 'online_boutique/latency_of_each_req_stats_d-spright.csv'
fileName_skmsg = 'online_boutique/latency_of_each_req_stats_s-spright.csv'

figsize = 5, 3

figure, ax = plt.subplots(figsize=figsize)
ind = np.arange(0, logFileNum*1 , 1)   # the x locations for the groups
width = 0.2
gap = -0.4

# ----------------------------------------------- #
# ------------ Process DPDK data ---------------- #
# ----------------------------------------------- #
dpdk_rest_1_d = [] # GET /1
dpdk_rest_2_d = [] # POST /1/setCurrency
dpdk_rest_3_d = [] # GET /1/product?
dpdk_rest_4_d = [] # GET /1/cart
dpdk_rest_5_d = [] # POST /1/cart?product_id=
dpdk_rest_6_d = [] # POST /1/cart/checkout?

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

      elif line_list[2].find("/1/cart") != -1:
        dpdk_rest_4_d.append(float(line_list[3].split("\n")[0]))

      elif line_list[2].find("/1") != -1:
        dpdk_rest_1_d.append(float(line_list[3].split("\n")[0]))

      else:
        print("Unknown (GET) Request Name!")

    elif line_list[1] == "POST":

      if line_list[2].find("/1/setCurrency") != -1:
        dpdk_rest_2_d.append(float(line_list[3].split("\n")[0]))

      elif line_list[2].find("/1/cart?product_id") != -1:
        dpdk_rest_5_d.append(float(line_list[3].split("\n")[0]))

      elif line_list[2].find("/1/cart/checkout?") != -1:
        dpdk_rest_6_d.append(float(line_list[3].split("\n")[0]))

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

percentiles = [x for x in range(10, 101, 1)]
dpdk_rest_1_p = np.percentile(dpdk_rest_1_d, percentiles)
dpdk_rest_2_p = np.percentile(dpdk_rest_2_d, percentiles)
dpdk_rest_3_p = np.percentile(dpdk_rest_3_d, percentiles)
dpdk_rest_4_p = np.percentile(dpdk_rest_4_d, percentiles)
dpdk_rest_5_p = np.percentile(dpdk_rest_5_d, percentiles)
dpdk_rest_6_p = np.percentile(dpdk_rest_6_d, percentiles)

# ----------------------------------------------- #
# ----------- Process SKMSG data ---------------- #
# ----------------------------------------------- #
skmsg_rest_1_d = []
skmsg_rest_2_d = []
skmsg_rest_3_d = []
skmsg_rest_4_d = []
skmsg_rest_5_d = []
skmsg_rest_6_d = []

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

      elif line_list[2].find("/1/cart") != -1:
        skmsg_rest_4_d.append(float(line_list[3].split("\n")[0]))

      elif line_list[2].find("/1") != -1:
        skmsg_rest_1_d.append(float(line_list[3].split("\n")[0]))

      else:
        print("Unknown (GET) Request Name!")

    elif line_list[1] == "POST":

      if line_list[2].find("/1/setCurrency") != -1:
        skmsg_rest_2_d.append(float(line_list[3].split("\n")[0]))

      elif line_list[2].find("/1/cart?product_id") != -1:
        skmsg_rest_5_d.append(float(line_list[3].split("\n")[0]))

      elif line_list[2].find("/1/cart/checkout?") != -1:
        skmsg_rest_6_d.append(float(line_list[3].split("\n")[0]))

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

percentiles = [x for x in range(10, 101, 1)]
skmsg_rest_1_p = np.percentile(skmsg_rest_1_d, percentiles)
skmsg_rest_2_p = np.percentile(skmsg_rest_2_d, percentiles)
skmsg_rest_3_p = np.percentile(skmsg_rest_3_d, percentiles)
skmsg_rest_4_p = np.percentile(skmsg_rest_4_d, percentiles)
skmsg_rest_5_p = np.percentile(skmsg_rest_5_d, percentiles)
skmsg_rest_6_p = np.percentile(skmsg_rest_6_d, percentiles)

# ----------------------------------------------- #
# -------------- FIGURE PLOT -------------------- #
# ----------------------------------------------- #
p11 = plt.plot(dpdk_rest_1_p, percentiles, marker = 'p', ms = 1, mew = 2, label = '', linewidth=2, linestyle="-", color='tab:blue')
p12 = plt.plot(dpdk_rest_2_p, percentiles, marker = '', ms = 4, mew = 2, label = '', linewidth=2, linestyle="-", color='limegreen')
p13 = plt.plot(dpdk_rest_3_p, percentiles, marker = '', ms = 4, mew = 2, label = '', linewidth=2, linestyle="-", color='tab:red')
p14 = plt.plot(dpdk_rest_4_p, percentiles, marker = 'v', ms = 2, mew = 2, label = '', linewidth=2, linestyle="-", color='#D4996A')
p15 = plt.plot(dpdk_rest_5_p, percentiles, marker = '', ms = 4, mew = 2, label = '', linewidth=2, linestyle="-", color='#FDA8AA')
p16 = plt.plot(dpdk_rest_6_p, percentiles, marker = 'o', ms = 1, mew = 1, label = '', linewidth=2, linestyle="-", color='#555CB5')

p21 = plt.plot(skmsg_rest_1_p, percentiles, marker = '', ms = 4, mew = 2, label = '', linewidth=2, linestyle="-.", color='tab:blue')
p22 = plt.plot(skmsg_rest_2_p, percentiles, marker = '', ms = 4, mew = 2, label = '', linewidth=2, linestyle="-.", color='limegreen')
p23 = plt.plot(skmsg_rest_3_p, percentiles, marker = '', ms = 4, mew = 2, label = '', linewidth=2, linestyle="-.", color='tab:red')
p24 = plt.plot(skmsg_rest_4_p, percentiles, marker = '', ms = 2, mew = 2, label = '', linewidth=2, linestyle="-.", color='#D4996A')
p25 = plt.plot(skmsg_rest_5_p, percentiles, marker = '', ms = 4, mew = 2, label = '', linewidth=2, linestyle="-.", color='#FDA8AA')
p26 = plt.plot(skmsg_rest_6_p, percentiles, marker = '', ms = 1, mew = 1, label = '', linewidth=2, linestyle="-.", color='#555CB5')

plt.tick_params(grid_linewidth = 3, grid_linestyle = ':', pad=0)
figure.subplots_adjust(bottom=0.25, left=0.2)
# plt.xticks(ind, ('0', '10','50','100','200','400'))
plt.setp(ax.get_xticklabels(), 
  rotation=lrotation, 
  ha="center",
  rotation_mode="anchor")
  # plt.grid(True)
plt.xlim((0, 200))
plt.xticks(np.arange(0, 200, 40))#, ['0', '5k', '10k', '15k', '20k'])
# plt.xticks(['0', '5k', '10k', '15k', '20k'])
# plt.xlim((0, 1))
# plt.grid(True)
plt.grid(color = 'gray', linestyle = ':', linewidth = 1.5)
plt.ylim((0, 101))
plt.yticks(np.arange(0, 100.001, 20))
plt.ylabel('% of requests', labelpad=-5)
plt.xlabel('(c) Response time CDF (ms)', labelpad=0)

prop = dict(size=11)
# plt.legend((p11[0], p12[0], p13[0],p14[0], p15[0], p16[0]), 
#   ('DPDK: Ch-1', 'DPDK: Ch-2','DPDK: Ch-3', 'DPDK: Ch-4', 'DPDK: Ch-5','DPDK: Ch-6'),
plt.legend((p11[0], p12[0], p13[0],p14[0], p15[0], p16[0], p21[0], p22[0], p23[0],p24[0], p25[0], p26[0]), 
  ('D: Ch-1', 'D: Ch-2','D: Ch-3', 'D: Ch-4', 'D: Ch-5','D: Ch-6', 'S: Ch-1', 'S: Ch-2','S: Ch-3', 'S: Ch-4', 'S: Ch-5','S: Ch-6'),
  loc = "lower right",
  ncol = 2,
  prop = prop,
  borderaxespad = 0,
  frameon = True,
  columnspacing = 0.7,
  labelspacing = 0.05,
  fancybox = False,
  edgecolor = 'black')

plt.tight_layout()
plt.savefig('fig-10-c.pdf' ,bbox_inches='tight',dpi=figure.dpi,pad_inches=0.01)
