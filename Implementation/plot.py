import seaborn as sns
import pandas as pd
from matplotlib import style
from matplotlib import pyplot as plt
import numpy as np

def plot_stuff(type, xmeas, X_train_extracted_data, dtrg_scores, dt_scores, dj_scores, dt_theta, L, title):
    if(type==1):
        style.use('default')
        box = dict(facecolor='yellow', pad=3, alpha=0.2)
        fig = plt.figure(figsize=(15,7))
        ax1 = fig.add_subplot(211)
        ax2 = fig.add_subplot(212)

        ax1.set_xlim(0,len(xmeas) + 100)
        ax2.set_xlim(0,len(xmeas) + 100)

        plt.subplots_adjust(hspace=0.3)

        xlables = list(range(0, len(xmeas) + 100, 1000))

        xmeasx_1 = list(range(501))
        xmeasx_2 = list(range(501, 2001))
        xmeasx_3 = list(range(2001,len(xmeas)))
        ax1.plot(xmeasx_1, xmeas[:501] ,'b', label='Initial Phase') 
        ax1.plot(xmeasx_2, xmeas[501:2001] ,'k', label='Threshold calculation') 
        ax1.plot(xmeasx_3, xmeas[2001:] ,'r', label='Detection')
        ax1.plot(X_train_extracted_data, 'g', linewidth=1, label='Extracted Signal' )
        ax1.set_xticklabels(xlables)
        ax1.title.set_text(title)
        ax1.set_ylabel('Sensor Reading', bbox=box)
        ylim = list(ax1.get_ylim())
        ax1.vlines(2000,ylim[0],ylim[1],linestyles='dashed', colors='r')
        X = np.array([[2000, len(xmeas) + 100],[2000, len(xmeas) + 100]])
        Y = np.array([[ylim[0],ylim[0]],[ylim[1],ylim[1]]])
        C = np.array([[2000]])
        print(X.shape, Y.shape, C.shape)
        ax1.pcolormesh(X, Y, C, cmap='cool_r', alpha=0.2)
        ax1.legend(loc='best', ncol=4)

        dy = dtrg_scores
        dx = list(range(L,len(dy)+L))
        ax2.plot(dx, dy, 'b', label='Initial Phase')
        dy = dt_scores
        dx = list(range(500,len(dy)+500))
        ax2.plot(dx, dy, 'k', label='Threshold calculation')
        dy = dj_scores
        dx = list(range(2000,len(dy)+2000))
        ax2.plot(dx, dy, 'r', label='Detection Phase')
        ylim = list(ax2.get_ylim())
        ax2.vlines(2000,ylim[0],ylim[1],linestyles='dashed', colors='r')
        ax2.set_xticklabels(xlables)
        ax2.hlines(dt_theta,0,len(xmeas) + 100,linestyles='dashed', label='Alarm Threshold')
        ax2.set_xlabel('Data points', bbox=box)
        ax2.set_ylabel('Departure Score', bbox=box)

        X = np.array([[2000, len(xmeas) + 100],[2000, len(xmeas) + 100]])
        Y = np.array([[ylim[0],ylim[0]],[ylim[1],ylim[1]]])
        C = np.array([[2000]])
        ax2.pcolormesh(X, Y, C, cmap='cool_r', alpha=0.2)
        ax2.legend(loc='upper left')
        fig.align_ylabels([ax1,ax2])
    elif(type==2):
        style.use('default')
        box = dict(facecolor='yellow', pad=3, alpha=0.2)
        fig = plt.figure(figsize=(15,7))
        ax1 = fig.add_subplot(211)
        ax2 = fig.add_subplot(212)

        ax1.set_xlim(0,len(xmeas) + 100)
        ax2.set_xlim(0,len(xmeas) + 100)

        plt.subplots_adjust(hspace=0.3)

        xlables = list(range(0, len(xmeas) + 100, 100000))

        xmeasx_1 = list(range(10001))
        xmeasx_2 = list(range(10001, 200001))
        xmeasx_3 = list(range(200001, len(xmeas)))
        ax1.plot(xmeasx_1, xmeas[:10001] ,'b', label='Training') 
        ax1.plot(xmeasx_2, xmeas[10001:200001] ,'k', label='Threshold calculation') 
        ax1.plot(xmeasx_3, xmeas[200001:] ,'r', label='Detection')
        ax1.plot(X_train_extracted_data, 'g', linewidth=1, label='Extracted Signal' )
        ax1.set_xticklabels(xlables)
        ax1.title.set_text(title)
        ax1.set_ylabel('Sensor Reading', bbox=box)
        ylim = list(ax1.get_ylim())
        ax1.vlines(200000,ylim[0],ylim[1],linestyles='dashed', colors='r')
        X = np.array([[200000, len(xmeas) + 100],[200000, len(xmeas) + 100]])
        Y = np.array([[ylim[0],ylim[0]],[ylim[1],ylim[1]]])
        C = np.array([[200000]])
        print(X.shape, Y.shape, C.shape)
        ax1.pcolormesh(X, Y, C, cmap='cool_r', alpha=0.2)
        ax1.legend(loc='best', ncol=4)

        dy = dtrg_scores
        dx = list(range(L,len(dy)+L))
        ax2.plot(dx, dy, 'c', label='Training phase')
        dy = dt_scores
        dx = list(range(10000,len(dy)+10000))
        ax2.plot(dx, dy, 'b', label='Threshold calculation')
        dy = dj_scores
        dx = list(range(200000,len(dy)+200000))
        ax2.plot(dx, dy, 'r', label='Detection Phase')
        ylim = list(ax2.get_ylim())
        ax2.vlines(200000,ylim[0],ylim[1],linestyles='dashed', colors='r')
        ax2.set_xticklabels(xlables)
        ax2.hlines(dt_theta,0,len(xmeas) + 100,linestyles='dashed', label='Alarm Threshold')
        ax2.set_xlabel('Time in hours', bbox=box)
        ax2.set_ylabel('Departure Score', bbox=box)

        X = np.array([[200000, len(xmeas) + 100],[200000, len(xmeas) + 100]])
        Y = np.array([[ylim[0],ylim[0]],[ylim[1],ylim[1]]])
        C = np.array([[200000]])
        ax2.pcolormesh(X, Y, C, cmap='cool_r', alpha=0.2)
        ax2.legend(loc='upper left')
        fig.align_ylabels([ax1,ax2])