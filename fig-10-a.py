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

# fileName_grpc = 'grpc/' + concurrency + '/stats.csv'

fileName_kn =  'online_boutique/latency_of_each_req_stats_kn.csv'

figsize = 5, 3

figure, ax = plt.subplots(figsize=figsize)


# ----------------------------------------------- #
# ------- Process Knative data and plot --------- #
# ----------------------------------------------- #
kn_rest_1_d = [] # GET /1
kn_rest_2_d = [] # POST /1/setCurrency
kn_rest_3_d = [] # GET /1/product?
kn_rest_4_d = [] # GET /1/cart
kn_rest_5_d = [] # POST /1/cart?product_id=
kn_rest_6_d = [] # POST /1/cart/checkout?

with open(fileName_kn) as fp:
  line = fp.readline()
  while line:
    line_list = line.split(";")
    if line_list[1] == "GET":

      if line_list[2].find("/product/") != -1:
        kn_rest_3_d.append(float(line_list[3].split("\n")[0]))

      elif line_list[2].find("/cart") != -1:
        kn_rest_4_d.append(float(line_list[3].split("\n")[0]))

      elif line_list[2].find("/") != -1:
        kn_rest_1_d.append(float(line_list[3].split("\n")[0]))

      else:
        print("Unknown (GET) Request Name!")

    elif line_list[1] == "POST":

      if line_list[2].find("/setCurrency") != -1:
        kn_rest_2_d.append(float(line_list[3].split("\n")[0]))

      elif line_list[2].find("/cart/checkout") != -1:
        kn_rest_6_d.append(float(line_list[3].split("\n")[0]))

      elif line_list[2].find("/cart") != -1:
        kn_rest_5_d.append(float(line_list[3].split("\n")[0]))

      else:
        print("Unknown (POST) Request Name!")

    else:
      print("Unknown Request Type!")

    line = fp.readline()
    if len(line) == 0:
      break

percentiles = [x for x in range(10, 101, 1)]
kn_rest_1_p = np.percentile(kn_rest_1_d, percentiles)
kn_rest_2_p = np.percentile(kn_rest_2_d, percentiles)
kn_rest_3_p = np.percentile(kn_rest_3_d, percentiles)
kn_rest_4_p = np.percentile(kn_rest_4_d, percentiles)
kn_rest_5_p = np.percentile(kn_rest_5_d, percentiles)
kn_rest_6_p = np.percentile(kn_rest_6_d, percentiles)

p21 = plt.plot(kn_rest_1_p, percentiles, marker = '', ms = 4, mew = 2, label = '', linewidth=2, linestyle="-.", color='tab:blue')
p22 = plt.plot(kn_rest_2_p, percentiles, marker = '', ms = 4, mew = 2, label = '', linewidth=2, linestyle="-.", color='limegreen')
p23 = plt.plot(kn_rest_3_p, percentiles, marker = '', ms = 4, mew = 2, label = '', linewidth=2, linestyle="-.", color='tab:red')
p24 = plt.plot(kn_rest_4_p, percentiles, marker = '', ms = 2, mew = 2, label = '', linewidth=2, linestyle="-.", color='#D4996A')
p25 = plt.plot(kn_rest_5_p, percentiles, marker = '', ms = 4, mew = 2, label = '', linewidth=2, linestyle="-.", color='#FDA8AA')
p26 = plt.plot(kn_rest_6_p, percentiles, marker = '', ms = 1, mew = 1, label = '', linewidth=2, linestyle="-.", color='#555CB5')


plt.tick_params(grid_linewidth = 3, grid_linestyle = ':', pad=0)
figure.subplots_adjust(bottom=0.25, left=0.2)
# plt.xticks(ind, ('0', '10','50','100','200','400'))
plt.setp(ax.get_xticklabels(), 
  rotation=lrotation, 
  ha="center",
  rotation_mode="anchor")

plt.xlim((0, 1300))
plt.xticks(np.arange(0, 1200, 300))#, ['0', '5k', '10k', '15k', '20k'])

plt.grid(color = 'gray', linestyle = ':', linewidth = 1.5)
plt.ylim((0, 101))
plt.yticks(np.arange(0, 100.001, 20))
plt.ylabel('% of requests', labelpad=-5)
plt.xlabel('(a) Response time CDF (ms)', labelpad=0)

prop = dict(size=11)
plt.legend((p21[0], p22[0], p23[0],p24[0], p25[0], p26[0]), 
  ('Kn: Ch-1', 'Kn: Ch-2','Kn: Ch-3', 'Kn: Ch-4', 'Kn: Ch-5','Kn: Ch-6'),
  loc = "lower right",
  ncol = 1,
  prop = prop,
  borderaxespad = 0,
  frameon = True,
  columnspacing = 0.7,
  labelspacing = 0.1,
  fancybox = False,
  edgecolor = 'black')

plt.tight_layout()
plt.savefig('fig-10-a.pdf' ,bbox_inches='tight',dpi=figure.dpi,pad_inches=0.01)
