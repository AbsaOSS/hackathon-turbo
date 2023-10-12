import requests
import pandas as pd
import random
import time
import os.path
import yfinance as yf
from datetime import datetime
import pandas_datareader as web
from bs4 import BeautifulSoup


# requests_cache.install_cache('yfinance.cache')

class Scraper:
    def get_name(self, stock: str) -> str:
        if stock.endswith('.JO'):
            return 'jse'
        elif stock.endswith('.SS') or stock.endswith('.SZ'):
            return 'ssx'
        elif stock.endswith('.T'):
            return 'jpx'
        elif stock.endswith('.AX'):
            return 'aux'
        elif '.' not in stock:
            return 'nyse'
        else:
            raise Exception('unknown ticker symbol')

    def get_top_100_stocks(self, exchange: str):
        exchange = exchange.upper()  # Ensure the exchange code is in uppercase

        # Define the URL to fetch the list of top 100 stocks
        url = f"https://finance.yahoo.com/screener/predefined/most_actives?count=100&offset=0&exchange={exchange}&count=100"

        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML response into a DataFrame
            df = pd.read_html(response.text)[0]
            return df
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None

    def download_stock_data(self, stock: str, start_date: datetime, end_date: datetime, interval: str, force: bool = False):
        dt_format = '%Y-%m-%d'
        
        fn = os.path.join(os.path.dirname(__file__), 'datasets', self.get_name(stock), f"{stock}_{start_date.strftime(dt_format)}_{end_date.strftime(dt_format)}.csv")

        if not force and os.path.isfile(fn):
            df = pd.read_csv(fn)
            if len(df) > 29:
                print(f"{stock} = Yes (already downloaded rows {len(df)})")
                return

        print(stock)
        df = yf.download(stock, start=start_date, end=end_date, interval=interval, ignore_tz=True)
        # Load the data into a pandas dataframe
        attempts = 3
        for i in range(attempts):
            df = pd.DataFrame(df)
            if len(df) < 29:
                print(f"not enough data {len(df)} - retrying")
                time.sleep(1)
            else:
                break
        if len(df) < 29:
            return
        # Save the dataframe to a csv file with the stock symbol as the file name
        os.makedirs(os.path.dirname(fn), exist_ok=True)
        df.to_csv(fn)
        # Print a message to indicate the file is saved
        print(f"Data for {stock} is saved to {fn}")


class NyseScraper(Scraper):
    def name(self) -> str:
        return "nyse"

    def get_top_100_stocks(self, num) -> list:
        return ["JPM",
            "V",
            "XOM",
            "TSM",
            "NVO",
            "CVX",
            "ORCL",
            "BAC",
            "KO",
            "BABA",
            "SHEL",
            "PFE",
            "WFC",
            "DIS",
            "HDB",
            "MS",
            "NKE",
            "VZ",
            "NEE",
            "BX",
            "BMY",
            "T",
            "BP",
            "RTX",
            "C",
            "SCHW",
            "PBR",
            "PBR",
            "CVS",
            "UBER",
            "SLB",
            "IBN",
            "BSX",
            "MO",
            "INFY",
            "SHOP",
            "FDX",
            "STLA",
            "EPD",
            "VALE",
            "OXY",
            "FCX",
            "ITUB",
            "USB",
            "VLO",
            "SNOW",
            "F",
            "GM",
            "SU",
            "PCG",
            "ET",
            "ABEV",
            "KVUE",
            "LYG",
            "HLN",
            "CRH",
            "TFC",
            "CVE",
            "KMI",
            "LVS",
            "NU",
            "NEM",
            "BBD",
            "CPNG",
            "PLTR",
            "DVN",
            "OKE",
            "BCS",
            "GOLD",
            "SQ",
            "HPQ",
            "DAL",
            "HPE",
            "NOK",
            "SE",
            "BEKE",
            "CTRA",
            "NET",
            "CCL",
            "UMC",
            "PINS",
            "OWL",
            "CNHI",
            "RF",
            "EQT",
            "MRO",
            "RBLX",
            "NIO",
            "XPEV",
            "SNAP",
            "MMP",
            "AMCR",
            "MGM",
            "MOS",
            "VST",
            "U",
            "TEVA",
            "ALLY",
            "NI",
            "AES"]


class JPXScraper(Scraper):
    def name(self) -> str:
        return "jpx"

    def get_top_100_stocks(self, num: int) -> list:
        return [
            "7203.T", # Toyota Motor Corporation
            "8306.T", # Mitsubishi UFJ Financial Group, Inc.
            "9432.T", # Nippon Telegraph and Telephone Corporation
            "6758.T", # Sony Group Corporation
            "6861.T", # Keyence Corporation
            "9983.T", # Fast Retailing Co., Ltd.
            "8058.T", # Mitsubishi Corporation
            "8316.T", # Sumitomo Mitsui Financial Group, Inc.
            "9433.T", # KDDI Corporation
            "8035.T", # Tokyo Electron Limited
            "4063.T", # Shin-Etsu Chemical Co., Ltd.
            "6501.T", # Hitachi, Ltd.
            "9984.T", # SoftBank Group Corp.
            "7267.T", # Honda Motor Co., Ltd.
            "8031.T", # Mitsui & Co., Ltd.
            "9434.T", # SoftBank Corp.
            "4661.T", # Oriental Land Co., Ltd.
            "8001.T", # ITOCHU Corporation
            "6902.T", # DENSO Corporation
            "6098.T", # Recruit Holdings Co., Ltd.
            "4568.T", # Daiichi Sankyo Company, Limited
            "4502.T", # Takeda Pharmaceutical Company Limited
            "8766.T", # Tokio Marine Holdings, Inc.
            "7974.T", # Nintendo Co., Ltd.
            "4519.T", # Chugai Pharmaceutical Co., Ltd.
            "6367.T", # Daikin Industries,Ltd.
            "8411.T", # Mizuho Financial Group, Inc.
            "2914.T", # Japan Tobacco Inc.
            "7741.T", # HOYA Corporation
            "3382.T", # Seven & i Holdings Co., Ltd.
            "6981.T", # Murata Manufacturing Co., Ltd.
            "7182.T", # JAPAN POST BANK Co., Ltd.
            "6273.T", # SMC Corporation
            "6178.T", # Japan Post Holdings Co., Ltd.
            "8002.T", # Marubeni Corporation
            "6301.T", # Komatsu Ltd.
            "5108.T", # Bridgestone Corporation
            "6594.T", # Nidec Corporation
            "6752.T", # Panasonic Holdings Corporation
            "6723.T", # Renesas Electronics Corporation
            "6503.T", # Mitsubishi Electric Corporation
            "8053.T", # Sumitomo Corporation
            "6201.T", # Toyota Industries Corporation
            "6954.T", # Fanuc Corporation
            "4503.T", # Astellas Pharma Inc.
            "9022.T", # Central Japan Railway Company
            "7751.T", # Canon Inc.
            "4901.T", # FUJIFILM Holdings Corporation
            "6702.T", # Fujitsu Limited
            "5401.T", # Nippon Steel Corporation
            "8591.T", # ORIX Corporation
            "9020.T", # East Japan Railway Company
            "8113.T", # Unicharm Corporation
            "8015.T", # Toyota Tsusho Corporation
            "8801.T", # Mitsui Fudosan Co., Ltd.
            "4689.T", # Z Holdings Corporation
            "4543.T", # Terumo Corporation
            "8725.T", # MS&AD Insurance Group Holdings, Inc.
            "8750.T", # Dai-ichi Life Holdings, Inc.
            "2802.T", # Ajinomoto Co., Inc.
            "9613.T", # NTT DATA Group Corporation
            "1605.T", # Inpex Corporation
            "6857.T", # Advantest Corporation
            "7269.T", # Suzuki Motor Corporation
            "2502.T", # Asahi Group Holdings, Ltd.
            "4578.T", # Otsuka Holdings Co., Ltd.
            "7011.T", # Mitsubishi Heavy Industries, Ltd.
            "6146.T", # Disco Corporation
            "6326.T", # Kubota Corporation
            "6971.T", # Kyocera Corporation
            "7201.T", # Nissan Motor Co., Ltd.
            "1925.T", # Daiwa House Industry Co., Ltd.
            "4452.T", # Kao Corporation
            "8802.T", # Mitsubishi Estate Co., Ltd.
            "4612.T", # Nippon Paint Holdings Co., Ltd.
            "8267.T", # Aeon Co., Ltd.
            "7733.T", # Olympus Corporation
            "4307.T", # Nomura Research Institute, Ltd.
            "4523.T", # Eisai Co., Ltd.
            "3659.T", # NEXON Co., Ltd.
            "8630.T", # Sompo Holdings, Inc.
            "7270.T", # Subaru Corporation
            "9735.T", # SECOM CO., LTD.
            "8309.T", # Sumitomo Mitsui Trust Holdings, Inc.
            "4911.T", # Shiseido Company, Limited
            "6701.T", # NEC Corporation
            "6762.T", # TDK Corporation
            "9101.T", # Nippon Yusen Kabushiki Kaisha
            "4684.T", # OBIC Co.,Ltd.
            "7832.T", # BANDAI NAMCO Holdings Inc.
            "8308.T", # Resona Holdings, Inc.
            "6920.T", # Lasertec Corporation
            "6502.T", # Toshiba Corporation
            "9503.T", # The Kansai Electric Power Company, Incorporated
            "1928.T", # Sekisui House, Ltd.
            "4507.T", # Shionogi & Co., Ltd.
            "8604.T", # Nomura Holdings, Inc.
            "9843.T", # Nitori Holdings Co., Ltd.
            "8830.T", # Sumitomo Realty & Development Co., Ltd.
            "5020.T", # ENEOS Holdings, Inc.
        ]


class ASXScraper(Scraper):
    def name(self) -> str:
        return "asx"

    def get_top_100_stocks(self, num: int) -> list:
        return [
            "WBCPI.AX", # Westpac Banking Corporation
            "WBCPH.AX", # Westpac Banking Corporation
            "BHP.AX", # BHP Group Limited
            "RIO.AX", # Rio Tinto Group
            "CBAPH.AX", # Commonwealth Bank of Australia
            "CBA.AX", # Commonwealth Bank of Australia
            "CSL.AX", # CSL Limited
            "NAB.AX", # National Australia Bank Limited
            "NABPF.AX", # National Australia Bank Limited
            "WBC.AX", # Westpac Banking Corporation
            "ANZ.AX", # ANZ Group Holdings Limited
            "WDS.AX", # Woodside Energy Group Ltd
            "FMG.AX", # Fortescue Metals Group Limited
            "WES.AX", # Wesfarmers Limited
            "MQG.AX", # Macquarie Group Limited
            "WOW.AX", # Woolworths Group Limited
            "TLS.AX", # Telstra Group Limited
            "SQ2.AX", # Block, Inc.
            "GMG.AX", # Goodman Group
            "TCL.AX", # Transurban Group
            "MQGPC.AX", # Macquarie Group Limited
            "RMD.AX", # ResMed Inc.
            "ALL.AX", # Aristocrat Leisure Limited
            "STO.AX", # Santos Limited
            "NCM.AX", # Newcrest Mining Limited
            "QBE.AX", # QBE Insurance Group Limited
            "WTC.AX", # WiseTech Global Limited
            "COL.AX", # Coles Group Limited
            "REA.AX", # REA Group Limited
            "AMC.AX", # Amcor plc
            "BXB.AX", # Brambles Limited
            "NWS.AX", # News Corporation
            "JHX.AX", # James Hardie Industries plc
            "SUN.AX", # Suncorp Group Limited
            "XRO.AX", # Xero Limited
            "COH.AX", # Cochlear Limited
            "CPU.AX", # Computershare Limited
            "S32.AX", # South32 Limited
            "ORG.AX", # Origin Energy Limited
            "SHL.AX", # Sonic Healthcare Limited
            "IAG.AX", # Insurance Australia Group Limited
            "RHCPA.AX", # Ramsay Health Care Limited
            "MIN.AX", # Mineral Resources Limited
            "SCG.AX", # Scentre Group
            "PLS.AX", # Pilbara Minerals Limited
            "MEZ.AX", # Meridian Energy Limited
            "NST.AX", # Northern Star Resources Limited
            "SOL.AX", # Washington H. Soul Pattinson and Company Limited
            "REH.AX", # Reece Limited
            "RHC.AX", # Ramsay Health Care Limited
            "FPH.AX", # Fisher & Paykel Healthcare Corporation Limited
            "URW.AX", # Unibail-Rodamco-Westfield SE
            "ASX.AX", # ASX Limited
            "LNW.AX", # Light & Wonder, Inc.
            "CAR.AX", # carsales.com Ltd
            "SVW.AX", # Seven Group Holdings Limited
            "AIA.AX", # Auckland International Airport Limited
            "APA.AX", # APA Group
            "TLC.AX", # The Lottery Corporation Limited
            "TPG.AX", # TPG Telecom Limited
            "MPL.AX", # Medibank Private Limited
            "EDV.AX", # Endeavour Group Limited
            "SGP.AX", # Stockland
            "IGO.AX", # IGO Limited
            "QAN.AX", # Qantas Airways Limited
            "WOR.AX", # Worley Limited
            "BSL.AX", # BlueScope Steel Limited
            "TWE.AX", # Treasury Wine Estates Limited
            "AFI.AX", # Australian Foundation Investment Company Limited
            "ALX.AX", # Atlas Arteria Limited
            "MGR.AX", # Mirvac Group
            "SPK.AX", # Spark New Zealand Limited
            "MCY.AX", # Mercury NZ Limited
            "ALD.AX", # Ampol Limited
            "IFT.AX", # Infratil Limited
            "SEK.AX", # SEEK Limited
            "VCX.AX", # Vicinity Centres
            "DXS.AX", # DEXUS
            "AKE.AX", # Allkem Limited
            "GPT.AX", # The GPT Group
            "PME.AX", # Pro Medicus Limited
            "AGL.AX", # AGL Energy Limited
            "ORI.AX", # Orica Limited
            "JHG.AX", # Janus Henderson Group plc
            "YAL.AX", # Yancoal Australia Ltd
            "LTR.AX", # Liontown Resources Limited
            "ARG.AX", # Argo Investments Limited
            "EVN.AX", # Evolution Mining Limited
            "AZJ.AX", # Aurizon Holdings Limited
            "IEL.AX", # IDP Education Limited
            "NXT.AX", # NEXTDC Limited
            "LYC.AX", # Lynas Rare Earths Limited
            "EBO.AX", # EBOS Group Limited
            "IPL.AX", # Incitec Pivot Limited
            "CEN.AX", # Contact Energy Limited
            "ALU.AX", # Altium Limited
            "SDF.AX", # Steadfast Group Limited
            "WHC.AX", # Whitehaven Coal Limited
            "ALQ.AX", # ALS Limited
            "BENPG.AX", # Bendigo and Adelaide Bank Limited
        ]


class JSEScraper(Scraper):
    def name(self) -> str:
        return "jse"

    def get_top_100_stocks(self, num: int) -> list:
        return [
            "PRX.JO", # Prosus N.V.
            "BHG.JO", # BHP Group Limited
            "ANH.JO", # Anheuser-Busch InBev SA/NV
            "CFR.JO", # Compagnie Financière Richemont SA
            "BTI.JO", # British American Tobacco p.l.c.
            "GLN.JO", # Glencore plc
            "AGL.JO", # Anglo American plc
            "NPN.JO", # Naspers Limited
            "FSR.JO", # FirstRand Limited
            "SBK.JO", # Standard Bank Group Limited
            "MTN.JO", # MTN Group Limited
            "VOD.JO", # Vodacom Group Limited
            "GFI.JO", # Gold Fields Limited
            "CPI.JO", # Capitec Bank Holdings Limited
            "S32.JO", # South32 Limited
            "AMS.JO", # Anglo American Platinum Limited
            "SOL.JO", # Sasol Limited
            "ABG.JO", # Absa Group Limited
            "MNP.JO", # Mondi plc
            "KIO.JO", # Kumba Iron Ore Limited
            "ANG.JO", # AngloGold Ashanti Limited
            "BID.JO", # Bid Corporation Limited
            "SHP.JO", # Shoprite Holdings Ltd
            "SLM.JO", # Sanlam Limited
            "NED.JO", # Nedbank Group Limited
            "BVT.JO", # The Bidvest Group Limited
            "DSY.JO", # Discovery Limited
            "REM.JO", # Remgro Limited
            "IMP.JO", # Impala Platinum Holdings Limited
            "SSW.JO", # Sibanye Stillwater Limited
            "APN.JO", # Aspen Pharmacare Holdings Limited
            "INP.JO", # Investec Group
            "RNI.JO", # Reinet Investments S.C.A.
            "NRP.JO", # NEPI Rockcastle N.V.
            "OUT.JO", # OUTsurance Group Limited
            "WHL.JO", # Woolworths Holdings Limited
            "PPH.JO", # Pepkor Holdings Limited
            "OMU.JO", # Old Mutual Limited
            "CLS.JO", # Clicks Group Limited
            "SHC.JO", # Shaftesbury Capital PLC
            "HAR.JO", # Harmony Gold Mining Company Limited
            "NPH.JO", # Northam Platinum Holdings Limited
            "EXX.JO", # Exxaro Resources Limited
            "N91.JO", # Ninety One Group
            "GRT.JO", # Growthpoint Properties Limited
            "NY1.JO", # Ninety One Group
            "MCG.JO", # MultiChoice Group Limited
            "MRP.JO", # Mr Price Group Limited
            "ARI.JO", # African Rainbow Minerals Limited
            "TFG.JO", # The Foschini Group Limited
            "LHC.JO", # Life Healthcare Group Holdings Limited
            "QLT.JO", # Quilter plc
            "HMN.JO", # Hammerson Plc
            "INL.JO", # Investec Group
            "TRU.JO", # Truworths International Limited
            "MTM.JO", # Momentum Metropolitan Holdings Limited
            "TBS.JO", # Tiger Brands Limited
            "PIK.JO", # Pick n Pay Stores Limited
            "AVI.JO", # AVI Limited
            "RDF.JO", # Redefine Properties Limited
            "SRE.JO", # Sirius Real Estate Limited
            "SAP.JO", # Sappi Limited
            "FFA.JO", # Fortress Real Estate Investments Limited
            "TGA.JO", # Thungela Resources Limited
            "FFB.JO", # Fortress Real Estate Investments Limited
            "DCP.JO", # Dis-Chem Pharmacies Limited
            "SPP.JO", # The SPAR Group Ltd
            "MTH.JO", # Motus Holdings Limited
            "HCI.JO", # Hosken Consolidated Investments Limited
            "NTC.JO", # Netcare Limited
            "KST.JO", # PSG Financial Services Limited
            "DRD.JO", # DRDGOLD Limited
            "RES.JO", # Resilient REIT Limited
            "VKE.JO", # Vukile Property Fund Limited
            "MSP.JO", # MAS P.L.C.
            "TSG.JO", # Tsogo Sun Limited
            "TKG.JO", # Telkom SA SOC Ltd
            "AFE.JO", # AECI Ltd
            "ADH.JO", # ADvTECH Limited
            "HYP.JO", # Hyprop Investments Limited
            "SPG.JO", # Super Group Limited
            "CML.JO", # Coronation Fund Managers Limited
            "RLO.JO", # Reunert Limited
            "SUI.JO", # Sun International Limited
            "RCL.JO", # RCL Foods Limited
            "EQU.JO", # Equites Property Fund Limited
            "LTE.JO", # Lighthouse Properties plc
            "OMN.JO", # Omnia Holdings Limited
            "OCE.JO", # Oceana Group Limited
            "DTC.JO", # Datatec Limited
            "AFT.JO", # Afrimat Limited
            "JSE.JO", # JSE Limited
            "GND.JO", # Grindrod Limited
            "PAN.JO", # Pan African Resources PLC
            "WBO.JO", # Wilson Bayly Holmes-Ovcon Limited
            "KAP.JO", # KAP Limited
            "FBR.JO", # Famous Brands Limited
            "COH.JO", # Curro Holdings Limited
            "SSS.JO", # Stor-Age Property REIT Limited
            "IPF.JO" # Investec Property Fund Limited
        ]


class SSXScraper(Scraper):
    def name(self) -> str:
        return "ssx"

    def get_top_100_stocks(self, num: int) -> list:
        return [
            "600519.SS", # Kweichow Moutai Co., Ltd.
            "601398.SS", # Industrial and Commercial Bank of China Limited
            "601857.SS", # PetroChina Company Limited
            "600941.SS", # China Mobile Limited
            "601288.SS", # Agricultural Bank of China Limited
            "601939.SS", # China Construction Bank Corporation
            "601988.SS", # Bank of China Limited
            "300750.SZ", # Contemporary Amperex Technology Co., Limited
            "601318.SS", # Ping An Insurance (Group) Company of China, Ltd.
            "601628.SS", # China Life Insurance Company Limited
            "600036.SS", # China Merchants Bank Co., Ltd.
            "002594.SZ", # BYD Company Limited
            "600028.SS", # China Petroleum & Chemical Corporation
            "600938.SS", # CNOOC Limited
            "000858.SZ", # Wuliangye Yibin Co.,Ltd.
            "601088.SS", # China Shenhua Energy Company Limited
            "600900.SS", # China Yangtze Power Co., Ltd.
            "601728.SS", # China Telecom Corporation Limited
            "601658.SS", # Postal Savings Bank of China Co., Ltd.
            "000333.SZ", # Midea Group Co., Ltd.
            "601138.SS", # Foxconn Industrial Internet Co., Ltd.
            "601328.SS", # Bank of Communications Co., Ltd.
            "000568.SZ", # Luzhou Laojiao Co.,Ltd
            "601166.SS", # Industrial Bank Co., Ltd.
            "300760.SZ", # Shenzhen Mindray Bio-Medical Electronics Co., Ltd.
            "601899.SS", # Zijin Mining Group Company Limited
            "600030.SS", # CITIC Securities Company Limited
            "002415.SZ", # Hangzhou Hikvision Digital Technology Co., Ltd.
            "600809.SS", # Shanxi Xinghuacun Fen Wine Factory Co.,Ltd.
            "600309.SS", # Wanhua Chemical Group Co., Ltd.
            "600276.SS", # Jiangsu Hengrui Medicine Co., Ltd.
            "601816.SS", # Beijing-Shanghai High-Speed Railway Co.,Ltd.
            "601601.SS", # China Pacific Insurance (Group) Co., Ltd.
            "601998.SS", # China CITIC Bank Corporation Limited
            "300059.SZ", # East Money Information Co.,Ltd.
            "601668.SS", # China State Construction Engineering Corporation Limited
            "601319.SS", # The People's Insurance Company (Group) of China Limited
            "603259.SS", # WuXi AppTec Co., Ltd.
            "601888.SS", # China Tourism Group Duty Free Corporation Limited
            "002714.SZ", # Muyuan Foods Co., Ltd.
            "603288.SS", # Foshan Haitian Flavouring and Food Company Ltd.
            "000001.SZ", # Ping An Bank Co., Ltd.
            "600690.SS", # Haier Smart Home Co., Ltd.
            "002475.SZ", # Luxshare Precision Industry Co., Ltd.
            "688981.SS", # Semiconductor Manufacturing International Corporation
            "600000.SS", # Shanghai Pudong Development Bank Co., Ltd.
            "000651.SZ", # Gree Electric Appliances, Inc. of Zhuhai
            "002304.SZ", # Jiangsu Yanghe Brewery Joint-Stock Co., Ltd.
            "002352.SZ", # S.F. Holding Co., Ltd.
            "601012.SS", # LONGi Green Energy Technology Co., Ltd.
            "300999.SZ", # Yihai Kerry Arawana Holdings Co., Ltd
            "002142.SZ", # Bank of Ningbo Co., Ltd.
            "601633.SS", # Great Wall Motor Company Limited
            "600406.SS", # NARI Technology Co., Ltd.
            "300124.SZ", # Shenzhen Inovance Technology Co.,Ltd
            "601225.SS", # Shaanxi Coal Industry Company Limited
            "600104.SS", # SAIC Motor Corporation Limited
            "688111.SS", # Beijing Kingsoft Office Software, Inc.
            "601818.SS", # China Everbright Bank Company Limited
            "300015.SZ", # Aier Eye Hospital Group Co., Ltd.
            "600887.SS", # Inner Mongolia Yili Industrial Group Co., Ltd.
            "600436.SS", # Zhangzhou Pientzehuang Pharmaceutical., Ltd
            "601066.SS", # CSC Financial Co., Ltd.
            "600050.SS", # China United Network Communications Limited
            "600048.SS", # Poly Developments and Holdings Group Co., Ltd.
            "601766.SS", # CRRC Corporation Limited
            "200725.SZ", # BOE Technology Group Company Limited
            "601390.SS", # China Railway Group Limited
            "000063.SZ", # ZTE Corporation
            "600016.SS", # China Minsheng Banking Corp., Ltd.
            "601919.SS", # COSCO SHIPPING Holdings Co., Ltd.
            "000002.SZ", # China Vanke Co., Ltd.
            "688235.SS", # BeiGene, Ltd.
            "000725.SZ", # BOE Technology Group Company Limited
            "003816.SZ", # CGN Power Co., Ltd.
            "601688.SS", # Huatai Securities Co., Ltd.
            "200596.SZ", # Anhui Gujing Distillery Co., Ltd.
            "600031.SS", # Sany Heavy Industry Co.,Ltd
            "600019.SS", # Baoshan Iron & Steel Co., Ltd.
            "601995.SS", # China International Capital Corporation Limited
            "600438.SS", # Tongwei Co.,Ltd
            "601985.SS", # China National Nuclear Power Co., Ltd.
            "600905.SS", # China Three Gorges Renewables (Group) Co.,Ltd.
            "600188.SS", # Yankuang Energy Group Company Limited
            "600025.SS", # Huaneng Lancang River Hydropower Inc.
            "600585.SS", # Anhui Conch Cement Company Limited
            "000596.SZ", # Anhui Gujing Distillery Co., Ltd.
            "300274.SZ", # Sungrow Power Supply Co., Ltd.
            "603993.SS", # CMOC Group Limited
            "600150.SS", # China CSSC Holdings Limited
            "688041.SS", # Hygon Information Technology Co., Ltd.
            "002371.SZ", # NAURA Technology Group Co., Ltd.
            "601211.SS", # Guotai Junan Securities Co., Ltd.
            "601800.SS", # China Communications Construction Company Limited
            "002493.SZ", # Rongsheng Petrochemical Co., Ltd.
            "600760.SS", # AVIC Shenyang Aircraft Company Limited
            "600018.SS", # Shanghai International Port (Group) Co., Ltd.
            "200625.SZ", # Chongqing Changan Automobile Company Limited
            "601111.SS", # Air China Limited
            "300122.SZ", # Chongqing Zhifei Biological Products Co., Ltd.
        ]
    
def get_market_cap(stock_symbol):
    market_cap = web.get_quote_yahoo(stock_symbol)['marketCap']
    return market_cap

class CustomScraper(Scraper):
    def __init__(self, tickers: list[str]) -> None:
        self.tickers = tickers
        super().__init__()

    def get_top_100_stocks(self, num: int) -> list:
        return self.tickers
