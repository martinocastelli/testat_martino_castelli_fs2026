#!/usr/bin/env python3
"""Solution for Python Testat FS2026.
author:Martino Castelli
"""

import pathlib  
import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

class MoveChillData:
    def __init__(self, csv_path, delimiter = (',')):
        if (not type(csv_path) in (str, pathlib.Path, pathlib.PosixPath)):
            raise TypeError (f'csv path must be of type Path or str, got {type(csv_path)}')
        self._df = pd.read_csv(csv_path, delimiter=delimiter)
        self._df.rename(columns={'zeitpunkt': 'time'}, inplace=True)
        self._df["time"] = self._df["time"].apply(lambda date:  datetime.strptime(str(date), "%Y%m%d%H%M%S"))
        self._features = []
        self._feature_analysis = {}
        self.report = ""

    def __str__(self):
        return "DataFrame shape: " + str(self._df.shape) + "\nTotal NaN values: " + str(self._df.isna().sum().sum()) + "\nExtracted features:" + str(self._features)

    def __len__(self):
        return len(self._df.index)

    def clean(self):
        self._df.dropna(inplace=True)
        self._df = self._df.query('0 <= humidity <= 100')
        self._df = self._df.query('0 <= temperature <= 100')
        self._df.drop(["sensor_eui", "geometry"], axis=1, inplace=True)

    def create_features(self):
        self._df['hour'] = self._df['time'].apply(lambda date: date.hour)
        self._df['weekday'] = self._df['time'].apply(lambda date: date.weekday())
        self._df['is_weekend'] = self._df['weekday'].apply(lambda day: 1 if day in (5, 6) else 0)
        self._features = [elem for elem in self._df.columns.values if not elem in ("objectid", "id", "time", "sit")]

    def analyze_features(self):
        for feature in self._features:
            sit = self._df['sit'].tolist()
            values = self._df[feature].tolist()


            mean = np.mean(sit)
            sit = [val - mean for val in sit]
            mean = np.mean(values)
            values = [val - mean for val in values]

            r = sum(np.multiply(sit, values)) / (np.sqrt(sum(np.square(sit))) * np.sqrt(sum(np.square(values))))
            self._feature_analysis[feature] = r
        return self._feature_analysis
    
    def generate_report(self):
        self.report = """"""
        feature_size = max([len(feat) for feat in self._features]) 
        for feature, value in sorted(self._feature_analysis.items(), key=lambda item: abs(item[1])):
            valutation = "WEAK - LOW IMPACT"
            if(abs(value) >= 0.05):
                if(abs(value) >= 0.3):
                    valutation = "GOOD FEATURE"
                else:
                    valutation = "MODERATE"
            self.report += f"{feature:{feature_size}} | r = {value:+0.3f} | {valutation}\n"

    def plot(self, save_path=None):
        self._feature_analysis = dict(sorted(self._feature_analysis.items(), key=lambda item: abs(item[1])))

        fig, ax = plt.subplots(tight_layout=True)
        bars = ax.barh(self._feature_analysis.keys(), self._feature_analysis.values())
        ax.axvline(0, color='black')
        ax.bar_label(bars, fmt='%+.2f')
        ax.set_xlabel('Correlation r')
        ax.set_xlim(-0.5, 0.5)
        ax.set_title('Feature Correlations')
        if save_path:
            fig.savefig(save_path)
        return fig


# --- Main --------------------------------------------------------------------
if __name__ == "__main__":
    # --- MoveChillData -------------------------------------------------------

    # -------------------------------------------------------------------------
    # --- 4.1 __init__(self, folder_path) -------------------------------------
    # -------------------------------------------------------------------------
    mcd = MoveChillData("taz.view_moveandchill.csv")
    # try:
    #     mcd = MoveChillData(pathlib.Path("taz.view_moveandchill.csv"))
    # except TypeError as e:
    #     print(e)
    # try:
    #     mcd = MoveChillData(["taz.view_moveandchill.csv"])
    # except TypeError as e:
    #     print(e)
    
    # print(type(mcd._features))
    # print(type(mcd._feature_analysis))
    # print(type(mcd.report))

    # print(mcd._df.head(5))
    # print(mcd._df.info())
    # print(mcd._features)
    # print(mcd._feature_analysis)
    # print(repr(mcd.report))
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # --- 4.2 __str__(self) ---------------------------------------------------
    # -------------------------------------------------------------------------
    # print(mcd)
    # print(repr(str(mcd)))
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # --- 4.3 __len__(self) ---------------------------------------------------
    # -------------------------------------------------------------------------
    # print(len(mcd))

    # -------------------------------------------------------------------------
    # --- 4.4 clean(self) -----------------------------------------------------
    # -------------------------------------------------------------------------
    # print(mcd._df.head(2))
    # print(
    #     f"Humidity in DataFrame: min = {mcd._df['humidity'].min()}, max = {mcd._df['humidity'].max()}"
    # )
    # print(
    #     f"Temperature in DataFrame: min = {mcd._df['temperature'].min()}, max = {mcd._df['temperature'].max()}"
    # )
    # print(mcd._df[mcd._df.isna().any(axis=1)].head(2))
    # print(mcd)
    # print("calling clean ----------------------------------------------------------------------")
    # mcd.clean()
    # print(mcd._df.head(2))
    # print(
    #     f"Humidity in DataFrame: min = {mcd._df['humidity'].min()}, max = {mcd._df['humidity'].max()}"
    # )
    # print(
    #     f"Temperature in DataFrame: min = {mcd._df['temperature'].min()}, max = {mcd._df['temperature'].max()}"
    # )
    # print(mcd._df[mcd._df.isna().any(axis=1)])
    # print(mcd)

    # -------------------------------------------------------------------------
    # --- 4.5 create_features(self) -------------------------------------------
    # -------------------------------------------------------------------------
    # print(mcd._features)
    # mcd.clean()
    # print(mcd._df.head(2))
    # mcd.create_features()
    # print(mcd._df.head(2))
    # print(mcd._features)
    # print(mcd)
    # print(mcd._df.head(2))
    # mcd.create_features()
    # print(mcd._df.head(2))
    # print(mcd)
    # print(mcd._features)

    # -------------------------------------------------------------------------
    # --- 4.6 analyze_features(self) ------------------------------------------
    # -------------------------------------------------------------------------
    # mcd.clean()
    # mcd.create_features()
    # mcd.analyze_features()
    # print(mcd._feature_analysis)
    # # print(mcd)
    # feature_analysis = mcd.analyze_features()

    # print(type(feature_analysis))
    # print(feature_analysis)

    # -------------------------------------------------------------------------
    # --- 4.7 generate_report(self) -------------------------------------------
    # -------------------------------------------------------------------------
    # mcd.clean()
    # mcd.create_features()
    # mcd.analyze_features()
    # mcd.generate_report()
    # print(mcd.report)
    # print(repr(mcd.report))

    # -------------------------------------------------------------------------
    # --- 4.8 plot(self, save_path) -------------------------------------------
    # -------------------------------------------------------------------------
    # mcd.clean()
    # mcd.create_features()
    # mcd.analyze_features()
    # mcd.generate_report()
    # fig = mcd.plot("feature_correlations.png")
    # print(type(fig))
    # plt.show()
