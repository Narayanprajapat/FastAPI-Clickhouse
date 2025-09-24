import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

BEARER_TOKEN = os.getenv('BEARER_TOKEN')

class SharpelyScrapper:

    def get_data(self) -> dict:
        url = "https://pyapiv2.mintbox.ai/api/core/getFinancialStatementsV2/ticker=TCS"

        headers = {
            "sec-ch-ua-platform": "macOS",
            "Authorization": f"Bearer {BEARER_TOKEN}",
            "Referer": "https://sharpely.in/",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "sec-ch-ua": "'Not;A=Brand';v='99', 'Google Chrome';v='139', 'Chromium';v='139'",
            "sec-ch-ua-mobile": "?0",
        }

        response = requests.get(url, headers=headers)

        return response.json()

    def balance_sheet_data_processing(self, data: dict, type: str) -> dict:
        side_headers = {
            "Cash & Short Term Investments": "SCSTI",
            "Cash & Cash Equivalents": "SCAE",
            "Short-Term Investments": "SSTI",
            "Financial Assets - Short-Term": "SFAC",
            "Short-Term Loans & Receivables": "SCLR",
            "Accounts Receivable": "SANR",
            "Loans - Short-Term": "SLNS",
            "Short-Term Income Tax Receivables": "STXS",
            "Total Inventories": "SINY",
            "Raw Materials": "SIRM",
            "Finished Goods": "SIFG",
            "Other Current Assets": "SOCA",
            "Total Current Assets": "STCA",
            "Long-Term Investments": "SILT",
            "Investment - Available for Sale/HTM - LT": "SLTI",
            "Loans - Long-Term": "SLNG",
            "Property Plant & Equipment - Net": "SPPE",
            "PPE - ex Lease - Net - Total": "SPXE",
            "Construction in Progress - Net": "SCPN",
            "Right of Use Tangible Assets - Total - Net": "SRTN",
            "Property Plant & Equipment - Other - Net": "SOPN",
            "Property Plant & Equipment - Gross": "SPPC",
            "PPE - ex Lease - Gross - Total": "SPXC",
            "Construction in Progress - Gross": "SCPC",
            "PPE - Other - Gross": " ",
            "Accumulated Depreciation & Impairment": "SDPP",
            "Other Non-Current Assets - Total": "SOAS",
            "Deferred Tax - Asset - Long-Term": "SDTA",
            "Other Non-Current Assets": "SNCA",
            "Intangible Assets - Net": "SINN",
            "Intangible Assets - ex Goodwill - Net": "STIN",
            "Total Non-Current Assets": "STLA",
            "Total Assets": "ATOT",
            "Accounts Payable & Accruals - ST": "SAPA",
            "Accounts & Notes Payable - ST": "SANC",
            "Accrued Expenses - ST": "SAEC",
            "ST Debt & CPLTD": "SSTD",
            "ST Debt & Notes Payable": "SSOD",
            "CPLTD incl Capitalized Leases": "SCLD",
            "CPLTD excl Capitalized Leases": "SCDE",
            "Capitalized Leases - Current Portion": "SCFL",
            "Income Taxes - Payable - Short-Term": "STXZ",
            "Dividends/Distributions Payable": "SDPB",
            "Other Current Liabilities": "SOCL",
            "Deferred Income - Short-Term": "SCAV",
            "Provisions - Short-Term": "SCPV",
            "Other Current Liabilities": "SCLO",
            "Total Current Liabilities": "SCLT",
            "Long Term Debt": "SLTD",
            "Long-Term Debt ex Capitalized Leases": "SDXL",
            "Debt - Non-Convertible - Long-Term": "LNCD",
            "Capitalized Lease Obligations - Long-Term": "SLCL",
            "Deferred & Investment Tax Credits - LT": "SDTX",
            "Deferred Tax - Liability - Long-Term": "SDTL",
            "Other Non-Current Liabilities - Total": "SLLT",
            "Provisions - Long-Term": "SNCP",
            "Other Non-Current Liabilities": "SOLL",
            "Total Non-Current Liabilities": "SLDL",
            "Total Liabilities": "STLB",
            "Total Shareholders' Equity": "QTEP",
            "Common Equity": "QCEP",
            "Common Stock - Treasury/Repurchased": "STSC",
            "Common Equity - Contributed": "SCOM",
            "Common Stock - Issued & Paid": "SCMS",
            "Common Stock - Addnl Paid in Capital": "SPIC",
            "Total Equity": "STLE",
            "Total Liabilities & Equity": "STBL",
            "Common Shares - Issued": "STCIC",
            "Common Shares - Outstanding": "STCOC",
            "Common Shares - Treasury": "STCTC",
            # Supplementary
            "Finance & Operating Lease Liabilities": "STFL",
            "Debt including Lease Liabilities": "STDL",
            "Total Investments": "STIV",
            "Total Loans & Receivables": "SLRE",
            "Other Assets": "SOAT",
            "Income Taxes - Payable - Total": "STXB",
            "Dividends Payable": "SDPT",
            "Payables & Accrued Expenses": "SPAB",
            "Trade Account Payables - Total": "SANP",
            "Accrued Expenses": "SAEA",
            "Net Debt": "SSND",
            "Debt - Total": "SLSD",
            "Capital Lease Maturities": "STLS",
            "Due within 1 Year": "SCL1",
            "Due in Year 5": "SCL5",
            "Remaining Maturities": "SCLX",
            "Due in 4-5 Years": "SCL45",
            "Due in Year 6 & Beyond": "SCL6B",
            "Accruals - Short-Term": "SACRU",
            "Asset Accruals": "SASAC",
            "Cash & Cash Equivalents": "SCASH",
            "Cash & Short Term Investments": "SCSTI",
            "Debt incl Preferred Equity & Minority Interest": "STDBT",
            "Investments - Permanent": "SINVP",
            "Net Book Capital": "SNBKC",
            "Net Operating Assets": "SNOPA",
            "Provisions": "SPROV",
            "Shareholders Equity - Common": "STCSE",
            "Cash & ST Investments - Net of Debt": "SCSID",
            "Tangible Total Equity": "STTAN",
            "Tangible Book Value": "SQTAN",
            "Total Book Capital": "STBKC",
            "Total Capital": "STCAP",
            "Total Long Term Capital": "STLTC",
            "Total Fixed Assets - Net": "STNCA",
            "Working Capital": "SWCAP",
            "Interest Bearing Liabilities - Total": "SINBL",
            "Working Capital - Non-Cash": "SNCWC",
            "Net Debt incl Preferred Equity & Minority Interest": "STDBND",
            "Other Assets - Total": "SOAST",
            "Other Liabilities - Total": "SOLBT",
            "Total Current Assets ex Inventories": "STCAXIN",
            "Current Liabilities ex Current Debt": "SCLCD",
            "Current Assets ex Cash & ST Investments": "SCACS",
            "Cash, ST Investments & Receivable - Total": "SCSAR",
            "Cash in Hand & with Banks - Total": "SCSH",
        }

        headers = data.get("header", [])

        side_headers_values = list(side_headers.values())
        raw_dataset = data.get("statement", {}).get("data", [])

        dataset = [d for d in raw_dataset if d[0] in side_headers_values]

        return {
            "tab_name": f"Balance Sheet ({type})",
            "upper_headers": headers,
            "side_headers": list(side_headers.keys()),
            "dataset": dataset,
        }

    def income_statement_data_processing(self, data: dict, type: str) -> dict:
        side_headers = {
            "Total Revenue": "STLR",
            "Cost of Operating Revenue": "SCOR",
            "Gross Profit": "SGRP",
            "Total Operating Expenses": "SOET",
            "Operating Profit": "SOPR",
            "Financing Income/(Expense) - Net": "SFIE",
            "Profit before Taxes": "SIBT",
            "Income Taxes": "STAX",
            "Profit after Tax": "SNIC",
            "EPS - Basic - ex Extraordinary Items": "SBCOC",
            "EPS - Diluted - ex Extraordinary Items": "SDCOC",
            "EBIT": "SEBIT",
            "EBITDA": "SEBITDA",
        }

        headers = data.get("header", [])

        side_headers_values = list(side_headers.values())
        raw_dataset = data.get("statement", {}).get("data", [])

        dataset = [d for d in raw_dataset if d[0] in side_headers_values]

        return {
            "tab_name": f"Income Statement ({type})",
            "upper_headers": headers,
            "side_headers": list(side_headers.keys()),
            "dataset": dataset,
        }

    def cash_flow_data_processing(self, data: dict, type: str) -> dict:
        side_headers = {
            "Operating CF bef Changes in Working Cap": "SONC",
            "Working Capital - Increase/(Decrease)": "SCWC",
            "Net CF from Operating Activities": "STLO",
            "Capital Expenditures - Net": "SCAP",
            "Capital Expenditures - Gross": "SCEX",
            "Net CF from Investing Activities": "STLI",
            "Dividends Paid - Cash - Total": "SCDP",
            "Stock - Issuance/(Retirement) - Net": "SPSS",
            "Debt - LT & ST - Issuance/(Retirement) - Total": "SPRD",
            "Net Cash Flow from Financing Activities": "STLF",
            "Free Cash Flow to Equity": "SFCFE",
            "Free Operating CF net dividend": "SFCFO",
            "Free Operating CF": "SFCFL",
        }

        headers = data.get("header", [])

        side_headers_values = list(side_headers.values())
        raw_dataset = data.get("statement", {}).get("data", [])

        dataset = [d for d in raw_dataset if d[0] in side_headers_values]

        return {
            "tab_name": f"Cash Flow ({type})",
            "upper_headers": headers,
            "side_headers": list(side_headers.keys()),
            "dataset": dataset,
        }

    def processing(self, raw_data: dict) -> dict:
        inc_consol_annual = self.income_statement_data_processing(
            data=raw_data["inc_consol_annual"], type="Consolidate Annual"
        )

        inc_consol_interim = self.income_statement_data_processing(
            data=raw_data["inc_consol_interim"], type="Consolidate Interim"
        )

        inc_standalone_annual = self.income_statement_data_processing(
            data=raw_data["inc_standalone_annual"], type="Standalone Annual"
        )

        bal_consol_annual = self.balance_sheet_data_processing(
            data=raw_data["bal_consol_annual"], type="Consolidate Annual"
        )

        bal_consol_interim = self.balance_sheet_data_processing(
            data=raw_data["bal_consol_interim"], type="Consolidate Interim"
        )

        bal_standalone_annual = self.balance_sheet_data_processing(
            data=raw_data["bal_standalone_annual"], type="Standalone Annual"
        )

        cas_consol_annual = self.cash_flow_data_processing(
            data=raw_data["cas_consol_annual"], type="Consolidate Annual"
        )

        cas_consol_interim = self.cash_flow_data_processing(
            data=raw_data["cas_consol_interim"], type="Consolidate Interim"
        )

        cas_standalone_annual = self.cash_flow_data_processing(
            data=raw_data["cas_standalone_annual"], type="Standalone Annual"
        )

        return {
            "inc_consol_annual": inc_consol_annual,
            "inc_consol_interim": inc_consol_interim,
            "inc_standalone_annual": inc_standalone_annual,
            "bal_consol_annual": bal_consol_annual,
            "bal_consol_interim": bal_consol_interim,
            "bal_standalone_annual": bal_standalone_annual,
            "cas_consol_annual": cas_consol_annual,
            "cas_consol_interim": cas_consol_interim,
            "cas_standalone_annual": cas_standalone_annual,
        }


if __name__ == "__main__":
    ins = SharpelyScrapper()
    raw_data = ins.get_data()
    dataset = ins.processing(raw_data=json.loads(raw_data["statements"]))
    print(dataset)
