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

    ALL = ['AFDABQ', 'AFDABR', 'AFDAFC', 'AFDAFG', 'AFDAJK', 'AFDAKQ', 'AFDALY',
           'AFDAMA', 'AFDAPX', 'AFDARX', 'AFDBGM', 'AFDBIS', 'AFDBMX', 'AFDBOI',
           'AFDBOU', 'AFDBOX', 'AFDBRO', 'AFDBTV', 'AFDBUF', 'AFDBYZ', 'AFDCAE',
           'AFDCAR', 'AFDCHS', 'AFDCLE', 'AFDCRP', 'AFDCTP', 'AFDCYS', 'AFDDDC',
           'AFDDLH', 'AFDDMX', 'AFDDPQ', 'AFDDTX', 'AFDDVN', 'AFDEAX', 'AFDEKA',
           'AFDEPZ', 'AFDEWX', 'AFDEYW', 'AFDFFC', 'AFDFGF', 'AFDFGZ', 'AFDFSD',
           'AFDFWD', 'AFDGGW', 'AFDGID', 'AFDGJT', 'AFDGLD', 'AFDGRB', 'AFDGRR',
           'AFDGSP', 'AFDGYX', 'AFDHFO', 'AFDHGX', 'AFDHNX', 'AFDHUN', 'AFDICT',
           'AFDILM', 'AFDILN', 'AFDILX', 'AFDIND', 'AFDIWX', 'AFDJAN', 'AFDJAX',
           'AFDJKL', 'AFDKEY', 'AFDLBF', 'AFDLCH', 'AFDLIX', 'AFDLKN', 'AFDLMK',
           'AFDLOT', 'AFDLOX', 'AFDLSX', 'AFDLUB', 'AFDLWX', 'AFDLZK', 'AFDMAF',
           'AFDMEG', 'AFDMFL', 'AFDMFR', 'AFDMHX', 'AFDMKX', 'AFDMLB', 'AFDMOB',
           'AFDMPX', 'AFDMQT', 'AFDMRX', 'AFDMSO', 'AFDMTR', 'AFDOAX', 'AFDOHX',
           'AFDOKX', 'AFDOTX', 'AFDOUN', 'AFDPAH', 'AFDPBZ', 'AFDPDT', 'AFDPHI',
           'AFDPIH', 'AFDPPG', 'AFDPQ', 'AFDPQR', 'AFDPSR', 'AFDPUB', 'AFDRAH',
           'AFDREV', 'AFDRIW', 'AFDRLX', 'AFDRNK', 'AFDSDF', 'AFDSEW', 'AFDSGF',
           'AFDSGX', 'AFDSHV', 'AFDSJT', 'AFDSJU', 'AFDSLC', 'AFDSTO', 'AFDTAE',
           'AFDTBW', 'AFDTFX', 'AFDTOP', 'AFDTSA', 'AFDTWC', 'AFDUNR', 'AFDVEF',
           'ALTK04', 'ALTK05', 'ALTK06', 'ALTK07', 'ALTK08', 'ALTK09', 'DAYDIS',
           'DAYDSF', 'DAYTDF', 'FFGMPD', 'FWDD38', 'FWDDY1', 'FWDDY2', 'HSFAT1',
           'HSFAT2', 'HSFEP', 'HSFEP1', 'HSFEP2', 'HSFEP3', 'HSFEPI', 'HSFNP',
           'HSFSP', 'LSRABQ', 'LSRABR', 'LSRAFC', 'LSRAFG', 'LSRAJK', 'LSRAKN',
           'LSRAKQ', 'LSRALY', 'LSRAMA', 'LSRAPX', 'LSRARX', 'LSRBGM', 'LSRBIS',
           'LSRBMX', 'LSRBOI', 'LSRBOU', 'LSRBOX', 'LSRBRO', 'LSRBRW', 'LSRBTV',
           'LSRBUF', 'LSRBYZ', 'LSRCAE', 'LSRCAR', 'LSRCDB', 'LSRCHS', 'LSRCLE',
           'LSRCRP', 'LSRCTP', 'LSRCYS', 'LSRDDC', 'LSRDLH', 'LSRDMX', 'LSRDTX',
           'LSRDVN', 'LSREAX', 'LSREKA', 'LSREPZ', 'LSREWX', 'LSRFFC', 'LSRFGF',
           'LSRFGZ', 'LSRFSD', 'LSRFWD', 'LSRGGW', 'LSRGID', 'LSRGJT', 'LSRGLD',
           'LSRGRB', 'LSRGRR', 'LSRGSP', 'LSRGUM', 'LSRGYX', 'LSRHFO', 'LSRHGX',
           'LSRHNX', 'LSRHUN', 'LSRICT', 'LSRILM', 'LSRILN', 'LSRILX', 'LSRIND',
           'LSRISN', 'LSRIWX', 'LSRJAN', 'LSRJAX', 'LSRJKL', 'LSRKEY', 'LSRLBF',
           'LSRLCH', 'LSRLIX', 'LSRLKN', 'LSRLMK', 'LSRLOT', 'LSRLOX', 'LSRLSX',
           'LSRLUB', 'LSRLWX', 'LSRLZK', 'LSRMAF', 'LSRMCG', 'LSRMEG', 'LSRMFL',
           'LSRMFR', 'LSRMHX', 'LSRMKX', 'LSRMLB', 'LSRMOB', 'LSRMPX', 'LSRMQT',
           'LSRMRX', 'LSRMSO', 'LSRMTR', 'LSRNY1', 'LSRNY2', 'LSRNY3', 'LSRNY4',
           'LSRNY7', 'LSROAX', 'LSROHX', 'LSROKX', 'LSROTX', 'LSROUN', 'LSRPAH',
           'LSRPBZ', 'LSRPDT', 'LSRPHI', 'LSRPIH', 'LSRPPG', 'LSRPQR', 'LSRPSR',
           'LSRPUB', 'LSRRAH', 'LSRREV', 'LSRRIW', 'LSRRLX', 'LSRRNK', 'LSROME',
           'LSRSEW', 'LSRSGF', 'LSRSGX', 'LSRSHV', 'LSRSJT', 'LSRSJU', 'LSRSLC',
           'LSRSTO', 'LSRTAE', 'LSRTBW', 'LSRTFX', 'LSRTOP', 'LSRTSA', 'LSRTWC',
           'LSRUNR', 'LSRVEF', 'LSRVWS', 'MIMATN', 'MIMATS', 'MIMPAC', 'NOWABQ',
           'NOWABR', 'NOWADQ', 'NOWAFC', 'NOWAFG', 'NOWAJK', 'NOWAKN', 'NOWAKQ',
           'NOWALY', 'NOWAMA', 'NOWANN', 'NOWAPX', 'NOWARX', 'NOWBET', 'NOWBGM',
           'NOWBIS', 'NOWBMX', 'NOWBOI', 'NOWBOU', 'NOWBOX', 'NOWBRO', 'NOWBRW',
           'NOWBTV', 'NOWBUF', 'NOWBYZ', 'NOWCAE', 'NOWCAR', 'NOWCDB', 'NOWCHS',
           'NOWCLE', 'NOWCRP', 'NOWCTP', 'NOWCYS', 'NOWDDC', 'NOWDLH', 'NOWDMX',
           'NOWDTX', 'NOWDVN', 'NOWEAX', 'NOWEKA', 'NOWEPZ', 'NOWEWX', 'NOWEYW',
           'NOWFFC', 'NOWFGF', 'NOWFGZ', 'NOWFSD', 'NOWFWD', 'NOWGGW', 'NOWGID',
           'NOWGJT', 'NOWGLD', 'NOWGRB', 'NOWGRR', 'NOWGSP', 'NOWGYX', 'NOWHFO',
           'NOWHGX', 'NOWHNX', 'NOWHUN', 'NOWICT', 'NOWILM', 'NOWILN', 'NOWILX',
           'NOWIND', 'NOWISN', 'NOWIWX', 'NOWJAN', 'NOWJAX', 'NOWJKL', 'NOWKEY',
           'NOWLBF', 'NOWLCH', 'NOWLIX', 'NOWLKN', 'NOWLMK', 'NOWLOT', 'NOWLOX',
           'NOWLSX', 'NOWLUB', 'NOWLWX', 'NOWLZK', 'NOWMAF', 'NOWMCG', 'NOWMEG',
           'NOWMFL', 'NOWMFR', 'NOWMHX', 'NOWMKX', 'NOWMLB', 'NOWMOB', 'NOWMPX',
           'NOWMQT', 'NOWMRX', 'NOWMSO', 'NOWMTR', 'NOWMY', 'NOWOAX', 'NOWOHX',
           'NOWOKX', 'NOWOME', 'NOWOTX', 'NOWOTZ', 'NOWOUN', 'NOWPAH', 'NOWPBZ',
           'NOWPDT', 'NOWPHI', 'NOWPIH', 'NOWPQR', 'NOWPSR', 'NOWPUB', 'NOWRAH',
           'NOWREV', 'NOWRIW', 'NOWRLX', 'NOWRNK', 'NOWSDF', 'NOWSEW', 'NOWSGF',
           'NOWSGX', 'NOWSHV', 'NOWSJT', 'NOWSJU', 'NOWSLC', 'NOWSNP', 'NOWSTO',
           'NOWTAE', 'NOWTBW', 'NOWTFX', 'NOWTOP', 'NOWTSA', 'NOWTWC', 'NOWUNR',
           'NOWVEF', 'NOWVWS', 'NOWYAK', 'OFFAER', 'OFFAFG', 'OFFAJK', 'OFFALU',
           'OFFHFO', 'OFFN01', 'OFFN02', 'OFFN03', 'OFFN04', 'OFFN05', 'OFFN06',
           'OFFN07', 'OFFN08', 'OFFN09', 'OFFN10', 'OFFN11', 'OFFN12', 'OFFN13',
           'OFFN14', 'OFFN15', 'OFFNT1', 'OFFNT2', 'OFFNT3', 'OFFNT4', 'OFFPZ5',
           'OFFPZ6', 'PMD30D', 'PMD90D', 'PMDAHU', 'PMDAK', 'PMDCA', 'PMDDRK',
           'PMDDRO', 'PMDENS', 'PMDEPD', 'PMDEPH', 'PMDHCO', 'PMDHI', 'PMDHMD',
           'PMDMRD', 'PMDSA', 'PMDSPD', 'PMDTHR', 'QPFERD', 'QPFHSD', 'SCCNS1',
           'SCCNS2', 'SCCNS3', 'SCCNS4', 'SCCNS5', 'SEL0', 'SEL1', 'SEL2', 'SEL3',
           'SEL4', 'SEL5', 'SEL6', 'SEL7', 'SEL8', 'SEL9', 'SWOD48', 'SWODY1',
           'SWODY2', 'SWODY3', 'SWOMCD', 'TCDAT1', 'TCDAT2', 'TCDAT3', 'TCDAT4',
           'TCDAT5', 'TCDCP1', 'TCDCP2', 'TCDCP3', 'TCDCP4', 'TCDCP5', 'TCDEP1',
           'TCDEP2', 'TCDEP3', 'TCDEP4', 'TCDEP5', 'TCPAT1', 'TCPAT2', 'TCPAT3',
           'TCPAT4', 'TCPAT5', 'TCPCP1', 'TCPCP2', 'TCPCP3', 'TCPCP4', 'TCPCP5',
           'TCPEP1', 'TCPEP2', 'TCPEP3', 'TCPEP4', 'TCPEP5', 'TCUAT', 'TCUAT1',
           'TCUAT2', 'TCUAT3', 'TCUAT4', 'TCUAT5', 'TCUCP1', 'TCUCP2', 'TCUCP3',
           'TCUCP4', 'TCUCP5', 'TCUEP', 'TCUEP1', 'TCUEP2', 'TCUEP3', 'TCUEP4',
           'TCUEP5', 'TWDAT', 'TWDEP']

    #26 products as a part of the "Special" cases
    Downloaded_Not_Included = ['FFSLWX', 'FFSPHI', 'FFWLWX', 'FFWPHI', 'FLSLWX',
                               'FLSPHI', 'FLWLWX', 'FLWPHI', 'WSWLWX', 'WSWPHI',
                               'SVRLWX', 'SVRPHI', 'SVSLWX',
                               'SVSPHI', 'TORLWX', 'TORPHI', 'PNSLWX', 'PNSPHI',
                               'FFALWX', 'FFAPHI', 'HWOLWX', 'HWOPHI']

    #23 products were deleted upon download.
    #Empty_Data = ["VOWLWX", "VOWPHI", "LSRADQ", "LSRANN", "LSRAT1", "LSRBA1", \
    #"LSRBET", "LSRBH1", "LSRBR1", "LSRCS1", "LSRHO1", "LSRJM1",\
    #"LSRNK1", "LSRNY5", "LSRNY6", "LSROTZ", "LSRSNP", "LSRTD1",\
    #"LSRYAK"] #END OF EMPTY DATA

    """

    BELOW ARE THE SPECIFIC FORECASTS THAT GO WITH EACH OPTION IN ~/Documentation/Preset_Options.txt

    """

    ALL_LSR = ['LSRABQ', 'LSRABR', 'LSRAFC', 'LSRAFG', 'LSRAJK', 'LSRAKN',
               'LSRAKQ', 'LSRALY', 'LSRAMA', 'LSRAPX', 'LSRARX',
               'LSRBGM', 'LSRBIS', 'LSRBMX', 'LSRBOI', 'LSRBOU', 'LSRBOX',
               'LSRBRO', 'LSRBRW', 'LSRBTV', 'LSRBUF', 'LSRBYZ',
               'LSRCAE', 'LSRCAR', 'LSRCDB', 'LSRCHS', 'LSRCLE', 'LSRCRP',
               'LSRCTP', 'LSRCYS', 'LSRDDC', 'LSRDLH', 'LSRDMX',
               'LSRDTX', 'LSRDVN', 'LSREAX', 'LSREKA', 'LSREPZ', 'LSREWX',
               'LSRFFC', 'LSRFGF', 'LSRFGZ', 'LSRFSD', 'LSRFWD',
               'LSRGGW', 'LSRGID', 'LSRGJT', 'LSRGLD', 'LSRGRB', 'LSRGRR',
               'LSRGSP', 'LSRGUM', 'LSRGYX', 'LSRHFO', 'LSRHGX',
               'LSRHNX', 'LSRHUN', 'LSRICT', 'LSRILM', 'LSRILN', 'LSRILX',
               'LSRIND', 'LSRISN', 'LSRIWX', 'LSRJAN', 'LSRJAX',
               'LSRJKL', 'LSRKEY', 'LSRLBF', 'LSRLCH', 'LSRLIX', 'LSRLKN',
               'LSRLMK', 'LSRLOT', 'LSRLOX', 'LSRLSX', 'LSRLUB',
               'LSRLWX', 'LSRLZK', 'LSRMAF', 'LSRMCG', 'LSRMEG', 'LSRMFL',
               'LSRMFR', 'LSRMHX', 'LSRMKX', 'LSRMLB', 'LSRMOB',
               'LSRMPX', 'LSRMQT', 'LSRMRX', 'LSRMSO', 'LSRMTR', 'LSRNY1',
               'LSRNY2', 'LSRNY3', 'LSRNY4', 'LSRNY7', 'LSROAX',
               'LSROHX', 'LSROKX', 'LSROTX', 'LSROUN', 'LSRPAH', 'LSRPBZ',
               'LSRPDT', 'LSRPHI', 'LSRPIH', 'LSRPPG', 'LSRPQR',
               'LSRPSR', 'LSRPUB', 'LSRRAH', 'LSRREV', 'LSRRIW', 'LSRRLX',
               'LSRRNK', 'LSROME', 'LSRSEW', 'LSRSGF', 'LSRSGX',
               'LSRSHV', 'LSRSJT', 'LSRSJU', 'LSRSLC', 'LSRSTO', 'LSRTAE',
               'LSRTBW', 'LSRTFX', 'LSRTOP', 'LSRTSA', 'LSRTWC',
               'LSRUNR', 'LSRVEF', 'LSRVWS']

    ALL_NCEP = ['ALTK04', 'ALTK05', 'ALTK06', 'ALTK07', 'ALTK08', 'ALTK09', 'DAYDIS', 'DAYDSF',
                'DAYTDF', 'FFGMPD', 'FWDD38', 'FWDDY1', 'FWDDY2', 'HSFAT1', 'HSFAT2', 'HSFEP',
                'HSFEP1', 'HSFEP2', 'HSFEP3', 'HSFEPI', 'HSFNP', 'HSFSP', 'MIMATN', 'MIMATS',
                'MIMPAC', 'OFFAER', 'OFFAFG', 'OFFAJK', 'OFFALU', 'OFFHFO', 'OFFN01', 'OFFN02',
                'OFFN03', 'OFFN04', 'OFFN05', 'OFFN06', 'OFFN07', 'OFFN08', 'OFFN09', 'OFFN10',
                'OFFN11', 'OFFN12', 'OFFN13', 'OFFN14', 'OFFN15', 'OFFNT1', 'OFFNT2', 'OFFNT3',
                'OFFNT4', 'OFFPZ5', 'OFFPZ6', 'PMD30D', 'PMD90D', 'PMDAHU', 'PMDAK', 'PMDCA',
                'PMDDRK', 'PMDDRO', 'PMDENS', 'PMDEPD', 'PMDEPH', 'PMDHCO', 'PMDHI', 'PMDHMD',
                'PMDMRD', 'PMDSA', 'PMDSPD', 'PMDTHR', 'QPFERD', 'QPFHSD', 'SCCNS1', 'SCCNS2',
                'SCCNS3', 'SCCNS4', 'SCCNS5', 'SEL0', 'SEL1', 'SEL2', 'SEL3', 'SEL4',
                'SEL5', 'SEL6', 'SEL7', 'SEL8', 'SEL9', 'SWOD48', 'SWODY1', 'SWODY2',
                'SWODY3', 'SWOMCD', 'TCDAT1', 'TCDAT2', 'TCDAT3', 'TCDAT4', 'TCDAT5', 'TCDCP1',
                'TCDCP2', 'TCDCP3', 'TCDCP4', 'TCDCP5', 'TCDEP1', 'TCDEP2', 'TCDEP3', 'TCDEP4',
                'TCDEP5', 'TCPAT1', 'TCPAT2', 'TCPAT3', 'TCPAT4', 'TCPAT5', 'TCPCP1', 'TCPCP2',
                'TCPCP3', 'TCPCP4', 'TCPCP5', 'TCPEP1', 'TCPEP2', 'TCPEP3', 'TCPEP4', 'TCPEP5',
                'TCUAT', 'TCUAT1', 'TCUAT2', 'TCUAT3', 'TCUAT4', 'TCUAT5', 'TCUCP1', 'TCUCP2',
                'TCUCP3', 'TCUCP4', 'TCUCP5', 'TCUEP', 'TCUEP1', 'TCUEP2', 'TCUEP3', 'TCUEP4',
                'TCUEP5', 'TWDAT', 'TWDEP']

    # =============================================================================
    # OCEAN PREDICTION CENTER - 9
    # =============================================================================
    #All OPC:
    ALL_OPC = ["MIMPAC", "OFFAER", "OFFAFG", "OFFAJK", "OFFALU", "OFFN11", "OFFN12",
               "OFFN13", "OFFN14", "OFFN15", "HSFEP3", "HSFSP", "OFFHFO", "OFFN10",
               "HSFEPI", "HSFEP", "OFFN07", "OFFN08", "OFFN09", "OFFPZ5", "OFFPZ6",
               "HSFEP1", "MIMATN", "MIMATS", "OFFN01", "OFFN02", "OFFN03",
               "OFFN04", "OFFN05", "OFFN06", "OFFNT1", "OFFNT2", "OFFNT3", "OFFNT4",
               "HSFAT1", "HSFAT2", 'HSFEP2', 'HSFNP']

    #Pacific OPC:
    PACIFIC_OPC = ["MIMPAC", "OFFAER", "OFFAFG", "OFFAJK", "OFFALU", "OFFN11", "OFFN12",
                   "OFFN13", "OFFN14", "OFFN15", "HSFEP3", "HSFSP", "OFFHFO", "OFFN10",
                   "HSFEPI", "HSFEP", "OFFN07", "OFFN08", "OFFN09", "OFFPZ5", "OFFPZ6",
                   "HSFEP1", "HSFEP2", 'HSFNP']

    #Pacific US:
    PACIFIC_US_OPC = ["MIMPAC", "OFFN07", "OFFN08", "OFFN09", "OFFPZ5", "OFFPZ6",
                      "HSFEP1", "HSFEP2", "HSFEPI", 'HSFNP']

    #Alaska OPC:
    ALASKA_OPC = ["MIMPAC", "OFFAER", "OFFAFG", "OFFAJK", "OFFALU", "OFFN11",
                  "OFFN12", "OFFN13", "OFFN14", "OFFN15"]

    #Hawaii/Pacific Tropical OPC:
    HAWAII_TROP_PAC_OPC = ["OFFHFO", "OFFN10", "HSFEPI", "HSFEP", 'HSFNP']

    #SH Pacific OPC:
    SH_PACIFIC_OPC = ["HSFEP3", "HSFSP"]

    #Atlantic OPC:
    ATLANTIC_OPC = ["MIMATN", "MIMATS", "OFFN01", "OFFN02", "OFFN03", "OFFN04",
                    "OFFN05", "OFFN06", "OFFNT1", "OFFNT2", "OFFNT3", "OFFNT4",
                    "HSFAT1", "HSFAT2"]

    #N. Atlantic OPC:
    NORTH_ATLANTIC_OPC = ["MIMATN", "OFFN01",
                          "OFFN02", "OFFNT1", "OFFNT2", "HSFAT1"]

    #Tropical Atlantic OPC:
    TROPICAL_ATLANTIC_OPC = ["MIMATS", "OFFN03", "OFFN04", "OFFN05", "OFFN06",
                             "OFFNT3", "OFFNT4", "HSFAT2"]

    # =============================================================================
    # NATIONAL HURRICANE CENTER - 17
    # =============================================================================
    ALL_NHC = ['TWDAT', 'TCUAT', 'TCUAT1', 'TCUAT2', 'TCUAT3', 'TCUAT4', 'TCUAT5',
               'TCDAT1', 'TCDAT2', 'TCDAT3', 'TCDAT4', 'TCDAT5', 'TCPAT1', 'TCPAT2',
               'TCPAT3', 'TCPAT4', 'TCPAT5', 'TCUCP1', 'TCUCP2', 'TCUCP3', 'TCUCP4',
               'TCUCP5', 'TCDCP1', 'TCDCP2', 'TCDCP3', 'TCDCP4', 'TCDCP5', 'TCPCP1',
               'TCPCP2', 'TCPCP3', 'TCPCP4', 'TCPCP5', 'TWDEP', 'TCUEP', 'TCUEP1',
               'TCUEP2', 'TCUEP3', 'TCUEP4', 'TCUEP5', 'TCDEP1', 'TCDEP2', 'TCDEP3',
               'TCDEP4', 'TCDEP5', 'TCPEP1', 'TCPEP2', 'TCPEP3', 'TCPEP4', 'TCPEP5']

    # ATLANTIC TROPICAL CYCLONES
    ATLANTIC_TC = ['TWDAT', 'TCUAT', 'TCUAT1', 'TCUAT2', 'TCUAT3', 'TCUAT4', 'TCUAT5',
                   'TCDAT1', 'TCDAT2', 'TCDAT3', 'TCDAT4', 'TCDAT5', 'TCPAT1', 'TCPAT2',
                   'TCPAT3', 'TCPAT4', 'TCPAT5']

    ATLANTIC_TC_UPDATE = ['TCUAT', 'TCUAT1',
                          'TCUAT2', 'TCUAT3', 'TCUAT4', 'TCUAT5']

    ATLANTIC_TC_DISCUSSION = ['TWDAT', 'TCDAT1',
                              'TCDAT2', 'TCDAT3', 'TCDAT4', 'TCDAT5']

    ATLANTIC_TC_ADVISORIES = ['TCPAT1', 'TCPAT2', 'TCPAT3', 'TCPAT4', 'TCPAT5']

    # PACIFIC TROPICAL CYCLONES
    PACIFIC_TC = ['TCUCP1', 'TCUCP2', 'TCUCP3', 'TCUCP4', 'TCUCP5', 'TCDCP1', 'TCDCP2',
                  'TCDCP3', 'TCDCP4', 'TCDCP5', 'TCPCP1', 'TCPCP2', 'TCPCP3', 'TCPCP4',
                  'TCPCP5', 'TWDEP', 'TCUEP', 'TCUEP1', 'TCUEP2', 'TCUEP3', 'TCUEP4',
                  'TCUEP5', 'TCDEP1', 'TCDEP2', 'TCDEP3', 'TCDEP4', 'TCDEP5', 'TCPEP1',
                  'TCPEP2', 'TCPEP3', 'TCPEP4', 'TCPEP5']

    PACIFIC_TC_UPDATE = ['TCUCP1', 'TCUCP2', 'TCUCP3', 'TCUCP4', 'TCUCP5', 'TCUEP',
                         'TCUEP1', 'TCUEP2', 'TCUEP3', 'TCUEP4', 'TCUEP5']

    PACIFIC_TC_DISCUSSION = ['TCDCP1', 'TCDCP2', 'TCDCP3', 'TCDCP4', 'TCDCP5', 'TWDEP',
                             'TCDEP1', 'TCDEP2', 'TCDEP3', 'TCDEP4', 'TCDEP5']

    PACIFIC_TC_ADVISORIES = ['TCPCP1', 'TCPCP2', 'TCPCP3', 'TCPCP4', 'TCPCP5', 'TCPEP1',
                             'TCPEP2', 'TCPEP3', 'TCPEP4', 'TCPEP5']

    # CENTRAL PACIFIC CYCLONES
    CENTRAL_PACIFIC_TC = ['TCUCP1', 'TCUCP2', 'TCUCP3', 'TCUCP4', 'TCUCP5', 'TCDCP1',
                          'TCDCP2', 'TCDCP3', 'TCDCP4', 'TCDCP5', 'TCPCP1', 'TCPCP2',
                          'TCPCP3', 'TCPCP4', 'TCPCP5']

    CENTRAL_PACIFIC_TC_UPDATE = [
        'TCUCP1', 'TCUCP2', 'TCUCP3', 'TCUCP4', 'TCUCP5']

    CENTRAL_PACIFIC_TC_DISCUSSION = [
        'TCDCP1', 'TCDCP2', 'TCDCP3', 'TCDCP4', 'TCDCP5']

    CENTRAL_PACIFIC_TC_ADVISORIES = [
        'TCPCP1', 'TCPCP2', 'TCPCP3', 'TCPCP4', 'TCPCP5']

    # EASTERN PACIFIC CYCLONES
    EASTERN_PACIFIC_TC = ['TWDEP', 'TCUEP', 'TCUEP1', 'TCUEP2', 'TCUEP3', 'TCUEP4',
                          'TCUEP5', 'TCDEP1', 'TCDEP2', 'TCDEP3', 'TCDEP4', 'TCDEP5',
                          'TCPEP1', 'TCPEP2', 'TCPEP3', 'TCPEP4', 'TCPEP5']

    EASTERN_PACIFIC_TC_UPDATE = ['TCUEP', 'TCUEP1',
                                 'TCUEP2', 'TCUEP3', 'TCUEP4', 'TCUEP5']

    EASTERN_PACIFIC_TC_DISCUSSION = [
        'TWDEP', 'TCDEP1', 'TCDEP2', 'TCDEP3', 'TCDEP4', 'TCDEP5']

    EASTERN_PACIFIC_TC_ADVISORIES = [
        'TCPEP1', 'TCPEP2', 'TCPEP3', 'TCPEP4', 'TCPEP5']

    # =============================================================================
    # SPC SEVERE WEATHER - 9
    # =============================================================================
    ALL_SPC = ['SWOMCD', 'SWODY1', 'SWODY2', 'SWODY3', "SWOD48", "SEL0", "SEL1", "SEL2",
               "SEL3", "SEL4", "SEL5", "SEL6", "SEL7", "SEL8", "SEL9"]

    SPC_SVR_OUTLOOKS = ['SWODY1', 'SWODY2', 'SWODY3', "SWOD48"]

    SEVERE_NEAR_TERM = ['SWOMCD', 'SWODY1', "SEL0", "SEL1", "SEL2", "SEL3", "SEL4", "SEL5",
                        "SEL6", "SEL7", "SEL8", "SEL9"]

    SPC_SVR_DAY1 = ['SWODY1']
    SPC_SVR_DAY2 = ['SWODY2']
    SPC_SVR_DAY3 = ['SWODY3']
    SPC_SVR_DAY48 = ["SWOD48"]
    MESOSCALE_DISCUSSION = ['SWOMCD']
    SPC_WATCHES = ["SEL0", "SEL1", "SEL2", "SEL3",
                   "SEL4", "SEL5", "SEL6", "SEL7", "SEL8", "SEL9"]

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
    ALL_SWPC = ['ALTK04', 'ALTK05', 'ALTK06', 'ALTK07', 'ALTK08',
                'ALTK09', 'DAYDSF', 'DAYTDF', 'DAYDIS']

    SPACE_WEATHER_WARNINGS = ['ALTK04', 'ALTK05',
                              'ALTK06', 'ALTK07', 'ALTK08', 'ALTK09']

    SWPC_DISCUSSION = ['DAYDIS']
    SWPC_3_DAY_FORECAST = ["DAYTDF"]
    SWPC_DAILY_SUMMARY = ["DAYDIS"]

    # =============================================================================
    # WEATHER PREDICTION CENTER - 13
    # =============================================================================
    ALL_WPC = ['FFGMPD', 'PMDSPD', 'PMDEPD', 'QPFERD', 'QPFHSD', 'PMDHMD', 'PMDHI', 'PMDAK',
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
    ALL_CPC = ['PMDAHU', 'PMDEPH', 'PMD30D', 'PMD90D', 'PMDDRK', 'PMDDRO',
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

    ALL_FORECAST_DISCUSSIONS = ['AFDABQ', 'AFDABR', 'AFDAFC', 'AFDAFG', 'AFDAJK',
                                'AFDAKQ', 'AFDALY', 'AFDAMA', 'AFDAPX', 'AFDARX',
                                'AFDBGM', 'AFDBIS', 'AFDBMX', 'AFDBOI', 'AFDBOU',
                                'AFDBOX', 'AFDBRO', 'AFDBTV', 'AFDBUF', 'AFDBYZ',
                                'AFDCAE', 'AFDCAR', 'AFDCHS', 'AFDCLE', 'AFDCRP',
                                'AFDCTP', 'AFDCYS', 'AFDDDC', 'AFDDLH', 'AFDDMX',
                                'AFDDPQ', 'AFDDTX', 'AFDDVN', 'AFDEAX', 'AFDEKA',
                                'AFDEPZ', 'AFDEWX', 'AFDEYW', 'AFDFFC', 'AFDFGF',
                                'AFDFGZ', 'AFDFSD', 'AFDFWD', 'AFDGGW', 'AFDGID',
                                'AFDGJT', 'AFDGLD', 'AFDGRB', 'AFDGRR', 'AFDGSP',
                                'AFDGYX', 'AFDHFO', 'AFDHGX', 'AFDHNX', 'AFDHUN',
                                'AFDICT', 'AFDILM', 'AFDILN', 'AFDILX', 'AFDIND',
                                'AFDIWX', 'AFDJAN', 'AFDJAX', 'AFDJKL', 'AFDKEY',
                                'AFDLBF', 'AFDLCH', 'AFDLIX', 'AFDLKN', 'AFDLMK',
                                'AFDLOT', 'AFDLOX', 'AFDLSX', 'AFDLUB', 'AFDLWX',
                                'AFDLZK', 'AFDMAF', 'AFDMEG', 'AFDMFL', 'AFDMFR',
                                'AFDMHX', 'AFDMKX', 'AFDMLB', 'AFDMOB', 'AFDMPX',
                                'AFDMQT', 'AFDMRX', 'AFDMSO', 'AFDMTR', 'AFDOAX',
                                'AFDOHX', 'AFDOKX', 'AFDOTX', 'AFDOUN', 'AFDPAH',
                                'AFDPBZ', 'AFDPDT', 'AFDPHI', 'AFDPIH', 'AFDPPG',
                                'AFDPQ', 'AFDPQR', 'AFDPSR', 'AFDPUB', 'AFDRAH',
                                'AFDREV', 'AFDRIW', 'AFDRLX', 'AFDRNK', 'AFDSDF',
                                'AFDSEW', 'AFDSGF', 'AFDSGX', 'AFDSHV', 'AFDSJT',
                                'AFDSJU', 'AFDSLC', 'AFDSTO', 'AFDTAE', 'AFDTBW',
                                'AFDTFX', 'AFDTOP', 'AFDTSA', 'AFDTWC', 'AFDUNR',
                                'AFDVEF']

    ALL_CONUS_DISCUSSIONS = ['AFDBOU', 'AFDGJT', 'AFDPUB', 'AFDLOT', 'AFDILX', 'AFDIND', 'AFDIWX',
                             'AFDDVN', 'AFDDMX', 'AFDDDC', 'AFDGLD', 'AFDTOP', 'AFDICT', 'AFDJKL',
                             'AFDLMK', 'AFDPAH', 'AFDDTX', 'AFDAPX', 'AFDGRR', 'AFDMQT', 'AFDDLH',
                             'AFDMPX', 'AFDEAX', 'AFDSGF', 'AFDLSX', 'AFDGID', 'AFDLBF', 'AFDOAX',
                             'AFDBIS', 'AFDFGF', 'AFDABR', 'AFDUNR', 'AFDFSD', 'AFDGRB', 'AFDARX',
                             'AFDMKX', 'AFDCYS', 'AFDRIW', 'AFDSDF', 'AFDCAR', 'AFDGYX', 'AFDBOX',
                             'AFDPHI', 'AFDALY', 'AFDBGM', 'AFDBUF', 'AFDOKX', 'AFDMHX', 'AFDILM',
                             'AFDRAH', 'AFDILN', 'AFDCLE', 'AFDPBZ', 'AFDCTP', 'AFDCHS', 'AFDCAE',
                             'AFDGSP', 'AFDBTV', 'AFDLWX', 'AFDRNK', 'AFDAKQ', 'AFDRLX', 'AFDKEY',
                             'AFDEYW', 'AFDBMX', 'AFDHUN', 'AFDMOB', 'AFDLZK', 'AFDJAX', 'AFDMLB',
                             'AFDMFL', 'AFDTAE', 'AFDTBW', 'AFDFFC', 'AFDLCH', 'AFDLIX', 'AFDSHV',
                             'AFDJAN', 'AFDABQ', 'AFDOUN', 'AFDTSA', 'AFDMEG', 'AFDMRX', 'AFDOHX',
                             'AFDAMA', 'AFDEWX', 'AFDBRO', 'AFDCRP', 'AFDEPZ', 'AFDFWD', 'AFDHGX',
                             'AFDLUB', 'AFDMAF', 'AFDSJT', 'AFDFGZ', 'AFDPSR', 'AFDTWC', 'AFDEKA',
                             'AFDLOX', 'AFDSTO', 'AFDSGX', 'AFDMTR', 'AFDHNX', 'AFDBOI', 'AFDPIH',
                             'AFDBYZ', 'AFDGGW', 'AFDTFX', 'AFDMSO', 'AFDLKN', 'AFDVEF', 'AFDREV',
                             'AFDMFR', 'AFDPDT', 'AFDPQR', 'AFDSLC', 'AFDSEW', 'AFDOTX']

    ATLANTIC_COASTAL_DISCUSSIONS = ['AFDKEY', 'AFDEYW', 'AFDMFL', 'AFDMLB', 'AFDJAX',
                                    'AFDCHS', 'AFDILM', 'AFDMHX', 'AFDAKQ', 'AFDPHI',
                                    'AFDOKX', 'AFDBOX', 'AFDGYX', 'AFDCAR']

    GULF_COASTAL_DISCUSSIONS = ['AFDBRO', 'AFDCRP', 'AFDHGX', 'AFDLCH', 'AFDLIX', 'AFDMOB',
                                'AFDTAE', 'AFDTBW', 'AFDKEY', 'AFDEYW', 'AFDMFL']

    PACIFIC_COASTAL_DISCUSSIONS = ['AFDSEW', 'AFDPQR', 'AFDMFR', 'AFDEKA', 'AFDMTR',
                                   'AFDLOX', 'AFDSGX', 'AFDPQ', 'AFDDPQ', 'AFDHFO',
                                   'AFDPPG']

    EASTERN_REGION_AFD = ["AFDCAR", "AFDGYX", "AFDBOX", "AFDPHI", "AFDALY", "AFDBGM",
                          "AFDBUF", "AFDOKX", "AFDMHX", "AFDILM", "AFDRAH", "AFDILN",
                          "AFDCLE", "AFDPBZ", "AFDCTP", "AFDCHS", "AFDCAE", "AFDGSP",
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

    CENTRAL_REGION_AFD = ["AFDBOU", "AFDGJT", "AFDPUB", "AFDLOT", "AFDILX", "AFDIND",
                          "AFDIWX", "AFDDVN", "AFDDMX", "AFDDDC", "AFDGLD", "AFDTOP",
                          "AFDICT", "AFDJKL", "AFDLMK", "AFDPAH", "AFDDTX", "AFDAPX",
                          "AFDGRR", "AFDMQT", "AFDDLH", "AFDMPX", "AFDEAX", "AFDSGF",
                          "AFDLSX", "AFDGID", "AFDLBF", "AFDOAX", "AFDBIS", "AFDFGF",
                          "AFDABR", "AFDUNR", "AFDFSD", "AFDGRB", "AFDARX", "AFDMKX",
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

    WESTERN_REGION_AFD = ["AFDFGZ", "AFDPSR", "AFDTWC", "AFDEKA", "AFDLOX", "AFDSTO",
                          "AFDSGX", "AFDMTR", "AFDHNX", "AFDBOI", "AFDPIH", "AFDBYZ",
                          "AFDGGW", "AFDTFX", "AFDMSO", "AFDLKN", "AFDVEF", "AFDREV",
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

    SOUTHERN_REGION_AFD = ["AFDKEY", "AFDEYW", "AFDBMX", "AFDHUN", "AFDMOB", "AFDLZK",
                           "AFDJAX", "AFDMLB", "AFDMFL", "AFDTAE", "AFDTBW", "AFDFFC",
                           "AFDLCH", "AFDLIX", "AFDSHV", "AFDJAN", "AFDABQ", "AFDOUN",
                           "AFDTSA", "AFDMEG", "AFDMRX", "AFDOHX", "AFDAMA", "AFDEWX",
                           "AFDBRO", "AFDCRP", "AFDEPZ", "AFDFWD", "AFDHGX", "AFDLUB",
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
    ALL_NOWCAST = ['NOWAJK', 'NOWAFC', 'NOWAFG', 'NOWBOU', 'NOWGJT', 'NOWPUB', 'NOWLOT',
                   'NOWILX', 'NOWIND', 'NOWIWX', 'NOWDVN', 'NOWDMX', 'NOWDDC', 'NOWGLD',
                   'NOWTOP', 'NOWICT', 'NOWJKL', 'NOWLMK', 'NOWPAH', 'NOWDTX', 'NOWAPX',
                   'NOWGRR', 'NOWMQT', 'NOWDLH', 'NOWMPX', 'NOWEAX', 'NOWSGF', 'NOWLSX',
                   'NOWGID', 'NOWLBF', 'NOWOAX', 'NOWBIS', 'NOWFGF', 'NOWABR', 'NOWUNR',
                   'NOWFSD', 'NOWGRB', 'NOWARX', 'NOWMKX', 'NOWCYS', 'NOWRIW', 'NOWCAR',
                   'NOWGYX', 'NOWBOX', 'NOWPHI', 'NOWALY', 'NOWBGM', 'NOWBUF', 'NOWOKX',
                   'NOWMHX', 'NOWILM', 'NOWRAH', 'NOWILN', 'NOWCLE', 'NOWPBZ', 'NOWCTP',
                   'NOWCHS', 'NOWCAE', 'NOWGSP', 'NOWBTV', 'NOWLWX', 'NOWRNK', 'NOWAKQ',
                   'NOWRLX', 'NOWHFO', 'NOWSJU', 'NOWKEY', 'NOWAKN', 'NOWADQ', 'NOWMY',
                   'NOWEYW', 'NOWBMX', 'NOWHUN', 'NOWMOB', 'NOWLZK', 'NOWJAX', 'NOWMLB',
                   'NOWMFL', 'NOWTAE', 'NOWTBW', 'NOWFFC', 'NOWLCH', 'NOWLIX', 'NOWSHV',
                   'NOWJAN', 'NOWABQ', 'NOWOUN', 'NOWTSA', 'NOWMEG', 'NOWMRX', 'NOWOHX',
                   'NOWAMA', 'NOWEWX', 'NOWBRO', 'NOWCRP', 'NOWEPZ', 'NOWFWD', 'NOWHGX',
                   'NOWLUB', 'NOWMAF', 'NOWSJT', 'NOWFGZ', 'NOWPSR', 'NOWTWC', 'NOWEKA',
                   'NOWLOX', 'NOWSTO', 'NOWSGX', 'NOWMTR', 'NOWHNX', 'NOWBOI', 'NOWPIH',
                   'NOWBYZ', 'NOWGGW', 'NOWTFX', 'NOWMSO', 'NOWLKN', 'NOWVEF', 'NOWREV',
                   'NOWMFR', 'NOWPDT', 'NOWPQR', 'NOWSLC', 'NOWSEW', 'NOWOTX', 'NOWSDF',
                   "NOWYAK", "NOWVWS", "NOWSNP", "NOWOTZ", 'NOWOME', 'NOWMCG', 'NOWCDB',
                   'NOWBRW', 'NOWBET', 'NOWANN', 'NOWISN']

    ALL_CONUS_NOWCASTS = ['NOWBOU', 'NOWGJT', 'NOWPUB', 'NOWLOT', 'NOWILX', 'NOWIND', 'NOWIWX',
                          'NOWDVN', 'NOWDMX', 'NOWDDC', 'NOWGLD', 'NOWTOP', 'NOWICT', 'NOWJKL',
                          'NOWLMK', 'NOWPAH', 'NOWDTX', 'NOWAPX', 'NOWGRR', 'NOWMQT', 'NOWDLH',
                          'NOWMPX', 'NOWEAX', 'NOWSGF', 'NOWLSX', 'NOWGID', 'NOWLBF', 'NOWOAX',
                          'NOWBIS', 'NOWFGF', 'NOWABR', 'NOWUNR', 'NOWFSD', 'NOWGRB', 'NOWARX',
                          'NOWMKX', 'NOWCYS', 'NOWRIW', 'NOWSDF', 'NOWCAR', 'NOWGYX', 'NOWBOX',
                          'NOWPHI', 'NOWALY', 'NOWBGM', 'NOWBUF', 'NOWOKX', 'NOWMHX', 'NOWILM',
                          'NOWRAH', 'NOWILN', 'NOWCLE', 'NOWPBZ', 'NOWCTP', 'NOWCHS', 'NOWCAE',
                          'NOWGSP', 'NOWBTV', 'NOWLWX', 'NOWRNK', 'NOWAKQ', 'NOWRLX', 'NOWKEY',
                          'NOWEYW', 'NOWBMX', 'NOWHUN', 'NOWMOB', 'NOWLZK', 'NOWJAX', 'NOWMLB',
                          'NOWMFL', 'NOWTAE', 'NOWTBW', 'NOWFFC', 'NOWLCH', 'NOWLIX', 'NOWSHV',
                          'NOWJAN', 'NOWABQ', 'NOWOUN', 'NOWTSA', 'NOWMEG', 'NOWMRX', 'NOWOHX',
                          'NOWAMA', 'NOWEWX', 'NOWBRO', 'NOWCRP', 'NOWEPZ', 'NOWFWD', 'NOWHGX',
                          'NOWLUB', 'NOWMAF', 'NOWSJT', 'NOWFGZ', 'NOWPSR', 'NOWTWC', 'NOWEKA',
                          'NOWLOX', 'NOWSTO', 'NOWSGX', 'NOWMTR', 'NOWHNX', 'NOWBOI', 'NOWPIH',
                          'NOWBYZ', 'NOWGGW', 'NOWTFX', 'NOWMSO', 'NOWLKN', 'NOWVEF', 'NOWREV',
                          'NOWMFR', 'NOWPDT', 'NOWPQR', 'NOWSLC', 'NOWSEW', 'NOWOTX', 'NOWISN']

    ATLANTIC_COASTAL_NOWCASTS = ['NOWKEY', 'NOWEYW', 'NOWMFL', 'NOWMLB', 'NOWJAX',
                                 'NOWCHS', 'NOWILM', 'NOWMHX', 'NOWAKQ', 'NOWPHI',
                                 'NOWOKX', 'NOWBOX', 'NOWGYX', 'NOWCAR']

    GULF_COASTAL_NOWCASTS = ['NOWBRO', 'NOWCRP', 'NOWHGX', 'NOWLCH', 'NOWLIX', 'NOWMOB',
                             'NOWTAE', 'NOWTBW', 'NOWKEY', 'NOWEYW', 'NOWMFL']

    PACIFIC_COASTAL_NOWCASTS = ['NOWSEW', 'NOWPQR', 'NOWMFR', 'NOWEKA', 'NOWMTR',
                                'NOWLOX', 'NOWSGX', 'NOWHFO']

    EASTERN_REGION_NOW = ["NOWCAR", "NOWGYX", "NOWBOX", "NOWPHI", "NOWALY", "NOWBGM",
                          "NOWBUF", "NOWOKX", "NOWMHX", "NOWILM", "NOWRAH", "NOWILN",
                          "NOWCLE", "NOWPBZ", "NOWCTP", "NOWCHS", "NOWCAE", "NOWGSP",
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

    CENTRAL_REGION_NOW = ["NOWBOU", "NOWGJT", "NOWPUB", "NOWLOT", "NOWILX", "NOWIND",
                          "NOWIWX", "NOWDVN", "NOWDMX", "NOWDDC", "NOWGLD", "NOWTOP",
                          "NOWICT", "NOWJKL", "NOWLMK", "NOWPAH", "NOWDTX", "NOWAPX",
                          "NOWGRR", "NOWMQT", "NOWDLH", "NOWMPX", "NOWEAX", "NOWSGF",
                          "NOWLSX", "NOWGID", "NOWLBF", "NOWOAX", "NOWBIS", "NOWFGF",
                          "NOWABR", "NOWUNR", "NOWFSD", "NOWGRB", "NOWARX", "NOWMKX",
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

    WESTERN_REGION_NOW = ["NOWFGZ", "NOWPSR", "NOWTWC", "NOWEKA", "NOWLOX", "NOWSTO",
                          "NOWSGX", "NOWMTR", "NOWHNX", "NOWBOI", "NOWPIH", "NOWBYZ",
                          "NOWGGW", "NOWTFX", "NOWMSO", "NOWLKN", "NOWVEF", "NOWREV",
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

    SOUTHERN_REGION_NOW = ["NOWKEY", "NOWEYW", "NOWBMX", "NOWHUN", "NOWMOB", "NOWLZK",
                           "NOWJAX", "NOWMLB", "NOWMFL", "NOWTAE", "NOWTBW", "NOWFFC",
                           "NOWLCH", "NOWLIX", "NOWSHV", "NOWJAN", "NOWABQ", "NOWOUN",
                           "NOWTSA", "NOWMEG", "NOWMRX", "NOWOHX", "NOWAMA", "NOWEWX",
                           "NOWBRO", "NOWCRP", "NOWEPZ", "NOWFWD", "NOWHGX", "NOWLUB",
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
    SAN_JUAN_PR_NOW = ["NOWSJU"]  # NOWSPN (SPANISH)

    PACIFIC_REGION_NOW = ["NOWHFO", 'NOWMY']

    HONOLULU_HI_NOW = ["NOWHFO"]
    TIYAN_GU_NOW = ['NOWMY']

    ALASKA_REGION_NOW = ["NOWAJK", "NOWAFC", "NOWAFG", "NOWYAK", "NOWVWS", "NOWSNP", "NOWOTZ",
                         'NOWOME', 'NOWMCG', 'NOWCDB', 'NOWBRW', 'NOWBET', 'NOWANN', 'NOWAKN',
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
    # SPECIAL MARINE WARNINGS
    # =============================================================================
    ALL_SMWS = [
        'SMWKEY', 'SMWEYW', 'SMWMFL', 'SMWMLB', 'SMWJAX',
        'SMWCHS', 'SMWILM', 'SMWMHX', 'SMWAKQ', 'SMWPHI',
        'SMWOKX', 'SMWBOX', 'SMWGYX', 'SMWCAR', 'SMWBRO',
        'SMWCRP', 'SMWHGX', 'SMWLCH', 'SMWLIX', 'SMWMOB',
        'SMWTAE', 'SMWTBW', 'SMWKEY', 'SMWEYW', 'SMWMFL',
        'SMWSEW', 'SMWPQR', 'SMWMFR', 'SMWEKA', 'SMWMTR',
        'SMWLOX', 'SMWLWX', 'SMWSGX', 'SMWPQ', 'SMWDPQ',
        'SMWHFO', 'SMWPPG', 'SMWSJU', "SMWAPX", "SMWCLE",
        "SMWDLH", "SMWDTX", "SMWGRB", "SMWGRR", "SMWIWX",
        "SMWMKX", "SMWMQT"]

    NEWPORT_MOREHEAD_CITY_NC_SMW = ["SMWMHX"]
    WILMINGTON_NC_SMW = ["SMWILM"]
    WAKEFIELD_VA_SMW = ["SMWAKQ"]
    CHARLESTON_SC_SMW = ["SMWCHS"]
    SAN_JUAN_PR_SMW = ["SMWSJU"]

    GREAT_LAKES_SMWS = ["SMWAPX", "SMWCLE", "SMWDLH", "SMWDTX", "SMWGRB", "SMWGRR",
                        "SMWIWX", "SMWMKX", "SMWMQT"]

    ATLANTIC_COASTAL_SMWS = ['SMWKEY', 'SMWEYW', 'SMWMFL', 'SMWMLB', 'SMWJAX',
                             'SMWCHS', 'SMWILM', 'SMWMHX', 'SMWAKQ', 'SMWLWX', 'SMWPHI',
                             'SMWOKX', 'SMWBOX', 'SMWGYX', 'SMWCAR']

    GULF_COASTAL_SMWS = ['SMWBRO', 'SMWCRP', 'SMWHGX', 'SMWLCH', 'SMWLIX', 'SMWMOB',
                         'SMWTAE', 'SMWTBW', 'SMWKEY', 'SMWEYW', 'SMWMFL']

    PACIFIC_COASTAL_SMWS = ['SMWSEW', 'SMWPQR', 'SMWMFR', 'SMWEKA', 'SMWMTR',
                            'SMWLOX', 'SMWSGX', 'SMWPQ', 'SMWDPQ', 'SMWHFO',
                            'SMWPPG']

    NC_SMW_PLUS_AKQ = ["SMWMHX", "SMWILM", "SMWCHS", "SMWAKQ"]

    GREAT_LAKES_MWS = ["MWSCLE", "MWSDTX", "MWSAPX", "MWSBUF"]

    # =============================================================================
    # ADMINISTRATIVE MESSAGES
    # =============================================================================
    ALL_ADMINISTRATIVE_EMERGENCY_PRODUCTS = [
        "ADRABQ", "ADRABQ", "ADRABR", "ADRADQ", "ADRAFC", "ADRAFG", "ADRAJK",
        "ADRAK", "ADRAKN", "ADRAKQ", "ADRAKQ", "ADRAL", "ADRALB", "ADRALY",
        "ADRALY", "ADRAMA", "ADRAPX", "ADRAPX", "ADRAR", "ADRARX", "ADRARX",
        "ADRAS", "ADRAZ", "ADRBET", "ADRBGM", "ADRBGM", "ADRBIS", "ADRBIS",
        "ADRBMX", "ADRBOI", "ADRBOU", "ADRBOU", "ADRBOX", "ADRBOX", "ADRBRO",
        "ADRBRW", "ADRBTV", "ADRBTV", "ADRBUF", "ADRBUF", "ADRBYZ", "ADRCA",
        "ADRCAE", "ADRCAE", "ADRCAR", "ADRCAR", "ADRCDB", "ADRCHS", "ADRCHS",
        "ADRCLE", "ADRCLE", "ADRCO", "ADRCRP", "ADRCT", "ADRCTP", "ADRCTP",
        "ADRCYS", "ADRDC", "ADRDDC", "ADRDE", "ADRDLH", "ADRDMX", "ADRDMX",
        "ADRDTX", "ADRDVN", "ADREAX", "ADREKA", "ADREPZ", "ADREVV", "ADREWX",
        "ADRFFC", "ADRFGF", "ADRFGF", "ADRFGZ", "ADRFL", "ADRFSD", "ADRFWD",
        "ADRGA", "ADRGGW", "ADRGID", "ADRGJT", "ADRGJT", "ADRGLD", "ADRGRB",
        "ADRGRB", "ADRGRR", "ADRGSP", "ADRGSP", "ADRGU", "ADRGUM", "ADRGUM",
        "ADRGYX", "ADRGYX", "ADRHFO", "ADRHFO", "ADRHGX", "ADRHI", "ADRHNX",
        "ADRHUN", "ADRIA", "ADRICT", "ADRID", "ADRIL", "ADRILM", "ADRILM",
        "ADRILN", "ADRILN", "ADRILX", "ADRILX", "ADRIN", "ADRIN", "ADRIND",
        "ADRIWX", "ADRIWX", "ADRJAN", "ADRJAX", "ADRJKL", "ADRJKL", "ADRKEY",
        "ADRKRF", "ADRKS", "ADRKY", "ADRKY", "ADRLA", "ADRLBF", "ADRLCH",
        "ADRLIX", "ADRLKN", "ADRLMK", "ADRLOT", "ADRLOX", "ADRLSX", "ADRLUB",
        "ADRLWX", "ADRLWX", "ADRLZK", "ADRMA", "ADRMCG", "ADRMCG", "ADRMD",
        "ADRMD", "ADRME", "ADRME", "ADRMEG", "ADRMEI", "ADRMFL", "ADRMFR",
        "ADRMHX", "ADRMHX", "ADRMI", "ADRMKX", "ADRMKX", "ADRMLB", "ADRMN",
        "ADRMO", "ADRMOB", "ADRMPX", "ADRMPX", "ADRMQT", "ADRMQT", "ADRMRX",
        "ADRMS", "ADRMSO", "ADRMSR", "ADRMT", "ADRMTR", "ADRNC", "ADRNC",
        "ADRND", "ADRND", "ADRNE", "ADRNE", "ADRNH", "ADRNH", "ADRNJ",
        "ADRNJ", "ADRNM", "ADRNMC", "ADRNV", "ADRNY", "ADRNY", "ADRNY",
        "ADROAX", "ADROAX", "ADROH", "ADROHX", "ADROK", "ADROKX", "ADROKX",
        "ADROME", "ADROR", "ADROTX", "ADROTZ", "ADROUN", "ADRPA", "ADRPA",
        "ADRPAH", "ADRPBZ", "ADRPBZ", "ADRPDT", "ADRPDT", "ADRPHI", "ADRPHI",
        "ADRPIH", "ADRPPG", "ADRPQR", "ADRPR", "ADRPSR", "ADRPTR", "ADRPUB",
        "ADRPUB", "ADRRAH", "ADRRAH", "ADRRDU", "ADRREV", "ADRRI", "ADRRIW",
        "ADRRIW", "ADRRLX", "ADRRLX", "ADRRNK", "ADRRNK", "ADRSC", "ADRSC",
        "ADRSC", "ADRSD", "ADRSD", "ADRSEW", "ADRSGF", "ADRSGF", "ADRSGX",
        "ADRSHV", "ADRSJT", "ADRSJU", "ADRSLC", "ADRSNP", "ADRSPN", "ADRSTO",
        "ADRSTR", "ADRTAE", "ADRTBW", "ADRTFX", "ADRTN", "ADRTOP", "ADRTSA",
        "ADRTWC", "ADRUNR", "ADRUT", "ADRVA", "ADRVA", "ADRVEF", "ADRVI",
        "ADRVT", "ADRVT", "ADRWA", "ADRWI", "ADRWSH", "ADRWV", "ADRWV",
        "ADRWY", "ADRWY", "AVAABQ", "AVAABR", "AVAADQ", "AVAAFC", "AVAAFG",
        "AVAAJK", "AVAAK", "AVAAKN", "AVAAKQ", "AVAAL", "AVAALY", "AVAAMA",
        "AVAAPX", "AVAAR", "AVAARX", "AVAAS", "AVAAZ", "AVABET", "AVABGM",
        "AVABIS", "AVABMX", "AVABOI", "AVABOU", "AVABOX", "AVABRO", "AVABRW",
        "AVABTV", "AVABUF", "AVABYZ", "AVACA", "AVACAE", "AVACAR", "AVACDB",
        "AVACHS", "AVACLE", "AVACO", "AVACRP", "AVACT", "AVACTP", "AVACYS",
        "AVADC", "AVADDC", "AVADE", "AVADLH", "AVADMX", "AVADTX", "AVADVN",
        "AVAEAX", "AVAEKA", "AVAEPZ", "AVAEWX", "AVAFFC", "AVAFGF", "AVAFGZ",
        "AVAFL", "AVAFSD", "AVAFWD", "AVAGA", "AVAGGW", "AVAGID", "AVAGJT",
        "AVAGLD", "AVAGRB", "AVAGRR", "AVAGSP", "AVAGU", "AVAGUM", "AVAGYX",
        "AVAHFO", "AVAHI", "AVAHNX", "AVAHUN", "AVAIA", "AVAICT", "AVAID",
        "AVAIL", "AVAILM", "AVAILN", "AVAILX", "AVAIN", "AVAIND", "AVAIWX",
        "AVAJAN", "AVAJAX", "AVAJKL", "AVAKEY", "AVAKS", "AVAKY", "AVALA",
        "AVALBF", "AVALCH", "AVALIX", "AVALKN", "AVALMK", "AVALOT", "AVALOX",
        "AVALSX", "AVALUB", "AVALWX", "AVALZK", "AVAMA", "AVAMAF", "AVAMCG",
        "AVAMCG", "AVAMD", "AVAME", "AVAMEG", "AVAMFL", "AVAMFR", "AVAMHX",
        "AVAMI", "AVAMKX", "AVAMLB", "AVAMN", "AVAMO", "AVAMOB", "AVAMPX",
        "AVAMQT", "AVAMRX", "AVAMS", "AVAMSO", "AVAMT", "AVAMTR", "AVANC",
        "AVAND", "AVANE", "AVANH", "AVANJ", "AVANV", "AVANY", "AVAOAX",
        "AVAOH", "AVAOHX", "AVAOK", "AVAOKX", "AVAOME", "AVAOR", "AVAOTX",
        "AVAOTZ", "AVAOUN", "AVAPA", "AVAPAH", "AVAPBZ", "AVAPDT", "AVAPHI",
        "AVAPIH", "AVAPPG", "AVAPQR", "AVAPR", "AVAPSR", "AVAPUB", "AVARAH",
        "AVAREV", "AVARI", "AVARIW", "AVARLX", "AVARNK", "AVASC", "AVASC",
        "AVASD", "AVASEW", "AVASGF", "AVASGX", "AVASHV", "AVASJT", "AVASJU",
        "AVASLC", "AVASNP", "AVASPN", "AVASTO", "AVATAE", "AVATBW", "AVATFX",
        "AVATN", "AVATOP", "AVATSA", "AVATWC", "AVAUNR", "AVAUT", "AVAVA",
        "AVAVEF", "AVAVI", "AVAVT", "AVAWA", "AVAWI", "AVAWV", "AVAWY",
        "AVWABQ", "AVWABR", "AVWADQ", "AVWAFC", "AVWAFG", "AVWAJK", "AVWAK",
        "AVWAKN", "AVWAKQ", "AVWAL", "AVWALY", "AVWAPX", "AVWAR", "AVWARX",
        "AVWAS", "AVWAZ", "AVWBET", "AVWBGM", "AVWBIS", "AVWBMX", "AVWBOI",
        "AVWBOU", "AVWBOX", "AVWBRO", "AVWBRW", "AVWBTV", "AVWBUF", "AVWBYZ",
        "AVWCA", "AVWCAE", "AVWCAR", "AVWCDB", "AVWCHS", "AVWCLE", "AVWCO",
        "AVWCRP", "AVWCT", "AVWCTP", "AVWCYS", "AVWDC", "AVWDDC", "AVWDE",
        "AVWDLH", "AVWDMX", "AVWDTX", "AVWDVN", "AVWEAX", "AVWEKA", "AVWEPZ",
        "AVWEWX", "AVWFFC", "AVWFGF", "AVWFGZ", "AVWFL", "AVWFSD", "AVWFWD",
        "AVWGA", "AVWGGW", "AVWGID", "AVWGJT", "AVWGLD", "AVWGRB", "AVWGRR",
        "AVWGSP", "AVWGU", "AVWGUM", "AVWGYX", "AVWHFO", "AVWHI", "AVWHNX",
        "AVWHUN", "AVWIA", "AVWICT", "AVWID", "AVWIL", "AVWILM", "AVWILN",
        "AVWILX", "AVWIN", "AVWIND", "AVWIWX", "AVWJAN", "AVWJAX", "AVWJKL",
        "AVWKEY", "AVWKS", "AVWKY", "AVWLA", "AVWLBF", "AVWLCH", "AVWLIX",
        "AVWLKN", "AVWLMK", "AVWLOT", "AVWLOX", "AVWLSX", "AVWLUB", "AVWLWX",
        "AVWLZK", "AVWMA", "AVWMAF", "AVWMCG", "AVWMCG", "AVWMD", "AVWME",
        "AVWMEG", "AVWMFL", "AVWMFR", "AVWMHX", "AVWMI", "AVWMKX", "AVWMLB",
        "AVWMN", "AVWMO", "AVWMOB", "AVWMPX", "AVWMQT", "AVWMRX", "AVWMS",
        "AVWMSO", "AVWMT", "AVWMTR", "AVWNC", "AVWND", "AVWNE", "AVWNH",
        "AVWNJ", "AVWNV", "AVWNY", "AVWOAX", "AVWOH", "AVWOHX", "AVWOK",
        "AVWOKX", "AVWOME", "AVWOR", "AVWOTX", "AVWOTZ", "AVWOUN", "AVWPA",
        "AVWPAH", "AVWPBZ", "AVWPDT", "AVWPHI", "AVWPIH", "AVWPPG", "AVWPQR",
        "AVWPR", "AVWPSR", "AVWPUB", "AVWRAH", "AVWREV", "AVWRI", "AVWRIW",
        "AVWRLX", "AVWRNK", "AVWSC", "AVWSC", "AVWSD", "AVWSEW", "AVWSGF",
        "AVWSGX", "AVWSHV", "AVWSJT", "AVWSJU", "AVWSLC", "AVWSNP", "AVWSPN",
        "AVWSTO", "AVWTAE", "AVWTBW", "AVWTFX", "AVWTN", "AVWTOP", "AVWTSA",
        "AVWTWC", "AVWUNR", "AVWUT", "AVWVA", "AVWVEF", "AVWVI", "AVWVT",
        "AVWWA", "AVWWI", "AVWWV", "AVWWY", "BLUABQ", "BLUABR", "BLUADQ",
        "BLUAFC", "BLUAFG", "BLUAJK", "BLUAK", "BLUAKQ", "BLUAL", "BLUALY",
        "BLUAMA", "BLUAPX", "BLUAR", "BLUARX", "BLUAS", "BLUAZ", "BLUBGM",
        "BLUBIS", "BLUBMX", "BLUBOI", "BLUBOU", "BLUBOX", "BLUBRO", "BLUBTV",
        "BLUBTV", "BLUBUF", "BLUBYZ", "BLUCA", "BLUCAE", "BLUCAR", "BLUCHS",
        "BLUCLE", "BLUCO", "BLUCRP", "BLUCT", "BLUCTP", "BLUCYS", "BLUDC",
        "BLUDDC", "BLUDE", "BLUDLH", "BLUDMX", "BLUDTX", "BLUDVN", "BLUEAX",
        "BLUEKA", "BLUEPZ", "BLUEWX", "BLUFFC", "BLUFGF", "BLUFGZ", "BLUFL",
        "BLUFSD", "BLUFWD", "BLUGA", "BLUGGW", "BLUGID", "BLUGJT", "BLUGLD",
        "BLUGRB", "BLUGRR", "BLUGSP", "BLUGU", "BLUGUM", "BLUGYX", "BLUHFO",
        "BLUHGX", "BLUHI", "BLUHNX", "BLUHUN", "BLUIA", "BLUICT", "BLUID",
        "BLUIL", "BLUILM", "BLUILN", "BLUILX", "BLUIN", "BLUIND", "BLUIWX",
        "BLUJAN", "BLUJAX", "BLUJKL", "BLUKEY", "BLUKS", "BLUKY", "BLULA",
        "BLULBF", "BLULCH", "BLULIX", "BLULKN", "BLULMK", "BLULOT", "BLULOX",
        "BLULSX", "BLULUB", "BLULWX", "BLULZK", "BLUMA", "BLUMAF", "BLUMD",
        "BLUME", "BLUMEG", "BLUMFL", "BLUMFR", "BLUMHX", "BLUMI", "BLUMKX",
        "BLUMLB", "BLUMN", "BLUMO", "BLUMOB", "BLUMPX", "BLUMQT", "BLUMRX",
        "BLUMS", "BLUMSO", "BLUMT", "BLUMTR", "BLUNC", "BLUND", "BLUNE",
        "BLUNH", "BLUNJ", "BLUNM", "BLUNV", "BLUNY", "BLUOAX", "BLUOH",
        "BLUOHX", "BLUOK", "BLUOKX", "BLUOME", "BLUOR", "BLUOTX", "BLUOUN",
        "BLUPA", "BLUPAH", "BLUPBZ", "BLUPDT", "BLUPHI", "BLUPIH", "BLUPPG",
        "BLUPQR", "BLUPR", "BLUPSR", "BLUPUB", "BLURAH", "BLUREV", "BLURI",
        "BLURIW", "BLURLX", "BLURNK", "BLUSC", "BLUSD", "BLUSEW", "BLUSGF",
        "BLUSGX", "BLUSHV", "BLUSJT", "BLUSJU", "BLUSLC", "BLUSPN", "BLUSTO",
        "BLUTAE", "BLUTBW", "BLUTFX", "BLUTN", "BLUTOP", "BLUTSA", "BLUTWC",
        "BLUTX", "BLUUNR", "BLUUT", "BLUVA", "BLUVEF", "BLUVI", "BLUWA",
        "BLUWI", "BLUWV", "BLUWY", "BLUYAK", "CAEABQ", "CAEABR", "CAEADQ",
        "CAEAFC", "CAEAFG", "CAEAJK", "CAEAK", "CAEAKN", "CAEAKQ", "CAEAL",
        "CAEALY", "CAEAMA", "CAEAPX", "CAEAR", "CAEARX", "CAEAS", "CAEAZ",
        "CAEBET", "CAEBGM", "CAEBIS", "CAEBMX", "CAEBOI", "CAEBOU", "CAEBOX",
        "CAEBRO", "CAEBRW", "CAEBTV", "CAEBUF", "CAEBYZ", "CAECA", "CAECAE",
        "CAECAR", "CAECDB", "CAECHS", "CAECLE", "CAECO", "CAECRP", "CAECT",
        "CAECTP", "CAECYS", "CAEDC", "CAEDDC", "CAEDE", "CAEDLH", "CAEDMX",
        "CAEDTX", "CAEDVN", "CAEEAX", "CAEEKA", "CAEEPZ", "CAEEWX", "CAEFFC",
        "CAEFGF", "CAEFGZ", "CAEFL", "CAEFSD", "CAEFWD", "CAEGA", "CAEGGW",
        "CAEGID", "CAEGJT", "CAEGLD", "CAEGRB", "CAEGRR", "CAEGSP", "CAEGU",
        "CAEGUM", "CAEGYX", "CAEHFO", "CAEHGX", "CAEHI", "CAEHNX", "CAEHUN",
        "CAEIA", "CAEICT", "CAEID", "CAEIL", "CAEILM", "CAEILN", "CAEILX",
        "CAEIN", "CAEIND", "CAEIWX", "CAEJAN", "CAEJAX", "CAEJKL", "CAEKEY",
        "CAEKS", "CAEKY", "CAELA", "CAELBF", "CAELCH", "CAELIX", "CAELKN",
        "CAELMK", "CAELOT", "CAELOX", "CAELSX", "CAELUB", "CAELWX", "CAELZK",
        "CAEMA", "CAEMAF", "CAEMCG", "CAEMCG", "CAEMD", "CAEME", "CAEMEG",
        "CAEMFL", "CAEMFR", "CAEMHX", "CAEMI", "CAEMKX", "CAEMLB", "CAEMN",
        "CAEMO", "CAEMOB", "CAEMPX", "CAEMQT", "CAEMRX", "CAEMS", "CAEMSO",
        "CAEMT", "CAEMTR", "CAENC", "CAEND", "CAENE", "CAENH", "CAENJ",
        "CAENV", "CAENY", "CAEOAX", "CAEOH", "CAEOHX", "CAEOK", "CAEOKX",
        "CAEOME", "CAEOR", "CAEOTX", "CAEOTZ", "CAEOUN", "CAEPA", "CAEPAH",
        "CAEPBZ", "CAEPDT", "CAEPHI", "CAEPIH", "CAEPPG", "CAEPQR", "CAEPR",
        "CAEPSR", "CAEPUB", "CAERAH", "CAEREV", "CAERI", "CAERIW", "CAERLX",
        "CAERNK", "CAESC", "CAESC", "CAESD", "CAESEW", "CAESGF", "CAESGX",
        "CAESHV", "CAESJT", "CAESJU", "CAESLC", "CAESNP", "CAESPN", "CAESTO",
        "CAETAE", "CAETBW", "CAETFX", "CAETN", "CAETOP", "CAETSA", "CAETWC",
        "CAEUNR", "CAEUT", "CAEVA", "CAEVEF", "CAEVI", "CAEVT", "CAEWA",
        "CAEWI", "CAEWV", "CAEWY", "CDWABQ", "CDWABR", "CDWADQ", "CDWAFC",
        "CDWAFG", "CDWAJK", "CDWAK", "CDWAKN", "CDWAKQ", "CDWAL", "CDWALY",
        "CDWAMA", "CDWAPX", "CDWAR", "CDWARX", "CDWAS", "CDWAZ", "CDWBET",
        "CDWBGM", "CDWBIS", "CDWBMX", "CDWBOI", "CDWBOU", "CDWBOX", "CDWBRO",
        "CDWBRW", "CDWBTV", "CDWBUF", "CDWBYZ", "CDWCA", "CDWCAE", "CDWCAR",
        "CDWCDB", "CDWCHS", "CDWCLE", "CDWCO", "CDWCRP", "CDWCT", "CDWCTP",
        "CDWCYS", "CDWDC", "CDWDDC", "CDWDE", "CDWDLH", "CDWDMX", "CDWDTX",
        "CDWDVN", "CDWEAX", "CDWEKA", "CDWEPZ", "CDWEWX", "CDWFFC", "CDWFGF",
        "CDWFGZ", "CDWFL", "CDWFSD", "CDWFWD", "CDWGA", "CDWGGW", "CDWGID",
        "CDWGJT", "CDWGLD", "CDWGRB", "CDWGRR", "CDWGSP", "CDWGU", "CDWGUM",
        "CDWGYX", "CDWHFO", "CDWHGX", "CDWHI", "CDWHNX", "CDWHUN", "CDWIA",
        "CDWICT", "CDWID", "CDWIL", "CDWILM", "CDWILN", "CDWILX", "CDWIN",
        "CDWIND", "CDWIWX", "CDWJAN", "CDWJAX", "CDWJKL", "CDWKEY", "CDWKS",
        "CDWKY", "CDWLA", "CDWLBF", "CDWLCH", "CDWLIX", "CDWLKN", "CDWLMK",
        "CDWLOT", "CDWLOX", "CDWLSX", "CDWLUB", "CDWLWX", "CDWLZK", "CDWMA",
        "CDWMAF", "CDWMCG", "CDWMCG", "CDWMD", "CDWME", "CDWMEG", "CDWMFL",
        "CDWMFR", "CDWMHX", "CDWMI", "CDWMI", "CDWMKX", "CDWMLB", "CDWMN",
        "CDWMO", "CDWMOB", "CDWMPX", "CDWMQT", "CDWMRX", "CDWMS", "CDWMSO",
        "CDWMT", "CDWMTR", "CDWNC", "CDWND", "CDWNE", "CDWNH", "CDWNJ",
        "CDWNV", "CDWNY", "CDWOAX", "CDWOH", "CDWOHX", "CDWOK", "CDWOKX",
        "CDWOME", "CDWOR", "CDWOTX", "CDWOTZ", "CDWOUN", "CDWPA", "CDWPAH",
        "CDWPBZ", "CDWPDT", "CDWPHI", "CDWPIH", "CDWPPG", "CDWPQR", "CDWPR",
        "CDWPSR", "CDWPUB", "CDWRAH", "CDWREV", "CDWRI", "CDWRIW", "CDWRLX",
        "CDWRNK", "CDWSC", "CDWSC", "CDWSD", "CDWSEW", "CDWSGF", "CDWSGX",
        "CDWSHV", "CDWSJT", "CDWSJU", "CDWSLC", "CDWSNP", "CDWSPN", "CDWSTO",
        "CDWTAE", "CDWTBW", "CDWTFX", "CDWTN", "CDWTOP", "CDWTSA", "CDWTWC",
        "CDWUNR", "CDWUT", "CDWVA", "CDWVEF", "CDWVI", "CDWVT", "CDWWA",
        "CDWWI", "CDWWV", "CDWWY", "CEMABQ", "CEMABR", "CEMADQ", "CEMAER",
        "CEMAFC", "CEMAFG", "CEMAJK", "CEMAK", "CEMAKN", "CEMAKQ", "CEMAL",
        "CEMALU", "CEMALY", "CEMAMA", "CEMAPX", "CEMAR", "CEMARX", "CEMAS",
        "CEMAZ", "CEMBET", "CEMBGM", "CEMBIS", "CEMBMX", "CEMBOI", "CEMBOU",
        "CEMBOX", "CEMBRO", "CEMBRW", "CEMBTV", "CEMBUF", "CEMBYZ", "CEMCA",
        "CEMCAE", "CEMCAR", "CEMCDB", "CEMCHS", "CEMCLE", "CEMCO", "CEMCRP",
        "CEMCT", "CEMCTP", "CEMCYS", "CEMDC", "CEMDDC", "CEMDE", "CEMDLH",
        "CEMDMX", "CEMDTX", "CEMDVN", "CEMEAX", "CEMEKA", "CEMEPZ", "CEMEWX",
        "CEMFFC", "CEMFGF", "CEMFGZ", "CEMFL", "CEMFSD", "CEMFWD", "CEMGA",
        "CEMGGW", "CEMGID", "CEMGJT", "CEMGLD", "CEMGRB", "CEMGRR", "CEMGSP",
        "CEMGU", "CEMGUM", "CEMGYX", "CEMHFO", "CEMHGX", "CEMHI", "CEMHNX",
        "CEMHON", "CEMHUN", "CEMIA", "CEMICT", "CEMID", "CEMIL", "CEMILM",
        "CEMILN", "CEMILX", "CEMIN", "CEMIND", "CEMIWX", "CEMJAN", "CEMJAX",
        "CEMJKL", "CEMKEY", "CEMKS", "CEMKY", "CEMLA", "CEMLBF", "CEMLCH",
        "CEMLIX", "CEMLKN", "CEMLMK", "CEMLOT", "CEMLOX", "CEMLSX", "CEMLUB",
        "CEMLWX", "CEMLZK", "CEMMA", "CEMMAF", "CEMMCG", "CEMMCG", "CEMMD",
        "CEMME", "CEMMEG", "CEMMFL", "CEMMFR", "CEMMHX", "CEMMI", "CEMMKX",
        "CEMMLB", "CEMMN", "CEMMO", "CEMMOB", "CEMMPX", "CEMMQT", "CEMMRX",
        "CEMMS", "CEMMSO", "CEMMT", "CEMMTR", "CEMMY", "CEMNC", "CEMND",
        "CEMNE", "CEMNH", "CEMNJ", "CEMNM", "CEMNV", "CEMNY", "CEMOAX",
        "CEMOH", "CEMOHX", "CEMOK", "CEMOKX", "CEMOME", "CEMOR", "CEMOTX",
        "CEMOTZ", "CEMOUN", "CEMPA", "CEMPAH", "CEMPBZ", "CEMPDT", "CEMPHI",
        "CEMPIH", "CEMPPG", "CEMPQR", "CEMPR", "CEMPSR", "CEMPUB", "CEMRAH",
        "CEMREV", "CEMRI", "CEMRIW", "CEMRLX", "CEMRNK", "CEMSC", "CEMSC",
        "CEMSD", "CEMSEW", "CEMSGF", "CEMSGX", "CEMSHV", "CEMSJT", "CEMSJU",
        "CEMSLC", "CEMSNP", "CEMSPN", "CEMSTO", "CEMTAE", "CEMTBW", "CEMTFX",
        "CEMTN", "CEMTOP", "CEMTSA", "CEMTWC", "CEMTX", "CEMUNR", "CEMUT",
        "CEMVA", "CEMVEF", "CEMVI", "CEMVT", "CEMVWS", "CEMWA", "CEMWI",
        "CEMWV", "CEMWY", "DMOABQ", "DMOABR", "DMOADQ", "DMOAFC", "DMOAFG",
        "DMOAJK", "DMOAK", "DMOAKQ", "DMOAL", "DMOALY", "DMOAPX", "DMOAR",
        "DMOARX", "DMOAS", "DMOAZ", "DMOBGM", "DMOBIS", "DMOBMX", "DMOBOI",
        "DMOBOU", "DMOBOX", "DMOBRO", "DMOBTV", "DMOBUF", "DMOBYZ", "DMOCA",
        "DMOCAE", "DMOCAR", "DMOCHS", "DMOCLE", "DMOCO", "DMOCRP", "DMOCT",
        "DMOCTP", "DMOCYS", "DMODC", "DMODDC", "DMODE", "DMODLH", "DMODMX",
        "DMODTX", "DMODVN", "DMOEAX", "DMOEKA", "DMOEPZ", "DMOEWX", "DMOFFC",
        "DMOFGF", "DMOFGZ", "DMOFL", "DMOFSD", "DMOGA", "DMOGGW", "DMOGID",
        "DMOGJT", "DMOGLD", "DMOGRB", "DMOGRR", "DMOGSP", "DMOGU", "DMOGUM",
        "DMOGYX", "DMOHFO", "DMOHGX", "DMOHI", "DMOHNX", "DMOIA", "DMOICT",
        "DMOID", "DMOIL", "DMOILM", "DMOILN", "DMOILX", "DMOIN", "DMOIND",
        "DMOIWX", "DMOJAN", "DMOJAX", "DMOJKL", "DMOKEY", "DMOKS", "DMOKY",
        "DMOLA", "DMOLBF", "DMOLIX", "DMOLKN", "DMOLMK", "DMOLOT", "DMOLOX",
        "DMOLSX", "DMOLUB", "DMOLWX", "DMOLZK", "DMOMA", "DMOMD", "DMOME",
        "DMOMEG", "DMOMFL", "DMOMFR", "DMOMHX", "DMOMI", "DMOMKX", "DMOMLB",
        "DMOMN", "DMOMO", "DMOMOB", "DMOMPX", "DMOMQT", "DMOMRX", "DMOMS",
        "DMOMSO", "DMOMT", "DMOMTR", "DMONC", "DMOND", "DMONE", "DMONH",
        "DMONJ", "DMONM", "DMONV", "DMONY", "DMOOAX", "DMOOH", "DMOOHX",
        "DMOOK", "DMOOKX", "DMOOME", "DMOOR", "DMOOTX", "DMOOUN", "DMOPA",
        "DMOPAH", "DMOPBZ", "DMOPDT", "DMOPHI", "DMOPIH", "DMOPPG", "DMOPQR",
        "DMOPR", "DMOPSR", "DMOPUB", "DMORAH", "DMOREV", "DMORI", "DMORIW",
        "DMORLX", "DMORNK", "DMOSC", "DMOSD", "DMOSEW", "DMOSGF", "DMOSGX",
        "DMOSJT", "DMOSJU", "DMOSLC", "DMOSPN", "DMOSTO", "DMOTAE", "DMOTBW",
        "DMOTFX", "DMOTN", "DMOTOP", "DMOTSA", "DMOTWC", "DMOUNR", "DMOUT",
        "DMOVA", "DMOVEF", "DMOVI", "DMOVT", "DMOWA", "DMOWI", "DMOWV",
        "DMOWY", "EQWABQ", "EQWABR", "EQWADQ", "EQWAFC", "EQWAFG", "EQWAJK",
        "EQWAK", "EQWAKN", "EQWAKQ", "EQWAL", "EQWALY", "EQWAMA", "EQWAPX",
        "EQWAR", "EQWARX", "EQWAS", "EQWAZ", "EQWBET", "EQWBGM", "EQWBIS",
        "EQWBMX", "EQWBOI", "EQWBOU", "EQWBOX", "EQWBRO", "EQWBRW", "EQWBTV",
        "EQWBUF", "EQWBYZ", "EQWCA", "EQWCAE", "EQWCAR", "EQWCDB", "EQWCHS",
        "EQWCLE", "EQWCO", "EQWCRP", "EQWCT", "EQWCTP", "EQWCYS", "EQWDC",
        "EQWDDC", "EQWDE", "EQWDLH", "EQWDMX", "EQWDTX", "EQWDVN", "EQWEAX",
        "EQWEKA", "EQWEPZ", "EQWEWX", "EQWFFC", "EQWFGF", "EQWFGZ", "EQWFL",
        "EQWFSD", "EQWFWD", "EQWGA", "EQWGGW", "EQWGID", "EQWGJT", "EQWGLD",
        "EQWGRB", "EQWGRR", "EQWGSP", "EQWGU", "EQWGUM", "EQWGYX", "EQWHFO",
        "EQWHGX", "EQWHI", "EQWHNX", "EQWHUN", "EQWIA", "EQWICT", "EQWID",
        "EQWIL", "EQWILM", "EQWILN", "EQWILX", "EQWIN", "EQWIND", "EQWIWX",
        "EQWJAN", "EQWJAX", "EQWJKL", "EQWKEY", "EQWKS", "EQWKY", "EQWLA",
        "EQWLBF", "EQWLCH", "EQWLIX", "EQWLKN", "EQWLMK", "EQWLOT", "EQWLOX",
        "EQWLSX", "EQWLUB", "EQWLWX", "EQWLZK", "EQWMA", "EQWMAF", "EQWMCG",
        "EQWMCG", "EQWMD", "EQWME", "EQWMEG", "EQWMFL", "EQWMFR", "EQWMHX",
        "EQWMI", "EQWMKX", "EQWMLB", "EQWMN", "EQWMO", "EQWMOB", "EQWMPX",
        "EQWMQT", "EQWMRX", "EQWMS", "EQWMSO", "EQWMT", "EQWMTR", "EQWNC",
        "EQWND", "EQWNE", "EQWNH", "EQWNJ", "EQWNV", "EQWNY", "EQWOAX",
        "EQWOH", "EQWOHX", "EQWOK", "EQWOKX", "EQWOME", "EQWOR", "EQWOTX",
        "EQWOTZ", "EQWOUN", "EQWPA", "EQWPAH", "EQWPBZ", "EQWPDT", "EQWPHI",
        "EQWPIH", "EQWPPG", "EQWPQR", "EQWPR", "EQWPSR", "EQWPUB", "EQWRAH",
        "EQWREV", "EQWRI", "EQWRIW", "EQWRLX", "EQWRNK", "EQWSC", "EQWSC",
        "EQWSD", "EQWSEW", "EQWSGF", "EQWSGX", "EQWSJT", "EQWSJU", "EQWSLC",
        "EQWSNP", "EQWSPN", "EQWSTO", "EQWTAE", "EQWTBW", "EQWTFX", "EQWTN",
        "EQWTOP", "EQWTSA", "EQWTWC", "EQWUNR", "EQWUT", "EQWVA", "EQWVEF",
        "EQWVI", "EQWVT", "EQWWA", "EQWWI", "EQWWV", "EQWWY", "EVIABQ",
        "EVIABR", "EVIADQ", "EVIAFC", "EVIAFG", "EVIAJK", "EVIAK", "EVIAKN",
        "EVIAKQ", "EVIAL", "EVIALY", "EVIAMA", "EVIAPX", "EVIAR", "EVIARX",
        "EVIAS", "EVIAZ", "EVIBET", "EVIBGM", "EVIBIS", "EVIBMX", "EVIBOI",
        "EVIBOU", "EVIBOX", "EVIBRO", "EVIBRW", "EVIBTV", "EVIBUF", "EVIBYZ",
        "EVICA", "EVICAE", "EVICAR", "EVICDB", "EVICHS", "EVICLE", "EVICO",
        "EVICRP", "EVICT", "EVICTP", "EVICYS", "EVIDC", "EVIDDC", "EVIDE",
        "EVIDLH", "EVIDMX", "EVIDTX", "EVIDVN", "EVIEAX", "EVIEKA", "EVIEPZ",
        "EVIEWX", "EVIFFC", "EVIFGF", "EVIFGZ", "EVIFL", "EVIFSD", "EVIFWD",
        "EVIGA", "EVIGGW", "EVIGID", "EVIGJT", "EVIGLD", "EVIGRB", "EVIGRR",
        "EVIGSP", "EVIGU", "EVIGUM", "EVIGYX", "EVIHFO", "EVIHGX", "EVIHI",
        "EVIHNX", "EVIHUN", "EVIIA", "EVIICT", "EVIID", "EVIIL", "EVIILM",
        "EVIILN", "EVIILX", "EVIIN", "EVIIND", "EVIIWX", "EVIJAN", "EVIJAX",
        "EVIJKL", "EVIKEY", "EVIKS", "EVIKY", "EVILA", "EVILBF", "EVILCH",
        "EVILIX", "EVILKN", "EVILMK", "EVILOT", "EVILOX", "EVILSX", "EVILUB",
        "EVILWX", "EVILZK", "EVIMA", "EVIMAF", "EVIMCG", "EVIMCG", "EVIMD",
        "EVIME", "EVIMEG", "EVIMFL", "EVIMFR", "EVIMHX", "EVIMI", "EVIMKX",
        "EVIMLB", "EVIMN", "EVIMO", "EVIMOB", "EVIMPX", "EVIMQT", "EVIMRX",
        "EVIMS", "EVIMSO", "EVIMT", "EVIMTR", "EVINC", "EVIND", "EVINE",
        "EVINH", "EVINJ", "EVINV", "EVINY", "EVIOAX", "EVIOH", "EVIOHX",
        "EVIOK", "EVIOKX", "EVIOME", "EVIOR", "EVIOTX", "EVIOTZ", "EVIOUN",
        "EVIPA", "EVIPAH", "EVIPBZ", "EVIPDT", "EVIPHI", "EVIPIH", "EVIPPG",
        "EVIPQR", "EVIPR", "EVIPSR", "EVIPUB", "EVIRAH", "EVIREV", "EVIRI",
        "EVIRIW", "EVIRLX", "EVIRNK", "EVISC", "EVISC", "EVISD", "EVISEW",
        "EVISGF", "EVISGX", "EVISHV", "EVISJT", "EVISJU", "EVISLC", "EVISNP",
        "EVISPN", "EVISTO", "EVITAE", "EVITBW", "EVITFX", "EVITN", "EVITOP",
        "EVITSA", "EVITWC", "EVIUNR", "EVIUT", "EVIVA", "EVIVEF", "EVIVI",
        "EVIVT", "EVIWA", "EVIWI", "EVIWV", "EVIWY", "FRWABQ", "FRWABR",
        "FRWADQ", "FRWAFC", "FRWAFG", "FRWAJK", "FRWAK", "FRWAKN", "FRWAKQ",
        "FRWAL", "FRWALY", "FRWAMA", "FRWAPX", "FRWAR", "FRWARX", "FRWAS",
        "FRWAZ", "FRWBET", "FRWBGM", "FRWBIS", "FRWBMX", "FRWBOI", "FRWBOU",
        "FRWBOX", "FRWBRO", "FRWBRW", "FRWBTV", "FRWBUF", "FRWBYZ", "FRWCA",
        "FRWCAE", "FRWCAR", "FRWCDB", "FRWCHS", "FRWCLE", "FRWCO", "FRWCRP",
        "FRWCT", "FRWCTP", "FRWCYS", "FRWDC", "FRWDDC", "FRWDE", "FRWDLH",
        "FRWDMX", "FRWDTX", "FRWDVN", "FRWEAX", "FRWEKA", "FRWEPZ", "FRWEWX",
        "FRWFFC", "FRWFGF", "FRWFGZ", "FRWFL", "FRWFSD", "FRWFWD", "FRWGA",
        "FRWGGW", "FRWGID", "FRWGJT", "FRWGLD", "FRWGRB", "FRWGRR", "FRWGSP",
        "FRWGU", "FRWGUM", "FRWGYX", "FRWHFO", "FRWHGX", "FRWHI", "FRWHNX",
        "FRWHUN", "FRWIA", "FRWICT", "FRWID", "FRWIL", "FRWILM", "FRWILN",
        "FRWILX", "FRWIN", "FRWIND", "FRWIWX", "FRWJAN", "FRWJAX", "FRWJKL",
        "FRWKEY", "FRWKS", "FRWKY", "FRWLA", "FRWLBF", "FRWLIX", "FRWLKN",
        "FRWLMK", "FRWLOT", "FRWLOX", "FRWLSX", "FRWLUB", "FRWLWX", "FRWLZK",
        "FRWMA", "FRWMAF", "FRWMCG", "FRWMCG", "FRWMD", "FRWME", "FRWMEG",
        "FRWMFL", "FRWMFR", "FRWMHX", "FRWMI", "FRWMKX", "FRWMLB", "FRWMN",
        "FRWMO", "FRWMOB", "FRWMPX", "FRWMQT", "FRWMRX", "FRWMS", "FRWMSO",
        "FRWMT", "FRWMTR", "FRWNC", "FRWND", "FRWNE", "FRWNH", "FRWNJ",
        "FRWNV", "FRWNY", "FRWOAX", "FRWOH", "FRWOHX", "FRWOK", "FRWOKX",
        "FRWOME", "FRWOR", "FRWOTX", "FRWOTZ", "FRWOUN", "FRWPA", "FRWPAH",
        "FRWPBZ", "FRWPDT", "FRWPHI", "FRWPIH", "FRWPPG", "FRWPQR", "FRWPR",
        "FRWPSR", "FRWPUB", "FRWRAH", "FRWREV", "FRWRI", "FRWRIW", "FRWRLX",
        "FRWRNK", "FRWSC", "FRWSC", "FRWSD", "FRWSEW", "FRWSGF", "FRWSGX",
        "FRWSHV", "FRWSJT", "FRWSJU", "FRWSLC", "FRWSNP", "FRWSPN", "FRWSTO",
        "FRWTAE", "FRWTBW", "FRWTFX", "FRWTN", "FRWTOP", "FRWTSA", "FRWTWC",
        "FRWUNR", "FRWUT", "FRWVA", "FRWVEF", "FRWVI", "FRWVT", "FRWWA",
        "FRWWI", "FRWWV", "FRWWY", "HMWABQ", "HMWABR", "HMWADQ", "HMWAFC",
        "HMWAFG", "HMWAJK", "HMWAK", "HMWAKN", "HMWAKQ", "HMWAL", "HMWALY",
        "HMWAPX", "HMWAR", "HMWARX", "HMWAS", "HMWAZ", "HMWBET", "HMWBGM",
        "HMWBIS", "HMWBMX", "HMWBOI", "HMWBOU", "HMWBOX", "HMWBRO", "HMWBRW",
        "HMWBTV", "HMWBUF", "HMWBYZ", "HMWCA", "HMWCAE", "HMWCAR", "HMWCDB",
        "HMWCHS", "HMWCLE", "HMWCO", "HMWCRP", "HMWCT", "HMWCTP", "HMWCYS",
        "HMWDC", "HMWDDC", "HMWDE", "HMWDLH", "HMWDMX", "HMWDTX", "HMWDVN",
        "HMWEAX", "HMWEKA", "HMWEPZ", "HMWEWX", "HMWFFC", "HMWFGF", "HMWFGZ",
        "HMWFL", "HMWFSD", "HMWFWD", "HMWGA", "HMWGGW", "HMWGID", "HMWGJT",
        "HMWGLD", "HMWGRB", "HMWGRR", "HMWGSP", "HMWGU", "HMWGUM", "HMWGYX",
        "HMWHFO", "HMWHGX", "HMWHI", "HMWHNX", "HMWHUN", "HMWIA", "HMWICT",
        "HMWID", "HMWIL", "HMWILM", "HMWILN", "HMWILX", "HMWIN", "HMWIND",
        "HMWIWX", "HMWJAN", "HMWJAX", "HMWJKL", "HMWKEY", "HMWKS", "HMWKY",
        "HMWLA", "HMWLBF", "HMWLCH", "HMWLIX", "HMWLKN", "HMWLMK", "HMWLOT",
        "HMWLOX", "HMWLSX", "HMWLUB", "HMWLWX", "HMWLZK", "HMWMA", "HMWMAF",
        "HMWMCG", "HMWMCG", "HMWMD", "HMWME", "HMWMEG", "HMWMFL", "HMWMFR",
        "HMWMHX", "HMWMI", "HMWMKX", "HMWMLB", "HMWMN", "HMWMO", "HMWMOB",
        "HMWMPX", "HMWMQT", "HMWMRX", "HMWMS", "HMWMSO", "HMWMT", "HMWMTR",
        "HMWNC", "HMWND", "HMWNE", "HMWNH", "HMWNJ", "HMWNV", "HMWNY",
        "HMWOAX", "HMWOH", "HMWOHX", "HMWOK", "HMWOKX", "HMWOME", "HMWOR",
        "HMWOTX", "HMWOTZ", "HMWOUN", "HMWPA", "HMWPAH", "HMWPBZ", "HMWPDT",
        "HMWPHI", "HMWPIH", "HMWPPG", "HMWPQR", "HMWPR", "HMWPSR", "HMWPUB",
        "HMWRAH", "HMWREV", "HMWRI", "HMWRIW", "HMWRLX", "HMWRNK", "HMWSC",
        "HMWSC", "HMWSD", "HMWSEW", "HMWSGF", "HMWSGX", "HMWSHV", "HMWSJT",
        "HMWSJU", "HMWSLC", "HMWSNP", "HMWSPN", "HMWSTO", "HMWTAE", "HMWTBW",
        "HMWTFX", "HMWTN", "HMWTOP", "HMWTSA", "HMWTWC", "HMWUNR", "HMWUT",
        "HMWVA", "HMWVEF", "HMWVI", "HMWVT", "HMWWA", "HMWWI", "HMWWV",
        "HMWWY", "LAEABQ", "LAEABR", "LAEADQ", "LAEAFC", "LAEAFG", "LAEAJK",
        "LAEAK", "LAEAKN", "LAEAKQ", "LAEAL", "LAEALY", "LAEAMA", "LAEAPX",
        "LAEAR", "LAEARX", "LAEAS", "LAEAZ", "LAEBET", "LAEBGM", "LAEBIS",
        "LAEBMX", "LAEBOI", "LAEBOU", "LAEBOX", "LAEBRO", "LAEBRW", "LAEBTV",
        "LAEBUF", "LAEBYZ", "LAECA", "LAECAE", "LAECAR", "LAECDB", "LAECHS",
        "LAECLE", "LAECO", "LAECRP", "LAECT", "LAECTP", "LAECYS", "LAEDC",
        "LAEDDC", "LAEDE", "LAEDLH", "LAEDMX", "LAEDTX", "LAEDVN", "LAEEAX",
        "LAEEKA", "LAEEPZ", "LAEEWX", "LAEFFC", "LAEFGF", "LAEFGZ", "LAEFL",
        "LAEFSD", "LAEFWD", "LAEGA", "LAEGGW", "LAEGID", "LAEGJT", "LAEGLD",
        "LAEGRB", "LAEGRR", "LAEGSP", "LAEGU", "LAEGUM", "LAEGYX", "LAEHFO",
        "LAEHGX", "LAEHI", "LAEHNX", "LAEHUN", "LAEIA", "LAEICT", "LAEID",
        "LAEIL", "LAEILM", "LAEILN", "LAEILX", "LAEIN", "LAEIND", "LAEIWX",
        "LAEJAN", "LAEJAX", "LAEJKL", "LAEKEY", "LAEKS", "LAEKY", "LAELA",
        "LAELBF", "LAELCH", "LAELIX", "LAELKN", "LAELMK", "LAELOT", "LAELOX",
        "LAELSX", "LAELUB", "LAELWX", "LAELZK", "LAEMA", "LAEMAF", "LAEMCG",
        "LAEMCG", "LAEMD", "LAEME", "LAEMEG", "LAEMFL", "LAEMFR", "LAEMHX",
        "LAEMI", "LAEMKX", "LAEMLB", "LAEMN", "LAEMO", "LAEMOB", "LAEMPX",
        "LAEMQT", "LAEMRX", "LAEMS", "LAEMSO", "LAEMT", "LAEMTR", "LAENC",
        "LAEND", "LAENE", "LAENH", "LAENJ", "LAENV", "LAENY", "LAEOAX",
        "LAEOH", "LAEOHX", "LAEOK", "LAEOKX", "LAEOME", "LAEOR", "LAEOTX",
        "LAEOTZ", "LAEOUN", "LAEPA", "LAEPAH", "LAEPBZ", "LAEPDT", "LAEPHI",
        "LAEPIH", "LAEPPG", "LAEPQR", "LAEPR", "LAEPSR", "LAEPUB", "LAERAH",
        "LAEREV", "LAERI", "LAERIW", "LAERLX", "LAERNK", "LAESC", "LAESC",
        "LAESD", "LAESEW", "LAESGF", "LAESGX", "LAESHV", "LAESJT", "LAESJU",
        "LAESLC", "LAESNP", "LAESPN", "LAESTO", "LAETAE", "LAETBW", "LAETFX",
        "LAETN", "LAETOP", "LAETSA", "LAETWC", "LAEUNR", "LAEUT", "LAEVA",
        "LAEVEF", "LAEVI", "LAEVT", "LAEWA", "LAEWI", "LAEWV", "LAEWY",
        "LEWABQ", "LEWABR", "LEWADQ", "LEWAFC", "LEWAFG", "LEWAJK", "LEWAK",
        "LEWAKN", "LEWAKQ", "LEWAL", "LEWALY", "LEWAMA", "LEWAPX", "LEWAR",
        "LEWARX", "LEWAS", "LEWAZ", "LEWBET", "LEWBGM", "LEWBIS", "LEWBMX",
        "LEWBOI", "LEWBOU", "LEWBOX", "LEWBRO", "LEWBRW", "LEWBTV", "LEWBUF",
        "LEWBYZ", "LEWCA", "LEWCAE", "LEWCAR", "LEWCDB", "LEWCHS", "LEWCLE",
        "LEWCO", "LEWCRP", "LEWCT", "LEWCTP", "LEWCYS", "LEWDC", "LEWDDC",
        "LEWDE", "LEWDLH", "LEWDMX", "LEWDTX", "LEWDVN", "LEWEAX", "LEWEKA",
        "LEWEPZ", "LEWEWX", "LEWFFC", "LEWFGF", "LEWFGZ", "LEWFL", "LEWFSD",
        "LEWFWD", "LEWGA", "LEWGGW", "LEWGID", "LEWGJT", "LEWGLD", "LEWGRB",
        "LEWGRR", "LEWGSP", "LEWGU", "LEWGUM", "LEWGYX", "LEWHFO", "LEWHGX",
        "LEWHI", "LEWHNX", "LEWHUN", "LEWIA", "LEWICT", "LEWID", "LEWIL",
        "LEWILM", "LEWILN", "LEWILX", "LEWIN", "LEWIND", "LEWIWX", "LEWJAN",
        "LEWJAX", "LEWJKL", "LEWKEY", "LEWKS", "LEWKY", "LEWLA", "LEWLBF",
        "LEWLCH", "LEWLIX", "LEWLKN", "LEWLMK", "LEWLOT", "LEWLOX", "LEWLSX",
        "LEWLUB", "LEWLWX", "LEWLZK", "LEWMA", "LEWMAF", "LEWMCG", "LEWMCG",
        "LEWMD", "LEWME", "LEWMEG", "LEWMFL", "LEWMFR", "LEWMHX", "LEWMI",
        "LEWMKX", "LEWMLB", "LEWMN", "LEWMO", "LEWMOB", "LEWMPX", "LEWMQT",
        "LEWMRX", "LEWMS", "LEWMSO", "LEWMT", "LEWMTR", "LEWNC", "LEWND",
        "LEWNE", "LEWNH", "LEWNJ", "LEWNV", "LEWNY", "LEWOAX", "LEWOH",
        "LEWOHX", "LEWOK", "LEWOKX", "LEWOME", "LEWOR", "LEWOTX", "LEWOTZ",
        "LEWOUN", "LEWPA", "LEWPAH", "LEWPBZ", "LEWPDT", "LEWPHI", "LEWPIH",
        "LEWPPG", "LEWPQR", "LEWPR", "LEWPSR", "LEWPUB", "LEWRAH", "LEWREV",
        "LEWRI", "LEWRIW", "LEWRLX", "LEWRNK", "LEWSC", "LEWSC", "LEWSD",
        "LEWSEW", "LEWSGF", "LEWSGX", "LEWSHV", "LEWSJT", "LEWSJU", "LEWSLC",
        "LEWSNP", "LEWSPN", "LEWSTO", "LEWTAE", "LEWTBW", "LEWTFX", "LEWTN",
        "LEWTOP", "LEWTSA", "LEWTWC", "LEWUNR", "LEWUT", "LEWVA", "LEWVEF",
        "LEWVI", "LEWVT", "LEWWA", "LEWWI", "LEWWV", "LEWWY", "NUWABQ",
        "NUWABR", "NUWADQ", "NUWAFC", "NUWAFG", "NUWAJK", "NUWAK", "NUWAKN",
        "NUWAKQ", "NUWAL", "NUWALY", "NUWAMA", "NUWAPX", "NUWAR", "NUWARX",
        "NUWAS", "NUWAZ", "NUWBET", "NUWBGM", "NUWBIS", "NUWBMX", "NUWBOI",
        "NUWBOU", "NUWBOX", "NUWBRO", "NUWBRW", "NUWBTV", "NUWBUF", "NUWBYZ",
        "NUWCA", "NUWCAE", "NUWCAR", "NUWCDB", "NUWCHS", "NUWCLE", "NUWCO",
        "NUWCRP", "NUWCT", "NUWCTP", "NUWCYS", "NUWDC", "NUWDDC", "NUWDE",
        "NUWDLH", "NUWDMX", "NUWDTX", "NUWDVN", "NUWEAX", "NUWEKA", "NUWEPZ",
        "NUWEWX", "NUWFFC", "NUWFGF", "NUWFGZ", "NUWFL", "NUWFSD", "NUWFWD",
        "NUWGA", "NUWGGW", "NUWGID", "NUWGJT", "NUWGLD", "NUWGRB", "NUWGRR",
        "NUWGSP", "NUWGU", "NUWGUM", "NUWGYX", "NUWHFO", "NUWHGX", "NUWHI",
        "NUWHNX", "NUWHUN", "NUWIA", "NUWICT", "NUWID", "NUWIL", "NUWILM",
        "NUWILN", "NUWILX", "NUWIN", "NUWIND", "NUWIWX", "NUWJAN", "NUWJAX",
        "NUWJKL", "NUWKEY", "NUWKS", "NUWKY", "NUWLA", "NUWLBF", "NUWLCH",
        "NUWLIX", "NUWLKN", "NUWLMK", "NUWLOT", "NUWLOX", "NUWLSX", "NUWLUB",
        "NUWLWX", "NUWLZK", "NUWMA", "NUWMAF", "NUWMCG", "NUWMCG", "NUWMD",
        "NUWME", "NUWMEG", "NUWMFL", "NUWMFR", "NUWMHX", "NUWMI", "NUWMKX",
        "NUWMLB", "NUWMN", "NUWMO", "NUWMOB", "NUWMPX", "NUWMQT", "NUWMRX",
        "NUWMS", "NUWMSO", "NUWMT", "NUWMTR", "NUWNC", "NUWND", "NUWNE",
        "NUWNH", "NUWNJ", "NUWNV", "NUWNY", "NUWOAX", "NUWOH", "NUWOHX",
        "NUWOK", "NUWOKX", "NUWOME", "NUWOR", "NUWOTX", "NUWOTZ", "NUWOUN",
        "NUWPA", "NUWPAH", "NUWPBZ", "NUWPDT", "NUWPHI", "NUWPIH", "NUWPPG",
        "NUWPQR", "NUWPR", "NUWPSR", "NUWPUB", "NUWRAH", "NUWREV", "NUWRI",
        "NUWRIW", "NUWRLX", "NUWRNK", "NUWSC", "NUWSC", "NUWSD", "NUWSEW",
        "NUWSGF", "NUWSGX", "NUWSHV", "NUWSJT", "NUWSJU", "NUWSLC", "NUWSNP",
        "NUWSPN", "NUWSTO", "NUWTAE", "NUWTBW", "NUWTFX", "NUWTN", "NUWTOP",
        "NUWTSA", "NUWTWC", "NUWUNR", "NUWUT", "NUWVA", "NUWVEF", "NUWVI",
        "NUWVT", "NUWWA", "NUWWI", "NUWWV", "NUWWY", "RHWABQ", "RHWABR",
        "RHWADQ", "RHWAFC", "RHWAFG", "RHWAJK", "RHWAK", "RHWAKN", "RHWAKQ",
        "RHWAL", "RHWALY", "RHWAMA", "RHWAPX", "RHWAR", "RHWARX", "RHWAS",
        "RHWAZ", "RHWBET", "RHWBGM", "RHWBIS", "RHWBMX", "RHWBOI", "RHWBOU",
        "RHWBOX", "RHWBRO", "RHWBRW", "RHWBTV", "RHWBUF", "RHWBYZ", "RHWCA",
        "RHWCAE", "RHWCAR", "RHWCDB", "RHWCHS", "RHWCLE", "RHWCO", "RHWCRP",
        "RHWCT", "RHWCTP", "RHWCYS", "RHWDC", "RHWDDC", "RHWDE", "RHWDLH",
        "RHWDMX", "RHWDTX", "RHWDVN", "RHWEAX", "RHWEKA", "RHWEPZ", "RHWEWX",
        "RHWFFC", "RHWFGF", "RHWFGZ", "RHWFL", "RHWFSD", "RHWFWD", "RHWGA",
        "RHWGGW", "RHWGID", "RHWGJT", "RHWGLD", "RHWGRB", "RHWGRR", "RHWGSP",
        "RHWGU", "RHWGUM", "RHWGYX", "RHWHFO", "RHWHGX", "RHWHI", "RHWHNX",
        "RHWHUN", "RHWIA", "RHWICT", "RHWID", "RHWIL", "RHWILM", "RHWILN",
        "RHWILX", "RHWIN", "RHWIND", "RHWIWX", "RHWJAN", "RHWJAX", "RHWJKL",
        "RHWKEY", "RHWKS", "RHWKY", "RHWLA", "RHWLBF", "RHWLCH", "RHWLIX",
        "RHWLKN", "RHWLMK", "RHWLOT", "RHWLOX", "RHWLSX", "RHWLUB", "RHWLWX",
        "RHWLZK", "RHWMA", "RHWMAF", "RHWMCG", "RHWMCG", "RHWMD", "RHWME",
        "RHWMEG", "RHWMFL", "RHWMFR", "RHWMHX", "RHWMI", "RHWMKX", "RHWMLB",
        "RHWMN", "RHWMO", "RHWMOB", "RHWMPX", "RHWMQT", "RHWMRX", "RHWMS",
        "RHWMSO", "RHWMT", "RHWMTR", "RHWNC", "RHWND", "RHWNE", "RHWNH",
        "RHWNJ", "RHWNV", "RHWNY", "RHWOAX", "RHWOH", "RHWOHX", "RHWOK",
        "RHWOKX", "RHWOME", "RHWOR", "RHWOTX", "RHWOTZ", "RHWOUN", "RHWPA",
        "RHWPAH", "RHWPBZ", "RHWPDT", "RHWPHI", "RHWPIH", "RHWPPG", "RHWPQR",
        "RHWPR", "RHWPSR", "RHWPUB", "RHWRAH", "RHWREV", "RHWRI", "RHWRIW",
        "RHWRLX", "RHWRNK", "RHWSC", "RHWSC", "RHWSD", "RHWSEW", "RHWSGF",
        "RHWSGX", "RHWSHV", "RHWSJT", "RHWSJU", "RHWSLC", "RHWSNP", "RHWSPN",
        "RHWSTO", "RHWTAE", "RHWTBW", "RHWTFX", "RHWTN", "RHWTOP", "RHWTSA",
        "RHWTWC", "RHWUNR", "RHWUT", "RHWVA", "RHWVEF", "RHWVI", "RHWVT",
        "RHWWA", "RHWWI", "RHWWV", "RHWWY", "SPWABQ", "SPWABR", "SPWADQ",
        "SPWAFC", "SPWAFG", "SPWAJK", "SPWAK", "SPWAKN", "SPWAKQ", "SPWAL",
        "SPWALY", "SPWAMA", "SPWAPX", "SPWAR", "SPWARX", "SPWAS", "SPWAZ",
        "SPWBET", "SPWBGM", "SPWBIS", "SPWBMX", "SPWBOI", "SPWBOU", "SPWBOX",
        "SPWBRO", "SPWBRW", "SPWBTV", "SPWBUF", "SPWBYZ", "SPWCA", "SPWCAE",
        "SPWCAR", "SPWCDB", "SPWCHS", "SPWCLE", "SPWCO", "SPWCRP", "SPWCT",
        "SPWCTP", "SPWCYS", "SPWDC", "SPWDDC", "SPWDE", "SPWDLH", "SPWDMX",
        "SPWDTX", "SPWDVN", "SPWEAX", "SPWEKA", "SPWEPZ", "SPWEWX", "SPWFFC",
        "SPWFGF", "SPWFGZ", "SPWFL", "SPWFSD", "SPWFWD", "SPWGA", "SPWGGW",
        "SPWGID", "SPWGJT", "SPWGLD", "SPWGRB", "SPWGRR", "SPWGSP", "SPWGU",
        "SPWGUM", "SPWGYX", "SPWHFO", "SPWHI", "SPWHNX", "SPWHUN", "SPWIA",
        "SPWICT", "SPWID", "SPWIL", "SPWILM", "SPWILN", "SPWILX", "SPWIN",
        "SPWIND", "SPWIWX", "SPWJAN", "SPWJAX", "SPWJKL", "SPWKEY", "SPWKS",
        "SPWKY", "SPWLA", "SPWLBF", "SPWLCH", "SPWLIX", "SPWLKN", "SPWLMK",
        "SPWLOT", "SPWLOX", "SPWLSX", "SPWLUB", "SPWLWX", "SPWLZK", "SPWMA",
        "SPWMAF", "SPWMCG", "SPWMCG", "SPWMD", "SPWME", "SPWMEG", "SPWMFL",
        "SPWMFR", "SPWMHX", "SPWMI", "SPWMKX", "SPWMLB", "SPWMN", "SPWMO",
        "SPWMOB", "SPWMPX", "SPWMQT", "SPWMRX", "SPWMS", "SPWMSO", "SPWMT",
        "SPWMTR", "SPWNC", "SPWND", "SPWNE", "SPWNH", "SPWNJ", "SPWNV",
        "SPWNY", "SPWOAX", "SPWOH", "SPWOHX", "SPWOK", "SPWOKX", "SPWOME",
        "SPWOR", "SPWOTX", "SPWOTZ", "SPWOUN", "SPWPA", "SPWPAH", "SPWPBZ",
        "SPWPDT", "SPWPHI", "SPWPIH", "SPWPPG", "SPWPQR", "SPWPR", "SPWPSR",
        "SPWPUB", "SPWRAH", "SPWREV", "SPWRI", "SPWRIW", "SPWRLX", "SPWRNK",
        "SPWSC", "SPWSC", "SPWSD", "SPWSEW", "SPWSGF", "SPWSGX", "SPWSHV",
        "SPWSJT", "SPWSJU", "SPWSLC", "SPWSNP", "SPWSPN", "SPWSTO", "SPWTAE",
        "SPWTBW", "SPWTFX", "SPWTN", "SPWTOP", "SPWTSA", "SPWTWC", "SPWUNR",
        "SPWUT", "SPWVA", "SPWVEF", "SPWVI", "SPWVT", "SPWWA", "SPWWI",
        "SPWWV", "SPWWY", "TOEABQ", "TOEABR", "TOEADQ", "TOEAFC", "TOEAFG",
        "TOEAJK", "TOEAK", "TOEAKN", "TOEAKQ", "TOEAL", "TOEALY", "TOEAMA",
        "TOEAPX", "TOEAR", "TOEARX", "TOEAS", "TOEAZ", "TOEBET", "TOEBGM",
        "TOEBIS", "TOEBMX", "TOEBOI", "TOEBOU", "TOEBOX", "TOEBRO", "TOEBRW",
        "TOEBTV", "TOEBUF", "TOEBYZ", "TOECA", "TOECAE", "TOECAR", "TOECDB",
        "TOECHS", "TOECLE", "TOECO", "TOECRP", "TOECT", "TOECTP", "TOECYS",
        "TOEDC", "TOEDDC", "TOEDE", "TOEDLH", "TOEDMX", "TOEDTX", "TOEDVN",
        "TOEEAX", "TOEEKA", "TOEEPZ", "TOEEWX", "TOEFFC", "TOEFGF", "TOEFGZ",
        "TOEFL", "TOEFSD", "TOEFWD", "TOEGA", "TOEGGW", "TOEGID", "TOEGJT",
        "TOEGLD", "TOEGRB", "TOEGRR", "TOEGSP", "TOEGU", "TOEGUM", "TOEGYX",
        "TOEHFO", "TOEHGX", "TOEHI", "TOEHNX", "TOEHUN", "TOEIA", "TOEICT",
        "TOEID", "TOEIL", "TOEILM", "TOEILN", "TOEILX", "TOEIN", "TOEIND",
        "TOEIWX", "TOEJAN", "TOEJAX", "TOEJKL", "TOEKEY", "TOEKS", "TOEKY",
        "TOELA", "TOELBF", "TOELCH", "TOELIX", "TOELKN", "TOELMK", "TOELOT",
        "TOELOX", "TOELSX", "TOELUB", "TOELWX", "TOELZK", "TOEMA", "TOEMAF",
        "TOEMCG", "TOEMCG", "TOEMD", "TOEME", "TOEMEG", "TOEMFL", "TOEMFR",
        "TOEMHX", "TOEMI", "TOEMKX", "TOEMLB", "TOEMN", "TOEMO", "TOEMOB",
        "TOEMPX", "TOEMQT", "TOEMRX", "TOEMS", "TOEMSO", "TOEMT", "TOEMTR",
        "TOENC", "TOEND", "TOENE", "TOENH", "TOENJ", "TOENV", "TOENY",
        "TOEOAX", "TOEOH", "TOEOHX", "TOEOK", "TOEOKX", "TOEOME", "TOEOR",
        "TOEOTX", "TOEOTZ", "TOEOUN", "TOEPA", "TOEPAH", "TOEPBZ", "TOEPDT",
        "TOEPHI", "TOEPIH", "TOEPPG", "TOEPQR", "TOEPR", "TOEPSR", "TOEPUB",
        "TOERAH", "TOEREV", "TOERI", "TOERIW", "TOERLX", "TOERNK", "TOESC",
        "TOESC", "TOESD", "TOESEW", "TOESGF", "TOESGX", "TOESHV", "TOESJT",
        "TOESJU", "TOESLC", "TOESNP", "TOESPN", "TOESTO", "TOETAE", "TOETBW",
        "TOETFX", "TOETN", "TOETOP", "TOETSA", "TOETWC", "TOEUNR", "TOEUT",
        "TOEVA", "TOEVEF", "TOEVI", "TOEVT", "TOEWA", "TOEWI", "TOEWV",
        "TOEWY", "VOWABQ", "VOWABR", "VOWADQ", "VOWAFC", "VOWAFG", "VOWAJK",
        "VOWAK", "VOWAKN", "VOWAKQ", "VOWAL", "VOWALY", "VOWAMA", "VOWAPX",
        "VOWAR", "VOWARX", "VOWAS", "VOWAZ", "VOWBET", "VOWBGM", "VOWBIS",
        "VOWBMX", "VOWBOI", "VOWBOU", "VOWBOX", "VOWBRO", "VOWBRW", "VOWBTV",
        "VOWBUF", "VOWBYZ", "VOWCA", "VOWCAE", "VOWCAR", "VOWCDB", "VOWCHS",
        "VOWCLE", "VOWCO", "VOWCRP", "VOWCT", "VOWCTP", "VOWCYS", "VOWDC",
        "VOWDDC", "VOWDE", "VOWDLH", "VOWDMX", "VOWDTX", "VOWDVN", "VOWEAX",
        "VOWEKA", "VOWEPZ", "VOWEWX", "VOWFFC", "VOWFGF", "VOWFGZ", "VOWFL",
        "VOWFSD", "VOWFWD", "VOWGA", "VOWGGW", "VOWGID", "VOWGJT", "VOWGLD",
        "VOWGRB", "VOWGRR", "VOWGSP", "VOWGU", "VOWGUM", "VOWGYX", "VOWHFO",
        "VOWHGX", "VOWHI", "VOWHNX", "VOWHUN", "VOWIA", "VOWICT", "VOWID",
        "VOWIL", "VOWILM", "VOWILN", "VOWILX", "VOWIN", "VOWIND", "VOWIWX",
        "VOWJAN", "VOWJAX", "VOWJKL", "VOWKEY", "VOWKS", "VOWKY", "VOWLA",
        "VOWLBF", "VOWLCH", "VOWLIX", "VOWLKN", "VOWLMK", "VOWLOT", "VOWLOX",
        "VOWLSX", "VOWLUB", "VOWLWX", "VOWLZK", "VOWMA", "VOWMAF", "VOWMCG",
        "VOWMCG", "VOWMD", "VOWME", "VOWMEG", "VOWMFL", "VOWMFR", "VOWMHX",
        "VOWMI", "VOWMKX", "VOWMLB", "VOWMN", "VOWMO", "VOWMOB", "VOWMPX",
        "VOWMQT", "VOWMRX", "VOWMS", "VOWMSO", "VOWMT", "VOWMTR", "VOWNC",
        "VOWND", "VOWNE", "VOWNH", "VOWNJ", "VOWNV", "VOWNY", "VOWOAX",
        "VOWOH", "VOWOHX", "VOWOK", "VOWOKX", "VOWOME", "VOWOR", "VOWOTX",
        "VOWOTZ", "VOWOUN", "VOWPA", "VOWPAH", "VOWPBZ", "VOWPDT", "VOWPHI",
        "VOWPIH", "VOWPPG", "VOWPQR", "VOWPR", "VOWPSR", "VOWPUB", "VOWRAH",
        "VOWREV", "VOWRI", "VOWRIW", "VOWRLX", "VOWRNK", "VOWSC", "VOWSC",
        "VOWSD", "VOWSEW", "VOWSGF", "VOWSGX", "VOWSHV", "VOWSJT", "VOWSJU",
        "VOWSLC", "VOWSNP", "VOWSPN", "VOWSTO", "VOWTAE", "VOWTBW", "VOWTFX",
        "VOWTN", "VOWTOP", "VOWTSA", "VOWTWC", "VOWUNR", "VOWUT", "VOWVA",
        "VOWVEF", "VOWVI", "VOWVT", "VOWWA", "VOWWI", "VOWWV", "VOWWY"]

    ALL_ADMINISTRATIVE_MESSAGE = [
        "ADRABQ", "ADRABQ", "ADRABR", "ADRADQ", "ADRAFC", "ADRAFG", "ADRAJK",
        "ADRAK", "ADRAKN", "ADRAKQ", "ADRAKQ", "ADRAL", "ADRALB", "ADRALY",
        "ADRALY", "ADRAMA", "ADRAPX", "ADRAPX", "ADRAR", "ADRARX", "ADRARX",
        "ADRAS", "ADRAZ", "ADRBET", "ADRBGM", "ADRBGM", "ADRBIS", "ADRBIS",
        "ADRBMX", "ADRBOI", "ADRBOU", "ADRBOU", "ADRBOX", "ADRBOX", "ADRBRO",
        "ADRBRW", "ADRBTV", "ADRBTV", "ADRBUF", "ADRBUF", "ADRBYZ", "ADRCA",
        "ADRCAE", "ADRCAE", "ADRCAR", "ADRCAR", "ADRCDB", "ADRCHS", "ADRCHS",
        "ADRCLE", "ADRCLE", "ADRCO", "ADRCRP", "ADRCT", "ADRCTP", "ADRCTP",
        "ADRCYS", "ADRDC", "ADRDDC", "ADRDE", "ADRDLH", "ADRDMX", "ADRDMX",
        "ADRDTX", "ADRDVN", "ADREAX", "ADREKA", "ADREPZ", "ADREVV", "ADREWX",
        "ADRFFC", "ADRFGF", "ADRFGF", "ADRFGZ", "ADRFL", "ADRFSD", "ADRFWD",
        "ADRGA", "ADRGGW", "ADRGID", "ADRGJT", "ADRGJT", "ADRGLD", "ADRGRB",
        "ADRGRB", "ADRGRR", "ADRGSP", "ADRGSP", "ADRGU", "ADRGUM", "ADRGUM",
        "ADRGYX", "ADRGYX", "ADRHFO", "ADRHFO", "ADRHGX", "ADRHI", "ADRHNX",
        "ADRHUN", "ADRIA", "ADRICT", "ADRID", "ADRIL", "ADRILM", "ADRILM",
        "ADRILN", "ADRILN", "ADRILX", "ADRILX", "ADRIN", "ADRIN", "ADRIND",
        "ADRIWX", "ADRIWX", "ADRJAN", "ADRJAX", "ADRJKL", "ADRJKL", "ADRKEY",
        "ADRKRF", "ADRKS", "ADRKY", "ADRKY", "ADRLA", "ADRLBF", "ADRLCH",
        "ADRLIX", "ADRLKN", "ADRLMK", "ADRLOT", "ADRLOX", "ADRLSX", "ADRLUB",
        "ADRLWX", "ADRLWX", "ADRLZK", "ADRMA", "ADRMCG", "ADRMCG", "ADRMD",
        "ADRMD", "ADRME", "ADRME", "ADRMEG", "ADRMEI", "ADRMFL", "ADRMFR",
        "ADRMHX", "ADRMHX", "ADRMI", "ADRMKX", "ADRMKX", "ADRMLB", "ADRMN",
        "ADRMO", "ADRMOB", "ADRMPX", "ADRMPX", "ADRMQT", "ADRMQT", "ADRMRX",
        "ADRMS", "ADRMSO", "ADRMSR", "ADRMT", "ADRMTR", "ADRNC", "ADRNC",
        "ADRND", "ADRND", "ADRNE", "ADRNE", "ADRNH", "ADRNH", "ADRNJ",
        "ADRNJ", "ADRNM", "ADRNMC", "ADRNV", "ADRNY", "ADRNY", "ADRNY",
        "ADROAX", "ADROAX", "ADROH", "ADROHX", "ADROK", "ADROKX", "ADROKX",
        "ADROME", "ADROR", "ADROTX", "ADROTZ", "ADROUN", "ADRPA", "ADRPA",
        "ADRPAH", "ADRPBZ", "ADRPBZ", "ADRPDT", "ADRPDT", "ADRPHI", "ADRPHI",
        "ADRPIH", "ADRPPG", "ADRPQR", "ADRPR", "ADRPSR", "ADRPTR", "ADRPUB",
        "ADRPUB", "ADRRAH", "ADRRAH", "ADRRDU", "ADRREV", "ADRRI", "ADRRIW",
        "ADRRIW", "ADRRLX", "ADRRLX", "ADRRNK", "ADRRNK", "ADRSC", "ADRSC",
        "ADRSC", "ADRSD", "ADRSD", "ADRSEW", "ADRSGF", "ADRSGF", "ADRSGX",
        "ADRSHV", "ADRSJT", "ADRSJU", "ADRSLC", "ADRSNP", "ADRSPN", "ADRSTO",
        "ADRSTR", "ADRTAE", "ADRTBW", "ADRTFX", "ADRTN", "ADRTOP", "ADRTSA",
        "ADRTWC", "ADRUNR", "ADRUT", "ADRVA", "ADRVA", "ADRVEF", "ADRVI",
        "ADRVT", "ADRVT", "ADRWA", "ADRWI", "ADRWSH", "ADRWV", "ADRWV",
        "ADRWY", "ADRWY"]

    ALL_AVALANCHE_WATCH = [
        "AVAABQ", "AVAABR", "AVAADQ", "AVAAFC", "AVAAFG", "AVAAJK", "AVAAK",
        "AVAAKN", "AVAAKQ", "AVAAL", "AVAALY", "AVAAMA", "AVAAPX", "AVAAR",
        "AVAARX", "AVAAS", "AVAAZ", "AVABET", "AVABGM", "AVABIS", "AVABMX",
        "AVABOI", "AVABOU", "AVABOX", "AVABRO", "AVABRW", "AVABTV", "AVABUF",
        "AVABYZ", "AVACA", "AVACAE", "AVACAR", "AVACDB", "AVACHS", "AVACLE",
        "AVACO", "AVACRP", "AVACT", "AVACTP", "AVACYS", "AVADC", "AVADDC",
        "AVADE", "AVADLH", "AVADMX", "AVADTX", "AVADVN", "AVAEAX", "AVAEKA",
        "AVAEPZ", "AVAEWX", "AVAFFC", "AVAFGF", "AVAFGZ", "AVAFL", "AVAFSD",
        "AVAFWD", "AVAGA", "AVAGGW", "AVAGID", "AVAGJT", "AVAGLD", "AVAGRB",
        "AVAGRR", "AVAGSP", "AVAGU", "AVAGUM", "AVAGYX", "AVAHFO", "AVAHI",
        "AVAHNX", "AVAHUN", "AVAIA", "AVAICT", "AVAID", "AVAIL", "AVAILM",
        "AVAILN", "AVAILX", "AVAIN", "AVAIND", "AVAIWX", "AVAJAN", "AVAJAX",
        "AVAJKL", "AVAKEY", "AVAKS", "AVAKY", "AVALA", "AVALBF", "AVALCH",
        "AVALIX", "AVALKN", "AVALMK", "AVALOT", "AVALOX", "AVALSX", "AVALUB",
        "AVALWX", "AVALZK", "AVAMA", "AVAMAF", "AVAMCG", "AVAMCG", "AVAMD",
        "AVAME", "AVAMEG", "AVAMFL", "AVAMFR", "AVAMHX", "AVAMI", "AVAMKX",
        "AVAMLB", "AVAMN", "AVAMO", "AVAMOB", "AVAMPX", "AVAMQT", "AVAMRX",
        "AVAMS", "AVAMSO", "AVAMT", "AVAMTR", "AVANC", "AVAND", "AVANE",
        "AVANH", "AVANJ", "AVANV", "AVANY", "AVAOAX", "AVAOH", "AVAOHX",
        "AVAOK", "AVAOKX", "AVAOME", "AVAOR", "AVAOTX", "AVAOTZ", "AVAOUN",
        "AVAPA", "AVAPAH", "AVAPBZ", "AVAPDT", "AVAPHI", "AVAPIH", "AVAPPG",
        "AVAPQR", "AVAPR", "AVAPSR", "AVAPUB", "AVARAH", "AVAREV", "AVARI",
        "AVARIW", "AVARLX", "AVARNK", "AVASC", "AVASC", "AVASD", "AVASEW",
        "AVASGF", "AVASGX", "AVASHV", "AVASJT", "AVASJU", "AVASLC", "AVASNP",
        "AVASPN", "AVASTO", "AVATAE", "AVATBW", "AVATFX", "AVATN", "AVATOP",
        "AVATSA", "AVATWC", "AVAUNR", "AVAUT", "AVAVA", "AVAVEF", "AVAVI",
        "AVAVT", "AVAWA", "AVAWI", "AVAWV", "AVAWY"]

    ALL_AVALANCHE_WARNING = [
        "AVWABQ", "AVWABR", "AVWADQ", "AVWAFC", "AVWAFG", "AVWAJK", "AVWAK",
        "AVWAKN", "AVWAKQ", "AVWAL", "AVWALY", "AVWAPX", "AVWAR", "AVWARX",
        "AVWAS", "AVWAZ", "AVWBET", "AVWBGM", "AVWBIS", "AVWBMX", "AVWBOI",
        "AVWBOU", "AVWBOX", "AVWBRO", "AVWBRW", "AVWBTV", "AVWBUF", "AVWBYZ",
        "AVWCA", "AVWCAE", "AVWCAR", "AVWCDB", "AVWCHS", "AVWCLE", "AVWCO",
        "AVWCRP", "AVWCT", "AVWCTP", "AVWCYS", "AVWDC", "AVWDDC", "AVWDE",
        "AVWDLH", "AVWDMX", "AVWDTX", "AVWDVN", "AVWEAX", "AVWEKA", "AVWEPZ",
        "AVWEWX", "AVWFFC", "AVWFGF", "AVWFGZ", "AVWFL", "AVWFSD", "AVWFWD",
        "AVWGA", "AVWGGW", "AVWGID", "AVWGJT", "AVWGLD", "AVWGRB", "AVWGRR",
        "AVWGSP", "AVWGU", "AVWGUM", "AVWGYX", "AVWHFO", "AVWHI", "AVWHNX",
        "AVWHUN", "AVWIA", "AVWICT", "AVWID", "AVWIL", "AVWILM", "AVWILN",
        "AVWILX", "AVWIN", "AVWIND", "AVWIWX", "AVWJAN", "AVWJAX", "AVWJKL",
        "AVWKEY", "AVWKS", "AVWKY", "AVWLA", "AVWLBF", "AVWLCH", "AVWLIX",
        "AVWLKN", "AVWLMK", "AVWLOT", "AVWLOX", "AVWLSX", "AVWLUB", "AVWLWX",
        "AVWLZK", "AVWMA", "AVWMAF", "AVWMCG", "AVWMCG", "AVWMD", "AVWME",
        "AVWMEG", "AVWMFL", "AVWMFR", "AVWMHX", "AVWMI", "AVWMKX", "AVWMLB",
        "AVWMN", "AVWMO", "AVWMOB", "AVWMPX", "AVWMQT", "AVWMRX", "AVWMS",
        "AVWMSO", "AVWMT", "AVWMTR", "AVWNC", "AVWND", "AVWNE", "AVWNH",
        "AVWNJ", "AVWNV", "AVWNY", "AVWOAX", "AVWOH", "AVWOHX", "AVWOK",
        "AVWOKX", "AVWOME", "AVWOR", "AVWOTX", "AVWOTZ", "AVWOUN", "AVWPA",
        "AVWPAH", "AVWPBZ", "AVWPDT", "AVWPHI", "AVWPIH", "AVWPPG", "AVWPQR",
        "AVWPR", "AVWPSR", "AVWPUB", "AVWRAH", "AVWREV", "AVWRI", "AVWRIW",
        "AVWRLX", "AVWRNK", "AVWSC", "AVWSC", "AVWSD", "AVWSEW", "AVWSGF",
        "AVWSGX", "AVWSHV", "AVWSJT", "AVWSJU", "AVWSLC", "AVWSNP", "AVWSPN",
        "AVWSTO", "AVWTAE", "AVWTBW", "AVWTFX", "AVWTN", "AVWTOP", "AVWTSA",
        "AVWTWC", "AVWUNR", "AVWUT", "AVWVA", "AVWVEF", "AVWVI", "AVWVT",
        "AVWWA", "AVWWI", "AVWWV", "AVWWY"]

    ALL_BLUE_ALERT = [
        "BLUABQ", "BLUABR", "BLUADQ", "BLUAFC", "BLUAFG", "BLUAJK", "BLUAK",
        "BLUAKQ", "BLUAL", "BLUALY", "BLUAMA", "BLUAPX", "BLUAR", "BLUARX",
        "BLUAS", "BLUAZ", "BLUBGM", "BLUBIS", "BLUBMX", "BLUBOI", "BLUBOU",
        "BLUBOX", "BLUBRO", "BLUBTV", "BLUBTV", "BLUBUF", "BLUBYZ", "BLUCA",
        "BLUCAE", "BLUCAR", "BLUCHS", "BLUCLE", "BLUCO", "BLUCRP", "BLUCT",
        "BLUCTP", "BLUCYS", "BLUDC", "BLUDDC", "BLUDE", "BLUDLH", "BLUDMX",
        "BLUDTX", "BLUDVN", "BLUEAX", "BLUEKA", "BLUEPZ", "BLUEWX", "BLUFFC",
        "BLUFGF", "BLUFGZ", "BLUFL", "BLUFSD", "BLUFWD", "BLUGA", "BLUGGW",
        "BLUGID", "BLUGJT", "BLUGLD", "BLUGRB", "BLUGRR", "BLUGSP", "BLUGU",
        "BLUGUM", "BLUGYX", "BLUHFO", "BLUHGX", "BLUHI", "BLUHNX", "BLUHUN",
        "BLUIA", "BLUICT", "BLUID", "BLUIL", "BLUILM", "BLUILN", "BLUILX",
        "BLUIN", "BLUIND", "BLUIWX", "BLUJAN", "BLUJAX", "BLUJKL", "BLUKEY",
        "BLUKS", "BLUKY", "BLULA", "BLULBF", "BLULCH", "BLULIX", "BLULKN",
        "BLULMK", "BLULOT", "BLULOX", "BLULSX", "BLULUB", "BLULWX", "BLULZK",
        "BLUMA", "BLUMAF", "BLUMD", "BLUME", "BLUMEG", "BLUMFL", "BLUMFR",
        "BLUMHX", "BLUMI", "BLUMKX", "BLUMLB", "BLUMN", "BLUMO", "BLUMOB",
        "BLUMPX", "BLUMQT", "BLUMRX", "BLUMS", "BLUMSO", "BLUMT", "BLUMTR",
        "BLUNC", "BLUND", "BLUNE", "BLUNH", "BLUNJ", "BLUNM", "BLUNV",
        "BLUNY", "BLUOAX", "BLUOH", "BLUOHX", "BLUOK", "BLUOKX", "BLUOME",
        "BLUOR", "BLUOTX", "BLUOUN", "BLUPA", "BLUPAH", "BLUPBZ", "BLUPDT",
        "BLUPHI", "BLUPIH", "BLUPPG", "BLUPQR", "BLUPR", "BLUPSR", "BLUPUB",
        "BLURAH", "BLUREV", "BLURI", "BLURIW", "BLURLX", "BLURNK", "BLUSC",
        "BLUSD", "BLUSEW", "BLUSGF", "BLUSGX", "BLUSHV", "BLUSJT", "BLUSJU",
        "BLUSLC", "BLUSPN", "BLUSTO", "BLUTAE", "BLUTBW", "BLUTFX", "BLUTN",
        "BLUTOP", "BLUTSA", "BLUTWC", "BLUTX", "BLUUNR", "BLUUT", "BLUVA",
        "BLUVEF", "BLUVI", "BLUWA", "BLUWI", "BLUWV", "BLUWY", "BLUYAK"]

    ALL_CHILD_ABDUCTION_EMERGENCY = [
        "CAEABQ", "CAEABR", "CAEADQ", "CAEAFC", "CAEAFG", "CAEAJK", "CAEAK",
        "CAEAKN", "CAEAKQ", "CAEAL", "CAEALY", "CAEAMA", "CAEAPX", "CAEAR",
        "CAEARX", "CAEAS", "CAEAZ", "CAEBET", "CAEBGM", "CAEBIS", "CAEBMX",
        "CAEBOI", "CAEBOU", "CAEBOX", "CAEBRO", "CAEBRW", "CAEBTV", "CAEBUF",
        "CAEBYZ", "CAECA", "CAECAE", "CAECAR", "CAECDB", "CAECHS", "CAECLE",
        "CAECO", "CAECRP", "CAECT", "CAECTP", "CAECYS", "CAEDC", "CAEDDC",
        "CAEDE", "CAEDLH", "CAEDMX", "CAEDTX", "CAEDVN", "CAEEAX", "CAEEKA",
        "CAEEPZ", "CAEEWX", "CAEFFC", "CAEFGF", "CAEFGZ", "CAEFL", "CAEFSD",
        "CAEFWD", "CAEGA", "CAEGGW", "CAEGID", "CAEGJT", "CAEGLD", "CAEGRB",
        "CAEGRR", "CAEGSP", "CAEGU", "CAEGUM", "CAEGYX", "CAEHFO", "CAEHGX",
        "CAEHI", "CAEHNX", "CAEHUN", "CAEIA", "CAEICT", "CAEID", "CAEIL",
        "CAEILM", "CAEILN", "CAEILX", "CAEIN", "CAEIND", "CAEIWX", "CAEJAN",
        "CAEJAX", "CAEJKL", "CAEKEY", "CAEKS", "CAEKY", "CAELA", "CAELBF",
        "CAELCH", "CAELIX", "CAELKN", "CAELMK", "CAELOT", "CAELOX", "CAELSX",
        "CAELUB", "CAELWX", "CAELZK", "CAEMA", "CAEMAF", "CAEMCG", "CAEMCG",
        "CAEMD", "CAEME", "CAEMEG", "CAEMFL", "CAEMFR", "CAEMHX", "CAEMI",
        "CAEMKX", "CAEMLB", "CAEMN", "CAEMO", "CAEMOB", "CAEMPX", "CAEMQT",
        "CAEMRX", "CAEMS", "CAEMSO", "CAEMT", "CAEMTR", "CAENC", "CAEND",
        "CAENE", "CAENH", "CAENJ", "CAENV", "CAENY", "CAEOAX", "CAEOH",
        "CAEOHX", "CAEOK", "CAEOKX", "CAEOME", "CAEOR", "CAEOTX", "CAEOTZ",
        "CAEOUN", "CAEPA", "CAEPAH", "CAEPBZ", "CAEPDT", "CAEPHI", "CAEPIH",
        "CAEPPG", "CAEPQR", "CAEPR", "CAEPSR", "CAEPUB", "CAERAH", "CAEREV",
        "CAERI", "CAERIW", "CAERLX", "CAERNK", "CAESC", "CAESC", "CAESD",
        "CAESEW", "CAESGF", "CAESGX", "CAESHV", "CAESJT", "CAESJU", "CAESLC",
        "CAESNP", "CAESPN", "CAESTO", "CAETAE", "CAETBW", "CAETFX", "CAETN",
        "CAETOP", "CAETSA", "CAETWC", "CAEUNR", "CAEUT", "CAEVA", "CAEVEF",
        "CAEVI", "CAEVT", "CAEWA", "CAEWI", "CAEWV", "CAEWY"]

    ALL_CIVIL_DANGER_WARNING = [
        "CDWABQ", "CDWABR", "CDWADQ", "CDWAFC", "CDWAFG", "CDWAJK", "CDWAK",
        "CDWAKN", "CDWAKQ", "CDWAL", "CDWALY", "CDWAMA", "CDWAPX", "CDWAR",
        "CDWARX", "CDWAS", "CDWAZ", "CDWBET", "CDWBGM", "CDWBIS", "CDWBMX",
        "CDWBOI", "CDWBOU", "CDWBOX", "CDWBRO", "CDWBRW", "CDWBTV", "CDWBUF",
        "CDWBYZ", "CDWCA", "CDWCAE", "CDWCAR", "CDWCDB", "CDWCHS", "CDWCLE",
        "CDWCO", "CDWCRP", "CDWCT", "CDWCTP", "CDWCYS", "CDWDC", "CDWDDC",
        "CDWDE", "CDWDLH", "CDWDMX", "CDWDTX", "CDWDVN", "CDWEAX", "CDWEKA",
        "CDWEPZ", "CDWEWX", "CDWFFC", "CDWFGF", "CDWFGZ", "CDWFL", "CDWFSD",
        "CDWFWD", "CDWGA", "CDWGGW", "CDWGID", "CDWGJT", "CDWGLD", "CDWGRB",
        "CDWGRR", "CDWGSP", "CDWGU", "CDWGUM", "CDWGYX", "CDWHFO", "CDWHGX",
        "CDWHI", "CDWHNX", "CDWHUN", "CDWIA", "CDWICT", "CDWID", "CDWIL",
        "CDWILM", "CDWILN", "CDWILX", "CDWIN", "CDWIND", "CDWIWX", "CDWJAN",
        "CDWJAX", "CDWJKL", "CDWKEY", "CDWKS", "CDWKY", "CDWLA", "CDWLBF",
        "CDWLCH", "CDWLIX", "CDWLKN", "CDWLMK", "CDWLOT", "CDWLOX", "CDWLSX",
        "CDWLUB", "CDWLWX", "CDWLZK", "CDWMA", "CDWMAF", "CDWMCG", "CDWMCG",
        "CDWMD", "CDWME", "CDWMEG", "CDWMFL", "CDWMFR", "CDWMHX", "CDWMI",
        "CDWMI", "CDWMKX", "CDWMLB", "CDWMN", "CDWMO", "CDWMOB", "CDWMPX",
        "CDWMQT", "CDWMRX", "CDWMS", "CDWMSO", "CDWMT", "CDWMTR", "CDWNC",
        "CDWND", "CDWNE", "CDWNH", "CDWNJ", "CDWNV", "CDWNY", "CDWOAX",
        "CDWOH", "CDWOHX", "CDWOK", "CDWOKX", "CDWOME", "CDWOR", "CDWOTX",
        "CDWOTZ", "CDWOUN", "CDWPA", "CDWPAH", "CDWPBZ", "CDWPDT", "CDWPHI",
        "CDWPIH", "CDWPPG", "CDWPQR", "CDWPR", "CDWPSR", "CDWPUB", "CDWRAH",
        "CDWREV", "CDWRI", "CDWRIW", "CDWRLX", "CDWRNK", "CDWSC", "CDWSC",
        "CDWSD", "CDWSEW", "CDWSGF", "CDWSGX", "CDWSHV", "CDWSJT", "CDWSJU",
        "CDWSLC", "CDWSNP", "CDWSPN", "CDWSTO", "CDWTAE", "CDWTBW", "CDWTFX",
        "CDWTN", "CDWTOP", "CDWTSA", "CDWTWC", "CDWUNR", "CDWUT", "CDWVA",
        "CDWVEF", "CDWVI", "CDWVT", "CDWWA", "CDWWI", "CDWWV", "CDWWY"]

    ALL_CIVIL_EMERGENCY_MESSAGE = [
        "CEMABQ", "CEMABR", "CEMADQ", "CEMAER", "CEMAFC", "CEMAFG", "CEMAJK",
        "CEMAK", "CEMAKN", "CEMAKQ", "CEMAL", "CEMALU", "CEMALY", "CEMAMA",
        "CEMAPX", "CEMAR", "CEMARX", "CEMAS", "CEMAZ", "CEMBET", "CEMBGM",
        "CEMBIS", "CEMBMX", "CEMBOI", "CEMBOU", "CEMBOX", "CEMBRO", "CEMBRW",
        "CEMBTV", "CEMBUF", "CEMBYZ", "CEMCA", "CEMCAE", "CEMCAR", "CEMCDB",
        "CEMCHS", "CEMCLE", "CEMCO", "CEMCRP", "CEMCT", "CEMCTP", "CEMCYS",
        "CEMDC", "CEMDDC", "CEMDE", "CEMDLH", "CEMDMX", "CEMDTX", "CEMDVN",
        "CEMEAX", "CEMEKA", "CEMEPZ", "CEMEWX", "CEMFFC", "CEMFGF", "CEMFGZ",
        "CEMFL", "CEMFSD", "CEMFWD", "CEMGA", "CEMGGW", "CEMGID", "CEMGJT",
        "CEMGLD", "CEMGRB", "CEMGRR", "CEMGSP", "CEMGU", "CEMGUM", "CEMGYX",
        "CEMHFO", "CEMHGX", "CEMHI", "CEMHNX", "CEMHON", "CEMHUN", "CEMIA",
        "CEMICT", "CEMID", "CEMIL", "CEMILM", "CEMILN", "CEMILX", "CEMIN",
        "CEMIND", "CEMIWX", "CEMJAN", "CEMJAX", "CEMJKL", "CEMKEY", "CEMKS",
        "CEMKY", "CEMLA", "CEMLBF", "CEMLCH", "CEMLIX", "CEMLKN", "CEMLMK",
        "CEMLOT", "CEMLOX", "CEMLSX", "CEMLUB", "CEMLWX", "CEMLZK", "CEMMA",
        "CEMMAF", "CEMMCG", "CEMMCG", "CEMMD", "CEMME", "CEMMEG", "CEMMFL",
        "CEMMFR", "CEMMHX", "CEMMI", "CEMMKX", "CEMMLB", "CEMMN", "CEMMO",
        "CEMMOB", "CEMMPX", "CEMMQT", "CEMMRX", "CEMMS", "CEMMSO", "CEMMT",
        "CEMMTR", "CEMMY", "CEMNC", "CEMND", "CEMNE", "CEMNH", "CEMNJ",
        "CEMNM", "CEMNV", "CEMNY", "CEMOAX", "CEMOH", "CEMOHX", "CEMOK",
        "CEMOKX", "CEMOME", "CEMOR", "CEMOTX", "CEMOTZ", "CEMOUN", "CEMPA",
        "CEMPAH", "CEMPBZ", "CEMPDT", "CEMPHI", "CEMPIH", "CEMPPG", "CEMPQR",
        "CEMPR", "CEMPSR", "CEMPUB", "CEMRAH", "CEMREV", "CEMRI", "CEMRIW",
        "CEMRLX", "CEMRNK", "CEMSC", "CEMSC", "CEMSD", "CEMSEW", "CEMSGF",
        "CEMSGX", "CEMSHV", "CEMSJT", "CEMSJU", "CEMSLC", "CEMSNP", "CEMSPN",
        "CEMSTO", "CEMTAE", "CEMTBW", "CEMTFX", "CEMTN", "CEMTOP", "CEMTSA",
        "CEMTWC", "CEMTX", "CEMUNR", "CEMUT", "CEMVA", "CEMVEF", "CEMVI",
        "CEMVT", "CEMVWS", "CEMWA", "CEMWI", "CEMWV", "CEMWY"]

    ALL_EARTHQUAKE_WARNING = [
        "EQWABQ", "EQWABR", "EQWADQ", "EQWAFC", "EQWAFG", "EQWAJK", "EQWAK",
        "EQWAKN", "EQWAKQ", "EQWAL", "EQWALY", "EQWAMA", "EQWAPX", "EQWAR",
        "EQWARX", "EQWAS", "EQWAZ", "EQWBET", "EQWBGM", "EQWBIS", "EQWBMX",
        "EQWBOI", "EQWBOU", "EQWBOX", "EQWBRO", "EQWBRW", "EQWBTV", "EQWBUF",
        "EQWBYZ", "EQWCA", "EQWCAE", "EQWCAR", "EQWCDB", "EQWCHS", "EQWCLE",
        "EQWCO", "EQWCRP", "EQWCT", "EQWCTP", "EQWCYS", "EQWDC", "EQWDDC",
        "EQWDE", "EQWDLH", "EQWDMX", "EQWDTX", "EQWDVN", "EQWEAX", "EQWEKA",
        "EQWEPZ", "EQWEWX", "EQWFFC", "EQWFGF", "EQWFGZ", "EQWFL", "EQWFSD",
        "EQWFWD", "EQWGA", "EQWGGW", "EQWGID", "EQWGJT", "EQWGLD", "EQWGRB",
        "EQWGRR", "EQWGSP", "EQWGU", "EQWGUM", "EQWGYX", "EQWHFO", "EQWHGX",
        "EQWHI", "EQWHNX", "EQWHUN", "EQWIA", "EQWICT", "EQWID", "EQWIL",
        "EQWILM", "EQWILN", "EQWILX", "EQWIN", "EQWIND", "EQWIWX", "EQWJAN",
        "EQWJAX", "EQWJKL", "EQWKEY", "EQWKS", "EQWKY", "EQWLA", "EQWLBF",
        "EQWLCH", "EQWLIX", "EQWLKN", "EQWLMK", "EQWLOT", "EQWLOX", "EQWLSX",
        "EQWLUB", "EQWLWX", "EQWLZK", "EQWMA", "EQWMAF", "EQWMCG", "EQWMCG",
        "EQWMD", "EQWME", "EQWMEG", "EQWMFL", "EQWMFR", "EQWMHX", "EQWMI",
        "EQWMKX", "EQWMLB", "EQWMN", "EQWMO", "EQWMOB", "EQWMPX", "EQWMQT",
        "EQWMRX", "EQWMS", "EQWMSO", "EQWMT", "EQWMTR", "EQWNC", "EQWND",
        "EQWNE", "EQWNH", "EQWNJ", "EQWNV", "EQWNY", "EQWOAX", "EQWOH",
        "EQWOHX", "EQWOK", "EQWOKX", "EQWOME", "EQWOR", "EQWOTX", "EQWOTZ",
        "EQWOUN", "EQWPA", "EQWPAH", "EQWPBZ", "EQWPDT", "EQWPHI", "EQWPIH",
        "EQWPPG", "EQWPQR", "EQWPR", "EQWPSR", "EQWPUB", "EQWRAH", "EQWREV",
        "EQWRI", "EQWRIW", "EQWRLX", "EQWRNK", "EQWSC", "EQWSC", "EQWSD",
        "EQWSEW", "EQWSGF", "EQWSGX", "EQWSJT", "EQWSJU", "EQWSLC", "EQWSNP",
        "EQWSPN", "EQWSTO", "EQWTAE", "EQWTBW", "EQWTFX", "EQWTN", "EQWTOP",
        "EQWTSA", "EQWTWC", "EQWUNR", "EQWUT", "EQWVA", "EQWVEF", "EQWVI",
        "EQWVT", "EQWWA", "EQWWI", "EQWWV", "EQWWY"]

    ALL_EVACUATION_IMMEDIATE = [
        "EVIABQ", "EVIABR", "EVIADQ", "EVIAFC", "EVIAFG", "EVIAJK", "EVIAK",
        "EVIAKN", "EVIAKQ", "EVIAL", "EVIALY", "EVIAMA", "EVIAPX", "EVIAR",
        "EVIARX", "EVIAS", "EVIAZ", "EVIBET", "EVIBGM", "EVIBIS", "EVIBMX",
        "EVIBOI", "EVIBOU", "EVIBOX", "EVIBRO", "EVIBRW", "EVIBTV", "EVIBUF",
        "EVIBYZ", "EVICA", "EVICAE", "EVICAR", "EVICDB", "EVICHS", "EVICLE",
        "EVICO", "EVICRP", "EVICT", "EVICTP", "EVICYS", "EVIDC", "EVIDDC",
        "EVIDE", "EVIDLH", "EVIDMX", "EVIDTX", "EVIDVN", "EVIEAX", "EVIEKA",
        "EVIEPZ", "EVIEWX", "EVIFFC", "EVIFGF", "EVIFGZ", "EVIFL", "EVIFSD",
        "EVIFWD", "EVIGA", "EVIGGW", "EVIGID", "EVIGJT", "EVIGLD", "EVIGRB",
        "EVIGRR", "EVIGSP", "EVIGU", "EVIGUM", "EVIGYX", "EVIHFO", "EVIHGX",
        "EVIHI", "EVIHNX", "EVIHUN", "EVIIA", "EVIICT", "EVIID", "EVIIL",
        "EVIILM", "EVIILN", "EVIILX", "EVIIN", "EVIIND", "EVIIWX", "EVIJAN",
        "EVIJAX", "EVIJKL", "EVIKEY", "EVIKS", "EVIKY", "EVILA", "EVILBF",
        "EVILCH", "EVILIX", "EVILKN", "EVILMK", "EVILOT", "EVILOX", "EVILSX",
        "EVILUB", "EVILWX", "EVILZK", "EVIMA", "EVIMAF", "EVIMCG", "EVIMCG",
        "EVIMD", "EVIME", "EVIMEG", "EVIMFL", "EVIMFR", "EVIMHX", "EVIMI",
        "EVIMKX", "EVIMLB", "EVIMN", "EVIMO", "EVIMOB", "EVIMPX", "EVIMQT",
        "EVIMRX", "EVIMS", "EVIMSO", "EVIMT", "EVIMTR", "EVINC", "EVIND",
        "EVINE", "EVINH", "EVINJ", "EVINV", "EVINY", "EVIOAX", "EVIOH",
        "EVIOHX", "EVIOK", "EVIOKX", "EVIOME", "EVIOR", "EVIOTX", "EVIOTZ",
        "EVIOUN", "EVIPA", "EVIPAH", "EVIPBZ", "EVIPDT", "EVIPHI", "EVIPIH",
        "EVIPPG", "EVIPQR", "EVIPR", "EVIPSR", "EVIPUB", "EVIRAH", "EVIREV",
        "EVIRI", "EVIRIW", "EVIRLX", "EVIRNK", "EVISC", "EVISC", "EVISD",
        "EVISEW", "EVISGF", "EVISGX", "EVISHV", "EVISJT", "EVISJU", "EVISLC",
        "EVISNP", "EVISPN", "EVISTO", "EVITAE", "EVITBW", "EVITFX", "EVITN",
        "EVITOP", "EVITSA", "EVITWC", "EVIUNR", "EVIUT", "EVIVA", "EVIVEF",
        "EVIVI", "EVIVT", "EVIWA", "EVIWI", "EVIWV", "EVIWY"]

    ALL_FIRE_WARNING = [
        "FRWABQ", "FRWABR", "FRWADQ", "FRWAFC", "FRWAFG", "FRWAJK", "FRWAK",
        "FRWAKN", "FRWAKQ", "FRWAL", "FRWALY", "FRWAMA", "FRWAPX", "FRWAR",
        "FRWARX", "FRWAS", "FRWAZ", "FRWBET", "FRWBGM", "FRWBIS", "FRWBMX",
        "FRWBOI", "FRWBOU", "FRWBOX", "FRWBRO", "FRWBRW", "FRWBTV", "FRWBUF",
        "FRWBYZ", "FRWCA", "FRWCAE", "FRWCAR", "FRWCDB", "FRWCHS", "FRWCLE",
        "FRWCO", "FRWCRP", "FRWCT", "FRWCTP", "FRWCYS", "FRWDC", "FRWDDC",
        "FRWDE", "FRWDLH", "FRWDMX", "FRWDTX", "FRWDVN", "FRWEAX", "FRWEKA",
        "FRWEPZ", "FRWEWX", "FRWFFC", "FRWFGF", "FRWFGZ", "FRWFL", "FRWFSD",
        "FRWFWD", "FRWGA", "FRWGGW", "FRWGID", "FRWGJT", "FRWGLD", "FRWGRB",
        "FRWGRR", "FRWGSP", "FRWGU", "FRWGUM", "FRWGYX", "FRWHFO", "FRWHGX",
        "FRWHI", "FRWHNX", "FRWHUN", "FRWIA", "FRWICT", "FRWID", "FRWIL",
        "FRWILM", "FRWILN", "FRWILX", "FRWIN", "FRWIND", "FRWIWX", "FRWJAN",
        "FRWJAX", "FRWJKL", "FRWKEY", "FRWKS", "FRWKY", "FRWLA", "FRWLBF",
        "FRWLIX", "FRWLKN", "FRWLMK", "FRWLOT", "FRWLOX", "FRWLSX", "FRWLUB",
        "FRWLWX", "FRWLZK", "FRWMA", "FRWMAF", "FRWMCG", "FRWMCG", "FRWMD",
        "FRWME", "FRWMEG", "FRWMFL", "FRWMFR", "FRWMHX", "FRWMI", "FRWMKX",
        "FRWMLB", "FRWMN", "FRWMO", "FRWMOB", "FRWMPX", "FRWMQT", "FRWMRX",
        "FRWMS", "FRWMSO", "FRWMT", "FRWMTR", "FRWNC", "FRWND", "FRWNE",
        "FRWNH", "FRWNJ", "FRWNV", "FRWNY", "FRWOAX", "FRWOH", "FRWOHX",
        "FRWOK", "FRWOKX", "FRWOME", "FRWOR", "FRWOTX", "FRWOTZ", "FRWOUN",
        "FRWPA", "FRWPAH", "FRWPBZ", "FRWPDT", "FRWPHI", "FRWPIH", "FRWPPG",
        "FRWPQR", "FRWPR", "FRWPSR", "FRWPUB", "FRWRAH", "FRWREV", "FRWRI",
        "FRWRIW", "FRWRLX", "FRWRNK", "FRWSC", "FRWSC", "FRWSD", "FRWSEW",
        "FRWSGF", "FRWSGX", "FRWSHV", "FRWSJT", "FRWSJU", "FRWSLC", "FRWSNP",
        "FRWSPN", "FRWSTO", "FRWTAE", "FRWTBW", "FRWTFX", "FRWTN", "FRWTOP",
        "FRWTSA", "FRWTWC", "FRWUNR", "FRWUT", "FRWVA", "FRWVEF", "FRWVI",
        "FRWVT", "FRWWA", "FRWWI", "FRWWV", "FRWWY"]

    ALL_HAZARDOUS_MATERIALS_WARNING = [
        "HMWABQ", "HMWABR", "HMWADQ", "HMWAFC", "HMWAFG", "HMWAJK", "HMWAK",
        "HMWAKN", "HMWAKQ", "HMWAL", "HMWALY", "HMWAPX", "HMWAR", "HMWARX",
        "HMWAS", "HMWAZ", "HMWBET", "HMWBGM", "HMWBIS", "HMWBMX", "HMWBOI",
        "HMWBOU", "HMWBOX", "HMWBRO", "HMWBRW", "HMWBTV", "HMWBUF", "HMWBYZ",
        "HMWCA", "HMWCAE", "HMWCAR", "HMWCDB", "HMWCHS", "HMWCLE", "HMWCO",
        "HMWCRP", "HMWCT", "HMWCTP", "HMWCYS", "HMWDC", "HMWDDC", "HMWDE",
        "HMWDLH", "HMWDMX", "HMWDTX", "HMWDVN", "HMWEAX", "HMWEKA", "HMWEPZ",
        "HMWEWX", "HMWFFC", "HMWFGF", "HMWFGZ", "HMWFL", "HMWFSD", "HMWFWD",
        "HMWGA", "HMWGGW", "HMWGID", "HMWGJT", "HMWGLD", "HMWGRB", "HMWGRR",
        "HMWGSP", "HMWGU", "HMWGUM", "HMWGYX", "HMWHFO", "HMWHGX", "HMWHI",
        "HMWHNX", "HMWHUN", "HMWIA", "HMWICT", "HMWID", "HMWIL", "HMWILM",
        "HMWILN", "HMWILX", "HMWIN", "HMWIND", "HMWIWX", "HMWJAN", "HMWJAX",
        "HMWJKL", "HMWKEY", "HMWKS", "HMWKY", "HMWLA", "HMWLBF", "HMWLCH",
        "HMWLIX", "HMWLKN", "HMWLMK", "HMWLOT", "HMWLOX", "HMWLSX", "HMWLUB",
        "HMWLWX", "HMWLZK", "HMWMA", "HMWMAF", "HMWMCG", "HMWMCG", "HMWMD",
        "HMWME", "HMWMEG", "HMWMFL", "HMWMFR", "HMWMHX", "HMWMI", "HMWMKX",
        "HMWMLB", "HMWMN", "HMWMO", "HMWMOB", "HMWMPX", "HMWMQT", "HMWMRX",
        "HMWMS", "HMWMSO", "HMWMT", "HMWMTR", "HMWNC", "HMWND", "HMWNE",
        "HMWNH", "HMWNJ", "HMWNV", "HMWNY", "HMWOAX", "HMWOH", "HMWOHX",
        "HMWOK", "HMWOKX", "HMWOME", "HMWOR", "HMWOTX", "HMWOTZ", "HMWOUN",
        "HMWPA", "HMWPAH", "HMWPBZ", "HMWPDT", "HMWPHI", "HMWPIH", "HMWPPG",
        "HMWPQR", "HMWPR", "HMWPSR", "HMWPUB", "HMWRAH", "HMWREV", "HMWRI",
        "HMWRIW", "HMWRLX", "HMWRNK", "HMWSC", "HMWSC", "HMWSD", "HMWSEW",
        "HMWSGF", "HMWSGX", "HMWSHV", "HMWSJT", "HMWSJU", "HMWSLC", "HMWSNP",
        "HMWSPN", "HMWSTO", "HMWTAE", "HMWTBW", "HMWTFX", "HMWTN", "HMWTOP",
        "HMWTSA", "HMWTWC", "HMWUNR", "HMWUT", "HMWVA", "HMWVEF", "HMWVI",
        "HMWVT", "HMWWA", "HMWWI", "HMWWV", "HMWWY"]

    ALL_LOCAL_AREA_EMERGENCY = [
        "LAEABQ", "LAEABR", "LAEADQ", "LAEAFC", "LAEAFG", "LAEAJK", "LAEAK",
        "LAEAKN", "LAEAKQ", "LAEAL", "LAEALY", "LAEAMA", "LAEAPX", "LAEAR",
        "LAEARX", "LAEAS", "LAEAZ", "LAEBET", "LAEBGM", "LAEBIS", "LAEBMX",
        "LAEBOI", "LAEBOU", "LAEBOX", "LAEBRO", "LAEBRW", "LAEBTV", "LAEBUF",
        "LAEBYZ", "LAECA", "LAECAE", "LAECAR", "LAECDB", "LAECHS", "LAECLE",
        "LAECO", "LAECRP", "LAECT", "LAECTP", "LAECYS", "LAEDC", "LAEDDC",
        "LAEDE", "LAEDLH", "LAEDMX", "LAEDTX", "LAEDVN", "LAEEAX", "LAEEKA",
        "LAEEPZ", "LAEEWX", "LAEFFC", "LAEFGF", "LAEFGZ", "LAEFL", "LAEFSD",
        "LAEFWD", "LAEGA", "LAEGGW", "LAEGID", "LAEGJT", "LAEGLD", "LAEGRB",
        "LAEGRR", "LAEGSP", "LAEGU", "LAEGUM", "LAEGYX", "LAEHFO", "LAEHGX",
        "LAEHI", "LAEHNX", "LAEHUN", "LAEIA", "LAEICT", "LAEID", "LAEIL",
        "LAEILM", "LAEILN", "LAEILX", "LAEIN", "LAEIND", "LAEIWX", "LAEJAN",
        "LAEJAX", "LAEJKL", "LAEKEY", "LAEKS", "LAEKY", "LAELA", "LAELBF",
        "LAELCH", "LAELIX", "LAELKN", "LAELMK", "LAELOT", "LAELOX", "LAELSX",
        "LAELUB", "LAELWX", "LAELZK", "LAEMA", "LAEMAF", "LAEMCG", "LAEMCG",
        "LAEMD", "LAEME", "LAEMEG", "LAEMFL", "LAEMFR", "LAEMHX", "LAEMI",
        "LAEMKX", "LAEMLB", "LAEMN", "LAEMO", "LAEMOB", "LAEMPX", "LAEMQT",
        "LAEMRX", "LAEMS", "LAEMSO", "LAEMT", "LAEMTR", "LAENC", "LAEND",
        "LAENE", "LAENH", "LAENJ", "LAENV", "LAENY", "LAEOAX", "LAEOH",
        "LAEOHX", "LAEOK", "LAEOKX", "LAEOME", "LAEOR", "LAEOTX", "LAEOTZ",
        "LAEOUN", "LAEPA", "LAEPAH", "LAEPBZ", "LAEPDT", "LAEPHI", "LAEPIH",
        "LAEPPG", "LAEPQR", "LAEPR", "LAEPSR", "LAEPUB", "LAERAH", "LAEREV",
        "LAERI", "LAERIW", "LAERLX", "LAERNK", "LAESC", "LAESC", "LAESD",
        "LAESEW", "LAESGF", "LAESGX", "LAESHV", "LAESJT", "LAESJU", "LAESLC",
        "LAESNP", "LAESPN", "LAESTO", "LAETAE", "LAETBW", "LAETFX", "LAETN",
        "LAETOP", "LAETSA", "LAETWC", "LAEUNR", "LAEUT", "LAEVA", "LAEVEF",
        "LAEVI", "LAEVT", "LAEWA", "LAEWI", "LAEWV", "LAEWY"]

    ALL_LAW_ENFORCEMENT_WARNING = [
        "LEWABQ", "LEWABR", "LEWADQ", "LEWAFC", "LEWAFG", "LEWAJK", "LEWAK",
        "LEWAKN", "LEWAKQ", "LEWAL", "LEWALY", "LEWAMA", "LEWAPX", "LEWAR",
        "LEWARX", "LEWAS", "LEWAZ", "LEWBET", "LEWBGM", "LEWBIS", "LEWBMX",
        "LEWBOI", "LEWBOU", "LEWBOX", "LEWBRO", "LEWBRW", "LEWBTV", "LEWBUF",
        "LEWBYZ", "LEWCA", "LEWCAE", "LEWCAR", "LEWCDB", "LEWCHS", "LEWCLE",
        "LEWCO", "LEWCRP", "LEWCT", "LEWCTP", "LEWCYS", "LEWDC", "LEWDDC",
        "LEWDE", "LEWDLH", "LEWDMX", "LEWDTX", "LEWDVN", "LEWEAX", "LEWEKA",
        "LEWEPZ", "LEWEWX", "LEWFFC", "LEWFGF", "LEWFGZ", "LEWFL", "LEWFSD",
        "LEWFWD", "LEWGA", "LEWGGW", "LEWGID", "LEWGJT", "LEWGLD", "LEWGRB",
        "LEWGRR", "LEWGSP", "LEWGU", "LEWGUM", "LEWGYX", "LEWHFO", "LEWHGX",
        "LEWHI", "LEWHNX", "LEWHUN", "LEWIA", "LEWICT", "LEWID", "LEWIL",
        "LEWILM", "LEWILN", "LEWILX", "LEWIN", "LEWIND", "LEWIWX", "LEWJAN",
        "LEWJAX", "LEWJKL", "LEWKEY", "LEWKS", "LEWKY", "LEWLA", "LEWLBF",
        "LEWLCH", "LEWLIX", "LEWLKN", "LEWLMK", "LEWLOT", "LEWLOX", "LEWLSX",
        "LEWLUB", "LEWLWX", "LEWLZK", "LEWMA", "LEWMAF", "LEWMCG", "LEWMCG",
        "LEWMD", "LEWME", "LEWMEG", "LEWMFL", "LEWMFR", "LEWMHX", "LEWMI",
        "LEWMKX", "LEWMLB", "LEWMN", "LEWMO", "LEWMOB", "LEWMPX", "LEWMQT",
        "LEWMRX", "LEWMS", "LEWMSO", "LEWMT", "LEWMTR", "LEWNC", "LEWND",
        "LEWNE", "LEWNH", "LEWNJ", "LEWNV", "LEWNY", "LEWOAX", "LEWOH",
        "LEWOHX", "LEWOK", "LEWOKX", "LEWOME", "LEWOR", "LEWOTX", "LEWOTZ",
        "LEWOUN", "LEWPA", "LEWPAH", "LEWPBZ", "LEWPDT", "LEWPHI", "LEWPIH",
        "LEWPPG", "LEWPQR", "LEWPR", "LEWPSR", "LEWPUB", "LEWRAH", "LEWREV",
        "LEWRI", "LEWRIW", "LEWRLX", "LEWRNK", "LEWSC", "LEWSC", "LEWSD",
        "LEWSEW", "LEWSGF", "LEWSGX", "LEWSHV", "LEWSJT", "LEWSJU", "LEWSLC",
        "LEWSNP", "LEWSPN", "LEWSTO", "LEWTAE", "LEWTBW", "LEWTFX", "LEWTN",
        "LEWTOP", "LEWTSA", "LEWTWC", "LEWUNR", "LEWUT", "LEWVA", "LEWVEF",
        "LEWVI", "LEWVT", "LEWWA", "LEWWI", "LEWWV", "LEWWY"]

    ALL_NUCLEAR_POWER_PLANT_WARNING = [
        "NUWABQ", "NUWABR", "NUWADQ", "NUWAFC", "NUWAFG", "NUWAJK", "NUWAK",
        "NUWAKN", "NUWAKQ", "NUWAL", "NUWALY", "NUWAMA", "NUWAPX", "NUWAR",
        "NUWARX", "NUWAS", "NUWAZ", "NUWBET", "NUWBGM", "NUWBIS", "NUWBMX",
        "NUWBOI", "NUWBOU", "NUWBOX", "NUWBRO", "NUWBRW", "NUWBTV", "NUWBUF",
        "NUWBYZ", "NUWCA", "NUWCAE", "NUWCAR", "NUWCDB", "NUWCHS", "NUWCLE",
        "NUWCO", "NUWCRP", "NUWCT", "NUWCTP", "NUWCYS", "NUWDC", "NUWDDC",
        "NUWDE", "NUWDLH", "NUWDMX", "NUWDTX", "NUWDVN", "NUWEAX", "NUWEKA",
        "NUWEPZ", "NUWEWX", "NUWFFC", "NUWFGF", "NUWFGZ", "NUWFL", "NUWFSD",
        "NUWFWD", "NUWGA", "NUWGGW", "NUWGID", "NUWGJT", "NUWGLD", "NUWGRB",
        "NUWGRR", "NUWGSP", "NUWGU", "NUWGUM", "NUWGYX", "NUWHFO", "NUWHGX",
        "NUWHI", "NUWHNX", "NUWHUN", "NUWIA", "NUWICT", "NUWID", "NUWIL",
        "NUWILM", "NUWILN", "NUWILX", "NUWIN", "NUWIND", "NUWIWX", "NUWJAN",
        "NUWJAX", "NUWJKL", "NUWKEY", "NUWKS", "NUWKY", "NUWLA", "NUWLBF",
        "NUWLCH", "NUWLIX", "NUWLKN", "NUWLMK", "NUWLOT", "NUWLOX", "NUWLSX",
        "NUWLUB", "NUWLWX", "NUWLZK", "NUWMA", "NUWMAF", "NUWMCG", "NUWMCG",
        "NUWMD", "NUWME", "NUWMEG", "NUWMFL", "NUWMFR", "NUWMHX", "NUWMI",
        "NUWMKX", "NUWMLB", "NUWMN", "NUWMO", "NUWMOB", "NUWMPX", "NUWMQT",
        "NUWMRX", "NUWMS", "NUWMSO", "NUWMT", "NUWMTR", "NUWNC", "NUWND",
        "NUWNE", "NUWNH", "NUWNJ", "NUWNV", "NUWNY", "NUWOAX", "NUWOH",
        "NUWOHX", "NUWOK", "NUWOKX", "NUWOME", "NUWOR", "NUWOTX", "NUWOTZ",
        "NUWOUN", "NUWPA", "NUWPAH", "NUWPBZ", "NUWPDT", "NUWPHI", "NUWPIH",
        "NUWPPG", "NUWPQR", "NUWPR", "NUWPSR", "NUWPUB", "NUWRAH", "NUWREV",
        "NUWRI", "NUWRIW", "NUWRLX", "NUWRNK", "NUWSC", "NUWSC", "NUWSD",
        "NUWSEW", "NUWSGF", "NUWSGX", "NUWSHV", "NUWSJT", "NUWSJU", "NUWSLC",
        "NUWSNP", "NUWSPN", "NUWSTO", "NUWTAE", "NUWTBW", "NUWTFX", "NUWTN",
        "NUWTOP", "NUWTSA", "NUWTWC", "NUWUNR", "NUWUT", "NUWVA", "NUWVEF",
        "NUWVI", "NUWVT", "NUWWA", "NUWWI", "NUWWV", "NUWWY"]

    ALL_RADIOLOGICAL_HAZARD_WARNING = [
        "RHWABQ", "RHWABR", "RHWADQ", "RHWAFC", "RHWAFG", "RHWAJK", "RHWAK",
        "RHWAKN", "RHWAKQ", "RHWAL", "RHWALY", "RHWAMA", "RHWAPX", "RHWAR",
        "RHWARX", "RHWAS", "RHWAZ", "RHWBET", "RHWBGM", "RHWBIS", "RHWBMX",
        "RHWBOI", "RHWBOU", "RHWBOX", "RHWBRO", "RHWBRW", "RHWBTV", "RHWBUF",
        "RHWBYZ", "RHWCA", "RHWCAE", "RHWCAR", "RHWCDB", "RHWCHS", "RHWCLE",
        "RHWCO", "RHWCRP", "RHWCT", "RHWCTP", "RHWCYS", "RHWDC", "RHWDDC",
        "RHWDE", "RHWDLH", "RHWDMX", "RHWDTX", "RHWDVN", "RHWEAX", "RHWEKA",
        "RHWEPZ", "RHWEWX", "RHWFFC", "RHWFGF", "RHWFGZ", "RHWFL", "RHWFSD",
        "RHWFWD", "RHWGA", "RHWGGW", "RHWGID", "RHWGJT", "RHWGLD", "RHWGRB",
        "RHWGRR", "RHWGSP", "RHWGU", "RHWGUM", "RHWGYX", "RHWHFO", "RHWHGX",
        "RHWHI", "RHWHNX", "RHWHUN", "RHWIA", "RHWICT", "RHWID", "RHWIL",
        "RHWILM", "RHWILN", "RHWILX", "RHWIN", "RHWIND", "RHWIWX", "RHWJAN",
        "RHWJAX", "RHWJKL", "RHWKEY", "RHWKS", "RHWKY", "RHWLA", "RHWLBF",
        "RHWLCH", "RHWLIX", "RHWLKN", "RHWLMK", "RHWLOT", "RHWLOX", "RHWLSX",
        "RHWLUB", "RHWLWX", "RHWLZK", "RHWMA", "RHWMAF", "RHWMCG", "RHWMCG",
        "RHWMD", "RHWME", "RHWMEG", "RHWMFL", "RHWMFR", "RHWMHX", "RHWMI",
        "RHWMKX", "RHWMLB", "RHWMN", "RHWMO", "RHWMOB", "RHWMPX", "RHWMQT",
        "RHWMRX", "RHWMS", "RHWMSO", "RHWMT", "RHWMTR", "RHWNC", "RHWND",
        "RHWNE", "RHWNH", "RHWNJ", "RHWNV", "RHWNY", "RHWOAX", "RHWOH",
        "RHWOHX", "RHWOK", "RHWOKX", "RHWOME", "RHWOR", "RHWOTX", "RHWOTZ",
        "RHWOUN", "RHWPA", "RHWPAH", "RHWPBZ", "RHWPDT", "RHWPHI", "RHWPIH",
        "RHWPPG", "RHWPQR", "RHWPR", "RHWPSR", "RHWPUB", "RHWRAH", "RHWREV",
        "RHWRI", "RHWRIW", "RHWRLX", "RHWRNK", "RHWSC", "RHWSC", "RHWSD",
        "RHWSEW", "RHWSGF", "RHWSGX", "RHWSHV", "RHWSJT", "RHWSJU", "RHWSLC",
        "RHWSNP", "RHWSPN", "RHWSTO", "RHWTAE", "RHWTBW", "RHWTFX", "RHWTN",
        "RHWTOP", "RHWTSA", "RHWTWC", "RHWUNR", "RHWUT", "RHWVA", "RHWVEF",
        "RHWVI", "RHWVT", "RHWWA", "RHWWI", "RHWWV", "RHWWY"]

    ALL_SHELTER_IN_PLACE_WARNING = [
        "SPWABQ", "SPWABR", "SPWADQ", "SPWAFC", "SPWAFG", "SPWAJK", "SPWAK",
        "SPWAKN", "SPWAKQ", "SPWAL", "SPWALY", "SPWAMA", "SPWAPX", "SPWAR",
        "SPWARX", "SPWAS", "SPWAZ", "SPWBET", "SPWBGM", "SPWBIS", "SPWBMX",
        "SPWBOI", "SPWBOU", "SPWBOX", "SPWBRO", "SPWBRW", "SPWBTV", "SPWBUF",
        "SPWBYZ", "SPWCA", "SPWCAE", "SPWCAR", "SPWCDB", "SPWCHS", "SPWCLE",
        "SPWCO", "SPWCRP", "SPWCT", "SPWCTP", "SPWCYS", "SPWDC", "SPWDDC",
        "SPWDE", "SPWDLH", "SPWDMX", "SPWDTX", "SPWDVN", "SPWEAX", "SPWEKA",
        "SPWEPZ", "SPWEWX", "SPWFFC", "SPWFGF", "SPWFGZ", "SPWFL", "SPWFSD",
        "SPWFWD", "SPWGA", "SPWGGW", "SPWGID", "SPWGJT", "SPWGLD", "SPWGRB",
        "SPWGRR", "SPWGSP", "SPWGU", "SPWGUM", "SPWGYX", "SPWHFO", "SPWHI",
        "SPWHNX", "SPWHUN", "SPWIA", "SPWICT", "SPWID", "SPWIL", "SPWILM",
        "SPWILN", "SPWILX", "SPWIN", "SPWIND", "SPWIWX", "SPWJAN", "SPWJAX",
        "SPWJKL", "SPWKEY", "SPWKS", "SPWKY", "SPWLA", "SPWLBF", "SPWLCH",
        "SPWLIX", "SPWLKN", "SPWLMK", "SPWLOT", "SPWLOX", "SPWLSX", "SPWLUB",
        "SPWLWX", "SPWLZK", "SPWMA", "SPWMAF", "SPWMCG", "SPWMCG", "SPWMD",
        "SPWME", "SPWMEG", "SPWMFL", "SPWMFR", "SPWMHX", "SPWMI", "SPWMKX",
        "SPWMLB", "SPWMN", "SPWMO", "SPWMOB", "SPWMPX", "SPWMQT", "SPWMRX",
        "SPWMS", "SPWMSO", "SPWMT", "SPWMTR", "SPWNC", "SPWND", "SPWNE",
        "SPWNH", "SPWNJ", "SPWNV", "SPWNY", "SPWOAX", "SPWOH", "SPWOHX",
        "SPWOK", "SPWOKX", "SPWOME", "SPWOR", "SPWOTX", "SPWOTZ", "SPWOUN",
        "SPWPA", "SPWPAH", "SPWPBZ", "SPWPDT", "SPWPHI", "SPWPIH", "SPWPPG",
        "SPWPQR", "SPWPR", "SPWPSR", "SPWPUB", "SPWRAH", "SPWREV", "SPWRI",
        "SPWRIW", "SPWRLX", "SPWRNK", "SPWSC", "SPWSC", "SPWSD", "SPWSEW",
        "SPWSGF", "SPWSGX", "SPWSHV", "SPWSJT", "SPWSJU", "SPWSLC", "SPWSNP",
        "SPWSPN", "SPWSTO", "SPWTAE", "SPWTBW", "SPWTFX", "SPWTN", "SPWTOP",
        "SPWTSA", "SPWTWC", "SPWUNR", "SPWUT", "SPWVA", "SPWVEF", "SPWVI",
        "SPWVT", "SPWWA", "SPWWI", "SPWWV", "SPWWY"]

    ALL_911_TELEPHONE_OUTAGE_EMERGENCY = [
        "TOEABQ", "TOEABR", "TOEADQ", "TOEAFC", "TOEAFG", "TOEAJK", "TOEAK",
        "TOEAKN", "TOEAKQ", "TOEAL", "TOEALY", "TOEAMA", "TOEAPX", "TOEAR",
        "TOEARX", "TOEAS", "TOEAZ", "TOEBET", "TOEBGM", "TOEBIS", "TOEBMX",
        "TOEBOI", "TOEBOU", "TOEBOX", "TOEBRO", "TOEBRW", "TOEBTV", "TOEBUF",
        "TOEBYZ", "TOECA", "TOECAE", "TOECAR", "TOECDB", "TOECHS", "TOECLE",
        "TOECO", "TOECRP", "TOECT", "TOECTP", "TOECYS", "TOEDC", "TOEDDC",
        "TOEDE", "TOEDLH", "TOEDMX", "TOEDTX", "TOEDVN", "TOEEAX", "TOEEKA",
        "TOEEPZ", "TOEEWX", "TOEFFC", "TOEFGF", "TOEFGZ", "TOEFL", "TOEFSD",
        "TOEFWD", "TOEGA", "TOEGGW", "TOEGID", "TOEGJT", "TOEGLD", "TOEGRB",
        "TOEGRR", "TOEGSP", "TOEGU", "TOEGUM", "TOEGYX", "TOEHFO", "TOEHGX",
        "TOEHI", "TOEHNX", "TOEHUN", "TOEIA", "TOEICT", "TOEID", "TOEIL",
        "TOEILM", "TOEILN", "TOEILX", "TOEIN", "TOEIND", "TOEIWX", "TOEJAN",
        "TOEJAX", "TOEJKL", "TOEKEY", "TOEKS", "TOEKY", "TOELA", "TOELBF",
        "TOELCH", "TOELIX", "TOELKN", "TOELMK", "TOELOT", "TOELOX", "TOELSX",
        "TOELUB", "TOELWX", "TOELZK", "TOEMA", "TOEMAF", "TOEMCG", "TOEMCG",
        "TOEMD", "TOEME", "TOEMEG", "TOEMFL", "TOEMFR", "TOEMHX", "TOEMI",
        "TOEMKX", "TOEMLB", "TOEMN", "TOEMO", "TOEMOB", "TOEMPX", "TOEMQT",
        "TOEMRX", "TOEMS", "TOEMSO", "TOEMT", "TOEMTR", "TOENC", "TOEND",
        "TOENE", "TOENH", "TOENJ", "TOENV", "TOENY", "TOEOAX", "TOEOH",
        "TOEOHX", "TOEOK", "TOEOKX", "TOEOME", "TOEOR", "TOEOTX", "TOEOTZ",
        "TOEOUN", "TOEPA", "TOEPAH", "TOEPBZ", "TOEPDT", "TOEPHI", "TOEPIH",
        "TOEPPG", "TOEPQR", "TOEPR", "TOEPSR", "TOEPUB", "TOERAH", "TOEREV",
        "TOERI", "TOERIW", "TOERLX", "TOERNK", "TOESC", "TOESC", "TOESD",
        "TOESEW", "TOESGF", "TOESGX", "TOESHV", "TOESJT", "TOESJU", "TOESLC",
        "TOESNP", "TOESPN", "TOESTO", "TOETAE", "TOETBW", "TOETFX", "TOETN",
        "TOETOP", "TOETSA", "TOETWC", "TOEUNR", "TOEUT", "TOEVA", "TOEVEF",
        "TOEVI", "TOEVT", "TOEWA", "TOEWI", "TOEWV", "TOEWY"]

    ALL_VOLCANO_WARNING = [
        "VOWABQ", "VOWABR", "VOWADQ", "VOWAFC", "VOWAFG", "VOWAJK", "VOWAK",
        "VOWAKN", "VOWAKQ", "VOWAL", "VOWALY", "VOWAMA", "VOWAPX", "VOWAR",
        "VOWARX", "VOWAS", "VOWAZ", "VOWBET", "VOWBGM", "VOWBIS", "VOWBMX",
        "VOWBOI", "VOWBOU", "VOWBOX", "VOWBRO", "VOWBRW", "VOWBTV", "VOWBUF",
        "VOWBYZ", "VOWCA", "VOWCAE", "VOWCAR", "VOWCDB", "VOWCHS", "VOWCLE",
        "VOWCO", "VOWCRP", "VOWCT", "VOWCTP", "VOWCYS", "VOWDC", "VOWDDC",
        "VOWDE", "VOWDLH", "VOWDMX", "VOWDTX", "VOWDVN", "VOWEAX", "VOWEKA",
        "VOWEPZ", "VOWEWX", "VOWFFC", "VOWFGF", "VOWFGZ", "VOWFL", "VOWFSD",
        "VOWFWD", "VOWGA", "VOWGGW", "VOWGID", "VOWGJT", "VOWGLD", "VOWGRB",
        "VOWGRR", "VOWGSP", "VOWGU", "VOWGUM", "VOWGYX", "VOWHFO", "VOWHGX",
        "VOWHI", "VOWHNX", "VOWHUN", "VOWIA", "VOWICT", "VOWID", "VOWIL",
        "VOWILM", "VOWILN", "VOWILX", "VOWIN", "VOWIND", "VOWIWX", "VOWJAN",
        "VOWJAX", "VOWJKL", "VOWKEY", "VOWKS", "VOWKY", "VOWLA", "VOWLBF",
        "VOWLCH", "VOWLIX", "VOWLKN", "VOWLMK", "VOWLOT", "VOWLOX", "VOWLSX",
        "VOWLUB", "VOWLWX", "VOWLZK", "VOWMA", "VOWMAF", "VOWMCG", "VOWMCG",
        "VOWMD", "VOWME", "VOWMEG", "VOWMFL", "VOWMFR", "VOWMHX", "VOWMI",
        "VOWMKX", "VOWMLB", "VOWMN", "VOWMO", "VOWMOB", "VOWMPX", "VOWMQT",
        "VOWMRX", "VOWMS", "VOWMSO", "VOWMT", "VOWMTR", "VOWNC", "VOWND",
        "VOWNE", "VOWNH", "VOWNJ", "VOWNV", "VOWNY", "VOWOAX", "VOWOH",
        "VOWOHX", "VOWOK", "VOWOKX", "VOWOME", "VOWOR", "VOWOTX", "VOWOTZ",
        "VOWOUN", "VOWPA", "VOWPAH", "VOWPBZ", "VOWPDT", "VOWPHI", "VOWPIH",
        "VOWPPG", "VOWPQR", "VOWPR", "VOWPSR", "VOWPUB", "VOWRAH", "VOWREV",
        "VOWRI", "VOWRIW", "VOWRLX", "VOWRNK", "VOWSC", "VOWSC", "VOWSD",
        "VOWSEW", "VOWSGF", "VOWSGX", "VOWSHV", "VOWSJT", "VOWSJU", "VOWSLC",
        "VOWSNP", "VOWSPN", "VOWSTO", "VOWTAE", "VOWTBW", "VOWTFX", "VOWTN",
        "VOWTOP", "VOWTSA", "VOWTWC", "VOWUNR", "VOWUT", "VOWVA", "VOWVEF",
        "VOWVI", "VOWVT", "VOWWA", "VOWWI", "VOWWV", "VOWWY"]

    ALL_DEMO_WARNING = [
        "DMOABQ", "DMOABR", "DMOADQ", "DMOAFC", "DMOAFG", "DMOAJK", "DMOAK",
        "DMOAKQ", "DMOAL", "DMOALY", "DMOAPX", "DMOAR", "DMOARX", "DMOAS",
        "DMOAZ", "DMOBGM", "DMOBIS", "DMOBMX", "DMOBOI", "DMOBOU", "DMOBOX",
        "DMOBRO", "DMOBTV", "DMOBUF", "DMOBYZ", "DMOCA", "DMOCAE", "DMOCAR",
        "DMOCHS", "DMOCLE", "DMOCO", "DMOCRP", "DMOCT", "DMOCTP", "DMOCYS",
        "DMODC", "DMODDC", "DMODE", "DMODLH", "DMODMX", "DMODTX", "DMODVN",
        "DMOEAX", "DMOEKA", "DMOEPZ", "DMOEWX", "DMOFFC", "DMOFGF", "DMOFGZ",
        "DMOFL", "DMOFSD", "DMOGA", "DMOGGW", "DMOGID", "DMOGJT", "DMOGLD",
        "DMOGRB", "DMOGRR", "DMOGSP", "DMOGU", "DMOGUM", "DMOGYX", "DMOHFO",
        "DMOHGX", "DMOHI", "DMOHNX", "DMOIA", "DMOICT", "DMOID", "DMOIL",
        "DMOILM", "DMOILN", "DMOILX", "DMOIN", "DMOIND", "DMOIWX", "DMOJAN",
        "DMOJAX", "DMOJKL", "DMOKEY", "DMOKS", "DMOKY", "DMOLA", "DMOLBF",
        "DMOLIX", "DMOLKN", "DMOLMK", "DMOLOT", "DMOLOX", "DMOLSX", "DMOLUB",
        "DMOLWX", "DMOLZK", "DMOMA", "DMOMD", "DMOME", "DMOMEG", "DMOMFL",
        "DMOMFR", "DMOMHX", "DMOMI", "DMOMKX", "DMOMLB", "DMOMN", "DMOMO",
        "DMOMOB", "DMOMPX", "DMOMQT", "DMOMRX", "DMOMS", "DMOMSO", "DMOMT",
        "DMOMTR", "DMONC", "DMOND", "DMONE", "DMONH", "DMONJ", "DMONM",
        "DMONV", "DMONY", "DMOOAX", "DMOOH", "DMOOHX", "DMOOK", "DMOOKX",
        "DMOOME", "DMOOR", "DMOOTX", "DMOOUN", "DMOPA", "DMOPAH", "DMOPBZ",
        "DMOPDT", "DMOPHI", "DMOPIH", "DMOPPG", "DMOPQR", "DMOPR", "DMOPSR",
        "DMOPUB", "DMORAH", "DMOREV", "DMORI", "DMORIW", "DMORLX", "DMORNK",
        "DMOSC", "DMOSD", "DMOSEW", "DMOSGF", "DMOSGX", "DMOSJT", "DMOSJU",
        "DMOSLC", "DMOSPN", "DMOSTO", "DMOTAE", "DMOTBW", "DMOTFX", "DMOTN",
        "DMOTOP", "DMOTSA", "DMOTWC", "DMOUNR", "DMOUT", "DMOVA", "DMOVEF",
        "DMOVI", "DMOVT", "DMOWA", "DMOWI", "DMOWV", "DMOWY"]
    
    ALL_NPW = ["NPWABQ", "NPWABR", "NPWADQ", "NPWAER", "NPWAFG", "NPWAJK", "NPWAKQ",
        "NPWALU", "NPWALY", "NPWAMA", "NPWAPX", "NPWARX", "NPWBGM", "NPWBIS",
        "NPWBMX", "NPWBOI", "NPWBOU", "NPWBOX", "NPWBRO", "NPWBRW", "NPWBTV",
        "NPWBUF", "NPWBYZ", "NPWCAE", "NPWCAR", "NPWCHS", "NPWCLE", "NPWCMH",
        "NPWCRP", "NPWCTP", "NPWCVG", "NPWCYS", "NPWDDC", "NPWDLH", "NPWDMX",
        "NPWDTX", "NPWDVN", "NPWEAX", "NPWEKA", "NPWEPZ", "NPWEWR", "NPWEWX",
        "NPWFFC", "NPWFGF", "NPWFGZ", "NPWFSD", "NPWFWD", "NPWGGW", "NPWGID",
        "NPWGJT", "NPWGLD", "NPWGRB", "NPWGRR", "NPWGSP", "NPWGYX", "NPWHFO",
        "NPWHGX", "NPWHI", "NPWHNX", "NPWHUN", "NPWICT", "NPWILM", "NPWILN",
        "NPWILX", "NPWIND", "NPWIWX", "NPWJAN", "NPWJAX", "NPWJKL", "NPWKEY",
        "NPWLBF", "NPWLCH", "NPWLIX", "NPWLKN", "NPWLMK", "NPWLOT", "NPWLOX",
        "NPWLSX", "NPWLUB", "NPWLWX", "NPWLZK", "NPWMAF", "NPWMCG", "NPWMEG",
        "NPWMFL", "NPWMFR", "NPWMHX", "NPWMKX", "NPWMLB", "NPWMOB", "NPWMPX",
        "NPWMQT", "NPWMRX", "NPWMSO", "NPWMTR", "NPWMY", "NPWNSB", "NPWOAX",
        "NPWOHX", "NPWOKX", "NPWOME", "NPWOTX", "NPWOTZ", "NPWOUN", "NPWPAH",
        "NPWPBZ", "NPWPDT", "NPWPHI", "NPWPIH", "NPWPPG", "NPWPQR", "NPWPSR",
        "NPWPUB", "NPWRAH", "NPWREV", "NPWRIW", "NPWRLX", "NPWRNK", "NPWSEW",
        "NPWSGF", "NPWSGX", "NPWSHV", "NPWSJT", "NPWSJU", "NPWSLC", "NPWSPN",
        "NPWSTO", "NPWTAE", "NPWTBW", "NPWTFX", "NPWTOP", "NPWTSA", "NPWTWC",
        "NPWUNR", "NPWVEF", "NPWWCZ"]
    # =============================================================================
    # SPECIAL CONFIGURATIONS
    # =============================================================================
    BLUE_HEN_SPECIAL = ["AFDPHI", "NOWPHI", "SMWPHI", "TORPHI", "SVRPHI", "SVSPHI",
                        "LSRPHI", "HWOPHI", "FFAPHI", "FFSPHI", "FFWPHI", "FLSPHI",
                        "FLWPHI", "PNSPHI", "WSWPHI"]

    ERIC_ALLEN_SPECIAL = ["AFDLWX", "NOWLWX", "SMWLWX", "TORLWX", "SVRLWX", "SVSLWX",
                          "LSRLWX", "HWOLWX", "FFALWX", "FFSLWX", "FFWLWX", "FLSLWX",
                          "FLWLWX", "PNSLWX", "WSWLWX"]

    RYAN_SPECIAL = ["SMWMHX", "SMWILM", "SMWCHS", "SMWAKQ"]

    MASTER_LIST = ['AFDABQ', 'AFDABR', 'AFDAFC', 'AFDAFG', 'AFDAJK', 'AFDAKQ',
                   'AFDALY', 'AFDAMA', 'AFDAPX', 'AFDARX', 'AFDBGM', 'AFDBIS',
                   'AFDBMX', 'AFDBOI', 'AFDBOU', 'AFDBOX', 'AFDBRO', 'AFDBTV',
                   'AFDBUF', 'AFDBYZ', 'AFDCAE', 'AFDCAR', 'AFDCHS', 'AFDCLE',
                   'AFDCRP', 'AFDCTP', 'AFDCYS', 'AFDDDC', 'AFDDLH', 'AFDDMX',
                   'AFDDPQ', 'AFDDTX', 'AFDDVN', 'AFDEAX', 'AFDEKA', 'AFDEPZ',
                   'AFDEWX', 'AFDEYW', 'AFDFFC', 'AFDFGF', 'AFDFGZ', 'AFDFSD',
                   'AFDFWD', 'AFDGGW', 'AFDGID', 'AFDGJT', 'AFDGLD', 'AFDGRB',
                   'AFDGRR', 'AFDGSP', 'AFDGYX', 'AFDHFO', 'AFDHGX', 'AFDHNX',
                   'AFDHUN', 'AFDICT', 'AFDILM', 'AFDILN', 'AFDILX', 'AFDIND',
                   'AFDIWX', 'AFDJAN', 'AFDJAX', 'AFDJKL', 'AFDKEY', 'AFDLBF',
                   'AFDLCH', 'AFDLIX', 'AFDLKN', 'AFDLMK', 'AFDLOT', 'AFDLOX',
                   'AFDLSX', 'AFDLUB', 'AFDLWX', 'AFDLZK', 'AFDMAF', 'AFDMEG',
                   'AFDMFL', 'AFDMFR', 'AFDMHX', 'AFDMKX', 'AFDMLB', 'AFDMOB',
                   'AFDMPX', 'AFDMQT', 'AFDMRX', 'AFDMSO', 'AFDMTR', 'AFDOAX',
                   'AFDOHX', 'AFDOKX', 'AFDOTX', 'AFDOUN', 'AFDPAH', 'AFDPBZ',
                   'AFDPDT', 'AFDPHI', 'AFDPIH', 'AFDPPG', 'AFDPQ', 'AFDPQR',
                   'AFDPSR', 'AFDPUB', 'AFDRAH', 'AFDREV', 'AFDRIW', 'AFDRLX',
                   'AFDRNK', 'AFDSDF', 'AFDSEW', 'AFDSGF', 'AFDSGX', 'AFDSHV',
                   'AFDSJT', 'AFDSJU', 'AFDSLC', 'AFDSTO', 'AFDTAE', 'AFDTBW',
                   'AFDTFX', 'AFDTOP', 'AFDTSA', 'AFDTWC', 'AFDUNR', 'AFDVEF',
                   'ALTK04', 'ALTK05', 'ALTK06', 'ALTK07', 'ALTK08', 'ALTK09',
                   'DAYDIS', 'DAYDSF', 'DAYTDF', 'FFALWX', 'FFAPHI', 'FFGMPD',
                   'FFSLWX', 'FFSPHI', 'FFWLWX', 'FFWPHI', 'FLSLWX', 'FLSPHI',
                   'FLWLWX', 'FLWPHI', 'FWDD38', 'FWDDY1', 'FWDDY2', 'HSFAT1',
                   'HSFAT2', 'HSFEP', 'HSFEP1', 'HSFEP2', 'HSFEP3', 'HSFEPI',
                   'HSFNP', 'HSFSP', 'HWOLWX', 'HWOPHI', 'LSRABQ', 'LSRABR',
                   'LSRAFC', 'LSRAFG', 'LSRAJK', 'LSRAKQ', 'LSRALY', 'LSRAMA',
                   'LSRAPX', 'LSRARX', 'LSRBGM', 'LSRBIS', 'LSRBMX', 'LSRBOI',
                   'LSRBOU', 'LSRBOX', 'LSRBRO', 'LSRBRW', 'LSRBTV', 'LSRBUF',
                   'LSRBYZ', 'LSRCAE', 'LSRCAR', 'LSRCDB', 'LSRCHS', 'LSRCLE',
                   'LSRCRP', 'LSRCTP', 'LSRCYS', 'LSRDDC', 'LSRDLH', 'LSRDMX',
                   'LSRDTX', 'LSRDVN', 'LSREAX', 'LSREKA', 'LSREPZ', 'LSREWX',
                   'LSRFFC', 'LSRFGF', 'LSRFGZ', 'LSRFSD', 'LSRFWD', 'LSRGGW',
                   'LSRGID', 'LSRGJT', 'LSRGLD', 'LSRGRB', 'LSRGRR', 'LSRGSP',
                   'LSRGUM', 'LSRGYX', 'LSRHFO', 'LSRHGX', 'LSRHNX', 'LSRHUN',
                   'LSRICT', 'LSRILM', 'LSRILN', 'LSRILX', 'LSRIND', 'LSRISN',
                   'LSRIWX', 'LSRJAN', 'LSRJAX', 'LSRJKL', 'LSRKEY', 'LSRLBF',
                   'LSRLCH', 'LSRLIX', 'LSRLKN', 'LSRLMK', 'LSRLOT', 'LSRLOX',
                   'LSRLSX', 'LSRLUB', 'LSRLWX', 'LSRLZK', 'LSRMAF', 'LSRMEG',
                   'LSRMFL', 'LSRMFR', 'LSRMHX', 'LSRMKX', 'LSRMLB', 'LSRMOB',
                   'LSRMPX', 'LSRMQT', 'LSRMRX', 'LSRMSO', 'LSRMTR', 'LSRNY1',
                   'LSRNY2', 'LSRNY3', 'LSRNY4', 'LSRNY7', 'LSROAX', 'LSROHX',
                   'LSROKX', 'LSROTX', 'LSROUN', 'LSRPAH', 'LSRPBZ', 'LSRPDT',
                   'LSRPHI', 'LSRPIH', 'LSRPQR', 'LSRPSR', 'LSRPUB', 'LSRRAH',
                   'LSRREV', 'LSRRIW', 'LSRRLX', 'LSRRNK', 'LSRSEW', 'LSRSGF',
                   'LSRSGX', 'LSRSHV', 'LSRSJT', 'LSRSJU', 'LSRSLC', 'LSRSTO',
                   'LSRTAE', 'LSRTBW', 'LSRTFX', 'LSRTOP', 'LSRTSA', 'LSRTWC',
                   'LSRUNR', 'LSRVEF', 'LSRVWS', 'MIMATN', 'MIMATS', 'MIMPAC',
                   'NOWABQ', 'NOWABR', 'NOWADQ', 'NOWAFC', 'NOWAFG', 'NOWAJK',
                   'NOWAKN', 'NOWAKQ', 'NOWALY', 'NOWAMA', 'NOWANN', 'NOWAPX',
                   'NOWARX', 'NOWBET', 'NOWBGM', 'NOWBIS', 'NOWBMX', 'NOWBOI',
                   'NOWBOU', 'NOWBOX', 'NOWBRO', 'NOWBRW', 'NOWBTV', 'NOWBUF',
                   'NOWBYZ', 'NOWCAE', 'NOWCAR', 'NOWCDB', 'NOWCHS', 'NOWCLE',
                   'NOWCRP', 'NOWCTP', 'NOWCYS', 'NOWDDC', 'NOWDLH', 'NOWDMX',
                   'NOWDTX', 'NOWDVN', 'NOWEAX', 'NOWEKA', 'NOWEPZ', 'NOWEWX',
                   'NOWEYW', 'NOWFFC', 'NOWFGF', 'NOWFGZ', 'NOWFSD', 'NOWFWD',
                   'NOWGGW', 'NOWGID', 'NOWGJT', 'NOWGLD', 'NOWGRB', 'NOWGRR',
                   'NOWGSP', 'NOWGYX', 'NOWHFO', 'NOWHGX', 'NOWHNX', 'NOWHUN',
                   'NOWICT', 'NOWILM', 'NOWILN', 'NOWILX', 'NOWIND', 'NOWISN',
                   'NOWIWX', 'NOWJAN', 'NOWJAX', 'NOWJKL', 'NOWKEY', 'NOWLBF',
                   'NOWLCH', 'NOWLIX', 'NOWLKN', 'NOWLMK', 'NOWLOT', 'NOWLOX',
                   'NOWLSX', 'NOWLUB', 'NOWLWX', 'NOWLZK', 'NOWMAF', 'NOWMCG',
                   'NOWMEG', 'NOWMFL', 'NOWMFR', 'NOWMHX', 'NOWMKX', 'NOWMLB',
                   'NOWMOB', 'NOWMPX', 'NOWMQT', 'NOWMRX', 'NOWMSO', 'NOWMTR',
                   'NOWMY', 'NOWOAX', 'NOWOHX', 'NOWOKX', 'NOWOME', 'NOWOTX',
                   'NOWOTZ', 'NOWOUN', 'NOWPAH', 'NOWPBZ', 'NOWPDT', 'NOWPHI',
                   'NOWPIH', 'NOWPQR', 'NOWPSR', 'NOWPUB', 'NOWRAH', 'NOWREV',
                   'NOWRIW', 'NOWRLX', 'NOWRNK', 'NOWSDF', 'NOWSEW', 'NOWSGF',
                   'NOWSGX', 'NOWSHV', 'NOWSJT', 'NOWSJU', 'NOWSLC', 'NOWSNP',
                   'NOWSTO', 'NOWTAE', 'NOWTBW', 'NOWTFX', 'NOWTOP', 'NOWTSA',
                   'NOWTWC', 'NOWUNR', 'NOWVEF', 'NOWVWS', 'NOWYAK', 'OFFAER',
                   'OFFAFG', 'OFFAJK', 'OFFALU', 'OFFHFO', 'OFFN01', 'OFFN02',
                   'OFFN03', 'OFFN04', 'OFFN05', 'OFFN06', 'OFFN07', 'OFFN08',
                   'OFFN09', 'OFFN10', 'OFFN11', 'OFFN12', 'OFFN13', 'OFFN14',
                   'OFFN15', 'OFFNT1', 'OFFNT2', 'OFFNT3', 'OFFNT4', 'OFFPZ5',
                   'OFFPZ6', 'PMD30D', 'PMD90D', 'PMDAHU', 'PMDAK', 'PMDCA',
                   'PMDDRK', 'PMDDRO', 'PMDENS', 'PMDEPD', 'PMDEPH', 'PMDHCO',
                   'PMDHI', 'PMDHMD', 'PMDMRD', 'PMDSA', 'PMDSPD', 'PMDTHR',
                   'PNSLWX', 'PNSPHI', 'QPFERD', 'QPFHSD', 'SCCNS1', 'SCCNS2',
                   'SCCNS3', 'SCCNS4', 'SCCNS5', 'SEL0', 'SEL1', 'SEL2', 'SEL3',
                   'SEL4', 'SEL5', 'SEL6', 'SEL7', 'SEL8', 'SEL9', 'SVRLWX',
                   'SVRPHI', 'SVSLWX', 'SVSPHI', 'SWOD48',
                   'SWODY1', 'SWODY2', 'SWODY3', 'SWOMCD', 'TCDAT1', 'TCDAT2',
                   'TCDAT3', 'TCDAT4', 'TCDAT5', 'TCDCP1', 'TCDCP2', 'TCDCP3',
                   'TCDCP4', 'TCDCP5', 'TCDEP1', 'TCDEP2', 'TCDEP3', 'TCDEP4',
                   'TCDEP5', 'TCPAT1', 'TCPAT2', 'TCPAT3', 'TCPAT4', 'TCPAT5',
                   'TCPCP1', 'TCPCP2', 'TCPCP3', 'TCPCP4', 'TCPCP5', 'TCPEP1',
                   'TCPEP2', 'TCPEP3', 'TCPEP4', 'TCPEP5', 'TCUAT', 'TCUAT1',
                   'TCUAT2', 'TCUAT3', 'TCUAT4', 'TCUAT5', 'TCUCP1', 'TCUCP2',
                   'TCUCP3', 'TCUCP4', 'TCUCP5', 'TCUEP', 'TCUEP1', 'TCUEP2',
                   'TCUEP3', 'TCUEP4', 'TCUEP5', 'TORLWX', 'TORPHI', 'TWDAT',
                   'TWDEP', 'WSWLWX', 'WSWPHI', "LSRADQ", "LSRAKN", "LSRANN",
                   "LSRAT1", "LSRBA1", "LSRBET", "LSRBH1", "LSRBR1", "LSRCS1",
                   "LSRHO1", "LSRJM1", "LSRMCG", "LSRNK1", "LSRNY5", "LSRNY6",
                   "LSROME", "LSROTZ", "LSRPPG", "LSRSNP", "LSRTD1", "LSRYAK",
                   "VOWLWX", "VOWPHI", 'SMWKEY', 'SMWEYW', 'SMWMFL', 'SMWMLB',
                   'SMWJAX', 'SMWCHS', 'SMWILM', 'SMWMHX', 'SMWAKQ', 'SMWPHI',
                   'SMWOKX', 'SMWBOX', 'SMWGYX', 'SMWCAR', 'SMWBRO', 'SMWCRP',
                   'SMWHGX', 'SMWLCH', 'SMWLIX', 'SMWMOB', 'SMWTAE', 'SMWTBW',
                   'SMWKEY', 'SMWEYW', 'SMWMFL', 'SMWSEW', 'SMWPQR', 'SMWMFR',
                   'SMWEKA', 'SMWMTR', 'SMWLOX', 'SMWSGX', 'SMWPQ', 'SMWDPQ',
                   'SMWHFO', 'SMWPPG', 'SMWLWX', "SMWSJU", "SMWAPX",
                   "SMWMKX", "SMWMQT", "MWSCLE", "MWSDTX", "MWSAPX", "MWSBUF",
                   "ADRABQ", "ADRABQ", "ADRABR", "ADRADQ", "ADRAFC", "ADRAFG", "ADRAJK",
                   "ADRAK", "ADRAKN", "ADRAKQ", "ADRAKQ", "ADRAL", "ADRALB", "ADRALY",
                   "ADRALY", "ADRAMA", "ADRAPX", "ADRAPX", "ADRAR", "ADRARX", "ADRARX",
                   "ADRAS", "ADRAZ", "ADRBET", "ADRBGM", "ADRBGM", "ADRBIS", "ADRBIS",
                   "ADRBMX", "ADRBOI", "ADRBOU", "ADRBOU", "ADRBOX", "ADRBOX", "ADRBRO",
                   "ADRBRW", "ADRBTV", "ADRBTV", "ADRBUF", "ADRBUF", "ADRBYZ", "ADRCA",
                   "ADRCAE", "ADRCAE", "ADRCAR", "ADRCAR", "ADRCDB", "ADRCHS", "ADRCHS",
                   "ADRCLE", "ADRCLE", "ADRCO", "ADRCRP", "ADRCT", "ADRCTP", "ADRCTP",
                   "ADRCYS", "ADRDC", "ADRDDC", "ADRDE", "ADRDLH", "ADRDMX", "ADRDMX",
                   "ADRDTX", "ADRDVN", "ADREAX", "ADREKA", "ADREPZ", "ADREVV", "ADREWX",
                   "ADRFFC", "ADRFGF", "ADRFGF", "ADRFGZ", "ADRFL", "ADRFSD", "ADRFWD",
                   "ADRGA", "ADRGGW", "ADRGID", "ADRGJT", "ADRGJT", "ADRGLD", "ADRGRB",
                   "ADRGRB", "ADRGRR", "ADRGSP", "ADRGSP", "ADRGU", "ADRGUM", "ADRGUM",
                   "ADRGYX", "ADRGYX", "ADRHFO", "ADRHFO", "ADRHGX", "ADRHI", "ADRHNX",
                   "ADRHUN", "ADRIA", "ADRICT", "ADRID", "ADRIL", "ADRILM", "ADRILM",
                   "ADRILN", "ADRILN", "ADRILX", "ADRILX", "ADRIN", "ADRIN", "ADRIND",
                   "ADRIWX", "ADRIWX", "ADRJAN", "ADRJAX", "ADRJKL", "ADRJKL", "ADRKEY",
                   "ADRKRF", "ADRKS", "ADRKY", "ADRKY", "ADRLA", "ADRLBF", "ADRLCH",
                   "ADRLIX", "ADRLKN", "ADRLMK", "ADRLOT", "ADRLOX", "ADRLSX", "ADRLUB",
                   "ADRLWX", "ADRLWX", "ADRLZK", "ADRMA", "ADRMCG", "ADRMCG", "ADRMD",
                   "ADRMD", "ADRME", "ADRME", "ADRMEG", "ADRMEI", "ADRMFL", "ADRMFR",
                   "ADRMHX", "ADRMHX", "ADRMI", "ADRMKX", "ADRMKX", "ADRMLB", "ADRMN",
                   "ADRMO", "ADRMOB", "ADRMPX", "ADRMPX", "ADRMQT", "ADRMQT", "ADRMRX",
                   "ADRMS", "ADRMSO", "ADRMSR", "ADRMT", "ADRMTR", "ADRNC", "ADRNC",
                   "ADRND", "ADRND", "ADRNE", "ADRNE", "ADRNH", "ADRNH", "ADRNJ",
                   "ADRNJ", "ADRNM", "ADRNMC", "ADRNV", "ADRNY", "ADRNY", "ADRNY",
                   "ADROAX", "ADROAX", "ADROH", "ADROHX", "ADROK", "ADROKX", "ADROKX",
                   "ADROME", "ADROR", "ADROTX", "ADROTZ", "ADROUN", "ADRPA", "ADRPA",
                   "ADRPAH", "ADRPBZ", "ADRPBZ", "ADRPDT", "ADRPDT", "ADRPHI", "ADRPHI",
                   "ADRPIH", "ADRPPG", "ADRPQR", "ADRPR", "ADRPSR", "ADRPTR", "ADRPUB",
                   "ADRPUB", "ADRRAH", "ADRRAH", "ADRRDU", "ADRREV", "ADRRI", "ADRRIW",
                   "ADRRIW", "ADRRLX", "ADRRLX", "ADRRNK", "ADRRNK", "ADRSC", "ADRSC",
                   "ADRSC", "ADRSD", "ADRSD", "ADRSEW", "ADRSGF", "ADRSGF", "ADRSGX",
                   "ADRSHV", "ADRSJT", "ADRSJU", "ADRSLC", "ADRSNP", "ADRSPN", "ADRSTO",
                   "ADRSTR", "ADRTAE", "ADRTBW", "ADRTFX", "ADRTN", "ADRTOP", "ADRTSA",
                   "ADRTWC", "ADRUNR", "ADRUT", "ADRVA", "ADRVA", "ADRVEF", "ADRVI",
                   "ADRVT", "ADRVT", "ADRWA", "ADRWI", "ADRWSH", "ADRWV", "ADRWV",
                   "ADRWY", "ADRWY", "AVAABQ", "AVAABR", "AVAADQ", "AVAAFC", "AVAAFG",
                   "AVAAJK", "AVAAK", "AVAAKN", "AVAAKQ", "AVAAL", "AVAALY", "AVAAMA",
                   "AVAAPX", "AVAAR", "AVAARX", "AVAAS", "AVAAZ", "AVABET", "AVABGM",
                   "AVABIS", "AVABMX", "AVABOI", "AVABOU", "AVABOX", "AVABRO", "AVABRW",
                   "AVABTV", "AVABUF", "AVABYZ", "AVACA", "AVACAE", "AVACAR", "AVACDB",
                   "AVACHS", "AVACLE", "AVACO", "AVACRP", "AVACT", "AVACTP", "AVACYS",
                   "AVADC", "AVADDC", "AVADE", "AVADLH", "AVADMX", "AVADTX", "AVADVN",
                   "AVAEAX", "AVAEKA", "AVAEPZ", "AVAEWX", "AVAFFC", "AVAFGF", "AVAFGZ",
                   "AVAFL", "AVAFSD", "AVAFWD", "AVAGA", "AVAGGW", "AVAGID", "AVAGJT",
                   "AVAGLD", "AVAGRB", "AVAGRR", "AVAGSP", "AVAGU", "AVAGUM", "AVAGYX",
                   "AVAHFO", "AVAHI", "AVAHNX", "AVAHUN", "AVAIA", "AVAICT", "AVAID",
                   "AVAIL", "AVAILM", "AVAILN", "AVAILX", "AVAIN", "AVAIND", "AVAIWX",
                   "AVAJAN", "AVAJAX", "AVAJKL", "AVAKEY", "AVAKS", "AVAKY", "AVALA",
                   "AVALBF", "AVALCH", "AVALIX", "AVALKN", "AVALMK", "AVALOT", "AVALOX",
                   "AVALSX", "AVALUB", "AVALWX", "AVALZK", "AVAMA", "AVAMAF", "AVAMCG",
                   "AVAMCG", "AVAMD", "AVAME", "AVAMEG", "AVAMFL", "AVAMFR", "AVAMHX",
                   "AVAMI", "AVAMKX", "AVAMLB", "AVAMN", "AVAMO", "AVAMOB", "AVAMPX",
                   "AVAMQT", "AVAMRX", "AVAMS", "AVAMSO", "AVAMT", "AVAMTR", "AVANC",
                   "AVAND", "AVANE", "AVANH", "AVANJ", "AVANV", "AVANY", "AVAOAX",
                   "AVAOH", "AVAOHX", "AVAOK", "AVAOKX", "AVAOME", "AVAOR", "AVAOTX",
                   "AVAOTZ", "AVAOUN", "AVAPA", "AVAPAH", "AVAPBZ", "AVAPDT", "AVAPHI",
                   "AVAPIH", "AVAPPG", "AVAPQR", "AVAPR", "AVAPSR", "AVAPUB", "AVARAH",
                   "AVAREV", "AVARI", "AVARIW", "AVARLX", "AVARNK", "AVASC", "AVASC",
                   "AVASD", "AVASEW", "AVASGF", "AVASGX", "AVASHV", "AVASJT", "AVASJU",
                   "AVASLC", "AVASNP", "AVASPN", "AVASTO", "AVATAE", "AVATBW", "AVATFX",
                   "AVATN", "AVATOP", "AVATSA", "AVATWC", "AVAUNR", "AVAUT", "AVAVA",
                   "AVAVEF", "AVAVI", "AVAVT", "AVAWA", "AVAWI", "AVAWV", "AVAWY",
                   "AVWABQ", "AVWABR", "AVWADQ", "AVWAFC", "AVWAFG", "AVWAJK", "AVWAK",
                   "AVWAKN", "AVWAKQ", "AVWAL", "AVWALY", "AVWAPX", "AVWAR", "AVWARX",
                   "AVWAS", "AVWAZ", "AVWBET", "AVWBGM", "AVWBIS", "AVWBMX", "AVWBOI",
                   "AVWBOU", "AVWBOX", "AVWBRO", "AVWBRW", "AVWBTV", "AVWBUF", "AVWBYZ",
                   "AVWCA", "AVWCAE", "AVWCAR", "AVWCDB", "AVWCHS", "AVWCLE", "AVWCO",
                   "AVWCRP", "AVWCT", "AVWCTP", "AVWCYS", "AVWDC", "AVWDDC", "AVWDE",
                   "AVWDLH", "AVWDMX", "AVWDTX", "AVWDVN", "AVWEAX", "AVWEKA", "AVWEPZ",
                   "AVWEWX", "AVWFFC", "AVWFGF", "AVWFGZ", "AVWFL", "AVWFSD", "AVWFWD",
                   "AVWGA", "AVWGGW", "AVWGID", "AVWGJT", "AVWGLD", "AVWGRB", "AVWGRR",
                   "AVWGSP", "AVWGU", "AVWGUM", "AVWGYX", "AVWHFO", "AVWHI", "AVWHNX",
                   "AVWHUN", "AVWIA", "AVWICT", "AVWID", "AVWIL", "AVWILM", "AVWILN",
                   "AVWILX", "AVWIN", "AVWIND", "AVWIWX", "AVWJAN", "AVWJAX", "AVWJKL",
                   "AVWKEY", "AVWKS", "AVWKY", "AVWLA", "AVWLBF", "AVWLCH", "AVWLIX",
                   "AVWLKN", "AVWLMK", "AVWLOT", "AVWLOX", "AVWLSX", "AVWLUB", "AVWLWX",
                   "AVWLZK", "AVWMA", "AVWMAF", "AVWMCG", "AVWMCG", "AVWMD", "AVWME",
                   "AVWMEG", "AVWMFL", "AVWMFR", "AVWMHX", "AVWMI", "AVWMKX", "AVWMLB",
                   "AVWMN", "AVWMO", "AVWMOB", "AVWMPX", "AVWMQT", "AVWMRX", "AVWMS",
                   "AVWMSO", "AVWMT", "AVWMTR", "AVWNC", "AVWND", "AVWNE", "AVWNH",
                   "AVWNJ", "AVWNV", "AVWNY", "AVWOAX", "AVWOH", "AVWOHX", "AVWOK",
                   "AVWOKX", "AVWOME", "AVWOR", "AVWOTX", "AVWOTZ", "AVWOUN", "AVWPA",
                   "AVWPAH", "AVWPBZ", "AVWPDT", "AVWPHI", "AVWPIH", "AVWPPG", "AVWPQR",
                   "AVWPR", "AVWPSR", "AVWPUB", "AVWRAH", "AVWREV", "AVWRI", "AVWRIW",
                   "AVWRLX", "AVWRNK", "AVWSC", "AVWSC", "AVWSD", "AVWSEW", "AVWSGF",
                   "AVWSGX", "AVWSHV", "AVWSJT", "AVWSJU", "AVWSLC", "AVWSNP", "AVWSPN",
                   "AVWSTO", "AVWTAE", "AVWTBW", "AVWTFX", "AVWTN", "AVWTOP", "AVWTSA",
                   "AVWTWC", "AVWUNR", "AVWUT", "AVWVA", "AVWVEF", "AVWVI", "AVWVT",
                   "AVWWA", "AVWWI", "AVWWV", "AVWWY", "BLUABQ", "BLUABR", "BLUADQ",
                   "BLUAFC", "BLUAFG", "BLUAJK", "BLUAK", "BLUAKQ", "BLUAL", "BLUALY",
                   "BLUAMA", "BLUAPX", "BLUAR", "BLUARX", "BLUAS", "BLUAZ", "BLUBGM",
                   "BLUBIS", "BLUBMX", "BLUBOI", "BLUBOU", "BLUBOX", "BLUBRO", "BLUBTV",
                   "BLUBTV", "BLUBUF", "BLUBYZ", "BLUCA", "BLUCAE", "BLUCAR", "BLUCHS",
                   "BLUCLE", "BLUCO", "BLUCRP", "BLUCT", "BLUCTP", "BLUCYS", "BLUDC",
                   "BLUDDC", "BLUDE", "BLUDLH", "BLUDMX", "BLUDTX", "BLUDVN", "BLUEAX",
                   "BLUEKA", "BLUEPZ", "BLUEWX", "BLUFFC", "BLUFGF", "BLUFGZ", "BLUFL",
                   "BLUFSD", "BLUFWD", "BLUGA", "BLUGGW", "BLUGID", "BLUGJT", "BLUGLD",
                   "BLUGRB", "BLUGRR", "BLUGSP", "BLUGU", "BLUGUM", "BLUGYX", "BLUHFO",
                   "BLUHGX", "BLUHI", "BLUHNX", "BLUHUN", "BLUIA", "BLUICT", "BLUID",
                   "BLUIL", "BLUILM", "BLUILN", "BLUILX", "BLUIN", "BLUIND", "BLUIWX",
                   "BLUJAN", "BLUJAX", "BLUJKL", "BLUKEY", "BLUKS", "BLUKY", "BLULA",
                   "BLULBF", "BLULCH", "BLULIX", "BLULKN", "BLULMK", "BLULOT", "BLULOX",
                   "BLULSX", "BLULUB", "BLULWX", "BLULZK", "BLUMA", "BLUMAF", "BLUMD",
                   "BLUME", "BLUMEG", "BLUMFL", "BLUMFR", "BLUMHX", "BLUMI", "BLUMKX",
                   "BLUMLB", "BLUMN", "BLUMO", "BLUMOB", "BLUMPX", "BLUMQT", "BLUMRX",
                   "BLUMS", "BLUMSO", "BLUMT", "BLUMTR", "BLUNC", "BLUND", "BLUNE",
                   "BLUNH", "BLUNJ", "BLUNM", "BLUNV", "BLUNY", "BLUOAX", "BLUOH",
                   "BLUOHX", "BLUOK", "BLUOKX", "BLUOME", "BLUOR", "BLUOTX", "BLUOUN",
                   "BLUPA", "BLUPAH", "BLUPBZ", "BLUPDT", "BLUPHI", "BLUPIH", "BLUPPG",
                   "BLUPQR", "BLUPR", "BLUPSR", "BLUPUB", "BLURAH", "BLUREV", "BLURI",
                   "BLURIW", "BLURLX", "BLURNK", "BLUSC", "BLUSD", "BLUSEW", "BLUSGF",
                   "BLUSGX", "BLUSHV", "BLUSJT", "BLUSJU", "BLUSLC", "BLUSPN", "BLUSTO",
                   "BLUTAE", "BLUTBW", "BLUTFX", "BLUTN", "BLUTOP", "BLUTSA", "BLUTWC",
                   "BLUTX", "BLUUNR", "BLUUT", "BLUVA", "BLUVEF", "BLUVI", "BLUWA",
                   "BLUWI", "BLUWV", "BLUWY", "BLUYAK", "CAEABQ", "CAEABR", "CAEADQ",
                   "CAEAFC", "CAEAFG", "CAEAJK", "CAEAK", "CAEAKN", "CAEAKQ", "CAEAL",
                   "CAEALY", "CAEAMA", "CAEAPX", "CAEAR", "CAEARX", "CAEAS", "CAEAZ",
                   "CAEBET", "CAEBGM", "CAEBIS", "CAEBMX", "CAEBOI", "CAEBOU", "CAEBOX",
                   "CAEBRO", "CAEBRW", "CAEBTV", "CAEBUF", "CAEBYZ", "CAECA", "CAECAE",
                   "CAECAR", "CAECDB", "CAECHS", "CAECLE", "CAECO", "CAECRP", "CAECT",
                   "CAECTP", "CAECYS", "CAEDC", "CAEDDC", "CAEDE", "CAEDLH", "CAEDMX",
                   "CAEDTX", "CAEDVN", "CAEEAX", "CAEEKA", "CAEEPZ", "CAEEWX", "CAEFFC",
                   "CAEFGF", "CAEFGZ", "CAEFL", "CAEFSD", "CAEFWD", "CAEGA", "CAEGGW",
                   "CAEGID", "CAEGJT", "CAEGLD", "CAEGRB", "CAEGRR", "CAEGSP", "CAEGU",
                   "CAEGUM", "CAEGYX", "CAEHFO", "CAEHGX", "CAEHI", "CAEHNX", "CAEHUN",
                   "CAEIA", "CAEICT", "CAEID", "CAEIL", "CAEILM", "CAEILN", "CAEILX",
                   "CAEIN", "CAEIND", "CAEIWX", "CAEJAN", "CAEJAX", "CAEJKL", "CAEKEY",
                   "CAEKS", "CAEKY", "CAELA", "CAELBF", "CAELCH", "CAELIX", "CAELKN",
                   "CAELMK", "CAELOT", "CAELOX", "CAELSX", "CAELUB", "CAELWX", "CAELZK",
                   "CAEMA", "CAEMAF", "CAEMCG", "CAEMCG", "CAEMD", "CAEME", "CAEMEG",
                   "CAEMFL", "CAEMFR", "CAEMHX", "CAEMI", "CAEMKX", "CAEMLB", "CAEMN",
                   "CAEMO", "CAEMOB", "CAEMPX", "CAEMQT", "CAEMRX", "CAEMS", "CAEMSO",
                   "CAEMT", "CAEMTR", "CAENC", "CAEND", "CAENE", "CAENH", "CAENJ",
                   "CAENV", "CAENY", "CAEOAX", "CAEOH", "CAEOHX", "CAEOK", "CAEOKX",
                   "CAEOME", "CAEOR", "CAEOTX", "CAEOTZ", "CAEOUN", "CAEPA", "CAEPAH",
                   "CAEPBZ", "CAEPDT", "CAEPHI", "CAEPIH", "CAEPPG", "CAEPQR", "CAEPR",
                   "CAEPSR", "CAEPUB", "CAERAH", "CAEREV", "CAERI", "CAERIW", "CAERLX",
                   "CAERNK", "CAESC", "CAESC", "CAESD", "CAESEW", "CAESGF", "CAESGX",
                   "CAESHV", "CAESJT", "CAESJU", "CAESLC", "CAESNP", "CAESPN", "CAESTO",
                   "CAETAE", "CAETBW", "CAETFX", "CAETN", "CAETOP", "CAETSA", "CAETWC",
                   "CAEUNR", "CAEUT", "CAEVA", "CAEVEF", "CAEVI", "CAEVT", "CAEWA",
                   "CAEWI", "CAEWV", "CAEWY", "CDWABQ", "CDWABR", "CDWADQ", "CDWAFC",
                   "CDWAFG", "CDWAJK", "CDWAK", "CDWAKN", "CDWAKQ", "CDWAL", "CDWALY",
                   "CDWAMA", "CDWAPX", "CDWAR", "CDWARX", "CDWAS", "CDWAZ", "CDWBET",
                   "CDWBGM", "CDWBIS", "CDWBMX", "CDWBOI", "CDWBOU", "CDWBOX", "CDWBRO",
                   "CDWBRW", "CDWBTV", "CDWBUF", "CDWBYZ", "CDWCA", "CDWCAE", "CDWCAR",
                   "CDWCDB", "CDWCHS", "CDWCLE", "CDWCO", "CDWCRP", "CDWCT", "CDWCTP",
                   "CDWCYS", "CDWDC", "CDWDDC", "CDWDE", "CDWDLH", "CDWDMX", "CDWDTX",
                   "CDWDVN", "CDWEAX", "CDWEKA", "CDWEPZ", "CDWEWX", "CDWFFC", "CDWFGF",
                   "CDWFGZ", "CDWFL", "CDWFSD", "CDWFWD", "CDWGA", "CDWGGW", "CDWGID",
                   "CDWGJT", "CDWGLD", "CDWGRB", "CDWGRR", "CDWGSP", "CDWGU", "CDWGUM",
                   "CDWGYX", "CDWHFO", "CDWHGX", "CDWHI", "CDWHNX", "CDWHUN", "CDWIA",
                   "CDWICT", "CDWID", "CDWIL", "CDWILM", "CDWILN", "CDWILX", "CDWIN",
                   "CDWIND", "CDWIWX", "CDWJAN", "CDWJAX", "CDWJKL", "CDWKEY", "CDWKS",
                   "CDWKY", "CDWLA", "CDWLBF", "CDWLCH", "CDWLIX", "CDWLKN", "CDWLMK",
                   "CDWLOT", "CDWLOX", "CDWLSX", "CDWLUB", "CDWLWX", "CDWLZK", "CDWMA",
                   "CDWMAF", "CDWMCG", "CDWMCG", "CDWMD", "CDWME", "CDWMEG", "CDWMFL",
                   "CDWMFR", "CDWMHX", "CDWMI", "CDWMI", "CDWMKX", "CDWMLB", "CDWMN",
                   "CDWMO", "CDWMOB", "CDWMPX", "CDWMQT", "CDWMRX", "CDWMS", "CDWMSO",
                   "CDWMT", "CDWMTR", "CDWNC", "CDWND", "CDWNE", "CDWNH", "CDWNJ",
                   "CDWNV", "CDWNY", "CDWOAX", "CDWOH", "CDWOHX", "CDWOK", "CDWOKX",
                   "CDWOME", "CDWOR", "CDWOTX", "CDWOTZ", "CDWOUN", "CDWPA", "CDWPAH",
                   "CDWPBZ", "CDWPDT", "CDWPHI", "CDWPIH", "CDWPPG", "CDWPQR", "CDWPR",
                   "CDWPSR", "CDWPUB", "CDWRAH", "CDWREV", "CDWRI", "CDWRIW", "CDWRLX",
                   "CDWRNK", "CDWSC", "CDWSC", "CDWSD", "CDWSEW", "CDWSGF", "CDWSGX",
                   "CDWSHV", "CDWSJT", "CDWSJU", "CDWSLC", "CDWSNP", "CDWSPN", "CDWSTO",
                   "CDWTAE", "CDWTBW", "CDWTFX", "CDWTN", "CDWTOP", "CDWTSA", "CDWTWC",
                   "CDWUNR", "CDWUT", "CDWVA", "CDWVEF", "CDWVI", "CDWVT", "CDWWA",
                   "CDWWI", "CDWWV", "CDWWY", "CEMABQ", "CEMABR", "CEMADQ", "CEMAER",
                   "CEMAFC", "CEMAFG", "CEMAJK", "CEMAK", "CEMAKN", "CEMAKQ", "CEMAL",
                   "CEMALU", "CEMALY", "CEMAMA", "CEMAPX", "CEMAR", "CEMARX", "CEMAS",
                   "CEMAZ", "CEMBET", "CEMBGM", "CEMBIS", "CEMBMX", "CEMBOI", "CEMBOU",
                   "CEMBOX", "CEMBRO", "CEMBRW", "CEMBTV", "CEMBUF", "CEMBYZ", "CEMCA",
                   "CEMCAE", "CEMCAR", "CEMCDB", "CEMCHS", "CEMCLE", "CEMCO", "CEMCRP",
                   "CEMCT", "CEMCTP", "CEMCYS", "CEMDC", "CEMDDC", "CEMDE", "CEMDLH",
                   "CEMDMX", "CEMDTX", "CEMDVN", "CEMEAX", "CEMEKA", "CEMEPZ", "CEMEWX",
                   "CEMFFC", "CEMFGF", "CEMFGZ", "CEMFL", "CEMFSD", "CEMFWD", "CEMGA",
                   "CEMGGW", "CEMGID", "CEMGJT", "CEMGLD", "CEMGRB", "CEMGRR", "CEMGSP",
                   "CEMGU", "CEMGUM", "CEMGYX", "CEMHFO", "CEMHGX", "CEMHI", "CEMHNX",
                   "CEMHON", "CEMHUN", "CEMIA", "CEMICT", "CEMID", "CEMIL", "CEMILM",
                   "CEMILN", "CEMILX", "CEMIN", "CEMIND", "CEMIWX", "CEMJAN", "CEMJAX",
                   "CEMJKL", "CEMKEY", "CEMKS", "CEMKY", "CEMLA", "CEMLBF", "CEMLCH",
                   "CEMLIX", "CEMLKN", "CEMLMK", "CEMLOT", "CEMLOX", "CEMLSX", "CEMLUB",
                   "CEMLWX", "CEMLZK", "CEMMA", "CEMMAF", "CEMMCG", "CEMMCG", "CEMMD",
                   "CEMME", "CEMMEG", "CEMMFL", "CEMMFR", "CEMMHX", "CEMMI", "CEMMKX",
                   "CEMMLB", "CEMMN", "CEMMO", "CEMMOB", "CEMMPX", "CEMMQT", "CEMMRX",
                   "CEMMS", "CEMMSO", "CEMMT", "CEMMTR", "CEMMY", "CEMNC", "CEMND",
                   "CEMNE", "CEMNH", "CEMNJ", "CEMNM", "CEMNV", "CEMNY", "CEMOAX",
                   "CEMOH", "CEMOHX", "CEMOK", "CEMOKX", "CEMOME", "CEMOR", "CEMOTX",
                   "CEMOTZ", "CEMOUN", "CEMPA", "CEMPAH", "CEMPBZ", "CEMPDT", "CEMPHI",
                   "CEMPIH", "CEMPPG", "CEMPQR", "CEMPR", "CEMPSR", "CEMPUB", "CEMRAH",
                   "CEMREV", "CEMRI", "CEMRIW", "CEMRLX", "CEMRNK", "CEMSC", "CEMSC",
                   "CEMSD", "CEMSEW", "CEMSGF", "CEMSGX", "CEMSHV", "CEMSJT", "CEMSJU",
                   "CEMSLC", "CEMSNP", "CEMSPN", "CEMSTO", "CEMTAE", "CEMTBW", "CEMTFX",
                   "CEMTN", "CEMTOP", "CEMTSA", "CEMTWC", "CEMTX", "CEMUNR", "CEMUT",
                   "CEMVA", "CEMVEF", "CEMVI", "CEMVT", "CEMVWS", "CEMWA", "CEMWI",
                   "CEMWV", "CEMWY", "DMOABQ", "DMOABR", "DMOADQ", "DMOAFC", "DMOAFG",
                   "DMOAJK", "DMOAK", "DMOAKQ", "DMOAL", "DMOALY", "DMOAPX", "DMOAR",
                   "DMOARX", "DMOAS", "DMOAZ", "DMOBGM", "DMOBIS", "DMOBMX", "DMOBOI",
                   "DMOBOU", "DMOBOX", "DMOBRO", "DMOBTV", "DMOBUF", "DMOBYZ", "DMOCA",
                   "DMOCAE", "DMOCAR", "DMOCHS", "DMOCLE", "DMOCO", "DMOCRP", "DMOCT",
                   "DMOCTP", "DMOCYS", "DMODC", "DMODDC", "DMODE", "DMODLH", "DMODMX",
                   "DMODTX", "DMODVN", "DMOEAX", "DMOEKA", "DMOEPZ", "DMOEWX", "DMOFFC",
                   "DMOFGF", "DMOFGZ", "DMOFL", "DMOFSD", "DMOGA", "DMOGGW", "DMOGID",
                   "DMOGJT", "DMOGLD", "DMOGRB", "DMOGRR", "DMOGSP", "DMOGU", "DMOGUM",
                   "DMOGYX", "DMOHFO", "DMOHGX", "DMOHI", "DMOHNX", "DMOIA", "DMOICT",
                   "DMOID", "DMOIL", "DMOILM", "DMOILN", "DMOILX", "DMOIN", "DMOIND",
                   "DMOIWX", "DMOJAN", "DMOJAX", "DMOJKL", "DMOKEY", "DMOKS", "DMOKY",
                   "DMOLA", "DMOLBF", "DMOLIX", "DMOLKN", "DMOLMK", "DMOLOT", "DMOLOX",
                   "DMOLSX", "DMOLUB", "DMOLWX", "DMOLZK", "DMOMA", "DMOMD", "DMOME",
                   "DMOMEG", "DMOMFL", "DMOMFR", "DMOMHX", "DMOMI", "DMOMKX", "DMOMLB",
                   "DMOMN", "DMOMO", "DMOMOB", "DMOMPX", "DMOMQT", "DMOMRX", "DMOMS",
                   "DMOMSO", "DMOMT", "DMOMTR", "DMONC", "DMOND", "DMONE", "DMONH",
                   "DMONJ", "DMONM", "DMONV", "DMONY", "DMOOAX", "DMOOH", "DMOOHX",
                   "DMOOK", "DMOOKX", "DMOOME", "DMOOR", "DMOOTX", "DMOOUN", "DMOPA",
                   "DMOPAH", "DMOPBZ", "DMOPDT", "DMOPHI", "DMOPIH", "DMOPPG", "DMOPQR",
                   "DMOPR", "DMOPSR", "DMOPUB", "DMORAH", "DMOREV", "DMORI", "DMORIW",
                   "DMORLX", "DMORNK", "DMOSC", "DMOSD", "DMOSEW", "DMOSGF", "DMOSGX",
                   "DMOSJT", "DMOSJU", "DMOSLC", "DMOSPN", "DMOSTO", "DMOTAE", "DMOTBW",
                   "DMOTFX", "DMOTN", "DMOTOP", "DMOTSA", "DMOTWC", "DMOUNR", "DMOUT",
                   "DMOVA", "DMOVEF", "DMOVI", "DMOVT", "DMOWA", "DMOWI", "DMOWV",
                   "DMOWY", "EQWABQ", "EQWABR", "EQWADQ", "EQWAFC", "EQWAFG", "EQWAJK",
                   "EQWAK", "EQWAKN", "EQWAKQ", "EQWAL", "EQWALY", "EQWAMA", "EQWAPX",
                   "EQWAR", "EQWARX", "EQWAS", "EQWAZ", "EQWBET", "EQWBGM", "EQWBIS",
                   "EQWBMX", "EQWBOI", "EQWBOU", "EQWBOX", "EQWBRO", "EQWBRW", "EQWBTV",
                   "EQWBUF", "EQWBYZ", "EQWCA", "EQWCAE", "EQWCAR", "EQWCDB", "EQWCHS",
                   "EQWCLE", "EQWCO", "EQWCRP", "EQWCT", "EQWCTP", "EQWCYS", "EQWDC",
                   "EQWDDC", "EQWDE", "EQWDLH", "EQWDMX", "EQWDTX", "EQWDVN", "EQWEAX",
                   "EQWEKA", "EQWEPZ", "EQWEWX", "EQWFFC", "EQWFGF", "EQWFGZ", "EQWFL",
                   "EQWFSD", "EQWFWD", "EQWGA", "EQWGGW", "EQWGID", "EQWGJT", "EQWGLD",
                   "EQWGRB", "EQWGRR", "EQWGSP", "EQWGU", "EQWGUM", "EQWGYX", "EQWHFO",
                   "EQWHGX", "EQWHI", "EQWHNX", "EQWHUN", "EQWIA", "EQWICT", "EQWID",
                   "EQWIL", "EQWILM", "EQWILN", "EQWILX", "EQWIN", "EQWIND", "EQWIWX",
                   "EQWJAN", "EQWJAX", "EQWJKL", "EQWKEY", "EQWKS", "EQWKY", "EQWLA",
                   "EQWLBF", "EQWLCH", "EQWLIX", "EQWLKN", "EQWLMK", "EQWLOT", "EQWLOX",
                   "EQWLSX", "EQWLUB", "EQWLWX", "EQWLZK", "EQWMA", "EQWMAF", "EQWMCG",
                   "EQWMCG", "EQWMD", "EQWME", "EQWMEG", "EQWMFL", "EQWMFR", "EQWMHX",
                   "EQWMI", "EQWMKX", "EQWMLB", "EQWMN", "EQWMO", "EQWMOB", "EQWMPX",
                   "EQWMQT", "EQWMRX", "EQWMS", "EQWMSO", "EQWMT", "EQWMTR", "EQWNC",
                   "EQWND", "EQWNE", "EQWNH", "EQWNJ", "EQWNV", "EQWNY", "EQWOAX",
                   "EQWOH", "EQWOHX", "EQWOK", "EQWOKX", "EQWOME", "EQWOR", "EQWOTX",
                   "EQWOTZ", "EQWOUN", "EQWPA", "EQWPAH", "EQWPBZ", "EQWPDT", "EQWPHI",
                   "EQWPIH", "EQWPPG", "EQWPQR", "EQWPR", "EQWPSR", "EQWPUB", "EQWRAH",
                   "EQWREV", "EQWRI", "EQWRIW", "EQWRLX", "EQWRNK", "EQWSC", "EQWSC",
                   "EQWSD", "EQWSEW", "EQWSGF", "EQWSGX", "EQWSJT", "EQWSJU", "EQWSLC",
                   "EQWSNP", "EQWSPN", "EQWSTO", "EQWTAE", "EQWTBW", "EQWTFX", "EQWTN",
                   "EQWTOP", "EQWTSA", "EQWTWC", "EQWUNR", "EQWUT", "EQWVA", "EQWVEF",
                   "EQWVI", "EQWVT", "EQWWA", "EQWWI", "EQWWV", "EQWWY", "EVIABQ",
                   "EVIABR", "EVIADQ", "EVIAFC", "EVIAFG", "EVIAJK", "EVIAK", "EVIAKN",
                   "EVIAKQ", "EVIAL", "EVIALY", "EVIAMA", "EVIAPX", "EVIAR", "EVIARX",
                   "EVIAS", "EVIAZ", "EVIBET", "EVIBGM", "EVIBIS", "EVIBMX", "EVIBOI",
                   "EVIBOU", "EVIBOX", "EVIBRO", "EVIBRW", "EVIBTV", "EVIBUF", "EVIBYZ",
                   "EVICA", "EVICAE", "EVICAR", "EVICDB", "EVICHS", "EVICLE", "EVICO",
                   "EVICRP", "EVICT", "EVICTP", "EVICYS", "EVIDC", "EVIDDC", "EVIDE",
                   "EVIDLH", "EVIDMX", "EVIDTX", "EVIDVN", "EVIEAX", "EVIEKA", "EVIEPZ",
                   "EVIEWX", "EVIFFC", "EVIFGF", "EVIFGZ", "EVIFL", "EVIFSD", "EVIFWD",
                   "EVIGA", "EVIGGW", "EVIGID", "EVIGJT", "EVIGLD", "EVIGRB", "EVIGRR",
                   "EVIGSP", "EVIGU", "EVIGUM", "EVIGYX", "EVIHFO", "EVIHGX", "EVIHI",
                   "EVIHNX", "EVIHUN", "EVIIA", "EVIICT", "EVIID", "EVIIL", "EVIILM",
                   "EVIILN", "EVIILX", "EVIIN", "EVIIND", "EVIIWX", "EVIJAN", "EVIJAX",
                   "EVIJKL", "EVIKEY", "EVIKS", "EVIKY", "EVILA", "EVILBF", "EVILCH",
                   "EVILIX", "EVILKN", "EVILMK", "EVILOT", "EVILOX", "EVILSX", "EVILUB",
                   "EVILWX", "EVILZK", "EVIMA", "EVIMAF", "EVIMCG", "EVIMCG", "EVIMD",
                   "EVIME", "EVIMEG", "EVIMFL", "EVIMFR", "EVIMHX", "EVIMI", "EVIMKX",
                   "EVIMLB", "EVIMN", "EVIMO", "EVIMOB", "EVIMPX", "EVIMQT", "EVIMRX",
                   "EVIMS", "EVIMSO", "EVIMT", "EVIMTR", "EVINC", "EVIND", "EVINE",
                   "EVINH", "EVINJ", "EVINV", "EVINY", "EVIOAX", "EVIOH", "EVIOHX",
                   "EVIOK", "EVIOKX", "EVIOME", "EVIOR", "EVIOTX", "EVIOTZ", "EVIOUN",
                   "EVIPA", "EVIPAH", "EVIPBZ", "EVIPDT", "EVIPHI", "EVIPIH", "EVIPPG",
                   "EVIPQR", "EVIPR", "EVIPSR", "EVIPUB", "EVIRAH", "EVIREV", "EVIRI",
                   "EVIRIW", "EVIRLX", "EVIRNK", "EVISC", "EVISC", "EVISD", "EVISEW",
                   "EVISGF", "EVISGX", "EVISHV", "EVISJT", "EVISJU", "EVISLC", "EVISNP",
                   "EVISPN", "EVISTO", "EVITAE", "EVITBW", "EVITFX", "EVITN", "EVITOP",
                   "EVITSA", "EVITWC", "EVIUNR", "EVIUT", "EVIVA", "EVIVEF", "EVIVI",
                   "EVIVT", "EVIWA", "EVIWI", "EVIWV", "EVIWY", "FRWABQ", "FRWABR",
                   "FRWADQ", "FRWAFC", "FRWAFG", "FRWAJK", "FRWAK", "FRWAKN", "FRWAKQ",
                   "FRWAL", "FRWALY", "FRWAMA", "FRWAPX", "FRWAR", "FRWARX", "FRWAS",
                   "FRWAZ", "FRWBET", "FRWBGM", "FRWBIS", "FRWBMX", "FRWBOI", "FRWBOU",
                   "FRWBOX", "FRWBRO", "FRWBRW", "FRWBTV", "FRWBUF", "FRWBYZ", "FRWCA",
                   "FRWCAE", "FRWCAR", "FRWCDB", "FRWCHS", "FRWCLE", "FRWCO", "FRWCRP",
                   "FRWCT", "FRWCTP", "FRWCYS", "FRWDC", "FRWDDC", "FRWDE", "FRWDLH",
                   "FRWDMX", "FRWDTX", "FRWDVN", "FRWEAX", "FRWEKA", "FRWEPZ", "FRWEWX",
                   "FRWFFC", "FRWFGF", "FRWFGZ", "FRWFL", "FRWFSD", "FRWFWD", "FRWGA",
                   "FRWGGW", "FRWGID", "FRWGJT", "FRWGLD", "FRWGRB", "FRWGRR", "FRWGSP",
                   "FRWGU", "FRWGUM", "FRWGYX", "FRWHFO", "FRWHGX", "FRWHI", "FRWHNX",
                   "FRWHUN", "FRWIA", "FRWICT", "FRWID", "FRWIL", "FRWILM", "FRWILN",
                   "FRWILX", "FRWIN", "FRWIND", "FRWIWX", "FRWJAN", "FRWJAX", "FRWJKL",
                   "FRWKEY", "FRWKS", "FRWKY", "FRWLA", "FRWLBF", "FRWLIX", "FRWLKN",
                   "FRWLMK", "FRWLOT", "FRWLOX", "FRWLSX", "FRWLUB", "FRWLWX", "FRWLZK",
                   "FRWMA", "FRWMAF", "FRWMCG", "FRWMCG", "FRWMD", "FRWME", "FRWMEG",
                   "FRWMFL", "FRWMFR", "FRWMHX", "FRWMI", "FRWMKX", "FRWMLB", "FRWMN",
                   "FRWMO", "FRWMOB", "FRWMPX", "FRWMQT", "FRWMRX", "FRWMS", "FRWMSO",
                   "FRWMT", "FRWMTR", "FRWNC", "FRWND", "FRWNE", "FRWNH", "FRWNJ",
                   "FRWNV", "FRWNY", "FRWOAX", "FRWOH", "FRWOHX", "FRWOK", "FRWOKX",
                   "FRWOME", "FRWOR", "FRWOTX", "FRWOTZ", "FRWOUN", "FRWPA", "FRWPAH",
                   "FRWPBZ", "FRWPDT", "FRWPHI", "FRWPIH", "FRWPPG", "FRWPQR", "FRWPR",
                   "FRWPSR", "FRWPUB", "FRWRAH", "FRWREV", "FRWRI", "FRWRIW", "FRWRLX",
                   "FRWRNK", "FRWSC", "FRWSC", "FRWSD", "FRWSEW", "FRWSGF", "FRWSGX",
                   "FRWSHV", "FRWSJT", "FRWSJU", "FRWSLC", "FRWSNP", "FRWSPN", "FRWSTO",
                   "FRWTAE", "FRWTBW", "FRWTFX", "FRWTN", "FRWTOP", "FRWTSA", "FRWTWC",
                   "FRWUNR", "FRWUT", "FRWVA", "FRWVEF", "FRWVI", "FRWVT", "FRWWA",
                   "FRWWI", "FRWWV", "FRWWY", "HMWABQ", "HMWABR", "HMWADQ", "HMWAFC",
                   "HMWAFG", "HMWAJK", "HMWAK", "HMWAKN", "HMWAKQ", "HMWAL", "HMWALY",
                   "HMWAPX", "HMWAR", "HMWARX", "HMWAS", "HMWAZ", "HMWBET", "HMWBGM",
                   "HMWBIS", "HMWBMX", "HMWBOI", "HMWBOU", "HMWBOX", "HMWBRO", "HMWBRW",
                   "HMWBTV", "HMWBUF", "HMWBYZ", "HMWCA", "HMWCAE", "HMWCAR", "HMWCDB",
                   "HMWCHS", "HMWCLE", "HMWCO", "HMWCRP", "HMWCT", "HMWCTP", "HMWCYS",
                   "HMWDC", "HMWDDC", "HMWDE", "HMWDLH", "HMWDMX", "HMWDTX", "HMWDVN",
                   "HMWEAX", "HMWEKA", "HMWEPZ", "HMWEWX", "HMWFFC", "HMWFGF", "HMWFGZ",
                   "HMWFL", "HMWFSD", "HMWFWD", "HMWGA", "HMWGGW", "HMWGID", "HMWGJT",
                   "HMWGLD", "HMWGRB", "HMWGRR", "HMWGSP", "HMWGU", "HMWGUM", "HMWGYX",
                   "HMWHFO", "HMWHGX", "HMWHI", "HMWHNX", "HMWHUN", "HMWIA", "HMWICT",
                   "HMWID", "HMWIL", "HMWILM", "HMWILN", "HMWILX", "HMWIN", "HMWIND",
                   "HMWIWX", "HMWJAN", "HMWJAX", "HMWJKL", "HMWKEY", "HMWKS", "HMWKY",
                   "HMWLA", "HMWLBF", "HMWLCH", "HMWLIX", "HMWLKN", "HMWLMK", "HMWLOT",
                   "HMWLOX", "HMWLSX", "HMWLUB", "HMWLWX", "HMWLZK", "HMWMA", "HMWMAF",
                   "HMWMCG", "HMWMCG", "HMWMD", "HMWME", "HMWMEG", "HMWMFL", "HMWMFR",
                   "HMWMHX", "HMWMI", "HMWMKX", "HMWMLB", "HMWMN", "HMWMO", "HMWMOB",
                   "HMWMPX", "HMWMQT", "HMWMRX", "HMWMS", "HMWMSO", "HMWMT", "HMWMTR",
                   "HMWNC", "HMWND", "HMWNE", "HMWNH", "HMWNJ", "HMWNV", "HMWNY",
                   "HMWOAX", "HMWOH", "HMWOHX", "HMWOK", "HMWOKX", "HMWOME", "HMWOR",
                   "HMWOTX", "HMWOTZ", "HMWOUN", "HMWPA", "HMWPAH", "HMWPBZ", "HMWPDT",
                   "HMWPHI", "HMWPIH", "HMWPPG", "HMWPQR", "HMWPR", "HMWPSR", "HMWPUB",
                   "HMWRAH", "HMWREV", "HMWRI", "HMWRIW", "HMWRLX", "HMWRNK", "HMWSC",
                   "HMWSC", "HMWSD", "HMWSEW", "HMWSGF", "HMWSGX", "HMWSHV", "HMWSJT",
                   "HMWSJU", "HMWSLC", "HMWSNP", "HMWSPN", "HMWSTO", "HMWTAE", "HMWTBW",
                   "HMWTFX", "HMWTN", "HMWTOP", "HMWTSA", "HMWTWC", "HMWUNR", "HMWUT",
                   "HMWVA", "HMWVEF", "HMWVI", "HMWVT", "HMWWA", "HMWWI", "HMWWV",
                   "HMWWY", "LAEABQ", "LAEABR", "LAEADQ", "LAEAFC", "LAEAFG", "LAEAJK",
                   "LAEAK", "LAEAKN", "LAEAKQ", "LAEAL", "LAEALY", "LAEAMA", "LAEAPX",
                   "LAEAR", "LAEARX", "LAEAS", "LAEAZ", "LAEBET", "LAEBGM", "LAEBIS",
                   "LAEBMX", "LAEBOI", "LAEBOU", "LAEBOX", "LAEBRO", "LAEBRW", "LAEBTV",
                   "LAEBUF", "LAEBYZ", "LAECA", "LAECAE", "LAECAR", "LAECDB", "LAECHS",
                   "LAECLE", "LAECO", "LAECRP", "LAECT", "LAECTP", "LAECYS", "LAEDC",
                   "LAEDDC", "LAEDE", "LAEDLH", "LAEDMX", "LAEDTX", "LAEDVN", "LAEEAX",
                   "LAEEKA", "LAEEPZ", "LAEEWX", "LAEFFC", "LAEFGF", "LAEFGZ", "LAEFL",
                   "LAEFSD", "LAEFWD", "LAEGA", "LAEGGW", "LAEGID", "LAEGJT", "LAEGLD",
                   "LAEGRB", "LAEGRR", "LAEGSP", "LAEGU", "LAEGUM", "LAEGYX", "LAEHFO",
                   "LAEHGX", "LAEHI", "LAEHNX", "LAEHUN", "LAEIA", "LAEICT", "LAEID",
                   "LAEIL", "LAEILM", "LAEILN", "LAEILX", "LAEIN", "LAEIND", "LAEIWX",
                   "LAEJAN", "LAEJAX", "LAEJKL", "LAEKEY", "LAEKS", "LAEKY", "LAELA",
                   "LAELBF", "LAELCH", "LAELIX", "LAELKN", "LAELMK", "LAELOT", "LAELOX",
                   "LAELSX", "LAELUB", "LAELWX", "LAELZK", "LAEMA", "LAEMAF", "LAEMCG",
                   "LAEMCG", "LAEMD", "LAEME", "LAEMEG", "LAEMFL", "LAEMFR", "LAEMHX",
                   "LAEMI", "LAEMKX", "LAEMLB", "LAEMN", "LAEMO", "LAEMOB", "LAEMPX",
                   "LAEMQT", "LAEMRX", "LAEMS", "LAEMSO", "LAEMT", "LAEMTR", "LAENC",
                   "LAEND", "LAENE", "LAENH", "LAENJ", "LAENV", "LAENY", "LAEOAX",
                   "LAEOH", "LAEOHX", "LAEOK", "LAEOKX", "LAEOME", "LAEOR", "LAEOTX",
                   "LAEOTZ", "LAEOUN", "LAEPA", "LAEPAH", "LAEPBZ", "LAEPDT", "LAEPHI",
                   "LAEPIH", "LAEPPG", "LAEPQR", "LAEPR", "LAEPSR", "LAEPUB", "LAERAH",
                   "LAEREV", "LAERI", "LAERIW", "LAERLX", "LAERNK", "LAESC", "LAESC",
                   "LAESD", "LAESEW", "LAESGF", "LAESGX", "LAESHV", "LAESJT", "LAESJU",
                   "LAESLC", "LAESNP", "LAESPN", "LAESTO", "LAETAE", "LAETBW", "LAETFX",
                   "LAETN", "LAETOP", "LAETSA", "LAETWC", "LAEUNR", "LAEUT", "LAEVA",
                   "LAEVEF", "LAEVI", "LAEVT", "LAEWA", "LAEWI", "LAEWV", "LAEWY",
                   "LEWABQ", "LEWABR", "LEWADQ", "LEWAFC", "LEWAFG", "LEWAJK", "LEWAK",
                   "LEWAKN", "LEWAKQ", "LEWAL", "LEWALY", "LEWAMA", "LEWAPX", "LEWAR",
                   "LEWARX", "LEWAS", "LEWAZ", "LEWBET", "LEWBGM", "LEWBIS", "LEWBMX",
                   "LEWBOI", "LEWBOU", "LEWBOX", "LEWBRO", "LEWBRW", "LEWBTV", "LEWBUF",
                   "LEWBYZ", "LEWCA", "LEWCAE", "LEWCAR", "LEWCDB", "LEWCHS", "LEWCLE",
                   "LEWCO", "LEWCRP", "LEWCT", "LEWCTP", "LEWCYS", "LEWDC", "LEWDDC",
                   "LEWDE", "LEWDLH", "LEWDMX", "LEWDTX", "LEWDVN", "LEWEAX", "LEWEKA",
                   "LEWEPZ", "LEWEWX", "LEWFFC", "LEWFGF", "LEWFGZ", "LEWFL", "LEWFSD",
                   "LEWFWD", "LEWGA", "LEWGGW", "LEWGID", "LEWGJT", "LEWGLD", "LEWGRB",
                   "LEWGRR", "LEWGSP", "LEWGU", "LEWGUM", "LEWGYX", "LEWHFO", "LEWHGX",
                   "LEWHI", "LEWHNX", "LEWHUN", "LEWIA", "LEWICT", "LEWID", "LEWIL",
                   "LEWILM", "LEWILN", "LEWILX", "LEWIN", "LEWIND", "LEWIWX", "LEWJAN",
                   "LEWJAX", "LEWJKL", "LEWKEY", "LEWKS", "LEWKY", "LEWLA", "LEWLBF",
                   "LEWLCH", "LEWLIX", "LEWLKN", "LEWLMK", "LEWLOT", "LEWLOX", "LEWLSX",
                   "LEWLUB", "LEWLWX", "LEWLZK", "LEWMA", "LEWMAF", "LEWMCG", "LEWMCG",
                   "LEWMD", "LEWME", "LEWMEG", "LEWMFL", "LEWMFR", "LEWMHX", "LEWMI",
                   "LEWMKX", "LEWMLB", "LEWMN", "LEWMO", "LEWMOB", "LEWMPX", "LEWMQT",
                   "LEWMRX", "LEWMS", "LEWMSO", "LEWMT", "LEWMTR", "LEWNC", "LEWND",
                   "LEWNE", "LEWNH", "LEWNJ", "LEWNV", "LEWNY", "LEWOAX", "LEWOH",
                   "LEWOHX", "LEWOK", "LEWOKX", "LEWOME", "LEWOR", "LEWOTX", "LEWOTZ",
                   "LEWOUN", "LEWPA", "LEWPAH", "LEWPBZ", "LEWPDT", "LEWPHI", "LEWPIH",
                   "LEWPPG", "LEWPQR", "LEWPR", "LEWPSR", "LEWPUB", "LEWRAH", "LEWREV",
                   "LEWRI", "LEWRIW", "LEWRLX", "LEWRNK", "LEWSC", "LEWSC", "LEWSD",
                   "LEWSEW", "LEWSGF", "LEWSGX", "LEWSHV", "LEWSJT", "LEWSJU", "LEWSLC",
                   "LEWSNP", "LEWSPN", "LEWSTO", "LEWTAE", "LEWTBW", "LEWTFX", "LEWTN",
                   "LEWTOP", "LEWTSA", "LEWTWC", "LEWUNR", "LEWUT", "LEWVA", "LEWVEF",
                   "LEWVI", "LEWVT", "LEWWA", "LEWWI", "LEWWV", "LEWWY", "NUWABQ",
                   "NUWABR", "NUWADQ", "NUWAFC", "NUWAFG", "NUWAJK", "NUWAK", "NUWAKN",
                   "NUWAKQ", "NUWAL", "NUWALY", "NUWAMA", "NUWAPX", "NUWAR", "NUWARX",
                   "NUWAS", "NUWAZ", "NUWBET", "NUWBGM", "NUWBIS", "NUWBMX", "NUWBOI",
                   "NUWBOU", "NUWBOX", "NUWBRO", "NUWBRW", "NUWBTV", "NUWBUF", "NUWBYZ",
                   "NUWCA", "NUWCAE", "NUWCAR", "NUWCDB", "NUWCHS", "NUWCLE", "NUWCO",
                   "NUWCRP", "NUWCT", "NUWCTP", "NUWCYS", "NUWDC", "NUWDDC", "NUWDE",
                   "NUWDLH", "NUWDMX", "NUWDTX", "NUWDVN", "NUWEAX", "NUWEKA", "NUWEPZ",
                   "NUWEWX", "NUWFFC", "NUWFGF", "NUWFGZ", "NUWFL", "NUWFSD", "NUWFWD",
                   "NUWGA", "NUWGGW", "NUWGID", "NUWGJT", "NUWGLD", "NUWGRB", "NUWGRR",
                   "NUWGSP", "NUWGU", "NUWGUM", "NUWGYX", "NUWHFO", "NUWHGX", "NUWHI",
                   "NUWHNX", "NUWHUN", "NUWIA", "NUWICT", "NUWID", "NUWIL", "NUWILM",
                   "NUWILN", "NUWILX", "NUWIN", "NUWIND", "NUWIWX", "NUWJAN", "NUWJAX",
                   "NUWJKL", "NUWKEY", "NUWKS", "NUWKY", "NUWLA", "NUWLBF", "NUWLCH",
                   "NUWLIX", "NUWLKN", "NUWLMK", "NUWLOT", "NUWLOX", "NUWLSX", "NUWLUB",
                   "NUWLWX", "NUWLZK", "NUWMA", "NUWMAF", "NUWMCG", "NUWMCG", "NUWMD",
                   "NUWME", "NUWMEG", "NUWMFL", "NUWMFR", "NUWMHX", "NUWMI", "NUWMKX",
                   "NUWMLB", "NUWMN", "NUWMO", "NUWMOB", "NUWMPX", "NUWMQT", "NUWMRX",
                   "NUWMS", "NUWMSO", "NUWMT", "NUWMTR", "NUWNC", "NUWND", "NUWNE",
                   "NUWNH", "NUWNJ", "NUWNV", "NUWNY", "NUWOAX", "NUWOH", "NUWOHX",
                   "NUWOK", "NUWOKX", "NUWOME", "NUWOR", "NUWOTX", "NUWOTZ", "NUWOUN",
                   "NUWPA", "NUWPAH", "NUWPBZ", "NUWPDT", "NUWPHI", "NUWPIH", "NUWPPG",
                   "NUWPQR", "NUWPR", "NUWPSR", "NUWPUB", "NUWRAH", "NUWREV", "NUWRI",
                   "NUWRIW", "NUWRLX", "NUWRNK", "NUWSC", "NUWSC", "NUWSD", "NUWSEW",
                   "NUWSGF", "NUWSGX", "NUWSHV", "NUWSJT", "NUWSJU", "NUWSLC", "NUWSNP",
                   "NUWSPN", "NUWSTO", "NUWTAE", "NUWTBW", "NUWTFX", "NUWTN", "NUWTOP",
                   "NUWTSA", "NUWTWC", "NUWUNR", "NUWUT", "NUWVA", "NUWVEF", "NUWVI",
                   "NUWVT", "NUWWA", "NUWWI", "NUWWV", "NUWWY", "RHWABQ", "RHWABR",
                   "RHWADQ", "RHWAFC", "RHWAFG", "RHWAJK", "RHWAK", "RHWAKN", "RHWAKQ",
                   "RHWAL", "RHWALY", "RHWAMA", "RHWAPX", "RHWAR", "RHWARX", "RHWAS",
                   "RHWAZ", "RHWBET", "RHWBGM", "RHWBIS", "RHWBMX", "RHWBOI", "RHWBOU",
                   "RHWBOX", "RHWBRO", "RHWBRW", "RHWBTV", "RHWBUF", "RHWBYZ", "RHWCA",
                   "RHWCAE", "RHWCAR", "RHWCDB", "RHWCHS", "RHWCLE", "RHWCO", "RHWCRP",
                   "RHWCT", "RHWCTP", "RHWCYS", "RHWDC", "RHWDDC", "RHWDE", "RHWDLH",
                   "RHWDMX", "RHWDTX", "RHWDVN", "RHWEAX", "RHWEKA", "RHWEPZ", "RHWEWX",
                   "RHWFFC", "RHWFGF", "RHWFGZ", "RHWFL", "RHWFSD", "RHWFWD", "RHWGA",
                   "RHWGGW", "RHWGID", "RHWGJT", "RHWGLD", "RHWGRB", "RHWGRR", "RHWGSP",
                   "RHWGU", "RHWGUM", "RHWGYX", "RHWHFO", "RHWHGX", "RHWHI", "RHWHNX",
                   "RHWHUN", "RHWIA", "RHWICT", "RHWID", "RHWIL", "RHWILM", "RHWILN",
                   "RHWILX", "RHWIN", "RHWIND", "RHWIWX", "RHWJAN", "RHWJAX", "RHWJKL",
                   "RHWKEY", "RHWKS", "RHWKY", "RHWLA", "RHWLBF", "RHWLCH", "RHWLIX",
                   "RHWLKN", "RHWLMK", "RHWLOT", "RHWLOX", "RHWLSX", "RHWLUB", "RHWLWX",
                   "RHWLZK", "RHWMA", "RHWMAF", "RHWMCG", "RHWMCG", "RHWMD", "RHWME",
                   "RHWMEG", "RHWMFL", "RHWMFR", "RHWMHX", "RHWMI", "RHWMKX", "RHWMLB",
                   "RHWMN", "RHWMO", "RHWMOB", "RHWMPX", "RHWMQT", "RHWMRX", "RHWMS",
                   "RHWMSO", "RHWMT", "RHWMTR", "RHWNC", "RHWND", "RHWNE", "RHWNH",
                   "RHWNJ", "RHWNV", "RHWNY", "RHWOAX", "RHWOH", "RHWOHX", "RHWOK",
                   "RHWOKX", "RHWOME", "RHWOR", "RHWOTX", "RHWOTZ", "RHWOUN", "RHWPA",
                   "RHWPAH", "RHWPBZ", "RHWPDT", "RHWPHI", "RHWPIH", "RHWPPG", "RHWPQR",
                   "RHWPR", "RHWPSR", "RHWPUB", "RHWRAH", "RHWREV", "RHWRI", "RHWRIW",
                   "RHWRLX", "RHWRNK", "RHWSC", "RHWSC", "RHWSD", "RHWSEW", "RHWSGF",
                   "RHWSGX", "RHWSHV", "RHWSJT", "RHWSJU", "RHWSLC", "RHWSNP", "RHWSPN",
                   "RHWSTO", "RHWTAE", "RHWTBW", "RHWTFX", "RHWTN", "RHWTOP", "RHWTSA",
                   "RHWTWC", "RHWUNR", "RHWUT", "RHWVA", "RHWVEF", "RHWVI", "RHWVT",
                   "RHWWA", "RHWWI", "RHWWV", "RHWWY", "SPWABQ", "SPWABR", "SPWADQ",
                   "SPWAFC", "SPWAFG", "SPWAJK", "SPWAK", "SPWAKN", "SPWAKQ", "SPWAL",
                   "SPWALY", "SPWAMA", "SPWAPX", "SPWAR", "SPWARX", "SPWAS", "SPWAZ",
                   "SPWBET", "SPWBGM", "SPWBIS", "SPWBMX", "SPWBOI", "SPWBOU", "SPWBOX",
                   "SPWBRO", "SPWBRW", "SPWBTV", "SPWBUF", "SPWBYZ", "SPWCA", "SPWCAE",
                   "SPWCAR", "SPWCDB", "SPWCHS", "SPWCLE", "SPWCO", "SPWCRP", "SPWCT",
                   "SPWCTP", "SPWCYS", "SPWDC", "SPWDDC", "SPWDE", "SPWDLH", "SPWDMX",
                   "SPWDTX", "SPWDVN", "SPWEAX", "SPWEKA", "SPWEPZ", "SPWEWX", "SPWFFC",
                   "SPWFGF", "SPWFGZ", "SPWFL", "SPWFSD", "SPWFWD", "SPWGA", "SPWGGW",
                   "SPWGID", "SPWGJT", "SPWGLD", "SPWGRB", "SPWGRR", "SPWGSP", "SPWGU",
                   "SPWGUM", "SPWGYX", "SPWHFO", "SPWHI", "SPWHNX", "SPWHUN", "SPWIA",
                   "SPWICT", "SPWID", "SPWIL", "SPWILM", "SPWILN", "SPWILX", "SPWIN",
                   "SPWIND", "SPWIWX", "SPWJAN", "SPWJAX", "SPWJKL", "SPWKEY", "SPWKS",
                   "SPWKY", "SPWLA", "SPWLBF", "SPWLCH", "SPWLIX", "SPWLKN", "SPWLMK",
                   "SPWLOT", "SPWLOX", "SPWLSX", "SPWLUB", "SPWLWX", "SPWLZK", "SPWMA",
                   "SPWMAF", "SPWMCG", "SPWMCG", "SPWMD", "SPWME", "SPWMEG", "SPWMFL",
                   "SPWMFR", "SPWMHX", "SPWMI", "SPWMKX", "SPWMLB", "SPWMN", "SPWMO",
                   "SPWMOB", "SPWMPX", "SPWMQT", "SPWMRX", "SPWMS", "SPWMSO", "SPWMT",
                   "SPWMTR", "SPWNC", "SPWND", "SPWNE", "SPWNH", "SPWNJ", "SPWNV",
                   "SPWNY", "SPWOAX", "SPWOH", "SPWOHX", "SPWOK", "SPWOKX", "SPWOME",
                   "SPWOR", "SPWOTX", "SPWOTZ", "SPWOUN", "SPWPA", "SPWPAH", "SPWPBZ",
                   "SPWPDT", "SPWPHI", "SPWPIH", "SPWPPG", "SPWPQR", "SPWPR", "SPWPSR",
                   "SPWPUB", "SPWRAH", "SPWREV", "SPWRI", "SPWRIW", "SPWRLX", "SPWRNK",
                   "SPWSC", "SPWSC", "SPWSD", "SPWSEW", "SPWSGF", "SPWSGX", "SPWSHV",
                   "SPWSJT", "SPWSJU", "SPWSLC", "SPWSNP", "SPWSPN", "SPWSTO", "SPWTAE",
                   "SPWTBW", "SPWTFX", "SPWTN", "SPWTOP", "SPWTSA", "SPWTWC", "SPWUNR",
                   "SPWUT", "SPWVA", "SPWVEF", "SPWVI", "SPWVT", "SPWWA", "SPWWI",
                   "SPWWV", "SPWWY", "TOEABQ", "TOEABR", "TOEADQ", "TOEAFC", "TOEAFG",
                   "TOEAJK", "TOEAK", "TOEAKN", "TOEAKQ", "TOEAL", "TOEALY", "TOEAMA",
                   "TOEAPX", "TOEAR", "TOEARX", "TOEAS", "TOEAZ", "TOEBET", "TOEBGM",
                   "TOEBIS", "TOEBMX", "TOEBOI", "TOEBOU", "TOEBOX", "TOEBRO", "TOEBRW",
                   "TOEBTV", "TOEBUF", "TOEBYZ", "TOECA", "TOECAE", "TOECAR", "TOECDB",
                   "TOECHS", "TOECLE", "TOECO", "TOECRP", "TOECT", "TOECTP", "TOECYS",
                   "TOEDC", "TOEDDC", "TOEDE", "TOEDLH", "TOEDMX", "TOEDTX", "TOEDVN",
                   "TOEEAX", "TOEEKA", "TOEEPZ", "TOEEWX", "TOEFFC", "TOEFGF", "TOEFGZ",
                   "TOEFL", "TOEFSD", "TOEFWD", "TOEGA", "TOEGGW", "TOEGID", "TOEGJT",
                   "TOEGLD", "TOEGRB", "TOEGRR", "TOEGSP", "TOEGU", "TOEGUM", "TOEGYX",
                   "TOEHFO", "TOEHGX", "TOEHI", "TOEHNX", "TOEHUN", "TOEIA", "TOEICT",
                   "TOEID", "TOEIL", "TOEILM", "TOEILN", "TOEILX", "TOEIN", "TOEIND",
                   "TOEIWX", "TOEJAN", "TOEJAX", "TOEJKL", "TOEKEY", "TOEKS", "TOEKY",
                   "TOELA", "TOELBF", "TOELCH", "TOELIX", "TOELKN", "TOELMK", "TOELOT",
                   "TOELOX", "TOELSX", "TOELUB", "TOELWX", "TOELZK", "TOEMA", "TOEMAF",
                   "TOEMCG", "TOEMCG", "TOEMD", "TOEME", "TOEMEG", "TOEMFL", "TOEMFR",
                   "TOEMHX", "TOEMI", "TOEMKX", "TOEMLB", "TOEMN", "TOEMO", "TOEMOB",
                   "TOEMPX", "TOEMQT", "TOEMRX", "TOEMS", "TOEMSO", "TOEMT", "TOEMTR",
                   "TOENC", "TOEND", "TOENE", "TOENH", "TOENJ", "TOENV", "TOENY",
                   "TOEOAX", "TOEOH", "TOEOHX", "TOEOK", "TOEOKX", "TOEOME", "TOEOR",
                   "TOEOTX", "TOEOTZ", "TOEOUN", "TOEPA", "TOEPAH", "TOEPBZ", "TOEPDT",
                   "TOEPHI", "TOEPIH", "TOEPPG", "TOEPQR", "TOEPR", "TOEPSR", "TOEPUB",
                   "TOERAH", "TOEREV", "TOERI", "TOERIW", "TOERLX", "TOERNK", "TOESC",
                   "TOESC", "TOESD", "TOESEW", "TOESGF", "TOESGX", "TOESHV", "TOESJT",
                   "TOESJU", "TOESLC", "TOESNP", "TOESPN", "TOESTO", "TOETAE", "TOETBW",
                   "TOETFX", "TOETN", "TOETOP", "TOETSA", "TOETWC", "TOEUNR", "TOEUT",
                   "TOEVA", "TOEVEF", "TOEVI", "TOEVT", "TOEWA", "TOEWI", "TOEWV",
                   "TOEWY", "VOWABQ", "VOWABR", "VOWADQ", "VOWAFC", "VOWAFG", "VOWAJK",
                   "VOWAK", "VOWAKN", "VOWAKQ", "VOWAL", "VOWALY", "VOWAMA", "VOWAPX",
                   "VOWAR", "VOWARX", "VOWAS", "VOWAZ", "VOWBET", "VOWBGM", "VOWBIS",
                   "VOWBMX", "VOWBOI", "VOWBOU", "VOWBOX", "VOWBRO", "VOWBRW", "VOWBTV",
                   "VOWBUF", "VOWBYZ", "VOWCA", "VOWCAE", "VOWCAR", "VOWCDB", "VOWCHS",
                   "VOWCLE", "VOWCO", "VOWCRP", "VOWCT", "VOWCTP", "VOWCYS", "VOWDC",
                   "VOWDDC", "VOWDE", "VOWDLH", "VOWDMX", "VOWDTX", "VOWDVN", "VOWEAX",
                   "VOWEKA", "VOWEPZ", "VOWEWX", "VOWFFC", "VOWFGF", "VOWFGZ", "VOWFL",
                   "VOWFSD", "VOWFWD", "VOWGA", "VOWGGW", "VOWGID", "VOWGJT", "VOWGLD",
                   "VOWGRB", "VOWGRR", "VOWGSP", "VOWGU", "VOWGUM", "VOWGYX", "VOWHFO",
                   "VOWHGX", "VOWHI", "VOWHNX", "VOWHUN", "VOWIA", "VOWICT", "VOWID",
                   "VOWIL", "VOWILM", "VOWILN", "VOWILX", "VOWIN", "VOWIND", "VOWIWX",
                   "VOWJAN", "VOWJAX", "VOWJKL", "VOWKEY", "VOWKS", "VOWKY", "VOWLA",
                   "VOWLBF", "VOWLCH", "VOWLIX", "VOWLKN", "VOWLMK", "VOWLOT", "VOWLOX",
                   "VOWLSX", "VOWLUB", "VOWLWX", "VOWLZK", "VOWMA", "VOWMAF", "VOWMCG",
                   "VOWMCG", "VOWMD", "VOWME", "VOWMEG", "VOWMFL", "VOWMFR", "VOWMHX",
                   "VOWMI", "VOWMKX", "VOWMLB", "VOWMN", "VOWMO", "VOWMOB", "VOWMPX",
                   "VOWMQT", "VOWMRX", "VOWMS", "VOWMSO", "VOWMT", "VOWMTR", "VOWNC",
                   "VOWND", "VOWNE", "VOWNH", "VOWNJ", "VOWNV", "VOWNY", "VOWOAX",
                   "VOWOH", "VOWOHX", "VOWOK", "VOWOKX", "VOWOME", "VOWOR", "VOWOTX",
                   "VOWOTZ", "VOWOUN", "VOWPA", "VOWPAH", "VOWPBZ", "VOWPDT", "VOWPHI",
                   "VOWPIH", "VOWPPG", "VOWPQR", "VOWPR", "VOWPSR", "VOWPUB", "VOWRAH",
                   "VOWREV", "VOWRI", "VOWRIW", "VOWRLX", "VOWRNK", "VOWSC", "VOWSC",
                   "VOWSD", "VOWSEW", "VOWSGF", "VOWSGX", "VOWSHV", "VOWSJT", "VOWSJU",
                   "VOWSLC", "VOWSNP", "VOWSPN", "VOWSTO", "VOWTAE", "VOWTBW", "VOWTFX",
                   "VOWTN", "VOWTOP", "VOWTSA", "VOWTWC", "VOWUNR", "VOWUT", "VOWVA",
                   "VOWVEF", "VOWVI", "VOWVT", "VOWWA", "VOWWI", "VOWWV", "VOWWY",
                   "NPWABQ", "NPWABR", "NPWADQ", "NPWAER", "NPWAFG", "NPWAJK", "NPWAKQ",
                   "NPWALU", "NPWALY", "NPWAMA", "NPWAPX", "NPWARX", "NPWBGM", "NPWBIS",
                   "NPWBMX", "NPWBOI", "NPWBOU", "NPWBOX", "NPWBRO", "NPWBRW", "NPWBTV",
                   "NPWBUF", "NPWBYZ", "NPWCAE", "NPWCAR", "NPWCHS", "NPWCLE", "NPWCMH",
                   "NPWCRP", "NPWCTP", "NPWCVG", "NPWCYS", "NPWDDC", "NPWDLH", "NPWDMX",
                   "NPWDTX", "NPWDVN", "NPWEAX", "NPWEKA", "NPWEPZ", "NPWEWR", "NPWEWX",
                   "NPWFFC", "NPWFGF", "NPWFGZ", "NPWFSD", "NPWFWD", "NPWGGW", "NPWGID",
                   "NPWGJT", "NPWGLD", "NPWGRB", "NPWGRR", "NPWGSP", "NPWGYX", "NPWHFO",
                   "NPWHGX", "NPWHI", "NPWHNX", "NPWHUN", "NPWICT", "NPWILM", "NPWILN",
                   "NPWILX", "NPWIND", "NPWIWX", "NPWJAN", "NPWJAX", "NPWJKL", "NPWKEY",
                   "NPWLBF", "NPWLCH", "NPWLIX", "NPWLKN", "NPWLMK", "NPWLOT", "NPWLOX",
                   "NPWLSX", "NPWLUB", "NPWLWX", "NPWLZK", "NPWMAF", "NPWMCG", "NPWMEG",
                   "NPWMFL", "NPWMFR", "NPWMHX", "NPWMKX", "NPWMLB", "NPWMOB", "NPWMPX",
                   "NPWMQT", "NPWMRX", "NPWMSO", "NPWMTR", "NPWMY", "NPWNSB", "NPWOAX",
                   "NPWOHX", "NPWOKX", "NPWOME", "NPWOTX", "NPWOTZ", "NPWOUN", "NPWPAH",
                   "NPWPBZ", "NPWPDT", "NPWPHI", "NPWPIH", "NPWPPG", "NPWPQR", "NPWPSR",
                   "NPWPUB", "NPWRAH", "NPWREV", "NPWRIW", "NPWRLX", "NPWRNK", "NPWSEW",
                   "NPWSGF", "NPWSGX", "NPWSHV", "NPWSJT", "NPWSJU", "NPWSLC", "NPWSPN",
                   "NPWSTO", "NPWTAE", "NPWTBW", "NPWTFX", "NPWTOP", "NPWTSA", "NPWTWC",
                   "NPWUNR", "NPWVEF", "NPWWCZ"]
