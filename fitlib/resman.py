#!/usr/bin/env python
import sys,os
import time
import numpy as np

#--from qcdlib
import qcdlib
from   qcdlib import pdf0,ff0,pdf1,ff1,pdf2,ff2
import qcdlib.aux
import qcdlib.alphaS
import qcdlib.interpolator
import qcdlib.alphaS
import qcdlib.mellin

#--from obslib
import obslib.sidis.residuals
import obslib.sidis.reader
import obslib.sia.residuals
import obslib.sia.reader
import obslib.moments.reader
import obslib.moments.residuals
import obslib.AN_pp.residuals
import obslib.AN_pp.reader
import obslib.AN_ep.residuals
import obslib.AN_ep.reader
import obslib.ANgam_pp.residuals
import obslib.ANgam_pp.reader
import obslib.dy.reader
import obslib.dy.residuals
import obslib.wz.reader
import obslib.wz.residuals
import obslib.Soffer_Bound.reader
import obslib.Soffer_Bound.residuals

#--from fitlib
from fitlib.parman import PARMAN

#--from tools
from tools.tools    import checkdir
from tools.config   import conf,load_config
from tools.parallel import PARALLEL

class RESMAN:

    def __init__(self,nworkers=2,parallel=True,datasets=True):

        self.setup_core()
        self.parman=PARMAN()
        if datasets:

            if 'sidis'   in conf['datasets']: self.setup_sidis()
            if 'sidisEIC'   in conf['datasets']: self.setup_sidisEIC()
            if 'sidisSoLID' in conf['datasets']: self.setup_sidisSoLID()
            if 'sia'     in conf['datasets']: self.setup_sia()
            if 'moments' in conf['datasets']: self.setup_moments()
            if 'AN'      in conf['datasets']: self.setup_AN()
            if 'ANgam'   in conf['datasets']: self.setup_ANgam()
            if 'ANep'    in conf['datasets']: self.setup_ANep()
            if 'dy'      in conf['datasets']: self.setup_dy()
            if 'wz'      in conf['datasets']: self.setup_wz()
            if 'SB'      in conf['datasets']: self.setup_SB()

        if  parallel:
            self.setup_parallel(nworkers)
            self.requests=self.get_requests()

    def setup_core(self):

        conf['aux'] = qcdlib.aux.AUX()
        conf['mellin']= qcdlib.mellin.MELLIN(npts=16)
        conf['alphaS']= qcdlib.alphaS.ALPHAS()

        if 'pdf parametrization' in conf:

            if conf['pdf parametrization']==0: conf['pdf']= pdf0.PDF()
            if conf['pdf parametrization']==1: conf['pdf']= pdf1.PDF()
            if conf['pdf parametrization']==2: conf['pdf']= pdf2.PDF()
            if conf['pdf parametrization']==3: conf['pdf']= pdf3.PDF()

        if 'version' in conf: version=conf['version']
        else: version=0 #--for back compatibility

        if 'pdf'           in conf['params']: conf['pdf']          = pdf0.PDF()
        if 'pdfpi-'        in conf['params']: conf['pdfpi-']       = pdf0.PDF('pi-')
        if 'transversity'  in conf['params']:
            if version == 0:  conf['transversity'] = pdf1.PDF()
            if version == 'JAM20+':  conf['transversity'] = pdf2.PDF('h1')
        if 'sivers'        in conf['params']:
            if version == 0:
                conf['sivers']       = pdf1.PDF()
                conf['dsivers']      = pdf1.PDF('deriv')
            if version == 'JAM20+':
                conf['sivers']       = pdf2.PDF('Siv')
                conf['dsivers']      = pdf2.PDF('Siv','deriv')
        if 'boermulders' in conf['params']:
            if version == 0:
                conf['boermulders']  = pdf1.PDF()
                conf['dboermulders'] = pdf1.PDF('deriv')
            if version == 'JAM20+':
                conf['boermulders']  = pdf2.PDF('BM')
                conf['dboermulders'] = pdf2.PDF('BM','deriv')
        if 'ffpi'          in conf['params']: conf['ffpi']         = ff0.FF('pi')
        if 'ffk'           in conf['params']: conf['ffk']          = ff0.FF('k')
        if 'ffh'           in conf['params']: conf['ffh']          = ff0.FF('h')
        if 'collinspi'     in conf['params']:
            if version == 0:
                conf['collinspi']    = ff1.FF('pi')
                conf['dcollinspi']   = ff1.FF('pi','deriv')
            if version == 'JAM20+':
                conf['collinspi']    = ff2.FF('Col','pi')
                conf['dcollinspi']   = ff2.FF('Col','pi','deriv')
        if 'collinsk'      in conf['params']:
            if version == 0:
                conf['collinsk']     = ff1.FF('k')
                conf['dcollinsk']    = ff1.FF('k','deriv')
            if version == 'JAM20+':
                conf['collinsk']     = ff2.FF('Col','k')
                conf['dcollinsk']    = ff2.FF('Col','k','deriv')
        if 'Htildepi'      in conf['params']:
            if version == 0:
                conf['Htildepi']     = ff1.FF('pi')
            if version == 'JAM20+':
                conf['Htildepi']    = ff2.FF('Col','pi')  # Htilde (using same splitting functions as Collins)
        if 'Htildek'       in conf['params']:
            if version == 0:
                conf['Htildek']      = ff1.FF('k')
            if version == 'JAM20+':
                conf['Htildek']     = ff2.FF('Col','k')  # Htilde (using same splitting functions as Collins)

    def setup_sidis(self):
        conf['sidis tabs']    = obslib.sidis.reader.READER().load_data_sets('sidis')
        self.sidisres = obslib.sidis.residuals.RESIDUALS()

    def setup_sidisEIC(self):
        conf['sidisEIC tabs']  = obslib.sidis.reader.READER().load_data_sets('sidisEIC')
        self.sidisEICres = obslib.sidis.residuals.RESIDUALS('sidisEIC')

    def setup_sidisSoLID(self):
        conf['sidisSoLID tabs']  = obslib.sidis.reader.READER().load_data_sets('sidisSoLID')
        self.sidisSoLIDres = obslib.sidis.residuals.RESIDUALS('sidisSoLID')

    def setup_sia(self):
        conf['sia tabs']    = obslib.sia.reader.READER().load_data_sets('sia')
        self.siares = obslib.sia.residuals.RESIDUALS()

    def setup_AN(self):
        conf['AN tabs']   = obslib.AN_pp.reader.READER().load_data_sets('AN')
        self.ANres = obslib.AN_pp.residuals.RESIDUALS()

    def setup_ANep(self):
        conf['ANep tabs']   = obslib.AN_ep.reader.READER().load_data_sets('ANep')
        self.ANepres = obslib.AN_ep.residuals.RESIDUALS()

    def setup_ANgam(self):
        conf['ANgam tabs']   = obslib.ANgam_pp.reader.READER().load_data_sets('ANgam')
        self.ANgamres = obslib.ANgam_pp.residuals.RESIDUALS()

    def setup_dy(self):
        conf['dy tabs']   = obslib.dy.reader.READER().load_data_sets('dy')
        self.dyres = obslib.dy.residuals.RESIDUALS()

    def setup_wz(self):
        conf['wz tabs']   = obslib.wz.reader.READER().load_data_sets('wz')
        self.wzres = obslib.wz.residuals.RESIDUALS()

    def setup_SB(self):
        conf['SB tabs']   = obslib.Soffer_Bound.reader.READER().load_data_sets('SB')
        self.SBres = obslib.Soffer_Bound.residuals.RESIDUALS()

    def setup_moments(self):
        conf['moments tabs']   = obslib.moments.reader.READER().load_data_sets('moments')
        self.momentsres = obslib.moments.residuals.RESIDUALS()

    def setup_parallel(self,nworkers):
        self.parallel=PARALLEL()
        self.parallel.task=self.task
        self.parallel.set_state=self.set_state
        self.parallel.setup_master()
        self.parallel.setup_workers(nworkers)
        self.nworkers=nworkers

    def get_state(self):
        state={}
        if 'pdf'          in conf: state['pdf'         ]    = conf['pdf'          ].get_state()
        if 'pdfpi-'       in conf: state['pdfpi-'      ]    = conf['pdfpi-'       ].get_state()
        if 'transversity' in conf: state['transversity']    = conf['transversity' ].get_state()
        if 'sivers'       in conf:
            state['sivers'      ]    = conf['sivers'       ].get_state()
            state['dsivers'      ]   = conf['dsivers'      ].get_state()
        if 'boermulders'       in conf:
            state['boermulders'      ]    = conf['boermulders'       ].get_state()
            state['dboermulders'      ]   = conf['dboermulders'      ].get_state()
        if 'ffpi'         in conf: state['ffpi'        ]    = conf['ffpi'         ].get_state()
        if 'ffk'          in conf: state['ffk'         ]    = conf['ffk'          ].get_state()
        if 'ffh'          in conf: state['ffh'         ]    = conf['ffh'          ].get_state()
        if 'collinspi'    in conf:
            state['collinspi'   ]    = conf['collinspi'    ].get_state()
            state['dcollinspi'  ]    = conf['dcollinspi'   ].get_state()
        if 'collinsk'     in conf:
            state['collinsk'    ]    = conf['collinsk'     ].get_state()
            state['dcollinsk'    ]    = conf['dcollinsk'     ].get_state()
        if 'Htildepi'     in conf: state['Htildepi'    ]    = conf['Htildepi'     ].get_state()
        if 'Htildek'      in conf: state['Htildek'     ]    = conf['Htildek'      ].get_state()
        return state

    def set_state(self,state):
        if 'pdf'          in conf: conf['pdf'         ].set_state(state['pdf'         ])
        if 'pdfpi-'       in conf: conf['pdfpi-'      ].set_state(state['pdfpi-'      ])
        if 'transversity' in conf: conf['transversity'].set_state(state['transversity'])
        if 'sivers'       in conf:
            conf['sivers'      ].set_state(state['sivers'      ])
            conf['dsivers'     ].set_state(state['dsivers'     ])
        if 'boermulders'       in conf:
            conf['boermulders'      ].set_state(state['boermulders'      ])
            conf['dboermulders'     ].set_state(state['dboermulders'     ])
        if 'ffpi'         in conf: conf['ffpi'        ].set_state(state['ffpi'        ])
        if 'ffk'          in conf: conf['ffk'         ].set_state(state['ffk'         ])
        if 'ffh'          in conf: conf['ffh'         ].set_state(state['ffh'         ])
        if 'collinspi'    in conf:
            conf['collinspi'   ].set_state(state['collinspi'   ])
            conf['dcollinspi'  ].set_state(state['dcollinspi'  ])
        if 'collinsk'     in conf:
            conf['collinsk'    ].set_state(state['collinsk'    ])
            conf['dcollinsk'   ].set_state(state['dcollinsk'   ])
        if 'Htildepi'     in conf: conf['Htildepi'    ].set_state(state['Htildepi'    ])
        if 'Htildek'      in conf: conf['Htildek'     ].set_state(state['Htildek'     ])

    def distribute_requests(self,container,requests):
        cnt=0
        for request in requests:
            container[cnt].append(request)
            cnt+=1
            if cnt==self.nworkers: cnt=0

    def get_requests(self):
        container=[[] for _ in range(self.nworkers)]
        if 'sidis'  in conf['datasets']:  self.distribute_requests(container,self.sidisres.requests)
        if 'sidisEIC'  in conf['datasets']:  self.distribute_requests(container,self.sidisEICres.requests)
        if 'sidisSoLID'  in conf['datasets']:  self.distribute_requests(container,self.sidisSoLIDres.requests)
        if 'sia'    in conf['datasets']:  self.distribute_requests(container,self.siares.requests)
        if 'AN'     in conf['datasets']:  self.distribute_requests(container,self.ANres.requests)
        if 'ANgam'  in conf['datasets']:  self.distribute_requests(container,self.ANgamres.requests)
        if 'ANep'   in conf['datasets']:  self.distribute_requests(container,self.ANepres.requests)
        if 'dy'     in conf['datasets']:  self.distribute_requests(container,self.dyres.requests)
        if 'wz'     in conf['datasets']:  self.distribute_requests(container,self.wzres.requests)
        if 'SB'     in conf['datasets']:  self.distribute_requests(container,self.SBres.requests)
        if 'moments' in conf['datasets']:  self.distribute_requests(container,self.momentsres.requests)
        return container

    def task(self,request):
        for i in range(len(request)):
            if  request[i]['reaction']=='sidis' :  self.sidisres.process_request(request[i])
            if  request[i]['reaction']=='sidisEIC' :  self.sidisEICres.process_request(request[i])
            if  request[i]['reaction']=='sidisSoLID' :  self.sidisSoLIDres.process_request(request[i])
            if  request[i]['reaction']=='sia'   :  self.siares.process_request(request[i])
            if  request[i]['reaction']=='AN'    :  self.ANres.process_request(request[i])
            if  request[i]['reaction']=='ANgam' :  self.ANgamres.process_request(request[i])
            if  request[i]['reaction']=='ANep'  :  self.ANepres.process_request(request[i])
            if  request[i]['reaction']=='dy'    :  self.dyres.process_request(request[i])
            if  request[i]['reaction']=='wz'    :  self.wzres.process_request(request[i])
            if  request[i]['reaction']=='SB'    :  self.SBres.process_request(request[i])
            if  request[i]['reaction']=='moments' :  self.momentsres.process_request(request[i])
        return request

    def get_residuals(self,par):
        self.parman.set_new_params(par)
        state=self.get_state()
        self.parallel.update_workers(state)
        results=self.parallel.send_tasks(self.requests)

        #--update tables with the new theory values
        for chunk in results:
            for request in chunk:
                if request['reaction']=='sidis'  : self.sidisres.update_tabs_external(request)
                if request['reaction']=='sidisEIC'  : self.sidisEICres.update_tabs_external(request)
                if request['reaction']=='sidisSoLID'  : self.sidisSoLIDres.update_tabs_external(request)
                if request['reaction']=='sia'    : self.siares.update_tabs_external(request)
                if request['reaction']=='AN'     : self.ANres.update_tabs_external(request)
                if request['reaction']=='ANgam'  : self.ANgamres.update_tabs_external(request)
                if request['reaction']=='ANep'   : self.ANepres.update_tabs_external(request)
                if request['reaction']=='dy'     : self.dyres.update_tabs_external(request)
                if request['reaction']=='wz'     : self.wzres.update_tabs_external(request)
                if request['reaction']=='SB'     : self.SBres.update_tabs_external(request)
                if request['reaction']=='moments' : self.momentsres.update_tabs_external(request)

        #--compute residuals
        res,rres,nres=[],[],[]
        if 'sidis' in conf['datasets']:
            out=self.sidisres.get_residuals(calc=False)
            res=np.append(res,out[0])
            rres=np.append(rres,out[1])
            nres=np.append(nres,out[2])
        if 'sidisEIC' in conf['datasets']:
            out=self.sidisEICres.get_residuals(calc=False)
            res=np.append(res,out[0])
            rres=np.append(rres,out[1])
            nres=np.append(nres,out[2])
        if 'sidisSoLID' in conf['datasets']:
            out=self.sidisSoLIDres.get_residuals(calc=False)
            res=np.append(res,out[0])
            rres=np.append(rres,out[1])
            nres=np.append(nres,out[2])
        if 'sia' in conf['datasets']:
            out=self.siares.get_residuals(calc=False)
            res=np.append(res,out[0])
            rres=np.append(rres,out[1])
            nres=np.append(nres,out[2])
        if 'AN' in conf['datasets']:
            out=self.ANres.get_residuals(calc=False)
            res=np.append(res,out[0])
            rres=np.append(rres,out[1])
            nres=np.append(nres,out[2])
        if 'ANgam' in conf['datasets']:
            out=self.ANgamres.get_residuals(calc=False)
            res=np.append(res,out[0])
            rres=np.append(rres,out[1])
            nres=np.append(nres,out[2])
        if 'ANep' in conf['datasets']:
            out=self.ANepres.get_residuals(calc=False)
            res=np.append(res,out[0])
            rres=np.append(rres,out[1])
            nres=np.append(nres,out[2])
        if 'dy' in conf['datasets']:
            out=self.dyres.get_residuals(calc=False)
            res=np.append(res,out[0])
            rres=np.append(rres,out[1])
            nres=np.append(nres,out[2])
        if 'wz' in conf['datasets']:
            out=self.wzres.get_residuals(calc=False)
            res=np.append(res,out[0])
            rres=np.append(rres,out[1])
            nres=np.append(nres,out[2])
        if 'SB' in conf['datasets']:
            out=self.SBres.get_residuals(calc=False)
            res=np.append(res,out[0])
            rres=np.append(rres,out[1])
            nres=np.append(nres,out[2])
        if 'moments' in conf['datasets']:
            out=self.momentsres.get_residuals(calc=False)
            res=np.append(res,out[0])
            rres=np.append(rres,out[1])
            nres=np.append(nres,out[2])
        return res,rres,nres

    def get_data_info(self):

        #--compute residuals
        reaction=[]
        if 'sidis' in conf['datasets']:
            out=self.sidisres.get_residuals(calc=False)
            reaction.extend(['sidis' for _ in out[0]])
        if 'sidisEIC' in conf['datasets']:
            out=self.sidisEICres.get_residuals(calc=False)
            reaction.extend(['sidisEIC' for _ in out[0]])
        if 'sidisSoLID' in conf['datasets']:
            out=self.sidisSoLIDres.get_residuals(calc=False)
            reaction.extend(['sidisSoLID' for _ in out[0]])
        if 'sia' in conf['datasets']:
            out=self.siares.get_residuals(calc=False)
            reaction.extend(['sia' for _ in out[0]])
        if 'AN' in conf['datasets']:
            out=self.ANres.get_residuals(calc=False)
            reaction.extend(['AN' for _ in out[0]])
        if 'ANgam' in conf['datasets']:
            out=self.ANgamres.get_residuals(calc=False)
            reaction.extend(['ANgam' for _ in out[0]])
        if 'ANep' in conf['datasets']:
            out=self.ANepres.get_residuals(calc=False)
            reaction.extend(['ANep' for _ in out[0]])
        if 'dy' in conf['datasets']:
            out=self.dyres.get_residuals(calc=False)
            reaction.extend(['dy' for _ in out[0]])
        if 'wz' in conf['datasets']:
            out=self.wzres.get_residuals(calc=False)
            reaction.extend(['wz' for _ in out[0]])
        if 'SB' in conf['datasets']:
            out=self.SBres.get_residuals(calc=False)
            reaction.extend(['SB' for _ in out[0]])
        if 'moments' in conf['datasets']:
            out=self.momentsres.get_residuals(calc=False)
            reaction.extend(['moments' for _ in out[0]])
        return reaction

    def gen_report(self,verb=0,level=0):
        L=[]
        if 'sidis'   in conf['datasets']: L.extend(self.sidisres.gen_report(verb,level))
        if 'sidisEIC'   in conf['datasets']: L.extend(self.sidisEICres.gen_report(verb,level))
        if 'sidisSoLID'   in conf['datasets']: L.extend(self.sidisSoLIDres.gen_report(verb,level))
        if 'sia'     in conf['datasets']: L.extend(self.siares.gen_report(verb,level))
        if 'AN'      in conf['datasets']: L.extend(self.ANres.gen_report(verb,level))
        if 'ANgam'   in conf['datasets']: L.extend(self.ANgamres.gen_report(verb,level))
        if 'ANep'    in conf['datasets']: L.extend(self.ANepres.gen_report(verb,level))
        if 'dy'      in conf['datasets']: L.extend(self.dyres.gen_report(verb,level))
        if 'wz'      in conf['datasets']: L.extend(self.wzres.gen_report(verb,level))
        if 'SB'      in conf['datasets']: L.extend(self.SBres.gen_report(verb,level))
        if 'moments' in conf['datasets']: L.extend(self.momentsres.gen_report(verb,level))
        return L

    def get_chi2(self):
        data={}
        if 'sidis'   in conf['datasets']: data.update(self.sidisres.get_chi2())
        if 'sidisEIC'   in conf['datasets']: data.update(self.sidisEICres.get_chi2())
        if 'sidisSoLID'   in conf['datasets']: data.update(self.sidisSoLIDres.get_chi2())
        if 'sia'     in conf['datasets']: data.update(self.siares.get_chi2())
        if 'AN'      in conf['datasets']: data.update(self.ANres.get_chi2())
        if 'ANgam'   in conf['datasets']: data.update(self.ANgamres.get_chi2())
        if 'ANep'    in conf['datasets']: data.update(self.ANepres.get_chi2())
        if 'dy'      in conf['datasets']: data.update(self.dyres.get_chi2())
        if 'wz'      in conf['datasets']: data.update(self.wzres.get_chi2())
        if 'SB'      in conf['datasets']: data.update(self.SBres.get_chi2())
        if 'moments' in conf['datasets']: data.update(self.momentsres.get_chi2())
        return data

    def test(self,ntasks=10):
        #--loop over states
        print('='*20)
        t=time.time()
        for _ in range(ntasks):
            par=self.parman.par
            par*=(1+0.01*np.random.randn(par.size))
            res,rres,nres=self.get_residuals(par)
            chi2=np.sum(res**2)
            print('(%d/%d) chi2=%f'%(_,ntasks,chi2))
        print('='*20)
        elapsed_time=time.time()-t
        print('elapsed time :%f'%elapsed_time)
        return elapsed_time

    def shutdown(self):
        self.parallel.stop_workers()

if __name__=='__main__':

    load_config('input_dglap.py')
    nworkers=3
    resman=RESMAN(nworkers)
    resman.test()
    resman.shutdown()
