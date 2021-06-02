import sys
import os
import numpy as np
from numpy.random import choice, randn, uniform
from tools.config import conf, load_config
import pandas as pd

class PARMAN:

    def __init__(self):
        self.get_ordered_free_params()


    def get_ordered_free_params(self):
        self.par=[]
        self.order=[]
        self.pmin=[]
        self.pmax=[]

        if 'check lims' not in conf: conf['check lims']=False

        for k in conf['params']:
            for kk in conf['params'][k]:
                if  conf['params'][k][kk]['fixed']==False:
                    p=conf['params'][k][kk]['value']
                    pmin=conf['params'][k][kk]['min']
                    pmax=conf['params'][k][kk]['max']
                    self.pmin.append(pmin)
                    self.pmax.append(pmax)
                    if p<pmin or p>pmax:
                       if conf['check lims']: raise ValueError('par limits are not consistent with central: %s %s'%(k,kk))

                    self.par.append(p)
                    self.order.append([1,k,kk])

        if 'datasets' in conf:
            for k in conf['datasets']:
                for kk in conf['datasets'][k]['norm']:
                    if  conf['datasets'][k]['norm'][kk]['fixed']==False:
                        p=conf['datasets'][k]['norm'][kk]['value']
                        pmin=conf['datasets'][k]['norm'][kk]['min']
                        pmax=conf['datasets'][k]['norm'][kk]['max']
                        self.pmin.append(pmin)
                        self.pmax.append(pmax)
                        if p<pmin or p>pmax:
                           if conf['check lims']: raise ValueError('par limits are not consistend with central: %s %s'%(k,kk))
                        self.par.append(p)
                        self.order.append([2,k,kk])

        self.pmin=np.array(self.pmin)
        self.pmax=np.array(self.pmax)
        self.par=np.array(self.par)
        self.set_new_params(self.par,initial=True)

    def gen_flat(self,setup=True):
        r=uniform(0,1,len(self.par))
        par=self.pmin + r * (self.pmax-self.pmin)
        if setup: self.set_new_params(par,initial=True)
        return par
        #while 1:
        #  r=uniform(0,1,len(self.par))
        #  par=self.pmin + r * (self.pmax-self.pmin)
        #  self.set_new_params(par,initial=True)
        #  flag=False
        #  if 'pdf' in conf and conf['pdf'].params['g1'][0]<0: flag=True
        #  if 'pdf' in conf and conf['pdf'].params['s1'][0]<0: flag=True
        #  if flag==False: break
        #return par

    def check_lims(self):
        flag=True
        for k in conf['params']:
            for kk in conf['params'][k]:
                if  conf['params'][k][kk]['fixed']==False:
                    p=conf['params'][k][kk]['value']
                    pmin=conf['params'][k][kk]['min']
                    pmax=conf['params'][k][kk]['max']
                    if  p<pmin or p>pmax:
                        print(k,kk, p,pmin,pmax)
                        flag=False

        if  'datasets' in conf:
            for k in conf['datasets']:
                for kk in conf['datasets'][k]['norm']:
                    if  conf['datasets'][k]['norm'][kk]['fixed']==False:
                        p=conf['datasets'][k]['norm'][kk]['value']
                        pmin=conf['datasets'][k]['norm'][kk]['min']
                        pmax=conf['datasets'][k]['norm'][kk]['max']
                        if p<pmin or p>pmax:
                          flag=False
                          print(k,kk, p,pmin,pmax)

        return flag

    def set_new_params(self,parnew,initial=False):
        self.par=parnew
        self.shifts=0
        semaphore={}

        for i in range(len(self.order)):
            ii,k,kk=self.order[i]
            if  ii==1:
                if k not in semaphore: semaphore[k]=0
                if conf['params'][k][kk]['value']!=parnew[i]:
                  conf['params'][k][kk]['value']=parnew[i]
                  semaphore[k]=1
                  self.shifts+=1
            elif ii==2:
                if conf['datasets'][k]['norm'][kk]['value']!=parnew[i]:
                  conf['datasets'][k]['norm'][kk]['value']=parnew[i]
                  self.shifts+=1

        if  initial:
            for k in conf['params']: semaphore[k]=1

        #--This is needed so the pion widths get updated
        #--when they are set equal to the proton widths
        if semaphore['pdf']==1 and 'pdfpi-' in conf['params']: semaphore['pdfpi-']=1

        self.propagate_params(semaphore)

    def gen_report(self):
        L=[]
        cnt=0
        for k in conf['params']:
            for kk in sorted(conf['params'][k]):
                if  conf['params'][k][kk]['fixed']==False:
                    cnt+=1
                    if  conf['params'][k][kk]['value']<0:
                        L.append('%d %10s  %10s  %10.5e'%(cnt,k,kk,conf['params'][k][kk]['value']))
                    else:
                        L.append('%d %10s  %10s   %10.5e'%(cnt,k,kk,conf['params'][k][kk]['value']))

        for k in conf['datasets']:
            for kk in conf['datasets'][k]['norm']:
                if  conf['datasets'][k]['norm'][kk]['fixed']==False:
                    cnt+=1
                    L.append('%d %10s %10s %10d  %10.5e'%(cnt,'norm',k,kk,conf['datasets'][k]['norm'][kk]['value']))
        return L

    def propagate_params(self,semaphore):

      if 'version' in conf: version=conf['version']
      else: version=0 #--for back compatibility

      flag=False
      if 'pdf'          in semaphore and semaphore['pdf']          == 1: self.set_pdf_params()
      if 'pdfpi-'       in semaphore and semaphore['pdfpi-']       == 1: self.set_pdfpi_params()
      if 'transversity' in semaphore and semaphore['transversity'] == 1: self.set_transversity_params(version)
      if 'sivers'       in semaphore and semaphore['sivers']       == 1: self.set_sivers_params(version)
      if 'boermulders'  in semaphore and semaphore['boermulders']  == 1: self.set_boermulders_params(version)
      if 'ffpi'         in semaphore and semaphore['ffpi']         == 1: self.set_ffpi_params()
      if 'ffk'          in semaphore and semaphore['ffk']          == 1: self.set_ffk_params()
      if 'ffh'          in semaphore and semaphore['ffh']          == 1: self.set_ffh_params()
      if 'collinspi'    in semaphore and semaphore['collinspi']    == 1: self.set_collinspi_params(version)
      if 'collinsk'     in semaphore and semaphore['collinsk']     == 1: self.set_collinsk_params(version)
      if 'Htildepi'     in semaphore and semaphore['Htildepi']     == 1: self.set_Htildepi_params(version)
      if 'Htildek'      in semaphore and semaphore['Htildek']      == 1: self.set_Htildek_params(version)

    def set_constraits(self,dist,FLAV=None,PAR=None,version=0):

        if (dist in ['pdf','pdfpi-','ffpi','ffk']) or (version==0):
            parkind=dist
            for k in conf['params'][parkind]:
                if conf['params'][parkind][k]['fixed'] == True:  continue
                elif conf['params'][parkind][k]['fixed'] == False: continue
                elif 'proton widths uv' in conf['params'][parkind][k]['fixed']:
                    conf['params'][parkind][k]['value'] = conf['params']['pdf']['widths1_uv']['value']
                elif 'proton widths sea' in conf['params'][parkind][k]['fixed']:
                    conf['params'][parkind][k]['value'] = conf['params']['pdf']['widths1_sea']['value']
                else:
                    ref_par = conf['params'][parkind][k]['fixed']
                    conf['params'][parkind][k]['value'] = conf['params'][parkind][ref_par]['value']

        elif version=='JAM20+':
            for flav in FLAV:
                for par in PAR:
                    for s in ['1','2']:
                        if flav+' '+par+' '+s not in conf['params'][dist]: continue
                        if conf['params'][dist][flav+' '+par+' '+s]['fixed']==True: continue
                        if conf['params'][dist][flav+' '+par+' '+s]['fixed']==False: continue
                        reference_flav=conf['params'][dist][flav+' '+par+' '+s]['fixed']
                        conf['params'][dist][flav+' '+par+' '+s]['value']=conf['params'][dist][reference_flav]['value']

    def set_params(self,dist,FLAV,PAR,version):

        if version==0:
            iflav=0
            for flav in FLAV:
                iflav+=1
                ipar=-1
                for par in PAR:
                    ipar+=1
                    if '%s %s 1'%(flav,par) in conf['params'][dist]:
                        conf[dist].shape1[iflav][ipar] = conf['params'][dist]['%s %s 1'%(flav,par)]['value']
                        if 'd'+dist in conf: conf['d'+dist].shape1[iflav][ipar] = conf['params'][dist]['%s %s 1'%(flav,par)]['value']
                    if '%s %s 2'%(flav,par) in conf['params'][dist]:
                        conf[dist].shape2[iflav][ipar] = conf['params'][dist]['%s %s 2'%(flav,par)]['value']
                        if 'd'+dist in conf: conf['d'+dist].shape2[iflav][ipar] = conf['params'][dist]['%s %s 2'%(flav,par)]['value']

            conf[dist].setup()

        elif version=='JAM20+':
            #--update values at the class
            for flav in FLAV:
                idx=0
                for s in ['1','2']:
                    for par in PAR:
                        if  flav+' '+par+' '+s in conf['params'][dist]:
                            conf[dist].params[flav][idx]=conf['params'][dist][flav+' '+par+' '+s]['value']
                        else:
                            conf[dist].params[flav][idx]=0
                        idx+=1

            conf[dist].setup()

            #--update values at conf
            for flav in FLAV:
                idx=0
                for s in ['1','2']:
                    for par in PAR:
                        if  flav+' '+par+' '+s in conf['params'][dist]:
                            conf['params'][dist][flav+' '+par+' '+s]['value']= conf[dist].params[flav][idx]
                        idx+=1


    def set_pdf_params(self):
        self.set_constraits('pdf')
        hadron='p'
        conf['pdf']._widths1_uv  = conf['params']['pdf']['widths1_uv' ]['value']
        conf['pdf']._widths1_dv  = conf['params']['pdf']['widths1_dv' ]['value']
        conf['pdf']._widths1_sea = conf['params']['pdf']['widths1_sea']['value']
        conf['pdf']._widths2_uv  = conf['params']['pdf']['widths2_uv' ]['value']
        conf['pdf']._widths2_dv  = conf['params']['pdf']['widths2_dv' ]['value']
        conf['pdf']._widths2_sea = conf['params']['pdf']['widths2_sea']['value']
        conf['pdf'].setup(hadron)

    def set_pdfpi_params(self):
        self.set_constraits('pdfpi-')
        hadron='pi-'
        conf['pdfpi-']._widths1_ubv = conf['params']['pdfpi-']['widths1_ubv' ]['value']
        conf['pdfpi-']._widths1_dv  = conf['params']['pdfpi-']['widths1_dv' ]['value']
        conf['pdfpi-']._widths1_sea = conf['params']['pdfpi-']['widths1_sea']['value']
        conf['pdfpi-']._widths2_ubv = conf['params']['pdfpi-']['widths2_ubv' ]['value']
        conf['pdfpi-']._widths2_dv  = conf['params']['pdfpi-']['widths2_dv' ]['value']
        conf['pdfpi-']._widths2_sea = conf['params']['pdfpi-']['widths2_sea']['value']
        conf['pdfpi-'].setup(hadron)

    def set_transversity_params(self,version):
        self.set_constraits('transversity')
        conf['transversity']._widths1_uv  = conf['params']['transversity']['widths1_uv']['value']
        conf['transversity']._widths1_dv  = conf['params']['transversity']['widths1_dv']['value']
        conf['transversity']._widths1_sea = conf['params']['transversity']['widths1_sea']['value']

        conf['transversity']._widths2_uv  = conf['params']['transversity']['widths2_uv']['value']
        conf['transversity']._widths2_dv  = conf['params']['transversity']['widths2_dv']['value']
        conf['transversity']._widths2_sea = conf['params']['transversity']['widths2_sea']['value']

        if version == 0:
            FLAV = ['u','ub','d','db','s','sb']
            PAR = ['N0','a0','b0','c0','d0','N1','a1','b1','c1','d1']
            dist='transversity'
            self.set_constraits(dist,FLAV,PAR,version)
            self.set_params(dist,FLAV,PAR,version)

        if version == 'JAM20+':
            FLAV=['g1','uv1','dv1','sea1','sea2','db1','ub1','s1','sb1']
            PAR=['N','a','b','c','d']
            dist='transversity'
            self.set_constraits(dist,FLAV,PAR,version)
            self.set_params(dist,FLAV,PAR,version)

    def set_sivers_params(self,version):
        self.set_constraits('sivers')
        conf['sivers']._widths1_uv  = conf['params']['sivers']['widths1_uv']['value']
        conf['sivers']._widths1_dv  = conf['params']['sivers']['widths1_dv']['value']
        conf['sivers']._widths1_sea = conf['params']['sivers']['widths1_sea']['value']

        conf['sivers']._widths2_uv  = conf['params']['sivers']['widths2_uv']['value']
        conf['sivers']._widths2_dv  = conf['params']['sivers']['widths2_dv']['value']
        conf['sivers']._widths2_sea = conf['params']['sivers']['widths2_sea']['value']

        if version == 0:
            FLAV = ['u','ub','d','db','s','sb']
            PAR = ['N0','a0','b0','c0','d0','N1','a1','b1','c1','d1']
            dist='sivers'
            self.set_constraits(dist,FLAV,PAR,version)
            self.set_params(dist,FLAV,PAR,version)

        if version == 'JAM20+':
            FLAV=['g1','uv1','dv1','sea1','sea2','db1','ub1','s1','sb1']
            PAR=['N','a','b','c','d']
            dist='sivers'
            self.set_constraits(dist,FLAV,PAR,version)
            self.set_params(dist,FLAV,PAR,version)
            conf['dsivers'].BC3=conf['sivers'].BC3
            conf['dsivers'].BC4=conf['sivers'].BC4
            conf['dsivers'].BC5=conf['sivers'].BC5
            conf['dsivers'].storage={}

    def set_boermulders_params(self,version):
        self.set_constraits('boermulders')
        conf['boermulders']._widths1_uv  = conf['params']['boermulders']['widths1_uv']['value']
        conf['boermulders']._widths1_dv  = conf['params']['boermulders']['widths1_dv']['value']
        conf['boermulders']._widths1_sea = conf['params']['boermulders']['widths1_sea']['value']

        conf['boermulders']._widths2_uv  = conf['params']['boermulders']['widths2_uv']['value']
        conf['boermulders']._widths2_dv  = conf['params']['boermulders']['widths2_dv']['value']
        conf['boermulders']._widths2_sea = conf['params']['boermulders']['widths2_sea']['value']

        if version == 0:
            FLAV = ['u','ub','d','db','s','sb']
            PAR = ['N0','a0','b0','c0','d0','N1','a1','b1','c1','d1']
            dist='boermulders'
            self.set_constraits(dist,FLAV,PAR,version)
            self.set_params(dist,FLAV,PAR,version)

        if version == 'JAM20+':
            FLAV=['g1','uv1','dv1','sea1','sea2','db1','ub1','s1','sb1']
            PAR=['N','a','b','c','d']
            dist='boermulders'
            self.set_constraits(dist,FLAV,PAR,version)
            self.set_params(dist,FLAV,PAR,version)

    def set_ffpi_params(self):
        self.set_constraits('ffpi')
        conf['ffpi']._widths1_fav  = conf['params']['ffpi']['widths1_fav']['value']
        conf['ffpi']._widths1_ufav = conf['params']['ffpi']['widths1_ufav']['value']
        conf['ffpi']._widths2_fav  = conf['params']['ffpi']['widths2_fav']['value']
        conf['ffpi']._widths2_ufav = conf['params']['ffpi']['widths2_ufav']['value']
        conf['ffpi'].setup()

    def set_ffk_params(self):
        self.set_constraits('ffk')
        conf['ffk']._widths1_fav   = conf['params']['ffk']['widths1_fav']['value']
        conf['ffk']._widths1_ufav  = conf['params']['ffk']['widths1_ufav']['value']
        conf['ffk']._widths2_fav   = conf['params']['ffk']['widths2_fav']['value']
        conf['ffk']._widths2_ufav  = conf['params']['ffk']['widths2_ufav']['value']
        conf['ffk'].setup()

    def set_ffh_params(self):
        self.set_constraits('ffh')
        conf['ffh']._widths1_fav   = conf['params']['ffh']['widths1_fav']['value']
        conf['ffh']._widths1_ufav  = conf['params']['ffh']['widths1_ufav']['value']
        conf['ffh']._widths2_fav   = conf['params']['ffh']['widths2_fav']['value']
        conf['ffh']._widths2_ufav  = conf['params']['ffh']['widths2_ufav']['value']
        conf['ffh'].setup()

    def set_collinspi_params(self,version):
        self.set_constraits('collinspi')
        conf['collinspi']._widths1_fav  = conf['params']['collinspi']['widths1_fav']['value']
        conf['collinspi']._widths1_ufav = conf['params']['collinspi']['widths1_ufav']['value']
        conf['collinspi']._widths2_fav  = conf['params']['collinspi']['widths2_fav']['value']
        conf['collinspi']._widths2_ufav = conf['params']['collinspi']['widths2_ufav']['value']

        if version == 0:
            FLAV = ['u','ub','d','db','s','sb']
            PAR = ['N0','a0','b0','c0','d0','N1','a1','b1','c1','d1']
            dist='collinspi'
            self.set_constraits(dist,FLAV,PAR,version)
            self.set_params(dist,FLAV,PAR,version)

        if version == 'JAM20+':
            FLAV=['g1','u1','d1','s1','c1','b1','ub1','db1','sb1','cb1','bb1']
            PAR=['N','a','b','c','d']
            dist='collinspi'
            self.set_constraits(dist,FLAV,PAR,version)
            self.set_params(dist,FLAV,PAR,version)
            conf['dcollinspi'].BC3=conf['collinspi'].BC3
            conf['dcollinspi'].BC4=conf['collinspi'].BC4
            conf['dcollinspi'].BC5=conf['collinspi'].BC5
            conf['dcollinspi'].storage={}

    def set_collinsk_params(self):
        self.set_constraits('collinsk')
        conf['collinsk']._widths1_fav   = conf['params']['collinsk']['widths1_fav']['value']
        conf['collinsk']._widths1_ufav  = conf['params']['collinsk']['widths1_ufav']['value']
        conf['collinsk']._widths2_fav   = conf['params']['collinsk']['widths2_fav']['value']
        conf['collinsk']._widths2_ufav  = conf['params']['collinsk']['widths2_ufav']['value']

        if version == 0:
            FLAV = ['u','ub','d','db','s','sb']
            PAR = ['N0','a0','b0','c0','d0','N1','a1','b1','c1','d1']
            dist='collinsk'
            self.set_constraits(dist,FLAV,PAR,version)
            self.set_params(dist,FLAV,PAR,version)

        if version == 'JAM20+':
            FLAV=['g1','u1','d1','s1','c1','b1','ub1','db1','sb1','cb1','bb1']
            PAR=['N','a','b','c','d']
            dist='collinsk'
            self.set_constraits(dist,FLAV,PAR,version)
            self.set_params(dist,FLAV,PAR,version)

    def set_Htildepi_params(self,version):
        self.set_constraits('Htildepi')
        conf['Htildepi']._widths1_fav  = conf['params']['Htildepi']['widths1_fav']['value']
        conf['Htildepi']._widths1_ufav = conf['params']['Htildepi']['widths1_ufav']['value']
        conf['Htildepi']._widths2_fav  = conf['params']['Htildepi']['widths2_fav']['value']
        conf['Htildepi']._widths2_ufav = conf['params']['Htildepi']['widths2_ufav']['value']

        if version == 0:
            FLAV = ['u','ub','d','db','s','sb']
            PAR = ['N0','a0','b0','c0','d0','N1','a1','b1','c1','d1']
            dist='Htildepi'
            self.set_constraits(dist,FLAV,PAR,version)
            self.set_params(dist,FLAV,PAR,version)

        if version == 'JAM20+':
            FLAV=['g1','u1','d1','s1','c1','b1','ub1','db1','sb1','cb1','bb1']
            PAR=['N','a','b','c','d']
            dist='Htildepi'
            self.set_constraits(dist,FLAV,PAR,version)
            self.set_params(dist,FLAV,PAR,version)

    def set_Htildek_params(self,version):
        self.set_constraits('Htildek')
        conf['Htildek']._widths1_fav   = conf['params']['Htildek']['widths1_fav']['value']
        conf['Htildek']._widths1_ufav  = conf['params']['Htildek']['widths1_ufav']['value']
        conf['Htildek']._widths2_fav   = conf['params']['Htildek']['widths2_fav']['value']
        conf['Htildek']._widths2_ufav  = conf['params']['Htildek']['widths2_ufav']['value']

        if version == 0:
            FLAV = ['u','ub','d','db','s','sb']
            PAR = ['N0','a0','b0','c0','d0','N1','a1','b1','c1','d1']
            dist='Htildek'
            self.set_constraits(dist,FLAV,PAR,version)
            self.set_params(dist,FLAV,PAR,version)

        if version == 'JAM20+':
            FLAV=['g1','u1','d1','s1','c1','b1','ub1','db1','sb1','cb1','bb1']
            PAR=['N','a','b','c','d']
            dist='Htildek'
            self.set_constraits(dist,FLAV,PAR,version)
            self.set_params(dist,FLAV,PAR,version)
