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
concurrency = "5K"

fileName_grpc = 'online_boutique/latency_of_each_req_stats_grpc.csv'
# fileName_kn = 'kn/' + concurrency + '/stats.csv'

# ----------------------------------------------- #
# ------------ Process gRPC data ---------------- #
# ----------------------------------------------- #
grpc_rest_1_d = [] # GET /1
grpc_rest_2_d = [] # POST /1/setCurrency
grpc_rest_3_d = [] # GET /1/product?
grpc_rest_4_d = [] # GET /1/cart
grpc_rest_5_d = [] # POST /1/cart?product_id=
grpc_rest_6_d = [] # POST /1/cart/checkout?

grpc_rest_1_ts = []
grpc_rest_2_ts = []
grpc_rest_3_ts = []
grpc_rest_4_ts = []
grpc_rest_5_ts = []
grpc_rest_6_ts = []

with open(fileName_grpc) as fp:
  line = fp.readline()
  while line:
    line_list = line.split(";")
    if line_list[1] == "GET":

      if line_list[2].find("/product/") != -1:
        grpc_rest_3_d.append(float(line_list[3].split("\n")[0]))
        grpc_rest_3_ts.append(float(line_list[0]))

      elif line_list[2].find("/cart") != -1:
        grpc_rest_4_d.append(float(line_list[3].split("\n")[0]))
        grpc_rest_4_ts.append(float(line_list[0]))

      elif line_list[2].find("/") != -1:
        grpc_rest_1_d.append(float(line_list[3].split("\n")[0]))
        grpc_rest_1_ts.append(float(line_list[0]))

      else:
        print("Unknown (GET) Request Name!")

    elif line_list[1] == "POST":

      if line_list[2].find("/setCurrency") != -1:
        grpc_rest_2_d.append(float(line_list[3].split("\n")[0]))
        grpc_rest_2_ts.append(float(line_list[0]))

      elif line_list[2].find("/cart/checkout") != -1:
        grpc_rest_6_d.append(float(line_list[3].split("\n")[0]))
        grpc_rest_6_ts.append(float(line_list[0]))

      elif line_list[2].find("/cart") != -1:
        grpc_rest_5_d.append(float(line_list[3].split("\n")[0]))
        grpc_rest_5_ts.append(float(line_list[0]))

      else:
        print("Unknown (POST) Request Name!")

    else:
      print("Unknown Request Type!")

    line = fp.readline()
    if len(line) == 0:
      break

'''
# ----------------------------------------------- #
# ------- Process Knative data and plot --------- #
# ----------------------------------------------- #
kn_rest_1_d = [] # GET /1
kn_rest_2_d = [] # POST /1/setCurrency
kn_rest_3_d = [] # GET /1/product?
kn_rest_4_d = [] # GET /1/cart
kn_rest_5_d = [] # POST /1/cart?product_id=
kn_rest_6_d = [] # POST /1/cart/checkout?

kn_rest_1_ts = []
kn_rest_2_ts = []
kn_rest_3_ts = []
kn_rest_4_ts = []
kn_rest_5_ts = []
kn_rest_6_ts = []

with open(fileName_kn) as fp:
  line = fp.readline()
  while line:
    line_list = line.split(";")
    if line_list[1] == "GET":

      if line_list[2].find("/product/") != -1:
        kn_rest_3_d.append(float(line_list[3].split("\n")[0]))
        kn_rest_3_ts.append(float(line_list[0]))

      elif line_list[2].find("/cart") != -1:
        kn_rest_4_d.append(float(line_list[3].split("\n")[0]))
        kn_rest_4_ts.append(float(line_list[0]))

      elif line_list[2].find("/") != -1:
        kn_rest_1_d.append(float(line_list[3].split("\n")[0]))
        kn_rest_1_ts.append(float(line_list[0]))

      else:
        print("Unknown (GET) Request Name!")

    elif line_list[1] == "POST":

      if line_list[2].find("/setCurrency") != -1:
        kn_rest_2_d.append(float(line_list[3].split("\n")[0]))
        kn_rest_2_ts.append(float(line_list[0]))

      elif line_list[2].find("/cart/checkout") != -1:
        kn_rest_6_d.append(float(line_list[3].split("\n")[0]))
        kn_rest_6_ts.append(float(line_list[0]))

      elif line_list[2].find("/cart") != -1:
        kn_rest_5_d.append(float(line_list[3].split("\n")[0]))
        kn_rest_5_ts.append(float(line_list[0]))

      else:
        print("Unknown (POST) Request Name!")

    else:
      print("Unknown Request Type!")

    line = fp.readline()
    if len(line) == 0:
      break
'''
# ----------------------------------------------- #
# -------------- Align timestamp ---------------- #
# ----------------------------------------------- #
grpc_min_rests = []
grpc_min_rests.append(min(grpc_rest_1_ts))
grpc_min_rests.append(min(grpc_rest_2_ts))
grpc_min_rests.append(min(grpc_rest_3_ts))
grpc_min_rests.append(min(grpc_rest_4_ts))
grpc_min_rests.append(min(grpc_rest_5_ts))
grpc_min_rests.append(min(grpc_rest_6_ts))

# kn_min_rests = []
# kn_min_rests.append(min(kn_rest_1_ts))
# kn_min_rests.append(min(kn_rest_2_ts))
# kn_min_rests.append(min(kn_rest_3_ts))
# kn_min_rests.append(min(kn_rest_4_ts))
# kn_min_rests.append(min(kn_rest_5_ts))
# kn_min_rests.append(min(kn_rest_6_ts))

grpc_start_time = float(int(min(grpc_min_rests)))
align_offset = 0
grpc_rest_1_ts = [x - grpc_start_time + align_offset for x in grpc_rest_1_ts]
grpc_rest_2_ts = [x - grpc_start_time + align_offset for x in grpc_rest_2_ts]
grpc_rest_3_ts = [x - grpc_start_time + align_offset for x in grpc_rest_3_ts]
grpc_rest_4_ts = [x - grpc_start_time + align_offset for x in grpc_rest_4_ts]
grpc_rest_5_ts = [x - grpc_start_time + align_offset for x in grpc_rest_5_ts]
grpc_rest_6_ts = [x - grpc_start_time + align_offset for x in grpc_rest_6_ts]

# kn_start_time = float(int(min(kn_min_rests)))
# align_offset = 5
# kn_rest_1_ts = [x - kn_start_time + align_offset for x in kn_rest_1_ts]
# kn_rest_2_ts = [x - kn_start_time + align_offset for x in kn_rest_2_ts]
# kn_rest_3_ts = [x - kn_start_time + align_offset for x in kn_rest_3_ts]
# kn_rest_4_ts = [x - kn_start_time + align_offset for x in kn_rest_4_ts]
# kn_rest_5_ts = [x - kn_start_time + align_offset for x in kn_rest_5_ts]
# kn_rest_6_ts = [x - kn_start_time + align_offset for x in kn_rest_6_ts]

# ----------------------------------------------- #
# -------------- FIGURE PLOT -------------------- #
# ----------------------------------------------- #
figsize = 5, 3

figure, ax = plt.subplots(figsize=figsize)

# timestamps = [x for x in range(1 + align_offset, len(rest_1_d) + 1 + align_offset, 1)]
p11 = plt.plot(grpc_rest_1_ts, grpc_rest_1_d, marker = '.', ms = 4, mew = 1, label = '', linewidth=2.5, linestyle=" ", color='tab:blue')
p12 = plt.plot(grpc_rest_2_ts, grpc_rest_2_d, marker = '.', ms = 4, mew = 1, label = '', linewidth=2.5, linestyle=" ", color='limegreen')
p13 = plt.plot(grpc_rest_3_ts, grpc_rest_3_d, marker = '.', ms = 4, mew = 1, label = '', linewidth=2.5, linestyle=" ", color='tab:red')
p14 = plt.plot(grpc_rest_4_ts, grpc_rest_4_d, marker = '.', ms = 4, mew = 1, label = '', linewidth=2.5, linestyle=" ", color='#D4996A')
p15 = plt.plot(grpc_rest_5_ts, grpc_rest_5_d, marker = '.', ms = 4, mew = 1, label = '', linewidth=2.5, linestyle=" ", color='#FDA8AA')
p16 = plt.plot(grpc_rest_6_ts, grpc_rest_6_d, marker = '.', ms = 4, mew = 1, label = '', linewidth=2.5, linestyle=" ", color='#555CB5')

# p21 = plt.plot(kn_rest_1_ts, kn_rest_1_d, marker = 'x', ms = 4, mew = 1, label = '', linewidth=2.5, linestyle=" ", color='tab:blue')
# p22 = plt.plot(kn_rest_2_ts, kn_rest_2_d, marker = 'x', ms = 4, mew = 1, label = '', linewidth=2.5, linestyle=" ", color='limegreen')
# p23 = plt.plot(kn_rest_3_ts, kn_rest_3_d, marker = 'x', ms = 4, mew = 1, label = '', linewidth=2.5, linestyle=" ", color='tab:red')
# p24 = plt.plot(kn_rest_4_ts, kn_rest_4_d, marker = 'x', ms = 4, mew = 1, label = '', linewidth=2.5, linestyle=" ", color='#552600')
# p25 = plt.plot(kn_rest_5_ts, kn_rest_5_d, marker = 'x', ms = 4, mew = 1, label = '', linewidth=2.5, linestyle=" ", color='#FDA8AA')
# p26 = plt.plot(kn_rest_6_ts, kn_rest_6_d, marker = 'x', ms = 4, mew = 1, label = '', linewidth=2.5, linestyle=" ", color='#555CB5')


plt.tick_params(grid_linewidth = 3, grid_linestyle = ':', pad=0)
figure.subplots_adjust(bottom=0.25, left=0.2)
# plt.xticks(ind, ('0', '10','50','100','200','400'))
plt.setp(ax.get_xticklabels(), 
  rotation=lrotation, 
  ha="center",
  rotation_mode="anchor")

# plt.grid(True)
plt.grid(color = 'gray', linestyle = ':', linewidth = 1)
plt.ylim((0, 1100))
plt.xlim((0, 160))
plt.yticks(np.arange(0, 1000.1, 200), ['0', '200', '400', '600', '800', '1k'], rotation = 45)
plt.ylabel('Response time (ms)', labelpad = 0)
plt.xlabel('(e) timestamp (second)', labelpad=0)

prop = dict(size=10)
plt.legend((p11[0], p12[0], p13[0],p14[0], p15[0], p16[0]), 
  ('gRPC: Ch-1', 'gRPC: Ch-2','gRPC: Ch-3', 'gRPC: Ch-4', 'gRPC: Ch-5','gRPC: Ch-6'),
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
plt.savefig('fig-10-e.png' ,bbox_inches='tight', dpi=400, pad_inches=0.01)
