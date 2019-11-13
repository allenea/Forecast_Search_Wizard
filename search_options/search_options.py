"""Copyright (C) 2018-2019 Eric Allen - All Rights Reserved"""
#
# You may use, distribute and modify this code under the
# terms of the GNU General Public License v3.0 license.
#
# You should have received a copy of the GNU General Public
# License v3.0 packaged with the Forecast Search Wizard.
# If not vist https://www.gnu.org/licenses/gpl-3.0.en.html
#
# Please properly cite code, derivative code, and outputs
# of the Forecast Search Wizard in all scholarly work and
# publications.
#

class Option:
    """Pre-Set Search Options

    THESE ARE NOT NECESSARILY SORTED ALPHABETICALLY....

    # 1. USE ONE OR MORE OF THE PRE-SET OPTIONS BELOW.
          YOU MAY COMBINE MULTIPLE OPTIONS (AUTOMATICALLY REMOVING DUPLICATES)
              example: lst = list(set(Option.ALL) - set(Option.ALL_SPC))

    # 2. CREATE A LIST WITH THE PILs FOR THE FORECAST PRODUCTS THAT YOU WANT SEARCHED IN YOUR
             CONFIGURATION OF THE FORECAST SEARCH WIZARD. SEE EXAMPLES BELOW.
             TO MAKE MULTIPLE CONFIGURATIONS. PROVIDE UNIQUE VARIABLE NAMES.

         To access your search list: use  ~~  Option.MY_SEARCH   ~~  where MY_SEARCH is
                the variable name on the left-hand side of the equal sign below

    call Option.ALASKA_OPC to get the list for ALASKA_OPC products


    $ Option.ALASKA_OPC

    Returns: ['MIMPAC',
     'OFFAER',
     'OFFAFG',
     'OFFAJK',
     'OFFALU',
     'OFFN11',
     'OFFN12',
     'OFFN13',
     'OFFN14',
     'OFFN15']
    """

    ## TODO CREATE YOUR OWN HERE.
    MY_SEARCH = []

    MY_SEARCH2 = []


    ALL = ['AFDABQ', 'AFDABR', 'AFDAFC', 'AFDAFG', 'AFDAJK', 'AFDAKQ', 'AFDALY',\
           'AFDAMA', 'AFDAPX', 'AFDARX', 'AFDBGM', 'AFDBIS', 'AFDBMX', 'AFDBOI',\
           'AFDBOU', 'AFDBOX', 'AFDBRO', 'AFDBTV', 'AFDBUF', 'AFDBYZ', 'AFDCAE',\
           'AFDCAR', 'AFDCHS', 'AFDCLE', 'AFDCRP', 'AFDCTP', 'AFDCYS', 'AFDDDC',\
           'AFDDLH', 'AFDDMX', 'AFDDPQ', 'AFDDTX', 'AFDDVN', 'AFDEAX', 'AFDEKA',\
           'AFDEPZ', 'AFDEWX', 'AFDEYW', 'AFDFFC', 'AFDFGF', 'AFDFGZ', 'AFDFSD',\
           'AFDFWD', 'AFDGGW', 'AFDGID', 'AFDGJT', 'AFDGLD', 'AFDGRB', 'AFDGRR',\
           'AFDGSP', 'AFDGYX', 'AFDHFO', 'AFDHGX', 'AFDHNX', 'AFDHUN', 'AFDICT',\
           'AFDILM', 'AFDILN', 'AFDILX', 'AFDIND', 'AFDIWX', 'AFDJAN', 'AFDJAX',\
           'AFDJKL', 'AFDKEY', 'AFDLBF', 'AFDLCH', 'AFDLIX', 'AFDLKN', 'AFDLMK',\
           'AFDLOT', 'AFDLOX', 'AFDLSX', 'AFDLUB', 'AFDLWX', 'AFDLZK', 'AFDMAF',\
           'AFDMEG', 'AFDMFL', 'AFDMFR', 'AFDMHX', 'AFDMKX', 'AFDMLB', 'AFDMOB',\
           'AFDMPX', 'AFDMQT', 'AFDMRX', 'AFDMSO', 'AFDMTR', 'AFDOAX', 'AFDOHX',\
           'AFDOKX', 'AFDOTX', 'AFDOUN', 'AFDPAH', 'AFDPBZ', 'AFDPDT', 'AFDPHI',\
           'AFDPIH', 'AFDPPG', 'AFDPQ', 'AFDPQR', 'AFDPSR', 'AFDPUB', 'AFDRAH',\
           'AFDREV', 'AFDRIW', 'AFDRLX', 'AFDRNK', 'AFDSDF', 'AFDSEW', 'AFDSGF',\
           'AFDSGX', 'AFDSHV', 'AFDSJT', 'AFDSJU', 'AFDSLC', 'AFDSTO', 'AFDTAE',\
           'AFDTBW', 'AFDTFX', 'AFDTOP', 'AFDTSA', 'AFDTWC', 'AFDUNR', 'AFDVEF',\
           'ALTK04', 'ALTK05', 'ALTK06', 'ALTK07', 'ALTK08', 'ALTK09', 'DAYDIS',\
           'DAYDSF', 'DAYTDF', 'FFGMPD', 'FWDD38', 'FWDDY1', 'FWDDY2', 'HSFAT1',\
           'HSFAT2', 'HSFEP', 'HSFEP1', 'HSFEP2', 'HSFEP3', 'HSFEPI', 'HSFNP',\
           'HSFSP', 'LSRABQ', 'LSRABR', 'LSRAFC', 'LSRAFG', 'LSRAJK', 'LSRAKN',\
           'LSRAKQ', 'LSRALY', 'LSRAMA', 'LSRAPX', 'LSRARX', 'LSRBGM', 'LSRBIS',\
           'LSRBMX', 'LSRBOI', 'LSRBOU', 'LSRBOX', 'LSRBRO', 'LSRBRW', 'LSRBTV',\
           'LSRBUF', 'LSRBYZ', 'LSRCAE', 'LSRCAR', 'LSRCDB', 'LSRCHS', 'LSRCLE',\
           'LSRCRP', 'LSRCTP', 'LSRCYS', 'LSRDDC', 'LSRDLH', 'LSRDMX', 'LSRDTX',\
           'LSRDVN', 'LSREAX', 'LSREKA', 'LSREPZ', 'LSREWX', 'LSRFFC', 'LSRFGF',\
           'LSRFGZ', 'LSRFSD', 'LSRFWD', 'LSRGGW', 'LSRGID', 'LSRGJT', 'LSRGLD',\
           'LSRGRB', 'LSRGRR', 'LSRGSP', 'LSRGUM', 'LSRGYX', 'LSRHFO', 'LSRHGX',\
           'LSRHNX', 'LSRHUN', 'LSRICT', 'LSRILM', 'LSRILN', 'LSRILX', 'LSRIND',\
           'LSRISN', 'LSRIWX', 'LSRJAN', 'LSRJAX', 'LSRJKL', 'LSRKEY', 'LSRLBF',\
           'LSRLCH', 'LSRLIX', 'LSRLKN', 'LSRLMK', 'LSRLOT', 'LSRLOX', 'LSRLSX',\
           'LSRLUB', 'LSRLWX', 'LSRLZK', 'LSRMAF', 'LSRMCG', 'LSRMEG', 'LSRMFL',\
           'LSRMFR', 'LSRMHX', 'LSRMKX', 'LSRMLB', 'LSRMOB', 'LSRMPX', 'LSRMQT',\
           'LSRMRX', 'LSRMSO', 'LSRMTR', 'LSRNY1', 'LSRNY2', 'LSRNY3', 'LSRNY4',\
           'LSRNY7', 'LSROAX', 'LSROHX', 'LSROKX', 'LSROTX', 'LSROUN', 'LSRPAH',\
           'LSRPBZ', 'LSRPDT', 'LSRPHI', 'LSRPIH', 'LSRPPG', 'LSRPQR', 'LSRPSR',\
           'LSRPUB', 'LSRRAH', 'LSRREV', 'LSRRIW', 'LSRRLX', 'LSRRNK', 'LSROME',\
           'LSRSEW', 'LSRSGF', 'LSRSGX', 'LSRSHV', 'LSRSJT', 'LSRSJU', 'LSRSLC',\
           'LSRSTO', 'LSRTAE', 'LSRTBW', 'LSRTFX', 'LSRTOP', 'LSRTSA', 'LSRTWC',\
           'LSRUNR', 'LSRVEF', 'LSRVWS', 'MIMATN', 'MIMATS', 'MIMPAC', 'NOWABQ',\
           'NOWABR', 'NOWADQ', 'NOWAFC', 'NOWAFG', 'NOWAJK', 'NOWAKN', 'NOWAKQ',\
           'NOWALY', 'NOWAMA', 'NOWANN', 'NOWAPX', 'NOWARX', 'NOWBET', 'NOWBGM',\
           'NOWBIS', 'NOWBMX', 'NOWBOI', 'NOWBOU', 'NOWBOX', 'NOWBRO', 'NOWBRW',\
           'NOWBTV', 'NOWBUF', 'NOWBYZ', 'NOWCAE', 'NOWCAR', 'NOWCDB', 'NOWCHS',\
           'NOWCLE', 'NOWCRP', 'NOWCTP', 'NOWCYS', 'NOWDDC', 'NOWDLH', 'NOWDMX',\
           'NOWDTX', 'NOWDVN', 'NOWEAX', 'NOWEKA', 'NOWEPZ', 'NOWEWX', 'NOWEYW',\
           'NOWFFC', 'NOWFGF', 'NOWFGZ', 'NOWFSD', 'NOWFWD', 'NOWGGW', 'NOWGID',\
           'NOWGJT', 'NOWGLD', 'NOWGRB', 'NOWGRR', 'NOWGSP', 'NOWGYX', 'NOWHFO',\
           'NOWHGX', 'NOWHNX', 'NOWHUN', 'NOWICT', 'NOWILM', 'NOWILN', 'NOWILX',\
           'NOWIND', 'NOWISN', 'NOWIWX', 'NOWJAN', 'NOWJAX', 'NOWJKL', 'NOWKEY',\
           'NOWLBF', 'NOWLCH', 'NOWLIX', 'NOWLKN', 'NOWLMK', 'NOWLOT', 'NOWLOX',\
           'NOWLSX', 'NOWLUB', 'NOWLWX', 'NOWLZK', 'NOWMAF', 'NOWMCG', 'NOWMEG',\
           'NOWMFL', 'NOWMFR', 'NOWMHX', 'NOWMKX', 'NOWMLB', 'NOWMOB', 'NOWMPX',\
           'NOWMQT', 'NOWMRX', 'NOWMSO', 'NOWMTR', 'NOWMY', 'NOWOAX', 'NOWOHX',\
           'NOWOKX', 'NOWOME', 'NOWOTX', 'NOWOTZ', 'NOWOUN', 'NOWPAH', 'NOWPBZ',\
           'NOWPDT', 'NOWPHI', 'NOWPIH', 'NOWPQR', 'NOWPSR', 'NOWPUB', 'NOWRAH',\
           'NOWREV', 'NOWRIW', 'NOWRLX', 'NOWRNK', 'NOWSDF', 'NOWSEW', 'NOWSGF',\
           'NOWSGX', 'NOWSHV', 'NOWSJT', 'NOWSJU', 'NOWSLC', 'NOWSNP', 'NOWSTO',\
           'NOWTAE', 'NOWTBW', 'NOWTFX', 'NOWTOP', 'NOWTSA', 'NOWTWC', 'NOWUNR',\
           'NOWVEF', 'NOWVWS', 'NOWYAK', 'OFFAER', 'OFFAFG', 'OFFAJK', 'OFFALU',\
           'OFFHFO', 'OFFN01', 'OFFN02', 'OFFN03', 'OFFN04', 'OFFN05', 'OFFN06',\
           'OFFN07', 'OFFN08', 'OFFN09', 'OFFN10', 'OFFN11', 'OFFN12', 'OFFN13',\
           'OFFN14', 'OFFN15', 'OFFNT1', 'OFFNT2', 'OFFNT3', 'OFFNT4', 'OFFPZ5',\
           'OFFPZ6', 'PMD30D', 'PMD90D', 'PMDAHU', 'PMDAK', 'PMDCA', 'PMDDRK',\
           'PMDDRO', 'PMDENS', 'PMDEPD', 'PMDEPH', 'PMDHCO', 'PMDHI', 'PMDHMD',\
           'PMDMRD', 'PMDSA', 'PMDSPD', 'PMDTHR', 'QPFERD', 'QPFHSD', 'SCCNS1',\
           'SCCNS2', 'SCCNS3', 'SCCNS4', 'SCCNS5', 'SEL0', 'SEL1', 'SEL2', 'SEL3',\
           'SEL4', 'SEL5', 'SEL6', 'SEL7', 'SEL8', 'SEL9', 'SWOD48', 'SWODY1',\
           'SWODY2', 'SWODY3', 'SWOMCD', 'TCDAT1', 'TCDAT2', 'TCDAT3', 'TCDAT4',\
           'TCDAT5', 'TCDCP1', 'TCDCP2', 'TCDCP3', 'TCDCP4', 'TCDCP5', 'TCDEP1',\
           'TCDEP2', 'TCDEP3', 'TCDEP4', 'TCDEP5', 'TCPAT1', 'TCPAT2', 'TCPAT3',\
           'TCPAT4', 'TCPAT5', 'TCPCP1', 'TCPCP2', 'TCPCP3', 'TCPCP4', 'TCPCP5',\
           'TCPEP1', 'TCPEP2', 'TCPEP3', 'TCPEP4', 'TCPEP5', 'TCUAT', 'TCUAT1',\
           'TCUAT2', 'TCUAT3', 'TCUAT4', 'TCUAT5', 'TCUCP1', 'TCUCP2', 'TCUCP3',\
           'TCUCP4', 'TCUCP5', 'TCUEP', 'TCUEP1', 'TCUEP2', 'TCUEP3', 'TCUEP4',\
           'TCUEP5', 'TWDAT', 'TWDEP']

    #26 products as a part of the "Special" cases
    Downloaded_Not_Included = ['FFSLWX', 'FFSPHI', 'FFWLWX', 'FFWPHI', 'FLSLWX',\
                               'FLSPHI', 'FLWLWX', 'FLWPHI', 'WSWLWX', 'WSWPHI',\
                               'SMWLWX', 'SMWPHI', 'SVRLWX', 'SVRPHI', 'SVSLWX',\
                               'SVSPHI', 'TORLWX', 'TORPHI', 'PNSLWX', 'PNSPHI',\
                               'FFALWX', 'FFAPHI', 'HWOLWX', 'HWOPHI']

    #23 products were deleted upon download.
    #Empty_Data = ["VOWLWX", "VOWPHI", "LSRADQ", "LSRANN", "LSRAT1", "LSRBA1", \
                    #"LSRBET", "LSRBH1", "LSRBR1", "LSRCS1", "LSRHO1", "LSRJM1",\
                    #"LSRNK1", "LSRNY5", "LSRNY6", "LSROTZ", "LSRSNP", "LSRTD1",\
                   #"LSRYAK"] #END OF EMPTY DATA

    """

    BELOW ARE THE SPECIFIC FORECASTS THAT GO WITH EACH OPTION IN ~/Documentation/Preset_Options.txt

    """

    ALL_LSR = ['LSRABQ', 'LSRABR', 'LSRAFC', 'LSRAFG', 'LSRAJK', 'LSRAKN',\
               'LSRAKQ', 'LSRALY', 'LSRAMA', 'LSRAPX', 'LSRARX',\
               'LSRBGM', 'LSRBIS', 'LSRBMX', 'LSRBOI', 'LSRBOU', 'LSRBOX',\
               'LSRBRO', 'LSRBRW', 'LSRBTV', 'LSRBUF', 'LSRBYZ',\
               'LSRCAE', 'LSRCAR', 'LSRCDB', 'LSRCHS', 'LSRCLE', 'LSRCRP',\
               'LSRCTP', 'LSRCYS', 'LSRDDC', 'LSRDLH', 'LSRDMX',\
               'LSRDTX', 'LSRDVN', 'LSREAX', 'LSREKA', 'LSREPZ', 'LSREWX',\
               'LSRFFC', 'LSRFGF', 'LSRFGZ', 'LSRFSD', 'LSRFWD',\
               'LSRGGW', 'LSRGID', 'LSRGJT', 'LSRGLD', 'LSRGRB', 'LSRGRR',\
               'LSRGSP', 'LSRGUM', 'LSRGYX', 'LSRHFO', 'LSRHGX',\
               'LSRHNX', 'LSRHUN', 'LSRICT', 'LSRILM', 'LSRILN', 'LSRILX',\
               'LSRIND', 'LSRISN', 'LSRIWX', 'LSRJAN', 'LSRJAX',\
               'LSRJKL', 'LSRKEY', 'LSRLBF', 'LSRLCH', 'LSRLIX', 'LSRLKN',\
               'LSRLMK', 'LSRLOT', 'LSRLOX', 'LSRLSX', 'LSRLUB',\
               'LSRLWX', 'LSRLZK', 'LSRMAF', 'LSRMCG', 'LSRMEG', 'LSRMFL',\
               'LSRMFR', 'LSRMHX', 'LSRMKX', 'LSRMLB', 'LSRMOB',\
               'LSRMPX', 'LSRMQT', 'LSRMRX', 'LSRMSO', 'LSRMTR', 'LSRNY1',\
               'LSRNY2', 'LSRNY3', 'LSRNY4', 'LSRNY7', 'LSROAX',\
               'LSROHX', 'LSROKX', 'LSROTX', 'LSROUN', 'LSRPAH', 'LSRPBZ',\
               'LSRPDT', 'LSRPHI', 'LSRPIH', 'LSRPPG', 'LSRPQR',\
               'LSRPSR', 'LSRPUB', 'LSRRAH', 'LSRREV', 'LSRRIW', 'LSRRLX',\
               'LSRRNK', 'LSROME', 'LSRSEW', 'LSRSGF', 'LSRSGX',\
               'LSRSHV', 'LSRSJT', 'LSRSJU', 'LSRSLC', 'LSRSTO', 'LSRTAE',\
               'LSRTBW', 'LSRTFX', 'LSRTOP', 'LSRTSA', 'LSRTWC',\
               'LSRUNR', 'LSRVEF', 'LSRVWS']


    ALL_NCEP = ['ALTK04', 'ALTK05', 'ALTK06', 'ALTK07', 'ALTK08', 'ALTK09', 'DAYDIS', 'DAYDSF',\
                 'DAYTDF', 'FFGMPD', 'FWDD38', 'FWDDY1', 'FWDDY2', 'HSFAT1', 'HSFAT2', 'HSFEP',\
                 'HSFEP1', 'HSFEP2', 'HSFEP3', 'HSFEPI', 'HSFNP', 'HSFSP', 'MIMATN', 'MIMATS',\
                 'MIMPAC', 'OFFAER', 'OFFAFG', 'OFFAJK', 'OFFALU', 'OFFHFO', 'OFFN01', 'OFFN02',\
                 'OFFN03', 'OFFN04', 'OFFN05', 'OFFN06', 'OFFN07', 'OFFN08', 'OFFN09', 'OFFN10',\
                 'OFFN11', 'OFFN12', 'OFFN13', 'OFFN14', 'OFFN15', 'OFFNT1', 'OFFNT2', 'OFFNT3',\
                 'OFFNT4', 'OFFPZ5', 'OFFPZ6', 'PMD30D', 'PMD90D', 'PMDAHU', 'PMDAK', 'PMDCA',\
                 'PMDDRK', 'PMDDRO', 'PMDENS', 'PMDEPD', 'PMDEPH', 'PMDHCO', 'PMDHI', 'PMDHMD',\
                 'PMDMRD', 'PMDSA', 'PMDSPD', 'PMDTHR', 'QPFERD', 'QPFHSD', 'SCCNS1', 'SCCNS2',\
                 'SCCNS3', 'SCCNS4', 'SCCNS5', 'SEL0', 'SEL1', 'SEL2', 'SEL3', 'SEL4',\
                 'SEL5', 'SEL6', 'SEL7', 'SEL8', 'SEL9', 'SWOD48', 'SWODY1', 'SWODY2',\
                 'SWODY3', 'SWOMCD', 'TCDAT1', 'TCDAT2', 'TCDAT3', 'TCDAT4', 'TCDAT5', 'TCDCP1',\
                 'TCDCP2', 'TCDCP3', 'TCDCP4', 'TCDCP5', 'TCDEP1', 'TCDEP2', 'TCDEP3', 'TCDEP4',\
                 'TCDEP5', 'TCPAT1', 'TCPAT2', 'TCPAT3', 'TCPAT4', 'TCPAT5', 'TCPCP1', 'TCPCP2',\
                 'TCPCP3', 'TCPCP4', 'TCPCP5', 'TCPEP1', 'TCPEP2', 'TCPEP3', 'TCPEP4', 'TCPEP5',\
                 'TCUAT', 'TCUAT1', 'TCUAT2', 'TCUAT3', 'TCUAT4', 'TCUAT5', 'TCUCP1', 'TCUCP2',\
                 'TCUCP3', 'TCUCP4', 'TCUCP5', 'TCUEP', 'TCUEP1', 'TCUEP2', 'TCUEP3', 'TCUEP4',\
                 'TCUEP5', 'TWDAT', 'TWDEP']

    # =============================================================================
    # OCEAN PREDICTION CENTER - 9
    # =============================================================================
    #All OPC:
    ALL_OPC = ["MIMPAC", "OFFAER", "OFFAFG", "OFFAJK", "OFFALU", "OFFN11", "OFFN12",\
               "OFFN13", "OFFN14", "OFFN15", "HSFEP3", "HSFSP", "OFFHFO", "OFFN10",\
               "HSFEPI", "HSFEP", "OFFN07", "OFFN08", "OFFN09", "OFFPZ5", "OFFPZ6",\
               "HSFEP1", "MIMATN", "MIMATS", "OFFN01", "OFFN02", "OFFN03",\
               "OFFN04", "OFFN05", "OFFN06", "OFFNT1", "OFFNT2", "OFFNT3", "OFFNT4",\
               "HSFAT1", "HSFAT2", 'HSFEP2', 'HSFNP']

    #Pacific OPC:
    PACIFIC_OPC = ["MIMPAC", "OFFAER", "OFFAFG", "OFFAJK", "OFFALU", "OFFN11", "OFFN12",\
                  "OFFN13", "OFFN14", "OFFN15", "HSFEP3", "HSFSP", "OFFHFO", "OFFN10",\
                  "HSFEPI", "HSFEP", "OFFN07", "OFFN08", "OFFN09", "OFFPZ5", "OFFPZ6",\
                  "HSFEP1", "HSFEP2", 'HSFNP']

    #Pacific US:
    PACIFIC_US_OPC = ["MIMPAC", "OFFN07", "OFFN08", "OFFN09", "OFFPZ5", "OFFPZ6",\
                      "HSFEP1", "HSFEP2", "HSFEPI", 'HSFNP']

    #Alaska OPC:
    ALASKA_OPC = ["MIMPAC", "OFFAER", "OFFAFG", "OFFAJK", "OFFALU", "OFFN11",\
                  "OFFN12", "OFFN13", "OFFN14", "OFFN15"]

    #Hawaii/Pacific Tropical OPC:
    HAWAII_TROP_PAC_OPC = ["OFFHFO", "OFFN10", "HSFEPI", "HSFEP", 'HSFNP']

    #SH Pacific OPC:
    SH_PACIFIC_OPC = ["HSFEP3", "HSFSP"]

    #Atlantic OPC:
    ATLANTIC_OPC = ["MIMATN", "MIMATS", "OFFN01", "OFFN02", "OFFN03", "OFFN04",\
                    "OFFN05", "OFFN06", "OFFNT1", "OFFNT2", "OFFNT3", "OFFNT4",\
                    "HSFAT1", "HSFAT2"]

    #N. Atlantic OPC:
    NORTH_ATLANTIC_OPC = ["MIMATN", "OFFN01", "OFFN02", "OFFNT1", "OFFNT2", "HSFAT1"]

    #Tropical Atlantic OPC:
    TROPICAL_ATLANTIC_OPC = ["MIMATS", "OFFN03", "OFFN04", "OFFN05", "OFFN06",\
                             "OFFNT3", "OFFNT4", "HSFAT2"]


    # =============================================================================
    # NATIONAL HURRICANE CENTER - 17
    # =============================================================================
    ALL_NHC = ['TWDAT', 'TCUAT', 'TCUAT1', 'TCUAT2', 'TCUAT3', 'TCUAT4', 'TCUAT5',\
               'TCDAT1', 'TCDAT2', 'TCDAT3', 'TCDAT4', 'TCDAT5', 'TCPAT1', 'TCPAT2',\
               'TCPAT3', 'TCPAT4', 'TCPAT5', 'TCUCP1', 'TCUCP2', 'TCUCP3', 'TCUCP4',\
               'TCUCP5', 'TCDCP1', 'TCDCP2', 'TCDCP3', 'TCDCP4', 'TCDCP5', 'TCPCP1',\
               'TCPCP2', 'TCPCP3', 'TCPCP4', 'TCPCP5', 'TWDEP', 'TCUEP', 'TCUEP1',\
               'TCUEP2', 'TCUEP3', 'TCUEP4', 'TCUEP5', 'TCDEP1', 'TCDEP2', 'TCDEP3',\
               'TCDEP4', 'TCDEP5', 'TCPEP1', 'TCPEP2', 'TCPEP3', 'TCPEP4', 'TCPEP5']


    # ATLANTIC TROPICAL CYCLONES
    ATLANTIC_TC = ['TWDAT', 'TCUAT', 'TCUAT1', 'TCUAT2', 'TCUAT3', 'TCUAT4', 'TCUAT5',\
                   'TCDAT1', 'TCDAT2', 'TCDAT3', 'TCDAT4', 'TCDAT5', 'TCPAT1', 'TCPAT2',\
                   'TCPAT3', 'TCPAT4', 'TCPAT5']

    ATLANTIC_TC_UPDATE = ['TCUAT', 'TCUAT1', 'TCUAT2', 'TCUAT3', 'TCUAT4', 'TCUAT5']

    ATLANTIC_TC_DISCUSSION = ['TWDAT', 'TCDAT1', 'TCDAT2', 'TCDAT3', 'TCDAT4', 'TCDAT5']

    ATLANTIC_TC_ADVISORIES = ['TCPAT1', 'TCPAT2', 'TCPAT3', 'TCPAT4', 'TCPAT5']


    # PACIFIC TROPICAL CYCLONES
    PACIFIC_TC = ['TCUCP1', 'TCUCP2', 'TCUCP3', 'TCUCP4', 'TCUCP5', 'TCDCP1', 'TCDCP2',\
                'TCDCP3', 'TCDCP4', 'TCDCP5', 'TCPCP1', 'TCPCP2', 'TCPCP3', 'TCPCP4',\
                'TCPCP5', 'TWDEP', 'TCUEP', 'TCUEP1', 'TCUEP2', 'TCUEP3', 'TCUEP4',\
                'TCUEP5', 'TCDEP1', 'TCDEP2', 'TCDEP3', 'TCDEP4', 'TCDEP5', 'TCPEP1',\
                'TCPEP2', 'TCPEP3', 'TCPEP4', 'TCPEP5']

    PACIFIC_TC_UPDATE = ['TCUCP1', 'TCUCP2', 'TCUCP3', 'TCUCP4', 'TCUCP5', 'TCUEP',\
                         'TCUEP1', 'TCUEP2', 'TCUEP3', 'TCUEP4', 'TCUEP5']

    PACIFIC_TC_DISCUSSION = ['TCDCP1', 'TCDCP2', 'TCDCP3', 'TCDCP4', 'TCDCP5', 'TWDEP',\
                             'TCDEP1', 'TCDEP2', 'TCDEP3', 'TCDEP4', 'TCDEP5']

    PACIFIC_TC_ADVISORIES = ['TCPCP1', 'TCPCP2', 'TCPCP3', 'TCPCP4', 'TCPCP5', 'TCPEP1',\
                             'TCPEP2', 'TCPEP3', 'TCPEP4', 'TCPEP5']


    # CENTRAL PACIFIC CYCLONES
    CENTRAL_PACIFIC_TC = ['TCUCP1', 'TCUCP2', 'TCUCP3', 'TCUCP4', 'TCUCP5', 'TCDCP1',\
                         'TCDCP2', 'TCDCP3', 'TCDCP4', 'TCDCP5', 'TCPCP1', 'TCPCP2',\
                         'TCPCP3', 'TCPCP4', 'TCPCP5']

    CENTRAL_PACIFIC_TC_UPDATE = ['TCUCP1', 'TCUCP2', 'TCUCP3', 'TCUCP4', 'TCUCP5']

    CENTRAL_PACIFIC_TC_DISCUSSION = ['TCDCP1', 'TCDCP2', 'TCDCP3', 'TCDCP4', 'TCDCP5']

    CENTRAL_PACIFIC_TC_ADVISORIES = ['TCPCP1', 'TCPCP2', 'TCPCP3', 'TCPCP4', 'TCPCP5']


    # EASTERN PACIFIC CYCLONES
    EASTERN_PACIFIC_TC = ['TWDEP', 'TCUEP', 'TCUEP1', 'TCUEP2', 'TCUEP3', 'TCUEP4',\
                         'TCUEP5', 'TCDEP1', 'TCDEP2', 'TCDEP3', 'TCDEP4', 'TCDEP5',\
                         'TCPEP1', 'TCPEP2', 'TCPEP3', 'TCPEP4', 'TCPEP5']

    EASTERN_PACIFIC_TC_UPDATE = ['TCUEP', 'TCUEP1', 'TCUEP2', 'TCUEP3', 'TCUEP4', 'TCUEP5']

    EASTERN_PACIFIC_TC_DISCUSSION = ['TWDEP', 'TCDEP1', 'TCDEP2', 'TCDEP3', 'TCDEP4', 'TCDEP5']

    EASTERN_PACIFIC_TC_ADVISORIES = ['TCPEP1', 'TCPEP2', 'TCPEP3', 'TCPEP4', 'TCPEP5']


    # =============================================================================
    # SPC SEVERE WEATHER - 9
    # =============================================================================
    ALL_SPC = ['SWOMCD', 'SWODY1', 'SWODY2', 'SWODY3', "SWOD48", "SEL0", "SEL1", "SEL2",\
               "SEL3", "SEL4", "SEL5", "SEL6", "SEL7", "SEL8", "SEL9"]

    SPC_SVR_OUTLOOKS = ['SWODY1', 'SWODY2', 'SWODY3', "SWOD48"]

    SEVERE_NEAR_TERM = ['SWOMCD', 'SWODY1', "SEL0", "SEL1", "SEL2", "SEL3", "SEL4", "SEL5",\
                        "SEL6", "SEL7", "SEL8", "SEL9"]

    SPC_SVR_DAY1 = ['SWODY1']
    SPC_SVR_DAY2 = ['SWODY2']
    SPC_SVR_DAY3 = ['SWODY3']
    SPC_SVR_DAY48 = ["SWOD48"]
    MESOSCALE_DISCUSSION = ['SWOMCD']
    SPC_WATCHES = ["SEL0", "SEL1", "SEL2", "SEL3", "SEL4", "SEL5", "SEL6", "SEL7", "SEL8", "SEL9"]


    # =============================================================================
    # FIRE WEATHER - 5
    # =============================================================================
    ALL_FIRE = ['FWDDY1', 'FWDDY2', "FWDD38"]
    FIRE_OUTLOOKS = ['FWDDY1', 'FWDDY2', "FWDD38"]
    FIRE_DAY1 = ['FWDDY1']
    FIRE_DAY2 = ['FWDDY2']
    FIRE_DAY38 = ["FWDD38"]


    # =============================================================================
    # SPACE WEATHER  - 5
    # =============================================================================
    ALL_SWPC = ['ALTK04', 'ALTK05', 'ALTK06', 'ALTK07', 'ALTK08',\
                'ALTK09', 'DAYDSF', 'DAYTDF', 'DAYDIS']

    SPACE_WEATHER_WARNINGS = ['ALTK04', 'ALTK05', 'ALTK06', 'ALTK07', 'ALTK08', 'ALTK09']

    SWPC_DISCUSSION = ['DAYDIS']
    SWPC_3_DAY_FORECAST = ["DAYTDF"]
    SWPC_DAILY_SUMMARY = ["DAYDIS"]


    # =============================================================================
    # WEATHER PREDICTION CENTER - 13
    # =============================================================================
    ALL_WPC = ['FFGMPD', 'PMDSPD', 'PMDEPD', 'QPFERD', 'QPFHSD', 'PMDHMD', 'PMDHI', 'PMDAK',\
               'PMDSA', 'PMDCA', 'SCCNS1', 'SCCNS2', 'SCCNS3', 'SCCNS4', 'SCCNS5']

    WPC_NEAR_TERM = ['FFGMPD', 'PMDSPD', 'QPFERD', 'QPFHSD']
    MESOSCALE_PRECIP_DISCUSSION = ["FFGMPD"]
    SHORT_RAINGE_FORECAST_DISCUSSION = ['PMDSPD']
    EXTENDED_FORECAST_DISCUSSION = ['PMDEPD']
    EXCESSIVE_RAINFALL_DISCUSSION = ['QPFERD']
    HEAVY_SNOW_DISCUSSION = ['QPFHSD']
    MODEL_DISCUSSION = ['PMDHMD']
    ALASKA_EXTEND_DISCUSSION = ['PMDAK']
    HAWAII_EXTEND_DISCUSSION = ['PMDHI']
    SOUTH_AMERICA_DISCUSSION = ['PMDSA']
    CARRIBBEAN_DISCUSSION = ['PMDCA']
    STORM_SUMMARIES = ['SCCNS1', 'SCCNS2', 'SCCNS3', 'SCCNS4', 'SCCNS5']


    # =============================================================================
    # CLIMATE PREDICTION CENTER - 12
    # =============================================================================
    ALL_CPC = ['PMDAHU', 'PMDEPH', 'PMD30D', 'PMD90D', 'PMDDRK', 'PMDDRO',\
               'PMDENS', 'PMDHCO', 'PMDMRD', 'PMDTHR']

    SEAONAL_HURRICANE_OUTLOOKS = ['PMDAHU', 'PMDEPH']
    ATLANTIC_HURRICANE_OUTLOOK = ['PMDAHU']
    PACIFIC_HURRICANE_OUTLOOK = ['PMDEPH']
    DAY_30_OUTLOOK = ['PMD30D']
    DAY_90_OUTLOOK = ['PMD90D']
    DROUGHT_OUTLOOK = ['PMDDRK']
    DROUGHT_DISCUSSION = ['PMDDRO']
    ENSO_DISCUSSION = ['PMDENS']
    HAWAII_SEASONAL_OUTLOOK = ['PMDHCO']
    DAY_6_14_OUTLOOK = ['PMDMRD']
    HAZARDS_OUTLOOK = ['PMDTHR']


    # =============================================================================
    # NWS AFDs
    # =============================================================================

    ALL_FORECAST_DISCUSSIONS = ['AFDABQ', 'AFDABR', 'AFDAFC', 'AFDAFG', 'AFDAJK',\
                                'AFDAKQ', 'AFDALY', 'AFDAMA', 'AFDAPX', 'AFDARX',\
                                'AFDBGM', 'AFDBIS', 'AFDBMX', 'AFDBOI', 'AFDBOU',\
                                'AFDBOX', 'AFDBRO', 'AFDBTV', 'AFDBUF', 'AFDBYZ',\
                                'AFDCAE', 'AFDCAR', 'AFDCHS', 'AFDCLE', 'AFDCRP',\
                                'AFDCTP', 'AFDCYS', 'AFDDDC', 'AFDDLH', 'AFDDMX',\
                                'AFDDPQ', 'AFDDTX', 'AFDDVN', 'AFDEAX', 'AFDEKA',\
                                'AFDEPZ', 'AFDEWX', 'AFDEYW', 'AFDFFC', 'AFDFGF',\
                                'AFDFGZ', 'AFDFSD', 'AFDFWD', 'AFDGGW', 'AFDGID',\
                                'AFDGJT', 'AFDGLD', 'AFDGRB', 'AFDGRR', 'AFDGSP',\
                                'AFDGYX', 'AFDHFO', 'AFDHGX', 'AFDHNX', 'AFDHUN',\
                                'AFDICT', 'AFDILM', 'AFDILN', 'AFDILX', 'AFDIND',\
                                'AFDIWX', 'AFDJAN', 'AFDJAX', 'AFDJKL', 'AFDKEY',\
                                'AFDLBF', 'AFDLCH', 'AFDLIX', 'AFDLKN', 'AFDLMK',\
                                'AFDLOT', 'AFDLOX', 'AFDLSX', 'AFDLUB', 'AFDLWX',\
                                'AFDLZK', 'AFDMAF', 'AFDMEG', 'AFDMFL', 'AFDMFR',\
                                'AFDMHX', 'AFDMKX', 'AFDMLB', 'AFDMOB', 'AFDMPX',\
                                'AFDMQT', 'AFDMRX', 'AFDMSO', 'AFDMTR', 'AFDOAX',\
                                'AFDOHX', 'AFDOKX', 'AFDOTX', 'AFDOUN', 'AFDPAH',\
                                'AFDPBZ', 'AFDPDT', 'AFDPHI', 'AFDPIH', 'AFDPPG',\
                                'AFDPQ', 'AFDPQR', 'AFDPSR', 'AFDPUB', 'AFDRAH',\
                                'AFDREV', 'AFDRIW', 'AFDRLX', 'AFDRNK', 'AFDSDF',\
                                'AFDSEW', 'AFDSGF', 'AFDSGX', 'AFDSHV', 'AFDSJT',\
                                'AFDSJU', 'AFDSLC', 'AFDSTO', 'AFDTAE', 'AFDTBW',\
                                'AFDTFX', 'AFDTOP', 'AFDTSA', 'AFDTWC', 'AFDUNR',\
                                'AFDVEF']


    ALL_CONUS_DISCUSSIONS = ['AFDBOU', 'AFDGJT', 'AFDPUB', 'AFDLOT', 'AFDILX', 'AFDIND', 'AFDIWX',\
                             'AFDDVN', 'AFDDMX', 'AFDDDC', 'AFDGLD', 'AFDTOP', 'AFDICT', 'AFDJKL',\
                             'AFDLMK', 'AFDPAH', 'AFDDTX', 'AFDAPX', 'AFDGRR', 'AFDMQT', 'AFDDLH',\
                             'AFDMPX', 'AFDEAX', 'AFDSGF', 'AFDLSX', 'AFDGID', 'AFDLBF', 'AFDOAX',\
                             'AFDBIS', 'AFDFGF', 'AFDABR', 'AFDUNR', 'AFDFSD', 'AFDGRB', 'AFDARX',\
                             'AFDMKX', 'AFDCYS', 'AFDRIW', 'AFDSDF', 'AFDCAR', 'AFDGYX', 'AFDBOX',\
                             'AFDPHI', 'AFDALY', 'AFDBGM', 'AFDBUF', 'AFDOKX', 'AFDMHX', 'AFDILM',\
                             'AFDRAH', 'AFDILN', 'AFDCLE', 'AFDPBZ', 'AFDCTP', 'AFDCHS', 'AFDCAE',\
                             'AFDGSP', 'AFDBTV', 'AFDLWX', 'AFDRNK', 'AFDAKQ', 'AFDRLX', 'AFDKEY',\
                             'AFDEYW', 'AFDBMX', 'AFDHUN', 'AFDMOB', 'AFDLZK', 'AFDJAX', 'AFDMLB',\
                             'AFDMFL', 'AFDTAE', 'AFDTBW', 'AFDFFC', 'AFDLCH', 'AFDLIX', 'AFDSHV',\
                             'AFDJAN', 'AFDABQ', 'AFDOUN', 'AFDTSA', 'AFDMEG', 'AFDMRX', 'AFDOHX',\
                             'AFDAMA', 'AFDEWX', 'AFDBRO', 'AFDCRP', 'AFDEPZ', 'AFDFWD', 'AFDHGX',\
                             'AFDLUB', 'AFDMAF', 'AFDSJT', 'AFDFGZ', 'AFDPSR', 'AFDTWC', 'AFDEKA',\
                             'AFDLOX', 'AFDSTO', 'AFDSGX', 'AFDMTR', 'AFDHNX', 'AFDBOI', 'AFDPIH',\
                             'AFDBYZ', 'AFDGGW', 'AFDTFX', 'AFDMSO', 'AFDLKN', 'AFDVEF', 'AFDREV',\
                             'AFDMFR', 'AFDPDT', 'AFDPQR', 'AFDSLC', 'AFDSEW', 'AFDOTX']




    ATLANTIC_COASTAL_DISCUSSIONS = ['AFDKEY', 'AFDEYW', 'AFDMFL', 'AFDMLB', 'AFDJAX',\
                                    'AFDCHS', 'AFDILM', 'AFDMHX', 'AFDAKQ', 'AFDPHI',\
                                    'AFDOKX', 'AFDBOX', 'AFDGYX', 'AFDCAR']




    GULF_COASTAL_DISCUSSIONS = ['AFDBRO', 'AFDCRP', 'AFDHGX', 'AFDLCH', 'AFDLIX', 'AFDMOB',\
                                'AFDTAE', 'AFDTBW', 'AFDKEY', 'AFDEYW', 'AFDMFL']




    PACIFIC_COASTAL_DISCUSSIONS = ['AFDSEW', 'AFDPQR', 'AFDMFR', 'AFDEKA', 'AFDMTR',\
                                    'AFDLOX', 'AFDSGX', 'AFDPQ', 'AFDDPQ', 'AFDHFO',\
                                    'AFDPPG']



    EASTERN_REGION_AFD = ["AFDCAR", "AFDGYX", "AFDBOX", "AFDPHI", "AFDALY", "AFDBGM",\
                          "AFDBUF", "AFDOKX", "AFDMHX", "AFDILM", "AFDRAH", "AFDILN",\
                          "AFDCLE", "AFDPBZ", "AFDCTP", "AFDCHS", "AFDCAE", "AFDGSP",\
                          "AFDBTV", "AFDLWX", "AFDRNK", "AFDAKQ", "AFDRLX"]

    CARIBOU_ME_AFD = ["AFDCAR"]
    GRAY_PORTLAND_ME_AFD = ["AFDGYX"]
    BOSTON_MA_AFD = ["AFDBOX"]
    MT_HOLLY_PHILADELPHIA_NJ_AFD = ["AFDPHI"]
    ALBANY_NY_AFD = ["AFDALY"]
    BINGHAMTON_NY_AFD = ["AFDBGM"]
    BUFFALO_NY_AFD = ["AFDBUF"]
    NEW_YORK_CITY_NY_AFD = ["AFDOKX"]
    NEWPORT_MOREHEAD_CITY_NC_AFD = ["AFDMHX"]
    WILMINGTON_NC_AFD = ["AFDILM"]
    RALEIGH_NC_AFD = ["AFDRAH"]
    WILMINGTON_OH_AFD = ["AFDILN"]
    CLEVELAND_OH_AFD = ["AFDCLE"]
    PITTSBURGH_PA_AFD = ["AFDPBZ"]
    STATE_COLLEGE_PA_AFD = ["AFDCTP"]
    CHARLESTON_SC_AFD = ["AFDCHS"]
    COLUMBIA_SC_AFD = ["AFDCAE"]
    GREENVILLE_SPARTANBURG_SC_AFD = ["AFDGSP"]
    BURLINGTON_VT_AFD = ["AFDBTV"]
    BALTIMORE_WASHINGTON_VA_AFD = ["AFDLWX"]
    BLACKSBURG_ROANOKE_VA_AFD = ["AFDRNK"]
    WAKEFIELD_VA_AFD = ["AFDAKQ"]
    CHARLESTON_WV_AFD = ["AFDRLX"]



    CENTRAL_REGION_AFD = ["AFDBOU", "AFDGJT", "AFDPUB", "AFDLOT", "AFDILX", "AFDIND",\
                          "AFDIWX", "AFDDVN", "AFDDMX", "AFDDDC", "AFDGLD", "AFDTOP",\
                          "AFDICT", "AFDJKL", "AFDLMK", "AFDPAH", "AFDDTX", "AFDAPX",\
                          "AFDGRR", "AFDMQT", "AFDDLH", "AFDMPX", "AFDEAX", "AFDSGF",\
                          "AFDLSX", "AFDGID", "AFDLBF", "AFDOAX", "AFDBIS", "AFDFGF",\
                          "AFDABR", "AFDUNR", "AFDFSD", "AFDGRB", "AFDARX", "AFDMKX",\
                          "AFDCYS", "AFDRIW", "AFDSDF"]

    DENVER_BOULDER_CO_AFD = ["AFDBOU"]
    GRAND_JUNCTION_CO_AFD = ["AFDGJT"]
    PUEBLO_CO_AFD = ["AFDPUB"]
    CHICAGO_IL_AFD = ["AFDLOT"]
    LINCOLN_IL_AFD = ["AFDILX"]
    INDIANAPOLIS_IN_AFD = ["AFDIND"]
    NORTHERN_INDIANA_IN_AFD = ["AFDIWX"]
    QUAD_CITIES_IA_AFD = ["AFDDVN"]
    DES_MOINES_IA_AFD = ["AFDDMX"]
    DODGE_CITY_KS_AFD = ["AFDDDC"]
    GOODLAND_KS_AFD = ["AFDGLD"]
    TOPEKA_KS_AFD = ["AFDTOP"]
    WICHITA_KS_AFD = ["AFDICT"]
    JACKSON_KY_AFD = ["AFDJKL", "AFDSDF"]
    LOUISVILLE_KY_AFD = ["AFDLMK"]
    PADUCAH_KY_AFD = ["AFDPAH"]
    DETROIT_MI_AFD = ["AFDDTX"]
    GAYLORD_MI_AFD = ["AFDAPX"]
    GRAND_RAPIDS_MI_AFD = ["AFDGRR"]
    MARQUETTE_MI_AFD = ["AFDMQT"]
    DULUTH_MN_AFD = ["AFDDLH"]
    TWIN_CITIES_MN_AFD = ["AFDMPX"]
    KANSAS_CITY_MO_AFD = ["AFDEAX"]
    SPRINGFIELD_MO_AFD = ["AFDSGF"]
    ST_LOUIS_MO_AFD = ["AFDLSX"]
    HASTINGS_NE_AFD = ["AFDGID"]
    NORTH_PLATTE_NE_AFD = ["AFDLBF"]
    OMAHA_VALLEY_NE_AFD = ["AFDOAX"]
    BISMARK_ND_AFD = ["AFDBIS"]
    GRAND_FORKS_ND_AFD = ["AFDFGF"]
    ABERDEEN_SD_AFD = ["AFDABR"]
    RAPID_CITY_SD_AFD = ["AFDUNR"]
    SIOUX_FALLS_SD_AFD = ["AFDFSD"]
    GREEN_BAY_WI_AFD = ["AFDGRB"]
    LA_CROSSE_WI_AFD = ["AFDARX"]
    MILWAUKEE_SULLIVAN_WI_AFD = ["AFDMKX"]
    CHEYENNE_WY_AFD = ["AFDCYS"]
    RIVERTON_WY_AFD = ["AFDRIW"]



    WESTERN_REGION_AFD = ["AFDFGZ", "AFDPSR", "AFDTWC", "AFDEKA", "AFDLOX", "AFDSTO",\
                          "AFDSGX", "AFDMTR", "AFDHNX", "AFDBOI", "AFDPIH", "AFDBYZ",\
                          "AFDGGW", "AFDTFX", "AFDMSO", "AFDLKN", "AFDVEF", "AFDREV",\
                          "AFDMFR", "AFDPDT", "AFDPQR", "AFDSLC", "AFDSEW", "AFDOTX"]

    FLAGSTAFF_AZ_AFD = ["AFDFGZ"]
    PHOENIX_AZ_AFD = ["AFDPSR"]
    TUCSON_AZ_AFD = ["AFDTWC"]
    EUREKA_CA_AFD = ["AFDEKA"]
    LOS_ANGELES_CA_AFD = ["AFDLOX"]
    SACRAMENTO_CA_AFD = ["AFDSTO"]
    SAN_DIEGO_CA_AFD = ["AFDSGX"]
    SFO_MONTEREY_CA_AFD = ["AFDMTR"]
    HANFORD_CA_AFD = ["AFDHNX"]
    BOISE_ID_AFD = ["AFDBOI"]
    POCATELLO_ID_AFD = ["AFDPIH"]
    BILLINGS_MT_AFD = ["AFDBYZ"]
    GLASGOW_MT_AFD = ["AFDGGW"]
    GREAT_FALLS_MT_AFD = ["AFDTFX"]
    MISSOULA_MT_AFD = ["AFDMSO"]
    ELKO_NV_AFD = ["AFDLKN"]
    LAS_VEGAS_NV_AFD = ["AFDVEF"]
    RENO_NV_AFD = ["AFDREV"]
    MEDFORD_OR_AFD = ["AFDMFR"]
    PENDLETON_OR_AFD = ["AFDPDT"]
    PORTLAND_OR_AFD = ["AFDPQR"]
    SALT_LAKE_CITY_UT_AFD = ["AFDSLC"]
    SEATTLE_WA_AFD = ["AFDSEW"]
    SPOKANE_WA_AFD = ["AFDOTX"]



    SOUTHERN_REGION_AFD = ["AFDKEY", "AFDEYW", "AFDBMX", "AFDHUN", "AFDMOB", "AFDLZK",\
                       "AFDJAX", "AFDMLB", "AFDMFL", "AFDTAE", "AFDTBW", "AFDFFC",\
                       "AFDLCH", "AFDLIX", "AFDSHV", "AFDJAN", "AFDABQ", "AFDOUN",\
                       "AFDTSA", "AFDMEG", "AFDMRX", "AFDOHX", "AFDAMA", "AFDEWX",\
                       "AFDBRO", "AFDCRP", "AFDEPZ", "AFDFWD", "AFDHGX", "AFDLUB",\
                       "AFDMAF", "AFDSJT", "AFDSJU"]

    BIRMINGHAM_AL_AFD = ["AFDBMX"]
    HUNTSVILLE_AL_AFD = ["AFDHUN"]
    MOBILE_PENSACOLA_AL_AFD = ["AFDMOB"]
    LITTLE_ROCK_AR_AFD = ["AFDLZK"]
    JACKSONVILLE_FL_AFD = ["AFDJAX"]
    KEY_WEST_FL_AFD = ["AFDKEY", "AFDEYW"]
    MELBOURNE_FL_AFD = ["AFDMLB"]
    MIAMI_FL_AFD = ["AFDMFL"]
    TALLAHASSEE_FL_AFD = ["AFDTAE"]
    TAMPA_FL_AFD = ["AFDTBW"]
    ATLANTA_GA_AFD = ["AFDFFC"]
    LAKE_CHARLES_LA_AFD = ["AFDLCH"]
    NOLA_BATON_ROUGE_LA_AFD = ["AFDLIX"]
    SHREVEPORT_LA_AFD = ["AFDSHV"]
    JACKSON_MS_AFD = ["AFDJAN"]
    ALBUQUERQUE_NM_AFD = ["AFDABQ"]
    NORMAN_OKC_OK_AFD = ["AFDOUN"]
    TULSA_OK_AFD = ["AFDTSA"]
    MEMPHIS_TN_AFD = ["AFDMEG"]
    MORRISTOWN_KNOXVILLE_TN_AFD = ["AFDMRX"]
    NASHVILLE_TN_AFD = ["AFDOHX"]
    AMARILLO_TX_AFD = ["AFDAMA"]
    AUSTIN_SAN_ANTONIO_TX_AFD = ["AFDEWX"]
    BROWNSVILLE_TX_AFD = ["AFDBRO"]
    CORPUS_CHRISTI_TX_AFD = ["AFDCRP"]
    EL_PASO_TX_AFD = ["AFDEPZ"]
    FORTH_WORTH_DALLAS_TX_AFD = ["AFDFWD"]
    HOUSTON_GALVESTON_TX_AFD = ["AFDHGX"]
    LUBBOCK_TX_AFD = ["AFDLUB"]
    MIDLAND_ODESSA_TX_AFD = ["AFDMAF"]
    SAN_ANGELO_TX_AFD = ["AFDSJT"]
    SAN_JUAN_PR_AFD = ["AFDSJU"]


    PACIFIC_REGION_AFD = ["AFDPQ", "AFDDPQ", "AFDHFO", 'AFDPPG']

    GUAM_GU_AFD = ["AFDPQ", "AFDDPQ"]
    HONOLULU_HI_AFD = ["AFDHFO"]
    PAGO_AS_AFD = ['AFDPPG']

    ALASKA_REGION_AFD = ["AFDAJK", "AFDAFC", "AFDAFG"]

    ANCHORAGE_AK_AFD = ["AFDAFC"]
    FAIRBANKS_AK_AFD = ["AFDAFG"]
    JUNEAU_AK_AFD = ["AFDAJK"]

    # =============================================================================
    # NWS NOWCASTS - 147 OPTIONS
    # =============================================================================
    ALL_NOWCAST = ['NOWAJK', 'NOWAFC', 'NOWAFG', 'NOWBOU', 'NOWGJT', 'NOWPUB', 'NOWLOT',\
                   'NOWILX', 'NOWIND', 'NOWIWX', 'NOWDVN', 'NOWDMX', 'NOWDDC', 'NOWGLD',\
                   'NOWTOP', 'NOWICT', 'NOWJKL', 'NOWLMK', 'NOWPAH', 'NOWDTX', 'NOWAPX',\
                   'NOWGRR', 'NOWMQT', 'NOWDLH', 'NOWMPX', 'NOWEAX', 'NOWSGF', 'NOWLSX',\
                   'NOWGID', 'NOWLBF', 'NOWOAX', 'NOWBIS', 'NOWFGF', 'NOWABR', 'NOWUNR',\
                   'NOWFSD', 'NOWGRB', 'NOWARX', 'NOWMKX', 'NOWCYS', 'NOWRIW', 'NOWCAR',\
                   'NOWGYX', 'NOWBOX', 'NOWPHI', 'NOWALY', 'NOWBGM', 'NOWBUF', 'NOWOKX',\
                   'NOWMHX', 'NOWILM', 'NOWRAH', 'NOWILN', 'NOWCLE', 'NOWPBZ', 'NOWCTP',\
                   'NOWCHS', 'NOWCAE', 'NOWGSP', 'NOWBTV', 'NOWLWX', 'NOWRNK', 'NOWAKQ',\
                   'NOWRLX', 'NOWHFO', 'NOWSJU', 'NOWKEY', 'NOWAKN', 'NOWADQ', 'NOWMY',\
                   'NOWEYW', 'NOWBMX', 'NOWHUN', 'NOWMOB', 'NOWLZK', 'NOWJAX', 'NOWMLB',\
                   'NOWMFL', 'NOWTAE', 'NOWTBW', 'NOWFFC', 'NOWLCH', 'NOWLIX', 'NOWSHV',\
                   'NOWJAN', 'NOWABQ', 'NOWOUN', 'NOWTSA', 'NOWMEG', 'NOWMRX', 'NOWOHX',\
                   'NOWAMA', 'NOWEWX', 'NOWBRO', 'NOWCRP', 'NOWEPZ', 'NOWFWD', 'NOWHGX',\
                   'NOWLUB', 'NOWMAF', 'NOWSJT', 'NOWFGZ', 'NOWPSR', 'NOWTWC', 'NOWEKA',\
                   'NOWLOX', 'NOWSTO', 'NOWSGX', 'NOWMTR', 'NOWHNX', 'NOWBOI', 'NOWPIH',\
                   'NOWBYZ', 'NOWGGW', 'NOWTFX', 'NOWMSO', 'NOWLKN', 'NOWVEF', 'NOWREV',\
                   'NOWMFR', 'NOWPDT', 'NOWPQR', 'NOWSLC', 'NOWSEW', 'NOWOTX', 'NOWSDF',\
                   "NOWYAK", "NOWVWS", "NOWSNP", "NOWOTZ", 'NOWOME', 'NOWMCG', 'NOWCDB',\
                   'NOWBRW', 'NOWBET', 'NOWANN', 'NOWISN']





    ALL_CONUS_NOWCASTS = ['NOWBOU', 'NOWGJT', 'NOWPUB', 'NOWLOT', 'NOWILX', 'NOWIND', 'NOWIWX',\
                         'NOWDVN', 'NOWDMX', 'NOWDDC', 'NOWGLD', 'NOWTOP', 'NOWICT', 'NOWJKL',\
                         'NOWLMK', 'NOWPAH', 'NOWDTX', 'NOWAPX', 'NOWGRR', 'NOWMQT', 'NOWDLH',\
                         'NOWMPX', 'NOWEAX', 'NOWSGF', 'NOWLSX', 'NOWGID', 'NOWLBF', 'NOWOAX',\
                         'NOWBIS', 'NOWFGF', 'NOWABR', 'NOWUNR', 'NOWFSD', 'NOWGRB', 'NOWARX',\
                         'NOWMKX', 'NOWCYS', 'NOWRIW', 'NOWSDF', 'NOWCAR', 'NOWGYX', 'NOWBOX',\
                         'NOWPHI', 'NOWALY', 'NOWBGM', 'NOWBUF', 'NOWOKX', 'NOWMHX', 'NOWILM',\
                         'NOWRAH', 'NOWILN', 'NOWCLE', 'NOWPBZ', 'NOWCTP', 'NOWCHS', 'NOWCAE',\
                         'NOWGSP', 'NOWBTV', 'NOWLWX', 'NOWRNK', 'NOWAKQ', 'NOWRLX', 'NOWKEY',\
                         'NOWEYW', 'NOWBMX', 'NOWHUN', 'NOWMOB', 'NOWLZK', 'NOWJAX', 'NOWMLB',\
                         'NOWMFL', 'NOWTAE', 'NOWTBW', 'NOWFFC', 'NOWLCH', 'NOWLIX', 'NOWSHV',\
                         'NOWJAN', 'NOWABQ', 'NOWOUN', 'NOWTSA', 'NOWMEG', 'NOWMRX', 'NOWOHX',\
                         'NOWAMA', 'NOWEWX', 'NOWBRO', 'NOWCRP', 'NOWEPZ', 'NOWFWD', 'NOWHGX',\
                         'NOWLUB', 'NOWMAF', 'NOWSJT', 'NOWFGZ', 'NOWPSR', 'NOWTWC', 'NOWEKA',\
                         'NOWLOX', 'NOWSTO', 'NOWSGX', 'NOWMTR', 'NOWHNX', 'NOWBOI', 'NOWPIH',\
                         'NOWBYZ', 'NOWGGW', 'NOWTFX', 'NOWMSO', 'NOWLKN', 'NOWVEF', 'NOWREV',\
                         'NOWMFR', 'NOWPDT', 'NOWPQR', 'NOWSLC', 'NOWSEW', 'NOWOTX', 'NOWISN']




    ATLANTIC_COASTAL_NOWCASTS = ['NOWKEY', 'NOWEYW', 'NOWMFL', 'NOWMLB', 'NOWJAX',\
                                'NOWCHS', 'NOWILM', 'NOWMHX', 'NOWAKQ', 'NOWPHI',\
                                'NOWOKX', 'NOWBOX', 'NOWGYX', 'NOWCAR']




    GULF_COASTAL_NOWCASTS = ['NOWBRO', 'NOWCRP', 'NOWHGX', 'NOWLCH', 'NOWLIX', 'NOWMOB',\
                            'NOWTAE', 'NOWTBW', 'NOWKEY', 'NOWEYW', 'NOWMFL']




    PACIFIC_COASTAL_NOWCASTS = ['NOWSEW', 'NOWPQR', 'NOWMFR', 'NOWEKA', 'NOWMTR',\
                                'NOWLOX', 'NOWSGX', 'NOWHFO']




    EASTERN_REGION_NOW = ["NOWCAR", "NOWGYX", "NOWBOX", "NOWPHI", "NOWALY", "NOWBGM",\
                          "NOWBUF", "NOWOKX", "NOWMHX", "NOWILM", "NOWRAH", "NOWILN",\
                          "NOWCLE", "NOWPBZ", "NOWCTP", "NOWCHS", "NOWCAE", "NOWGSP",\
                          "NOWBTV", "NOWLWX", "NOWRNK", "NOWAKQ", "NOWRLX"]

    CARIBOU_ME_NOW = ["NOWCAR"]
    GRAY_PORTLAND_ME_NOW = ["NOWGYX"]
    BOSTON_MA_NOW = ["NOWBOX"]
    MT_HOLLY_PHILADELPHIA_NJ_NOW = ["NOWPHI"]
    ALBANY_NY_NOW = ["NOWALY"]
    BINGHAMTON_NY_NOW = ["NOWBGM"]
    BUFFALO_NY_NOW = ["NOWBUF"]
    NEW_YORK_CITY_NY_NOW = ["NOWOKX"]
    NEWPORT_MOREHEAD_CITY_NC_NOW = ["NOWMHX"]
    WILMINGTON_NC_NOW = ["NOWILM"]
    RALEIGH_NC_NOW = ["NOWRAH"]
    WILMINGTON_OH_NOW = ["NOWILN"]
    CLEVELAND_OH_NOW = ["NOWCLE"]
    PITTSBURGH_PA_NOW = ["NOWPBZ"]
    STATE_COLLEGE_PA_NOW = ["NOWCTP"]
    CHARLESTON_SC_NOW = ["NOWCHS"]
    COLUMBIA_SC_NOW = ["NOWCAE"]
    GREENVILLE_SPARTANBURG_SC_NOW = ["NOWGSP"]
    BURLINGTON_VT_NOW = ["NOWBTV"]
    BALTIMORE_WASHINGTON_VA_NOW = ["NOWLWX"]
    BLACKSBURG_ROANOKE_VA_NOW = ["NOWRNK"]
    WAKEFIELD_VA_NOW = ["NOWAKQ"]
    CHARLESTON_WV_NOW = ["NOWRLX"]



    CENTRAL_REGION_NOW = ["NOWBOU", "NOWGJT", "NOWPUB", "NOWLOT", "NOWILX", "NOWIND",\
                          "NOWIWX", "NOWDVN", "NOWDMX", "NOWDDC", "NOWGLD", "NOWTOP",\
                          "NOWICT", "NOWJKL", "NOWLMK", "NOWPAH", "NOWDTX", "NOWAPX",\
                          "NOWGRR", "NOWMQT", "NOWDLH", "NOWMPX", "NOWEAX", "NOWSGF",\
                          "NOWLSX", "NOWGID", "NOWLBF", "NOWOAX", "NOWBIS", "NOWFGF",\
                          "NOWABR", "NOWUNR", "NOWFSD", "NOWGRB", "NOWARX", "NOWMKX",\
                          "NOWCYS", "NOWRIW", 'NOWSDF', 'NOWISN']

    DENVER_BOULDER_CO_NOW = ["NOWBOU"]
    GRAND_JUNCTION_CO_NOW = ["NOWGJT"]
    PUEBLO_CO_NOW = ["NOWPUB"]
    CHICAGO_IL_NOW = ["NOWLOT"]
    LINCOLN_IL_NOW = ["NOWILX"]
    INDIANAPOLIS_IN_NOW = ["NOWIND"]
    NORTHERN_INDIANA_IN_NOW = ["NOWIWX"]
    QUAD_CITIES_IA_NOW = ["NOWDVN"]
    DES_MOINES_IA_NOW = ["NOWDMX"]
    DODGE_CITY_KS_NOW = ["NOWDDC"]
    GOODLAND_KS_NOW = ["NOWGLD"]
    TOPEKA_KS_NOW = ["NOWTOP"]
    WICHITA_KS_NOW = ["NOWICT"]
    JACKSON_KY_NOW = ["NOWJKL"]
    LOUISVILLE_KY_NOW = ["NOWLMK", 'NOWSDF']
    PADUCAH_KY_NOW = ["NOWPAH"]
    DETROIT_MI_NOW = ["NOWDTX"]
    GAYLORD_MI_NOW = ["NOWAPX"]
    GRAND_RAPIDS_MI_NOW = ["NOWGRR"]
    MARQUETTE_MI_NOW = ["NOWMQT"]
    DULUTH_MN_NOW = ["NOWDLH"]
    TWIN_CITIES_MN_NOW = ["NOWMPX"]
    KANSAS_CITY_MO_NOW = ["NOWEAX"]
    SPRINGFIELD_MO_NOW = ["NOWSGF"]
    ST_LOUIS_MO_NOW = ["NOWLSX"]
    HASTINGS_NE_NOW = ["NOWGID"]
    NORTH_PLATTE_NE_NOW = ["NOWLBF"]
    OMAHA_VALLEY_NE_NOW = ["NOWOAX"]
    BISMARK_ND_NOW = ["NOWBIS"]
    WILLISTON_ND_NOW = ['NOWISN']
    GRAND_FORKS_ND_NOW = ["NOWFGF"]
    ABERDEEN_SD_NOW = ["NOWABR"]
    RAPID_CITY_SD_NOW = ["NOWUNR"]
    SIOUX_FALLS_SD_NOW = ["NOWFSD"]
    GREEN_BAY_WI_NOW = ["NOWGRB"]
    LA_CROSSE_WI_NOW = ["NOWARX"]
    MILWAUKEE_SULLIVAN_WI_NOW = ["NOWMKX"]
    CHEYENNE_WY_NOW = ["NOWCYS"]
    RIVERTON_WY_NOW = ["NOWRIW"]



    WESTERN_REGION_NOW = ["NOWFGZ", "NOWPSR", "NOWTWC", "NOWEKA", "NOWLOX", "NOWSTO",\
                          "NOWSGX", "NOWMTR", "NOWHNX", "NOWBOI", "NOWPIH", "NOWBYZ",\
                          "NOWGGW", "NOWTFX", "NOWMSO", "NOWLKN", "NOWVEF", "NOWREV",\
                          "NOWMFR", "NOWPDT", "NOWPQR", "NOWSLC", "NOWSEW", "NOWOTX"]

    FLAGSTAFF_AZ_NOW = ["NOWFGZ"]
    PHOENIX_AZ_NOW = ["NOWPSR"]
    TUCSON_AZ_NOW = ["NOWTWC"]
    EUREKA_CA_NOW = ["NOWEKA"]
    LOS_ANGELES_CA_NOW = ["NOWLOX"]
    SACRAMENTO_CA_NOW = ["NOWSTO"]
    SAN_DIEGO_CA_NOW = ["NOWSGX"]
    SFO_MONTEREY_CA_NOW = ["NOWMTR"]
    HANFORD_CA_NOW = ["NOWHNX"]
    BOISE_ID_NOW = ["NOWBOI"]
    POCATELLO_ID_NOW = ["NOWPIH"]
    BILLINGS_MT_NOW = ["NOWBYZ"]
    GLASGOW_MT_NOW = ["NOWGGW"]
    GREAT_FALLS_MT_NOW = ["NOWTFX"]
    MISSOULA_MT_NOW = ["NOWMSO"]
    ELKO_NV_NOW = ["NOWLKN"]
    LAS_VEGAS_NV_NOW = ["NOWVEF"]
    RENO_NV_NOW = ["NOWREV"]
    MEDFORD_OR_NOW = ["NOWMFR"]
    PENDLETON_OR_NOW = ["NOWPDT"]
    PORTLAND_OR_NOW = ["NOWPQR"]
    SALT_LAKE_CITY_UT_NOW = ["NOWSLC"]
    SEATTLE_WA_NOW = ["NOWSEW"]
    SPOKANE_WA_NOW = ["NOWOTX"]



    SOUTHERN_REGION_NOW = ["NOWKEY", "NOWEYW", "NOWBMX", "NOWHUN", "NOWMOB", "NOWLZK",\
                           "NOWJAX", "NOWMLB", "NOWMFL", "NOWTAE", "NOWTBW", "NOWFFC",\
                           "NOWLCH", "NOWLIX", "NOWSHV", "NOWJAN", "NOWABQ", "NOWOUN",\
                           "NOWTSA", "NOWMEG", "NOWMRX", "NOWOHX", "NOWAMA", "NOWEWX",\
                           "NOWBRO", "NOWCRP", "NOWEPZ", "NOWFWD", "NOWHGX", "NOWLUB",\
                           "NOWMAF", "NOWSJT", "NOWSJU"]

    BIRMINGHAM_AL_NOW = ["NOWBMX"]
    HUNTSVILLE_AL_NOW = ["NOWHUN"]
    MOBILE_PENSACOLA_AL_NOW = ["NOWMOB"]
    LITTLE_ROCK_AR_NOW = ["NOWLZK"]
    JACKSONVILLE_FL_NOW = ["NOWJAX"]
    KEY_WEST_FL_NOW = ["NOWKEY", "NOWEYW"]
    MELBOURNE_FL_NOW = ["NOWMLB"]
    MIAMI_FL_NOW = ["NOWMFL"]
    TALLAHASSEE_FL_NOW = ["NOWTAE"]
    TAMPA_FL_NOW = ["NOWTBW"]
    ATLANTA_GA_NOW = ["NOWFFC"]
    LAKE_CHARLES_LA_NOW = ["NOWLCH"]
    NOLA_BATON_ROUGE_LA_NOW = ["NOWLIX"]
    SHREVEPORT_LA_NOW = ["NOWSHV"]
    JACKSON_MS_NOW = ["NOWJAN"]
    ALBUQUERQUE_NM_NOW = ["NOWABQ"]
    NORMAN_OKC_OK_NOW = ["NOWOUN"]
    TULSA_OK_NOW = ["NOWTSA"]
    MEMPHIS_TN_NOW = ["NOWMEG"]
    MORRISTOWN_KNOXVILLE_TN_NOW = ["NOWMRX"]
    NASHVILLE_TN_NOW = ["NOWOHX"]
    AMARILLO_TX_NOW = ["NOWAMA"]
    AUSTIN_SAN_ANTONIO_TX_NOW = ["NOWEWX"]
    BROWNSVILLE_TX_NOW = ["NOWBRO"]
    CORPUS_CHRISTI_TX_NOW = ["NOWCRP"]
    EL_PASO_TX_NOW = ["NOWEPZ"]
    FORTH_WORTH_DALLAS_TX_NOW = ["NOWFWD"]
    HOUSTON_GALVESTON_TX_NOW = ["NOWHGX"]
    LUBBOCK_TX_NOW = ["NOWLUB"]
    MIDLAND_ODESSA_TX_NOW = ["NOWMAF"]
    SAN_ANGELO_TX_NOW = ["NOWSJT"]
    SAN_JUAN_PR_NOW = ["NOWSJU"] #NOWSPN (SPANISH)

    PACIFIC_REGION_NOW = ["NOWHFO", 'NOWMY']

    HONOLULU_HI_NOW = ["NOWHFO"]
    TIYAN_GU_NOW = ['NOWMY']


    ALASKA_REGION_NOW = ["NOWAJK", "NOWAFC", "NOWAFG", "NOWYAK", "NOWVWS", "NOWSNP", "NOWOTZ",\
                         'NOWOME', 'NOWMCG', 'NOWCDB', 'NOWBRW', 'NOWBET', 'NOWANN', 'NOWAKN',\
                         'NOWADQ']

    ANCHORAGE_AK_NOW = ["NOWAFC"]
    FAIRBANKS_AK_NOW = ["NOWAFG"]
    JUNEAU_AK_NOW = ["NOWAJK"]
    YAKUTAT_AK_NOW = ["NOWYAK"]
    VALDEZ_AK_NOW = ["NOWVWS"]
    ST_PAUL_AK_NOW = ["NOWSNP"]
    KOTZEBUE_AK_NOW = ["NOWOTZ"]
    NOME_AK_NOW = ['NOWOME']
    MCGRATH_AK_NOW = ['NOWMCG']
    COLD_BAY_AK_NOW = ['NOWCDB']
    BARROW_AK_NOW = ['NOWBRW']
    BETHEL_AK_NOW = ['NOWBET']
    ANNETTE_AK_NOW = ['NOWANN']
    KING_SALMON_AK_NOW = ['NOWAKN']
    KODIAK_AK_NOW = ['NOWADQ']


    # =============================================================================
    # SPECIAL CONFIGURATIONS
    # =============================================================================
    BLUE_HEN_SPECIAL = ["AFDPHI", "NOWPHI", "SMWPHI", "TORPHI", "SVRPHI", "SVSPHI",\
                        "LSRPHI", "HWOPHI", "FFAPHI", "FFSPHI", "FFWPHI", "FLSPHI",\
                        "FLWPHI", "PNSPHI", "WSWPHI"]

    ERIC_ALLEN_SPECIAL = ["AFDLWX", "NOWLWX", "SMWLWX", "TORLWX", "SVRLWX", "SVSLWX",\
                          "LSRLWX", "HWOLWX", "FFALWX", "FFSLWX", "FFWLWX", "FLSLWX",\
                          "FLWLWX", "PNSLWX", "WSWLWX"]



    MASTER_LIST = ['AFDABQ', 'AFDABR', 'AFDAFC', 'AFDAFG', 'AFDAJK', 'AFDAKQ',\
                   'AFDALY', 'AFDAMA', 'AFDAPX', 'AFDARX', 'AFDBGM', 'AFDBIS',\
                   'AFDBMX', 'AFDBOI', 'AFDBOU', 'AFDBOX', 'AFDBRO', 'AFDBTV',\
                   'AFDBUF', 'AFDBYZ', 'AFDCAE', 'AFDCAR', 'AFDCHS', 'AFDCLE',\
                   'AFDCRP', 'AFDCTP', 'AFDCYS', 'AFDDDC', 'AFDDLH', 'AFDDMX',\
                   'AFDDPQ', 'AFDDTX', 'AFDDVN', 'AFDEAX', 'AFDEKA', 'AFDEPZ',\
                   'AFDEWX', 'AFDEYW', 'AFDFFC', 'AFDFGF', 'AFDFGZ', 'AFDFSD',\
                   'AFDFWD', 'AFDGGW', 'AFDGID', 'AFDGJT', 'AFDGLD', 'AFDGRB',\
                   'AFDGRR', 'AFDGSP', 'AFDGYX', 'AFDHFO', 'AFDHGX', 'AFDHNX',\
                   'AFDHUN', 'AFDICT', 'AFDILM', 'AFDILN', 'AFDILX', 'AFDIND',\
                   'AFDIWX', 'AFDJAN', 'AFDJAX', 'AFDJKL', 'AFDKEY', 'AFDLBF',\
                   'AFDLCH', 'AFDLIX', 'AFDLKN', 'AFDLMK', 'AFDLOT', 'AFDLOX',\
                   'AFDLSX', 'AFDLUB', 'AFDLWX', 'AFDLZK', 'AFDMAF', 'AFDMEG',\
                   'AFDMFL', 'AFDMFR', 'AFDMHX', 'AFDMKX', 'AFDMLB', 'AFDMOB',\
                   'AFDMPX', 'AFDMQT', 'AFDMRX', 'AFDMSO', 'AFDMTR', 'AFDOAX',\
                   'AFDOHX', 'AFDOKX', 'AFDOTX', 'AFDOUN', 'AFDPAH', 'AFDPBZ',\
                   'AFDPDT', 'AFDPHI', 'AFDPIH', 'AFDPPG', 'AFDPQ', 'AFDPQR',\
                   'AFDPSR', 'AFDPUB', 'AFDRAH', 'AFDREV', 'AFDRIW', 'AFDRLX',\
                   'AFDRNK', 'AFDSDF', 'AFDSEW', 'AFDSGF', 'AFDSGX', 'AFDSHV',\
                   'AFDSJT', 'AFDSJU', 'AFDSLC', 'AFDSTO', 'AFDTAE', 'AFDTBW',\
                   'AFDTFX', 'AFDTOP', 'AFDTSA', 'AFDTWC', 'AFDUNR', 'AFDVEF',\
                   'ALTK04', 'ALTK05', 'ALTK06', 'ALTK07', 'ALTK08', 'ALTK09',\
                   'DAYDIS', 'DAYDSF', 'DAYTDF', 'FFALWX', 'FFAPHI', 'FFGMPD',\
                   'FFSLWX', 'FFSPHI', 'FFWLWX', 'FFWPHI', 'FLSLWX', 'FLSPHI',\
                   'FLWLWX', 'FLWPHI', 'FWDD38', 'FWDDY1', 'FWDDY2', 'HSFAT1',\
                   'HSFAT2', 'HSFEP', 'HSFEP1', 'HSFEP2', 'HSFEP3', 'HSFEPI',\
                   'HSFNP', 'HSFSP', 'HWOLWX', 'HWOPHI', 'LSRABQ', 'LSRABR',\
                   'LSRAFC', 'LSRAFG', 'LSRAJK', 'LSRAKQ', 'LSRALY', 'LSRAMA',\
                   'LSRAPX', 'LSRARX', 'LSRBGM', 'LSRBIS', 'LSRBMX', 'LSRBOI',\
                   'LSRBOU', 'LSRBOX', 'LSRBRO', 'LSRBRW', 'LSRBTV', 'LSRBUF',\
                   'LSRBYZ', 'LSRCAE', 'LSRCAR', 'LSRCDB', 'LSRCHS', 'LSRCLE',\
                   'LSRCRP', 'LSRCTP', 'LSRCYS', 'LSRDDC', 'LSRDLH', 'LSRDMX',\
                   'LSRDTX', 'LSRDVN', 'LSREAX', 'LSREKA', 'LSREPZ', 'LSREWX',\
                   'LSRFFC', 'LSRFGF', 'LSRFGZ', 'LSRFSD', 'LSRFWD', 'LSRGGW',\
                   'LSRGID', 'LSRGJT', 'LSRGLD', 'LSRGRB', 'LSRGRR', 'LSRGSP',\
                   'LSRGUM', 'LSRGYX', 'LSRHFO', 'LSRHGX', 'LSRHNX', 'LSRHUN',\
                   'LSRICT', 'LSRILM', 'LSRILN', 'LSRILX', 'LSRIND', 'LSRISN',\
                   'LSRIWX', 'LSRJAN', 'LSRJAX', 'LSRJKL', 'LSRKEY', 'LSRLBF',\
                   'LSRLCH', 'LSRLIX', 'LSRLKN', 'LSRLMK', 'LSRLOT', 'LSRLOX',\
                   'LSRLSX', 'LSRLUB', 'LSRLWX', 'LSRLZK', 'LSRMAF', 'LSRMEG',\
                   'LSRMFL', 'LSRMFR', 'LSRMHX', 'LSRMKX', 'LSRMLB', 'LSRMOB',\
                   'LSRMPX', 'LSRMQT', 'LSRMRX', 'LSRMSO', 'LSRMTR', 'LSRNY1',\
                   'LSRNY2', 'LSRNY3', 'LSRNY4', 'LSRNY7', 'LSROAX', 'LSROHX',\
                   'LSROKX', 'LSROTX', 'LSROUN', 'LSRPAH', 'LSRPBZ', 'LSRPDT',\
                   'LSRPHI', 'LSRPIH', 'LSRPQR', 'LSRPSR', 'LSRPUB', 'LSRRAH',\
                   'LSRREV', 'LSRRIW', 'LSRRLX', 'LSRRNK', 'LSRSEW', 'LSRSGF',\
                   'LSRSGX', 'LSRSHV', 'LSRSJT', 'LSRSJU', 'LSRSLC', 'LSRSTO',\
                   'LSRTAE', 'LSRTBW', 'LSRTFX', 'LSRTOP', 'LSRTSA', 'LSRTWC',\
                   'LSRUNR', 'LSRVEF', 'LSRVWS', 'MIMATN', 'MIMATS', 'MIMPAC',\
                   'NOWABQ', 'NOWABR', 'NOWADQ', 'NOWAFC', 'NOWAFG', 'NOWAJK',\
                   'NOWAKN', 'NOWAKQ', 'NOWALY', 'NOWAMA', 'NOWANN', 'NOWAPX',\
                   'NOWARX', 'NOWBET', 'NOWBGM', 'NOWBIS', 'NOWBMX', 'NOWBOI',\
                   'NOWBOU', 'NOWBOX', 'NOWBRO', 'NOWBRW', 'NOWBTV', 'NOWBUF',\
                   'NOWBYZ', 'NOWCAE', 'NOWCAR', 'NOWCDB', 'NOWCHS', 'NOWCLE',\
                   'NOWCRP', 'NOWCTP', 'NOWCYS', 'NOWDDC', 'NOWDLH', 'NOWDMX',\
                   'NOWDTX', 'NOWDVN', 'NOWEAX', 'NOWEKA', 'NOWEPZ', 'NOWEWX',\
                   'NOWEYW', 'NOWFFC', 'NOWFGF', 'NOWFGZ', 'NOWFSD', 'NOWFWD',\
                   'NOWGGW', 'NOWGID', 'NOWGJT', 'NOWGLD', 'NOWGRB', 'NOWGRR',\
                   'NOWGSP', 'NOWGYX', 'NOWHFO', 'NOWHGX', 'NOWHNX', 'NOWHUN',\
                   'NOWICT', 'NOWILM', 'NOWILN', 'NOWILX', 'NOWIND', 'NOWISN',\
                   'NOWIWX', 'NOWJAN', 'NOWJAX', 'NOWJKL', 'NOWKEY', 'NOWLBF',\
                   'NOWLCH', 'NOWLIX', 'NOWLKN', 'NOWLMK', 'NOWLOT', 'NOWLOX',\
                   'NOWLSX', 'NOWLUB', 'NOWLWX', 'NOWLZK', 'NOWMAF', 'NOWMCG',\
                   'NOWMEG', 'NOWMFL', 'NOWMFR', 'NOWMHX', 'NOWMKX', 'NOWMLB',\
                   'NOWMOB', 'NOWMPX', 'NOWMQT', 'NOWMRX', 'NOWMSO', 'NOWMTR',\
                   'NOWMY', 'NOWOAX', 'NOWOHX', 'NOWOKX', 'NOWOME', 'NOWOTX',\
                   'NOWOTZ', 'NOWOUN', 'NOWPAH', 'NOWPBZ', 'NOWPDT', 'NOWPHI',\
                   'NOWPIH', 'NOWPQR', 'NOWPSR', 'NOWPUB', 'NOWRAH', 'NOWREV',\
                   'NOWRIW', 'NOWRLX', 'NOWRNK', 'NOWSDF', 'NOWSEW', 'NOWSGF',\
                   'NOWSGX', 'NOWSHV', 'NOWSJT', 'NOWSJU', 'NOWSLC', 'NOWSNP',\
                   'NOWSTO', 'NOWTAE', 'NOWTBW', 'NOWTFX', 'NOWTOP', 'NOWTSA',\
                   'NOWTWC', 'NOWUNR', 'NOWVEF', 'NOWVWS', 'NOWYAK', 'OFFAER',\
                   'OFFAFG', 'OFFAJK', 'OFFALU', 'OFFHFO', 'OFFN01', 'OFFN02',\
                   'OFFN03', 'OFFN04', 'OFFN05', 'OFFN06', 'OFFN07', 'OFFN08',\
                   'OFFN09', 'OFFN10', 'OFFN11', 'OFFN12', 'OFFN13', 'OFFN14',\
                   'OFFN15', 'OFFNT1', 'OFFNT2', 'OFFNT3', 'OFFNT4', 'OFFPZ5',\
                   'OFFPZ6', 'PMD30D', 'PMD90D', 'PMDAHU', 'PMDAK', 'PMDCA',\
                   'PMDDRK', 'PMDDRO', 'PMDENS', 'PMDEPD', 'PMDEPH', 'PMDHCO',\
                   'PMDHI', 'PMDHMD', 'PMDMRD', 'PMDSA', 'PMDSPD', 'PMDTHR',\
                   'PNSLWX', 'PNSPHI', 'QPFERD', 'QPFHSD', 'SCCNS1', 'SCCNS2',\
                   'SCCNS3', 'SCCNS4', 'SCCNS5', 'SEL0', 'SEL1', 'SEL2', 'SEL3',\
                   'SEL4', 'SEL5', 'SEL6', 'SEL7', 'SEL8', 'SEL9', 'SMWLWX',\
                   'SMWPHI', 'SVRLWX', 'SVRPHI', 'SVSLWX', 'SVSPHI', 'SWOD48',\
                   'SWODY1', 'SWODY2', 'SWODY3', 'SWOMCD', 'TCDAT1', 'TCDAT2',\
                   'TCDAT3', 'TCDAT4', 'TCDAT5', 'TCDCP1', 'TCDCP2', 'TCDCP3',\
                   'TCDCP4', 'TCDCP5', 'TCDEP1', 'TCDEP2', 'TCDEP3', 'TCDEP4',\
                   'TCDEP5', 'TCPAT1', 'TCPAT2', 'TCPAT3', 'TCPAT4', 'TCPAT5',\
                   'TCPCP1', 'TCPCP2', 'TCPCP3', 'TCPCP4', 'TCPCP5', 'TCPEP1',\
                   'TCPEP2', 'TCPEP3', 'TCPEP4', 'TCPEP5', 'TCUAT', 'TCUAT1',\
                   'TCUAT2', 'TCUAT3', 'TCUAT4', 'TCUAT5', 'TCUCP1', 'TCUCP2',\
                   'TCUCP3', 'TCUCP4', 'TCUCP5', 'TCUEP', 'TCUEP1', 'TCUEP2',\
                   'TCUEP3', 'TCUEP4', 'TCUEP5', 'TORLWX', 'TORPHI', 'TWDAT',\
                   'TWDEP', 'WSWLWX', 'WSWPHI', "LSRADQ", "LSRAKN", "LSRANN",\
                   "LSRAT1", "LSRBA1", "LSRBET", "LSRBH1", "LSRBR1", "LSRCS1",\
                   "LSRHO1", "LSRJM1", "LSRMCG", "LSRNK1", "LSRNY5", "LSRNY6",\
                   "LSROME", "LSROTZ", "LSRPPG", "LSRSNP", "LSRTD1", "LSRYAK",\
                   "VOWLWX", "VOWPHI"]
