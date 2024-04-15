# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 10:34:24 2024

@author: a107283
"""

import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np
import matplotlib.image as mpimg
import matplotlib.patheffects as pe

Data = pd.read_csv('SP500_2019_2024.csv')
Data['Date'] = pd.to_datetime(Data['Date'])

#%% static
S = 22
lw=1.5
plt.rcParams["font.size"] = S
plt.rcParams.update({'mathtext.default':  'regular' ,"ytick.color" : "k",
          "xtick.color" : "k",
          "axes.labelcolor" : "k",
          "axes.edgecolor" : "k",
          "font.sans-serif" : 'arial'})

plt.close()
plt.rcParams['figure.dpi'] = 200
fig, ax = plt.subplots(figsize=(10,6))
fign='Figure'


plt.plot(Data['Date'],Data['Value']/1000,lw=lw*2.5)

ax.set_yticks(np.arange(2.5,5,0.5))

ax.set_yticklabels(['2.5K','3.0K','3.5K','4.0K','4.5K'])



plt.xlim(datetime.date(2019, 1, 1),datetime.date(2024, 1, 1))
plt.ylim(2.109442, 4.924518000000001)
plt.ylabel('S&P 500 Value [$]')
plt.xlabel('Year')
ax.set_axisbelow(True)
ax.tick_params(axis="both",direction="in",bottom=True, top=True, left=True, right=True,width=lw,length=lw*3)

plt.grid(which='major',lw=lw/2)

ax.spines[['right','top','bottom','left']].set_linewidth(lw)

fig.tight_layout(pad=0.25)
plt.savefig(fign)

#%% create frames

S = 22
lw=1.5
plt.rcParams["font.size"] = S
plt.rcParams.update({'mathtext.default':  'regular' ,"ytick.color" : "k",
          "xtick.color" : "k",
          "axes.labelcolor" : "k",
          "axes.edgecolor" : "k",
          "font.sans-serif" : 'arial'})
plt.rcParams['figure.dpi'] = 200


plt.ioff()


for i in range(0,len(Data)):
    plt.close()
    fig, ax = plt.subplots(figsize=(10,6))
    fign='Figure000'
    
    plt.plot(Data['Date'][0:i],Data['Value'][0:i]/1000,lw=lw*2.5)
    ax.set_yticks(np.arange(2.5,5,0.5))
    ax.set_yticklabels(['2.5K','3.0K','3.5K','4.0K','4.5K'])
    
    plt.xlim(datetime.date(2019, 1, 1),datetime.date(2024, 1, 1))
    plt.ylim(2.109442, 4.924518000000001)
    plt.ylabel('S&P 500 Value [$]')
    plt.xlabel('Year')
    ax.set_axisbelow(True)
    ax.tick_params(axis="both",direction="in",bottom=True, top=True, left=True, right=True,width=lw,length=lw*3)
    plt.grid(which='major',lw=lw/2)
    
    ax.spines[['right','top','bottom','left']].set_linewidth(lw)

    
    fig.tight_layout(pad=0.25)
    plt.savefig('Frames/'+fign+str(i))


plt.ion()

#%% create frames styled

S = 22
lw=1.5
plt.rcParams["font.size"] = S
plt.rcParams.update({'mathtext.default':  'regular' ,"ytick.color" : "k",
          "xtick.color" : "k",
          "axes.labelcolor" : "k",
          "axes.edgecolor" : "k",
          "font.sans-serif" : 'arial'})
plt.rcParams['figure.dpi'] = 200


plt.ioff()
# for i in range(0,len(Data)):
for i in range(0,len(Data)):

    plt.close()
    fig, ax = plt.subplots(figsize=(10,6))
    fign='Figure000'
    
    
    plt.plot(Data['Date'][0:i],Data['Value'][0:i]/1000,lw=lw*2.5)
    plt.plot([Data['Date'].min(),Data['Date'].max()],[Data['Value'][i]/1000,Data['Value'][i]/1000],color='k',lw=lw,linestyle='--')
    plt.plot([Data['Date'][i],Data['Date'][i]],[2,5],color='k',lw=lw,linestyle='--')
    plt.scatter(Data['Date'][i],Data['Value'][i]/1000,color='gray',edgecolor='k',zorder=100,s=100)
    
    if Data['Date'][i].year<=2020:
        plt.text(Data['Date'][i]+ datetime.timedelta(weeks=2),Data['Value'][i]/1000+0.05,Data['Date'][i].strftime("%b %Y")+'\n'+'$'+str('{0:.2f}'.format(round(Data['Value'][i]/1000,2)))+'K',fontweight='bold',c='gray',path_effects=[pe.withStroke(linewidth=lw*2, foreground="k")])
    else:
        plt.text(Data['Date'][i]- datetime.timedelta(weeks=43),Data['Value'][i]/1000-0.33,Data['Date'][i].strftime("%b %Y")+'\n'+'$'+str('{0:.2f}'.format(round(Data['Value'][i]/1000,2)))+'K',fontweight='bold',c='gray',path_effects=[pe.withStroke(linewidth=lw*2, foreground="k")])
        
    ax.set_yticks(np.arange(2.5,5,0.5))
    
    ax.set_yticklabels(['2.5K','3.0K','3.5K','4.0K','4.5K'])
    
    
    
    plt.xlim(datetime.date(2019, 1, 1),datetime.date(2024, 1, 1))
    plt.ylim(2.109442, 4.924518000000001)
    plt.ylabel('S&P 500 Value [$]')
    plt.xlabel('Year')
    ax.set_axisbelow(True)
    ax.tick_params(axis="both",direction="in",bottom=True, top=True, left=True, right=True,width=lw,length=lw*3)
    
    plt.grid(which='major',lw=lw/2)
    plt.grid(which='minor',linestyle='--',lw=lw/3)
    
    ax.spines['right'].set_linewidth(lw)
    ax.spines['top'].set_linewidth(lw)
    ax.spines['bottom'].set_linewidth(lw)
    ax.spines['left'].set_linewidth(lw)
    
    
    fig.tight_layout(pad=0.25)
    plt.savefig('FramesS/'+fign+str(i))
    print(i/len(Data))



plt.ion()
#%% check resolution

import matplotlib.image as mpimg
img=mpimg.imread('Figure.png')
print(img.shape)


