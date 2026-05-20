"""Solution for Python Testat FS2026.
author:
"""


class MoveChillData:
    pass


# --- Main --------------------------------------------------------------------
if __name__ == "__main__":
    # --- MoveChillData -------------------------------------------------------

    # -------------------------------------------------------------------------
    # --- 4.1 __init__(self, folder_path) -------------------------------------
    # -------------------------------------------------------------------------
    mcd = MoveChillData("taz.view_moveandchill.csv")
    # mcd = MoveChillData(Path("taz.view_moveandchill.csv"))
    # mcd = MoveChillData(["taz.view_moveandchill.csv"])
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
    # mcd.clean()
    # print(mcd._df.head(2))
    # print(
    #     f"Humidity in DataFrame: min = {mcd._df['humidity'].min()}, max = {mcd._df['humidity'].max()}"
    # )
    # print(
    #     f"Temperature in DataFrame: min = {mcd._df['temperature'].min()}, max = {mcd._df['temperature'].max()}"
    # )
    # print(mcd._df[mcd._df.isna().any(axis=1)])

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
