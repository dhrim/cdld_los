"""CDLD-LoS graphical abstract. Source: final CMPB manuscript, Table 2.
Run with Python and matplotlib; outputs are saved beside this script.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
O=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'none'})
f=plt.figure(figsize=(16,10),facecolor='#F5F8FA'); a=f.add_axes([0,0,1,1]); a.set(xlim=(0,16),ylim=(0,10)); a.axis('off')
ink='#193249'; teal='#007F83'; grey='#607487'; blue='#658BA9'
def t(x,y,s,z=14,c=ink,b=False,ha='left'): a.text(x,y,s,fontsize=z,color=c,weight='bold' if b else 'normal',va='top',ha=ha,linespacing=1.45)
def box(x,y,w,h,c='white'): a.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.02,rounding_size=.16',facecolor=c,edgecolor='#D8E3EA',lw=1))
def ar(x,y,xx,yy,c=grey): a.add_patch(FancyArrowPatch((x,y),(xx,yy),arrowstyle='-|>',mutation_scale=18,color=c,lw=1.8))
t(.65,9.6,'Length-of-stay prediction using physician latent traits',26,b=True)
t(.65,9.03,'MIMIC-IV v3.1  •  294,701 admissions  •  148,239 patients  •  1,807 admitting physicians',13,c=grey)
box(.65,5.65,4.3,2.94)
t(.92,8.34,'01   INTERACTION RECORDS',12,c=teal,b=True)
t(.92,7.84,'Patient ↔ Physician → Length of stay',13,b=True)
# Simple physician glyph, constructed from vector shapes.
a.add_patch(Circle((1.28,7.13),.18,fc=blue,ec='none'))
box(.99,6.40,.58,.48,'#E8EFF4')
a.plot([1.17,1.39],[6.64,6.64],color=teal,lw=2); a.plot([1.28,1.28],[6.53,6.75],color=teal,lw=2)
t(1.86,7.32,'Physician ID available',14,b=True)
t(1.86,6.91,'No observed physician\nattributes',12,c=grey)
t(.92,6.10,'Learn from admissions handled by each physician',10,c=grey)
ar(5.03,7.10,5.5,7.10)
box(5.59,5.65,4.76,2.94,'#E9F3F4')
t(5.85,8.34,'02   CDLD REPRESENTATION LEARNING',11,c=teal,b=True)
t(7.97,7.84,'Patient Latent Finder',16,b=True,ha='center')
t(7.97,7.39,'↕',23,c=teal,ha='center')
t(7.97,6.98,'Physician Latent Finder',16,b=True,ha='center')
t(7.97,6.28,'64-dimensional physician vectors',13,c=teal,b=True,ha='center')
ar(10.43,7.1,10.9,7.1)
box(10.99,5.65,4.36,2.94)
t(11.25,8.34,'03   LENGTH-OF-STAY PREDICTION',11,c=teal,b=True)
t(13.17,7.86,'54 patient features at admission',13,b=True,ha='center')
t(13.17,7.48,'+',18,c=teal,ha='center')
t(13.17,7.11,'Physician latent traits',15,c=teal,b=True,ha='center')
ar(13.17,6.77,13.17,6.40)
t(13.17,6.27,'Predicted length of stay',14,b=True,ha='center')
box(.65,1.62,9.45,3.65)
t(.93,5.02,'PREDICTION ERROR',12,c=teal,b=True)
t(.93,4.62,'Five-fold cross-validation · RMSE in days (lower is better)',12,c=grey)
lo,hi=4.2,4.45; x0,x1=6.2,9.23
for v in [4.2,4.3,4.4]:
 x=x0+(v-lo)/(hi-lo)*(x1-x0)
 a.plot([x,x],[2.14,4.02],c='#E2E8EE',lw=1)
 t(x,1.97,f'{v:.1f}',10,c=grey,ha='center')
rows=[('Patient features',4.387,grey),('+ Physician historical mean',4.300,blue),('+ Shrunk physician historical mean',4.296,blue),('+ Physician latent traits (CDLD)',4.270,teal)]
for i,(label,value,c) in enumerate(rows):
 y=3.87-i*.51
 t(.97,y+.09,label,13,c=c,b=i==3)
 x=x0+(value-lo)/(hi-lo)*(x1-x0)
 a.scatter([x],[y],s=85,c=c,zorder=3)
 t(x+.13,y+.09,f'{value:.3f}',12,c=c,b=True)
box(10.39,1.62,4.96,3.65,'#E9F3F4')
t(10.69,5.02,'ADDING PHYSICIAN LATENT TRAITS',11,c=teal,b=True)
t(10.69,4.49,'0.117 days',29,c=teal,b=True)
t(10.69,3.96,'lower RMSE than patient features alone',11,c=grey)
t(10.69,3.46,'R²   0.048 → 0.098',22,b=True)
t(10.69,2.79,'Combines observed patient features',12)
t(10.69,2.43,'with physician information learned',12)
t(10.69,2.07,'from interaction records.',12)
box(.65,.59,14.7,.72,ink)
t(8,1.08,'Physicians can enter the prediction model even when their attributes are unrecorded.',17,c='white',b=True,ha='center')
t(.69,.37,'CDLD = cyclic dual latent discovery. All comparison rows use the same 54 patient features; point estimates are from manuscript Table 2.',9,c=grey)
for ext in ['png','svg']: f.savefig(O/f'20261004_graphical_abstract.{ext}',dpi=300)
f.savefig(O/'20261004_graphical_abstract_preview.png',dpi=110)
